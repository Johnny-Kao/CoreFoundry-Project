import importlib.util
import json
import tempfile
import unittest
import urllib.error
from pathlib import Path
from unittest import mock

SPEC = importlib.util.spec_from_file_location("sync", Path(__file__).resolve().parents[1] / "scripts/sync_contributions.py")
sync = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(sync)


def pr(repo="upstream/library", number=1, state="open", merged=False, draft=False):
    return {"number": number, "html_url": f"https://github.com/{repo}/pull/{number}",
            "title": "Avoid repeated allocations", "state": state,
            "draft": draft, "merged_at": "2026-01-01T00:00:00Z" if merged else None,
            "merge_commit_sha": "abcdef012345", "updated_at": "2026-01-01T00:00:00Z",
            "closed_at": None, "created_at": "2025-01-01T00:00:00Z",
            "base": {"repo": {"owner": {"login": "upstream"}}}}


class LedgerTests(unittest.TestCase):
    def test_state_classification(self):
        self.assertEqual(sync.status_of(pr(merged=True)), "merged")
        self.assertEqual(sync.status_of(pr(draft=True)), "draft")
        self.assertEqual(sync.status_of(pr()), "open")
        self.assertEqual(sync.status_of(pr(state="closed")), "closed")

    def test_closed_retained_and_personal_excluded(self):
        self.assertTrue(sync.should_include("upstream/library", pr(state="closed"), {}))
        sample = pr()
        sample["base"]["repo"]["owner"]["login"] = sync.AUTHOR
        self.assertFalse(sync.should_include("Johnny-Kao/research", sample, {}))
        self.assertFalse(sync.should_include("upstream/library", pr(), {"include": False}))

    def test_noop_and_historical_retention(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "data").mkdir()
            readme = "Header\n\n**[View the live contribution ledger →](CONTRIBUTIONS.md)**\n"
            (root / "README.md").write_text(readme, encoding="utf-8")
            (root / "data" / "contribution_metadata.json").write_text('{"entries": {}}', encoding="utf-8")
            existing = pr(number=45, state="closed")
            registry = {"schema_version": 1, "entries": {"upstream/library#45": {"repo": "upstream/library", "pr": existing}}}
            (root / "data" / "contribution_registry.json").write_text(json.dumps(registry), encoding="utf-8")
            with mock.patch.multiple(sync, METADATA_PATH=root / "data" / "contribution_metadata.json",
                                     OUTPUT_PATH=root / "CONTRIBUTIONS.md",
                                     README_PATH=root / "README.md",
                                     REGISTRY_PATH=root / "data" / "contribution_registry.json"), \
                 mock.patch.object(sync, "discover_prs", return_value=[]):
                sync.main()
                ledger = (root / "CONTRIBUTIONS.md").read_text()
                self.assertIn("upstream/library #45", ledger)
                self.assertIn("**Open PRs:** 0 | **Merged PRs:** 0", (root / "README.md").read_text())
                first = {x: (root / x).read_bytes() for x in ("CONTRIBUTIONS.md", "README.md", "data/contribution_registry.json")}
                sync.main()
                self.assertEqual(first, {x: (root / x).read_bytes() for x in first})

    def test_failed_pr_fetch_never_publishes(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "data").mkdir()
            (root / "data" / "contribution_metadata.json").write_text('{"entries": {}}')
            old = "DO NOT OVERWRITE"
            (root / "CONTRIBUTIONS.md").write_text(old)
            with mock.patch.multiple(sync, METADATA_PATH=root / "data" / "contribution_metadata.json",
                                     OUTPUT_PATH=root / "CONTRIBUTIONS.md", REGISTRY_PATH=root / "data" / "registry.json"), \
                 mock.patch.object(sync, "discover_prs", return_value=[{"html_url": "https://github.com/upstream/library/pull/1"}]), \
                 mock.patch.object(sync, "fetch_pr", side_effect=urllib.error.URLError("offline")):
                with self.assertRaises(RuntimeError):
                    sync.main()
                self.assertEqual((root / "CONTRIBUTIONS.md").read_text(), old)


if __name__ == "__main__":
    unittest.main()
