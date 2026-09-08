#!/usr/bin/env python3
"""Direct Notion API sync for explicitly registered wiki sources."""

from __future__ import annotations

import argparse
import json
import os
import sys
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from wiki_tools import ROOT, build_graph, lint


API = "https://api.notion.com/v1"
API_VERSION = "2026-03-11"
REGISTRY = ROOT / "sources" / "registry.json"
REPORT = ROOT / "generated" / "reports" / "notion-sync-plan.json"


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


def token() -> str:
    value = os.environ.get("NOTION_API_KEY")
    if not value:
        raise RuntimeError("NOTION_API_KEY is not set")
    return value


def api_get(path: str, query: dict[str, Any] | None = None) -> dict[str, Any]:
    url = API + path
    if query:
        url += "?" + urllib.parse.urlencode(query)
    request = urllib.request.Request(
        url,
        headers={
            "Authorization": f"Bearer {token()}",
            "Notion-Version": API_VERSION,
            "User-Agent": "llm-wiki-sync/1",
        },
    )
    for attempt in range(4):
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                return json.load(response)
        except urllib.error.HTTPError as exc:
            if exc.code != 429 or attempt == 3:
                raise
            retry_after = float(exc.headers.get("Retry-After", "1"))
            time.sleep(min(max(retry_after, 0.1), 30))
    raise RuntimeError("Notion request retry loop exited unexpectedly")


def page_id_for(source_id: str) -> str:
    provider, separator, page_id = source_id.partition(":")
    if provider != "notion" or not separator or not page_id:
        raise RuntimeError(f"not a Notion source ID: {source_id}")
    return page_id


def page_title(page: dict[str, Any]) -> str:
    for prop in page.get("properties", {}).values():
        if prop.get("type") == "title":
            return "".join(part.get("plain_text", "") for part in prop.get("title", []))
    return ""


def retrieve_page(source_id: str) -> dict[str, Any]:
    return api_get(f"/pages/{page_id_for(source_id)}")


def retrieve_markdown(page_or_block_id: str) -> dict[str, Any]:
    return api_get(f"/pages/{page_or_block_id}/markdown")


def fetch_markdown_parts(page_id: str) -> list[dict[str, Any]]:
    """Fetch a page plus any large subtrees Notion reports as unknown blocks."""
    pending = [page_id]
    seen = set()
    parts = []
    while pending:
        current = pending.pop(0)
        if current in seen:
            continue
        seen.add(current)
        part = retrieve_markdown(current)
        parts.append(part)
        pending.extend(
            block_id
            for block_id in part.get("unknown_block_ids", [])
            if block_id not in seen
        )
    return parts


def read_registry() -> dict[str, Any]:
    return json.loads(REGISTRY.read_text())


def atomic_write_registry(registry: dict[str, Any]) -> None:
    temporary = REGISTRY.with_suffix(".json.tmp")
    temporary.write_text(json.dumps(registry, ensure_ascii=False, indent=2) + "\n")
    temporary.replace(REGISTRY)


def notion_records(registry: dict[str, Any]) -> list[dict[str, Any]]:
    return [
        item for item in registry["sources"] if item.get("provider") == "notion"
    ]


def plan(write_report: bool) -> dict[str, Any]:
    changes = []
    for record in notion_records(read_registry()):
        source_id = record["source_id"]
        try:
            page = retrieve_page(source_id)
        except urllib.error.HTTPError as exc:
            if exc.code not in {403, 404}:
                raise
            changes.append(
                {
                    "source_id": source_id,
                    "change": "inaccessible-or-deleted",
                    "http_status": exc.code,
                    "title": record.get("title"),
                    "affected_pages": record.get("concepts", []),
                }
            )
            continue
        kinds = []
        live_title = page_title(page)
        live_version = page.get("last_edited_time")
        if live_title and live_title != record.get("title"):
            kinds.append("renamed")
        if live_version != record.get("last_ingested_version"):
            kinds.append("content-changed")
        if kinds:
            changes.append(
                {
                    "source_id": source_id,
                    "change": kinds,
                    "scope": record.get("scope"),
                    "title": live_title or record.get("title"),
                    "latest_version_id": live_version,
                    "affected_pages": record.get("concepts", []),
                }
            )
    result = {
        "planned_at": now(),
        "provider": "notion",
        "api_version": API_VERSION,
        "changes": changes,
        "change_count": len(changes),
    }
    if write_report:
        REPORT.parent.mkdir(parents=True, exist_ok=True)
        REPORT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    return result


def validate_temporary_output(output: Path) -> Path:
    resolved = output.expanduser().resolve()
    temporary_roots = {
        Path(tempfile.gettempdir()).resolve(),
        Path("/tmp").resolve(),
        Path("/private/tmp").resolve(),
    }
    if not any(resolved == root or root in resolved.parents for root in temporary_roots):
        raise RuntimeError("Notion source exports must be written under a temporary directory")
    if resolved.exists():
        raise RuntimeError(f"refusing to overwrite existing export: {resolved}")
    return resolved


def export_source(source_id: str, output: Path) -> Path:
    records = {item["source_id"]: item for item in notion_records(read_registry())}
    if source_id not in records:
        raise RuntimeError(f"Notion source is not registered: {source_id}")
    resolved = validate_temporary_output(output)
    page = retrieve_page(source_id)
    payload = {
        "fetched_at": now(),
        "api_version": API_VERSION,
        "source_id": source_id,
        "page": page,
        "markdown_parts": fetch_markdown_parts(page_id_for(source_id)),
    }
    resolved.parent.mkdir(parents=True, exist_ok=True)
    with resolved.open("x") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    return resolved


def acknowledge(source_ids: list[str]) -> None:
    build_graph()
    report = lint()
    if not report["ok"]:
        raise RuntimeError("lint failed; registry versions were not advanced")
    registry = read_registry()
    records = {item["source_id"]: item for item in registry["sources"]}
    wanted = []
    for source_id in source_ids:
        record = records.get(source_id)
        if not record or record.get("provider") != "notion":
            raise RuntimeError(f"Notion source is not registered: {source_id}")
        wanted.append(record)
    for record in wanted:
        page = retrieve_page(record["source_id"])
        version = page.get("last_edited_time")
        record["title"] = page_title(page) or record["title"]
        record["content_updated_at"] = version
        record["latest_version_id"] = version
        record["last_ingested_version"] = version
        record["last_ingested_at"] = now()
        record["api_version"] = API_VERSION
    registry["generated_at"] = now()
    atomic_write_registry(registry)
    with (ROOT / "log.md").open("a") as handle:
        handle.write(f"\n- Acknowledged processed Notion versions: {', '.join(source_ids)}.\n")


def main() -> int:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    plan_parser = sub.add_parser("plan")
    plan_parser.add_argument("--write-report", action="store_true")
    export_parser = sub.add_parser("export")
    export_parser.add_argument("--source-id", required=True)
    export_parser.add_argument("--output", type=Path, required=True)
    acknowledge_parser = sub.add_parser("acknowledge")
    acknowledge_parser.add_argument("--source-id", action="append", required=True)
    args = parser.parse_args()
    try:
        if args.command == "plan":
            print(json.dumps(plan(args.write_report), ensure_ascii=False, indent=2))
        elif args.command == "export":
            output = export_source(args.source_id, args.output)
            print(f"wrote temporary Notion export: {output}")
        else:
            acknowledge(args.source_id)
            print(f"acknowledged {len(args.source_id)} Notion source versions")
        return 0
    except (RuntimeError, KeyError, urllib.error.URLError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
