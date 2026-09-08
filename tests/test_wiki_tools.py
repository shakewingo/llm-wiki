import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import wiki_tools  # noqa: E402
import sync_yuque  # noqa: E402


class WikiToolsTest(unittest.TestCase):
    def test_graph_is_deterministic_and_nonempty(self):
        first = wiki_tools.build_graph()
        second = wiki_tools.build_graph()
        self.assertEqual(first, second)
        self.assertGreaterEqual(len(first["nodes"]), 20)
        self.assertGreater(len(first["edges"]), 0)

    def test_lint_passes(self):
        report = wiki_tools.lint()
        self.assertTrue(report["ok"], report["errors"])

    def test_alias_collision_is_reported(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            wiki = root / "wiki" / "concepts"
            wiki.mkdir(parents=True)
            (root / "sources").mkdir()
            (root / "sources" / "registry.json").write_text('{"sources": []}')
            body = (
                "---\nid: {id}\ntitle: {id}\ntype: concept\n"
                "domains: [test]\naliases: [Shared]\nsources: []\n---\n# Test\n"
            )
            (wiki / "first.md").write_text(body.format(id="first"))
            (wiki / "second.md").write_text(body.format(id="second"))
            with (
                patch.object(wiki_tools, "ROOT", root),
                patch.object(wiki_tools, "WIKI", root / "wiki"),
                patch.object(wiki_tools, "LINT_PATH", root / "lint.json"),
            ):
                report = wiki_tools.lint()
            self.assertTrue(any("shared" in error for error in report["errors"]))

    def test_obsidian_links_are_generated_and_idempotent(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            wiki = root / "wiki" / "concepts"
            wiki.mkdir(parents=True)
            (root / "sources").mkdir()
            (root / "sources" / "registry.json").write_text(
                '{"sources": [{"source_id": "yuque:1"}]}'
            )
            (wiki / "first.md").write_text(
                "---\nid: first\ntitle: First\ntype: concept\n"
                "relations:\n  enables: [second]\nsources: [yuque:1]\n"
                "---\n# First\n"
            )
            (wiki / "second.md").write_text(
                "---\nid: second\ntitle: Second Concept\ntype: concept\n"
                "relations: {}\nsources: [yuque:1]\n---\n# Second\n"
            )
            with (
                patch.object(wiki_tools, "ROOT", root),
                patch.object(wiki_tools, "WIKI", root / "wiki"),
                patch.object(wiki_tools, "LINT_PATH", root / "lint.json"),
            ):
                first = wiki_tools.write_obsidian_links()
                after_first = (wiki / "first.md").read_text()
                second = wiki_tools.write_obsidian_links()
                (wiki / "first.md").write_text(
                    after_first.replace(
                        "[[second|Second Concept]]", "[[second|Stale Title]]"
                    )
                )
                stale_report = wiki_tools.lint()
            self.assertEqual(first, {"pages": 2, "changed": 2})
            self.assertEqual(second, {"pages": 2, "changed": 0})
            self.assertIn("- Enables: [[second|Second Concept]]", after_first)
            self.assertEqual(after_first.count(wiki_tools.OBSIDIAN_BEGIN), 1)
            self.assertTrue(
                any("stale generated Obsidian" in error for error in stale_report["errors"])
            )


class SyncPlanTest(unittest.TestCase):
    def test_new_updated_renamed_deleted_and_unchanged(self):
        old_sources = [
            self.record(1, "Same", "2026-01-01"),
            self.record(2, "Old title", "2026-01-01"),
            self.record(3, "Deleted", "2026-01-01"),
        ]
        live = [
            self.document(1, "Same", "2026-01-01"),
            self.document(2, "New title", "2026-02-01"),
            self.document(4, "New", "2026-02-01"),
        ]
        with tempfile.TemporaryDirectory() as directory:
            registry = Path(directory) / "registry.json"
            registry.write_text(__import__("json").dumps({"sources": old_sources}))
            with (
                patch.object(sync_yuque, "REGISTRY", registry),
                patch.object(sync_yuque, "list_documents", return_value=live),
                patch.object(
                    sync_yuque,
                    "fetch_details",
                    side_effect=lambda documents: [
                        {**doc, "latest_version_id": 2 if doc["id"] == 2 else 1}
                        for doc in documents
                    ],
                ),
            ):
                result = sync_yuque.plan(False)
        changes = {item["source_id"]: item["change"] for item in result["changes"]}
        self.assertNotIn("yuque:1", changes)
        self.assertEqual(
            changes["yuque:2"], ["renamed", "version-changed", "content-changed"]
        )
        self.assertEqual(changes["yuque:3"], "inaccessible-or-deleted")
        self.assertEqual(changes["yuque:4"], "new")

    def test_partial_bootstrap_failure_preserves_registry(self):
        with tempfile.TemporaryDirectory() as directory:
            registry = Path(directory) / "registry.json"
            original = '{"sources": [{"source_id": "yuque:1"}]}\n'
            registry.write_text(original)
            with (
                patch.object(sync_yuque, "REGISTRY", registry),
                patch.object(sync_yuque, "list_documents", return_value=[]),
                patch.object(sync_yuque, "fetch_details", side_effect=RuntimeError("boom")),
            ):
                with self.assertRaises(RuntimeError):
                    sync_yuque.bootstrap(False)
            self.assertEqual(registry.read_text(), original)

    @staticmethod
    def record(source_id, title, updated):
        return {
            "source_id": f"yuque:{source_id}",
            "title": title,
            "content_updated_at": updated,
            "scope": "core",
            "concepts": [],
            "latest_version_id": 1,
        }

    @staticmethod
    def document(source_id, title, updated):
        return {
            "id": source_id,
            "title": title,
            "content_updated_at": updated,
        }


if __name__ == "__main__":
    unittest.main()
