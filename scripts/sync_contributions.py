#!/usr/bin/env python3
"""Synchronize the public CoreFoundry contribution ledger from upstream GitHub PRs.

Narrative metadata is curated in data/contribution_metadata.json.
Volatile PR state is always read from the canonical upstream repository.

The script intentionally ignores pull requests whose base repository belongs to
Johnny-Kao so disposable forks, staging repositories, and research harnesses do
not become durable public references.
"""

from __future__ import annotations

import datetime as dt
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
METADATA_PATH = ROOT / "data" / "contribution_metadata.json"
OUTPUT_PATH = ROOT / "CONTRIBUTIONS.md"

API = "https://api.github.com"
TOKEN = os.environ.get("GITHUB_TOKEN", "")
AUTHOR = os.environ.get("GITHUB_ACTOR_TO_TRACK", "Johnny-Kao")


def api_get(path: str):
    req = urllib.request.Request(
        API + path,
        headers={
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "CoreFoundry-contribution-sync",
            **({"Authorization": f"Bearer {TOKEN}"} if TOKEN else {}),
        },
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)


def load_metadata():
    with METADATA_PATH.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def discover_prs():
    q = urllib.parse.quote(f"author:{AUTHOR} is:pr")
    discovered = []
    for page in range(1, 11):
        payload = api_get(
            f"/search/issues?q={q}&sort=updated&order=desc&per_page=100&page={page}"
        )
        items = payload.get("items", [])
        if not items:
            break
        discovered.extend(items)
        if len(items) < 100:
            break
    return discovered


def fetch_pr(search_item):
    repo = search_item["repository_url"].split("/repos/", 1)[1]
    number = search_item["number"]
    return repo, api_get(f"/repos/{repo}/pulls/{number}")


def canonical_key(repo: str, number: int) -> str:
    return f"{repo}#{number}"


def status_of(pr):
    if pr.get("merged_at"):
        return "merged"
    if pr.get("state") == "open" and pr.get("draft"):
        return "draft"
    if pr.get("state") == "open":
        return "open"
    return "closed"


def should_include(repo, pr, meta):
    base_owner = ((pr.get("base") or {}).get("repo") or {}).get("owner", {}).get("login")
    if base_owner == AUTHOR:
        return False

    if meta.get("include") is False:
        return False

    status = status_of(pr)
    if status in {"merged", "open", "draft"}:
        return True
    return bool(meta.get("include_closed"))


def escape_cell(value):
    if value is None:
        return "—"
    return str(value).replace("|", "\\|").replace("\n", " ").strip() or "—"


def pr_link(repo, pr):
    number = pr["number"]
    url = pr["html_url"]
    cell = f"**[{repo} #{number}]({url})**"
    if pr.get("merged_at") and pr.get("merge_commit_sha"):
        sha = pr["merge_commit_sha"]
        commit_url = f"https://github.com/{repo}/commit/{sha}"
        cell += f"<br><sub>[merge commit `{sha[:7]}`]({commit_url})</sub>"
    return cell


def repo_display(repo):
    return repo.split("/", 1)[1]


def row_for(repo, pr, meta):
    return [
        pr_link(repo, pr),
        escape_cell(meta.get("what_it_is", repo_display(repo))),
        escape_cell(meta.get("what_changed", pr.get("title"))),
        escape_cell(meta.get("evidence")),
        escape_cell(meta.get("why_it_matters")),
    ]


def render_table(rows):
    lines = [
        "| Project / PR | What it is | What changed | Evidence / impact | Why this matters |",
        "|---|---|---|---:|---|",
    ]
    for row in rows:
        lines.append("| " + " | ".join(row) + " |")
    return "\n".join(lines)


def sort_key(item):
    _repo, pr, _meta = item
    for field in ("merged_at", "updated_at", "closed_at", "created_at"):
        if pr.get(field):
            return pr[field]
    return ""


def badge(label, value, color):
    label_q = urllib.parse.quote(label.replace("-", "--"), safe="")
    value_q = urllib.parse.quote(str(value).replace("-", "--"), safe="")
    return f"![{label}](https://img.shields.io/badge/{label_q}-{value_q}-{color})"


def main():
    metadata_doc = load_metadata()
    metadata = metadata_doc.get("entries", {})

    buckets = {"merged": [], "open": [], "draft": [], "closed": []}
    seen = set()

    for item in discover_prs():
        try:
            repo, pr = fetch_pr(item)
        except (urllib.error.HTTPError, urllib.error.URLError) as exc:
            print(f"warning: unable to fetch {item.get('html_url')}: {exc}", file=sys.stderr)
            continue

        key = canonical_key(repo, pr["number"])
        if key in seen:
            continue
        seen.add(key)
        meta = metadata.get(key, {})
        if not should_include(repo, pr, meta):
            continue

        buckets[status_of(pr)].append((repo, pr, meta))

    for values in buckets.values():
        values.sort(key=sort_key, reverse=True)

    now = dt.datetime.now(dt.timezone.utc).replace(microsecond=0)
    counts = {k: len(v) for k, v in buckets.items()}

    lines = [
        "# CoreFoundry Contribution Ledger",
        "",
        "A live public record of upstream open-source work tracked by CoreFoundry.",
        "",
        '<p align="center">',
        f"  {badge('merged', counts['merged'], '2ea44f')}",
        f"  {badge('open', counts['open'], '0969da')}",
        f"  {badge('draft', counts['draft'], 'd29922')}",
        f"  {badge('closed / retained', counts['closed'], '6e7781')}",
        "</p>",
        "",
        f"> **Last synchronized:** {now.strftime('%Y-%m-%d %H:%M UTC')}",
        "",
        "## Canonical-source policy",
        "",
        "CoreFoundry treats the **upstream pull request as the canonical public record**.",
        "",
        "- upstream PR links are always primary;",
        "- merged entries also retain the upstream merge-commit link when GitHub exposes one;",
        "- contributor forks, local branches, staging repositories, and research harnesses are never required to reconstruct the public record;",
        "- narrative metadata is curated, while PR state is synchronized automatically from GitHub.",
        "",
        "```mermaid",
        "flowchart LR",
        '    A["Research"] --> B["Draft PR"]',
        '    B --> C["Open / Review"]',
        '    C --> D["Merged"]',
        '    C --> E["Closed / lesson retained"]',
        "```",
        "",
    ]

    sections = [
        ("merged", "🚀 Merged upstream work"),
        ("open", "🟢 Open / in review"),
        ("draft", "🟡 Draft / validating"),
        ("closed", "⚪ Closed / lessons retained"),
    ]

    for key, title in sections:
        lines.append(f"## {title}")
        lines.append("")
        if buckets[key]:
            rows = [row_for(*entry) for entry in buckets[key]]
            lines.append(render_table(rows))
        else:
            lines.append("_No tracked entries in this state._")
        lines.append("")

    lines.extend(
        [
            "---",
            "",
            "## How this page is maintained",
            "",
            "This file is generated by `.github/workflows/sync-contributions.yml` from:",
            "",
            "1. public upstream PR state from GitHub;",
            "2. curated display metadata in `data/contribution_metadata.json`.",
            "",
            "New public upstream PRs authored by the tracked contributor are discovered automatically. "
            "Closed-but-unmerged work is included only when explicitly retained in metadata.",
            "",
            "> Do not edit this file by hand; changes will be overwritten by the next synchronization run.",
            "",
        ]
    )

    OUTPUT_PATH.write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
