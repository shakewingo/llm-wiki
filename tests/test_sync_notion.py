import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import sync_notion  # noqa: E402


SOURCE_ID = "notion:388cad4f-b605-8074-8c53-ff558a15beb0"


def page(title="Alisa’s book of LLMs", edited="2026-09-04T09:44:00.000Z"):
    return {
        "id": SOURCE_ID.split(":", 1)[1],
        "last_edited_time": edited,
        "properties": {
            "Document Title": {
                "type": "title",
                "title": [{"plain_text": title}],
            }
        },
    }


def registry(version="2026-09-04T09:44:00.000Z"):
    return {
        "sources": [
            {
                "source_id": SOURCE_ID,
                "provider": "notion",
                "title": "Alisa’s book of LLMs",
                "scope": "reference",
                "concepts": ["transformer-architecture"],
                "last_ingested_version": version,
            },
            {"source_id": "yuque:1", "provider": "yuque"},
        ]
    }


class NotionSyncTest(unittest.TestCase):
    def test_plan_detects_content_and_title_changes(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "registry.json"
            path.write_text(json.dumps(registry("2026-01-01T00:00:00.000Z")))
            with (
                patch.object(sync_notion, "REGISTRY", path),
                patch.object(
                    sync_notion,
                    "retrieve_page",
                    return_value=page("Renamed", "2026-02-01T00:00:00.000Z"),
                ),
            ):
                result = sync_notion.plan(False)
        self.assertEqual(result["change_count"], 1)
        self.assertEqual(result["changes"][0]["change"], ["renamed", "content-changed"])
        self.assertEqual(result["changes"][0]["affected_pages"], ["transformer-architecture"])

    def test_plan_is_empty_at_acknowledged_version(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "registry.json"
            path.write_text(json.dumps(registry()))
            with (
                patch.object(sync_notion, "REGISTRY", path),
                patch.object(sync_notion, "retrieve_page", return_value=page()),
            ):
                result = sync_notion.plan(False)
        self.assertEqual(result["changes"], [])

    def test_fetch_markdown_follows_unknown_blocks(self):
        responses = [
            {
                "id": "root",
                "markdown": "root",
                "unknown_block_ids": ["nested"],
            },
            {
                "id": "nested",
                "markdown": "nested",
                "unknown_block_ids": [],
            },
        ]
        with patch.object(sync_notion, "retrieve_markdown", side_effect=responses) as get:
            parts = sync_notion.fetch_markdown_parts("root")
        self.assertEqual([part["id"] for part in parts], ["root", "nested"])
        self.assertEqual(get.call_count, 2)

    def test_export_requires_temporary_output(self):
        with self.assertRaisesRegex(RuntimeError, "temporary directory"):
            sync_notion.validate_temporary_output(Path.cwd() / "notion.json")

    def test_acknowledge_updates_only_after_validation(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = root / "registry.json"
            path.write_text(json.dumps(registry("old")))
            (root / "log.md").write_text("")
            with (
                patch.object(sync_notion, "ROOT", root),
                patch.object(sync_notion, "REGISTRY", path),
                patch.object(sync_notion, "build_graph"),
                patch.object(sync_notion, "lint", return_value={"ok": True}),
                patch.object(sync_notion, "retrieve_page", return_value=page()),
            ):
                sync_notion.acknowledge([SOURCE_ID])
            record = json.loads(path.read_text())["sources"][0]
        self.assertEqual(record["last_ingested_version"], page()["last_edited_time"])
        self.assertEqual(record["api_version"], sync_notion.API_VERSION)


if __name__ == "__main__":
    unittest.main()
