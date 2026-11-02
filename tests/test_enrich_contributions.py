import importlib.util
import sys
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))
import enrich_contributions as agent


class NegativeGateTests(unittest.TestCase):
    def test_unsupported_performance_claim_removed_without_discarding_entry(self):
        sources = [{"url": "https://github.com/example/lib/pull/1",
                    "text": "Remove redundant allocations from a lookup path"}]
        output = agent.validate({
            "what_it_is": "Library infrastructure",
            "what_changed": "Removed redundant allocations",
            "evidence": "99% faster in production",
            "why_it_matters": "Reduced repeated work",
            "source_urls": ["https://invalid.example/claim"],
        }, sources)
        self.assertEqual(output["evidence"], "")
        self.assertEqual(output["what_changed"], "Removed redundant allocations")
        self.assertEqual(output["source_urls"], [sources[0]["url"]])

    def test_missing_benchmark_does_not_block(self):
        sources = [{"url": "https://github.com/example/lib/pull/2",
                    "text": "Fix incorrect edge-case handling"}]
        output = agent.validate({
            "what_it_is": "Core library",
            "what_changed": "Fixed edge-case handling",
            "evidence": "",
            "why_it_matters": "Correctness",
            "source_urls": [sources[0]["url"]],
        }, sources)
        self.assertEqual(output["evidence"], "")
        self.assertEqual(output["what_changed"], "Fixed edge-case handling")

    def test_merged_entry_skips_copilot_and_source_fetch(self):
        from unittest import mock
        event = {"key": "example/lib#1", "phase": "terminal", "url": "https://github.com/example/lib/pull/1"}
        registry = {"entries": {"example/lib#1": {"pr": {"merged_at": "2026-11-01T00:00:00Z", "state": "closed"}}}}
        metadata = {"entries": {"example/lib#1": {"what_changed": "Curated final summary"}}}
        with mock.patch.object(agent, "sources_for", side_effect=AssertionError("should not fetch")):
            self.assertFalse(agent.enrich(event, metadata, registry))
        self.assertEqual(metadata["entries"]["example/lib#1"]["what_changed"], "Curated final summary")

    def test_invalid_json_type_rejected(self):
        self.assertIsNone(agent.validate(["not a record"], [{"url": "https://example.com", "text": "x"}]))


if __name__ == "__main__":
    unittest.main()
