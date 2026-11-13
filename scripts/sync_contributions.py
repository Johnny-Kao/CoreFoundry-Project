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
REGISTRY_PATH = ROOT / "data" / "contribution_registry.json"

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
    if len(discovered) >= 1000:
        print("warning: 1,000-result search cap reached; discovery may be incomplete", file=sys.stderr)
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
    return True  # Retain closed, unmerged upstream work as historical records.


def escape_cell(value):
    if value is None:
        return "—"
    return str(value).replace("|", "\\|").replace("\n", " ").strip() or "—"


def integrated_upstream(pr, meta):
    """A closed PR separately integrated by an upstream commit."""
    record = meta.get("upstream_integration")
    if not isinstance(record, dict) or status_of(pr) != "closed":
        return None
    target_repo = record.get("repo")
    if (not isinstance(target_repo, str) or len(target_repo.split("/")) != 2
            or any(not part or not all(c.isalnum() or c in "-_." for c in part)
                   for part in target_repo.split("/"))):
        return None
    sha = record.get("commit")
    if (not isinstance(sha, str) or len(sha) != 40
            or any(c not in "0123456789abcdef" for c in sha)):
        return None
    return record


def pr_link(repo, pr, meta=None):
    return f"**[{repo} #{pr['number']}]({pr['html_url']})**"


def repo_display(repo):
    return repo.split("/", 1)[1]


def concise(value, limit=155):
    """Keep ledger cells scannable without altering curated source metadata."""
    import re
    value = re.sub(r"\s+", " ", str(value or "")).strip()
    value = re.sub(r"\s*\(\[source\]\(https?://[^)]+\)\)", "", value)
    if len(value) <= limit:
        return value
    cut = value[:limit].rsplit(" ", 1)[0]
    return (cut or value[:limit]).rstrip(" ,;:") + "…"


def row_for(repo, pr, meta):
    phase = "integrated" if integrated_upstream(pr, meta) else status_of(pr)
    status = {
        "merged": "✅ Merged",
        "integrated": "✅ Integrated",
        "open": "🟢 Open",
        "draft": "🟡 Draft",
        "closed": "⚪ Closed",
    }[phase]
    change = concise(meta.get("what_changed") or pr.get("title"), 150)
    evidence = concise(meta.get("evidence"), 135)
    return [
        pr_link(repo, pr, meta),
        status,
        escape_cell(change),
        escape_cell(evidence),
    ]


def render_table(rows):
    lines = [
        "| Project / PR | Status | Engineering contribution | Evidence / impact |",
        "|---|---|---|---|",
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

    buckets = {"merged": [], "integrated": [], "open": [], "draft": [], "closed": []}
    seen = set()
    errors = 0
    triggers = []
    registry = {"schema_version": 1, "entries": {}}
    if REGISTRY_PATH.exists():
        registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    historic = registry.get("entries", {})
    current = {}

    for item in discover_prs():
        try:
            repo, pr = fetch_pr(item)
        except (urllib.error.HTTPError, urllib.error.URLError) as exc:
            print(f"warning: unable to fetch {item.get('html_url')}: {exc}", file=sys.stderr)
            errors += 1
            continue

        key = canonical_key(repo, pr["number"])
        snapshot = {field: pr.get(field) for field in (
            "number", "html_url", "title", "merged_at", "merge_commit_sha",
            "state", "draft", "updated_at", "closed_at", "created_at"
        )}
        base_repo = (pr.get("base") or {}).get("repo") or {}
        owner = (base_repo.get("owner") or {}).get("login")
        snapshot["base"] = {"repo": {"owner": {"login": owner}}}
        if key in seen:
            continue
        seen.add(key)
        meta = metadata.get(key, {})
        if not should_include(repo, pr, meta):
            continue

        # Never persist excluded personal research/staging PRs in public data.
        current[key] = {"repo": repo, "pr": snapshot,
                        "enrichment": historic.get(key, {}).get("enrichment", {})}
        phase = status_of(pr)
        old = historic.get(key)
        enrichment = current[key]["enrichment"]
        has_curated_text = bool(meta.get("what_changed") and meta.get("why_it_matters"))
        # GitHub status always refreshes. Copilot only supplies initial copy for
        # active PRs; terminal (merged/integrated/closed) text remains untouched.
        if phase in {"open", "draft"}:
            if has_curated_text and (not old or not enrichment.get("initial")):
                enrichment["initial"] = "curated"
            elif not enrichment.get("initial") and not has_curated_text:
                triggers.append({"key": key, "phase": "initial", "url": pr["html_url"]})
        buckets["integrated" if integrated_upstream(pr, meta) else phase].append((repo, pr, meta))

    if errors:
        raise RuntimeError(f"{errors} PR fetches failed; refusing incomplete publication")

    # Preserve older entries outside the 1,000-result discovery window.
    for key, record in historic.items():
        if key in seen:
            continue
        repo, pr = record["repo"], record["pr"]
        meta = metadata.get(key, {})
        if should_include(repo, pr, meta):
            buckets["integrated" if integrated_upstream(pr, meta) else status_of(pr)].append((repo, pr, meta))
            current[key] = record

    queue_path = ROOT / "data" / "enrichment_queue.json"
    queue = {"schema_version": 1, "events": triggers[:3], "deferred": max(0, len(triggers) - 3)}
    queue_text = json.dumps(queue, indent=2, ensure_ascii=False, sort_keys=True) + "\n"
    if not queue_path.exists() or queue_path.read_text(encoding="utf-8") != queue_text:
        queue_path.write_text(queue_text, encoding="utf-8")
    for values in buckets.values():
        values.sort(key=sort_key, reverse=True)

    now = dt.datetime.now(dt.timezone.utc).replace(microsecond=0)
    # Manually verified upstream integrations submitted by another author.
    # Curated records persist across sync and do not affect authored-PR counts.
    credited = metadata_doc.get("credited_integrations", [])
    findings = metadata_doc.get("credited_findings", [])
    counts = {k: len(v) for k, v in buckets.items()}
    counts["integrated"] += len(credited)

    lines = [
        "# CoreFoundry Contribution Ledger",
        "",
        "A live public record of upstream open-source work tracked by CoreFoundry.",
        "",
        f"**Merged:** {counts['merged']} · **Integrated separately:** {counts['integrated']} · **Open:** {counts['open']} · **Draft:** {counts['draft']} · **Closed:** {counts['closed']}",
        "",
        f"> **Last synchronized:** {now.strftime('%Y-%m-%d %H:%M UTC')}",
        "",
        "## Record and attribution",
        "",
        "CoreFoundry treats the **upstream pull request as the canonical public record**.",
        "",
        "- upstream PR links are always primary;",
        "- status reflects GitHub PR state, except independently integrated work labeled Integrated;",
        "- contributor forks, local branches, staging repositories, and research harnesses are never required to reconstruct the public record;",
        "- GitHub PR status is synchronized automatically; Copilot only drafts active PR descriptions, while terminal records are frozen.",
        "- closed PRs integrated via another upstream commit are tracked separately, not counted as merged PRs.",
        "",
        "",
    ]

    lines.extend(["## Upstream contributions", ""])
    rows = [row_for(*entry) for key in ("merged", "integrated", "open", "draft", "closed")
            for entry in buckets[key]]
    for item in credited:
        rows.append([
            f"**[{item['repo']} #{item['number']}]({item['url']})**",
            "✅ Integrated",
            escape_cell(concise(item["what_changed"], 150)),
            escape_cell(concise(item["evidence"], 135)),
        ])
    lines.append(render_table(rows) if rows else "_No tracked entries._")
    lines.append("")

    # Curated issue discoveries are distinct from authored PRs and merged counts.
    if findings:
        lines.extend(["## Reported findings resolved upstream", "",
                      "Original upstream issue reports independently validated by the contributor; "
                      "fixes were authored and merged by upstream maintainers.", ""])
        finding_rows = []
        for finding in findings:
            finding_rows.append([
                f"**[{finding['repo']} #{finding['number']}]({finding['url']})**",
                "Fixed upstream" if finding.get("status") == "fixed_upstream" else "Reported",
                escape_cell(concise(finding.get("what_changed"), 190)),
                escape_cell(concise(finding.get("evidence"), 170)),
            ])
        lines.append(render_table(finding_rows))
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
            "2. curated display metadata in `data/contribution_metadata.json`;",
            "3. separately integrated upstream commit evidence and curated credited integrations.",
            "",
            "New public upstream PRs authored by the tracked contributor are discovered automatically. "
            "Closed-but-unmerged work remains visible unless explicitly excluded in metadata.",
            "",
            "> Do not edit this file by hand; changes will be overwritten by the next synchronization run.",
            "",
        ]
    )

    new_text = "\n".join(lines)
    old_text = OUTPUT_PATH.read_text(encoding="utf-8") if OUTPUT_PATH.exists() else ""
    import re
    # Ignore timestamp-only changes; no commit unless the ledger data actually changed.
    old_stamp = re.search(r"Last synchronized:\*\* ([^\n]+)", old_text)
    if old_stamp:
        comparable = re.sub(
            r"Last synchronized:\*\* [^\n]+",
            "Last synchronized:** " + old_stamp.group(1),
            new_text, count=1,
        )
        if comparable == old_text:
            new_text = old_text
    if new_text != old_text:
        OUTPUT_PATH.write_text(new_text, encoding="utf-8")

    registry_text = json.dumps({"schema_version": 1, "entries": current},
                               indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    if not REGISTRY_PATH.exists() or REGISTRY_PATH.read_text(encoding="utf-8") != registry_text:
        REGISTRY_PATH.write_text(registry_text, encoding="utf-8")


if __name__ == "__main__":
    main()
