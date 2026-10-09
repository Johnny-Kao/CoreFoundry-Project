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

    def test_invalid_json_type_rejected(self):
        self.assertIsNone(agent.validate(["not a record"], [{"url": "https://example.com", "text": "x"}]))


if __name__ == "__main__":
    unittest.main()
