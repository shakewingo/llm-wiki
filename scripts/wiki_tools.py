#!/usr/bin/env python3
"""Generate the concept graph and lint the maintained Markdown wiki."""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "wiki"
GRAPH_PATH = ROOT / "generated" / "graph.json"
LINT_PATH = ROOT / "generated" / "reports" / "lint.json"
ALLOWED_RELATIONS = {
    "prerequisites",
    "part_of",
    "enables",
    "used_by",
    "contrasts_with",
    "affects",
    "optimized_by",
    "implemented_in",
}
SOURCE_ID_PATTERNS = {
    "yuque": re.compile(r"^yuque:\d+$"),
    "notion": re.compile(
        r"^notion:[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$"
    ),
}
RELATION_LABELS = {
    "prerequisites": "Prerequisites",
    "part_of": "Part of",
    "enables": "Enables",
    "used_by": "Used by",
    "contrasts_with": "Contrasts with",
    "affects": "Affects",
    "optimized_by": "Optimized by",
    "implemented_in": "Implemented in",
}
OBSIDIAN_BEGIN = "<!-- BEGIN GENERATED OBSIDIAN LINKS -->"
OBSIDIAN_END = "<!-- END GENERATED OBSIDIAN LINKS -->"


def atomic_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")
    temporary.replace(path)


def read_page(path: Path) -> dict[str, Any]:
    text = path.read_text()
    if not text.startswith("---\n"):
        raise ValueError("missing YAML frontmatter")
    try:
        frontmatter, _ = text[4:].split("\n---\n", 1)
    except ValueError as exc:
        raise ValueError("unterminated YAML frontmatter") from exc
    data = yaml.safe_load(frontmatter) or {}
    if not isinstance(data, dict):
        raise ValueError("frontmatter must be a mapping")
    data["_path"] = path
    return data


def load_pages() -> tuple[list[dict[str, Any]], list[str]]:
    pages: list[dict[str, Any]] = []
    errors: list[str] = []
    for path in sorted(WIKI.rglob("*.md")):
        try:
            pages.append(read_page(path))
        except (OSError, ValueError, yaml.YAMLError) as exc:
            errors.append(f"{path.relative_to(ROOT)}: {exc}")
    return pages, errors


def load_source_ids() -> set[str]:
    path = ROOT / "sources" / "registry.json"
    if not path.exists():
        return set()
    registry = json.loads(path.read_text())
    return {item["source_id"] for item in registry.get("sources", [])}


def load_source_records() -> list[dict[str, Any]]:
    path = ROOT / "sources" / "registry.json"
    if not path.exists():
        return []
    return json.loads(path.read_text()).get("sources", [])


def render_obsidian_block(
    page: dict[str, Any], pages_by_id: dict[str, dict[str, Any]]
) -> str:
    """Render typed frontmatter relations as links understood by Obsidian."""
    lines = [OBSIDIAN_BEGIN, "## Obsidian relationships", ""]
    relations = page.get("relations") or {}
    found = False
    for relation, label in RELATION_LABELS.items():
        targets = relations.get(relation) or []
        if not targets:
            continue
        found = True
        links = []
        for target in targets:
            title = str(pages_by_id.get(target, {}).get("title", target))
            title = title.replace("|", "-").replace("\n", " ")
            links.append(f"[[{target}|{title}]]")
        lines.append(f"- {label}: {', '.join(links)}")
    if not found:
        lines.append("- No typed relationships.")
    lines.extend(["", OBSIDIAN_END])
    return "\n".join(lines)


def write_obsidian_links() -> dict[str, int]:
    """Insert or refresh a generated Obsidian relationship block on every page."""
    pages, errors = load_pages()
    if errors:
        raise ValueError("\n".join(errors))
    pages_by_id = {page["id"]: page for page in pages if page.get("id")}
    block_pattern = re.compile(
        rf"\n*{re.escape(OBSIDIAN_BEGIN)}.*?{re.escape(OBSIDIAN_END)}\n*",
        re.DOTALL,
    )
    changed = 0
    for page in pages:
        path = page["_path"]
        original = path.read_text()
        without_block = block_pattern.sub("\n", original).rstrip()
        updated = f"{without_block}\n\n{render_obsidian_block(page, pages_by_id)}\n"
        if updated == original:
            continue
        temporary = path.with_suffix(path.suffix + ".tmp")
        temporary.write_text(updated)
        temporary.replace(path)
        changed += 1
    return {"pages": len(pages), "changed": changed}


def build_graph() -> dict[str, Any]:
    pages, errors = load_pages()
    if errors:
        raise ValueError("\n".join(errors))
    nodes = []
    edges = []
    for page in pages:
        page_id = page.get("id")
        if not page_id:
            continue
        nodes.append(
            {
                "id": page_id,
                "title": page.get("title", page_id),
                "type": page.get("type", "unknown"),
                "domains": page.get("domains", []),
                "aliases": page.get("aliases", []),
                "sources": page.get("sources", []),
                "path": str(page["_path"].relative_to(ROOT)),
            }
        )
        relations = page.get("relations") or {}
        for relation, targets in sorted(relations.items()):
            for target in targets or []:
                edges.append({"source": page_id, "target": target, "type": relation})
    nodes.sort(key=lambda node: node["id"])
    edges.sort(key=lambda edge: (edge["source"], edge["type"], edge["target"]))
    graph = {"schema_version": 2, "nodes": nodes, "edges": edges}
    atomic_json(GRAPH_PATH, graph)
    return graph


def markdown_link_errors() -> list[str]:
    errors = []
    pattern = re.compile(r"\[[^]]+\]\(([^)]+)\)")
    for path in sorted(ROOT.rglob("*.md")):
        for destination in pattern.findall(path.read_text()):
            destination = destination.strip()
            if destination.startswith(("http://", "https://", "mailto:", "#")):
                continue
            raw_target = destination.split("#", 1)[0].split("?", 1)[0]
            if not raw_target:
                continue
            target = (path.parent / raw_target).resolve()
            if not target.exists():
                errors.append(
                    f"{path.relative_to(ROOT)}: broken link to {destination}"
                )
    return errors


def lint() -> dict[str, Any]:
    pages, errors = load_pages()
    errors.extend(markdown_link_errors())
    warnings: list[str] = []
    by_id: dict[str, dict[str, Any]] = {}
    aliases: dict[str, list[str]] = defaultdict(list)
    source_ids = load_source_ids()
    source_records = load_source_records()

    seen_source_ids: set[str] = set()
    for source in source_records:
        source_id = source.get("source_id")
        provider = source.get("provider")
        if source_id in seen_source_ids:
            errors.append(f"sources/registry.json: duplicate source {source_id}")
        seen_source_ids.add(source_id)
        pattern = SOURCE_ID_PATTERNS.get(provider)
        if pattern is None:
            errors.append(
                f"sources/registry.json: unsupported provider {provider!r} for {source_id}"
            )
        elif not isinstance(source_id, str) or not pattern.fullmatch(source_id):
            errors.append(
                f"sources/registry.json: invalid {provider} source id {source_id!r}"
            )

    for page in pages:
        path = page["_path"].relative_to(ROOT)
        page_id = page.get("id")
        if not page_id:
            errors.append(f"{path}: missing id")
            continue
        if page_id in by_id:
            errors.append(f"{path}: duplicate id {page_id}")
        by_id[page_id] = page
        if page["_path"].stem != page_id:
            errors.append(f"{path}: filename must match id {page_id}")
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", page_id):
            errors.append(f"{path}: id is not lowercase kebab-case")
        for alias in page.get("aliases") or []:
            aliases[str(alias).casefold()].append(page_id)
        for source_id in page.get("sources") or []:
            if source_id not in source_ids:
                errors.append(f"{path}: unknown source {source_id}")
        if page.get("type") == "concept" and not page.get("sources"):
            errors.append(f"{path}: concept has no evidence source")

    for alias, owners in sorted(aliases.items()):
        if len(set(owners)) > 1:
            errors.append(f"alias {alias!r} is shared by {sorted(set(owners))}")

    for page_id, page in by_id.items():
        path = page["_path"].relative_to(ROOT)
        text = page["_path"].read_text()
        expected = render_obsidian_block(page, by_id)
        if expected not in text:
            errors.append(
                f"{path}: missing or stale generated Obsidian relationship block"
            )

    related: set[str] = set()
    map_entries: set[str] = set()
    for page_id, page in by_id.items():
        path = page["_path"].relative_to(ROOT)
        relations = page.get("relations") or {}
        unknown = set(relations) - ALLOWED_RELATIONS
        if unknown:
            errors.append(f"{path}: unknown relation keys {sorted(unknown)}")
        for relation, targets in relations.items():
            for target in targets or []:
                if target not in by_id:
                    errors.append(f"{path}: {relation} points to unknown id {target}")
                else:
                    related.update((page_id, target))
                if relation == "contrasts_with" and target in by_id:
                    reverse = (by_id[target].get("relations") or {}).get(
                        "contrasts_with", []
                    )
                    if page_id not in reverse:
                        errors.append(
                            f"{path}: contrasts_with {target} is not symmetric"
                        )
        for entry in page.get("entry_points") or []:
            map_entries.add(entry)
            if entry not in by_id:
                errors.append(f"{path}: unknown map entry point {entry}")

    for page_id, page in sorted(by_id.items()):
        if page.get("type") == "concept" and page_id not in related | map_entries:
            warnings.append(f"orphan concept: {page_id}")

    report = {
        "ok": not errors,
        "errors": sorted(set(errors)),
        "warnings": sorted(set(warnings)),
        "counts": {
            "pages": len(pages),
            "concepts": sum(page.get("type") == "concept" for page in pages),
            "errors": len(set(errors)),
            "warnings": len(set(warnings)),
        },
    }
    atomic_json(LINT_PATH, report)
    return report


def append_log(message: str) -> None:
    timestamp = datetime.now(timezone.utc).isoformat()
    with (ROOT / "log.md").open("a") as handle:
        handle.write(f"\n- {timestamp}: {message}\n")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=("graph", "lint", "obsidian"))
    args = parser.parse_args()
    if args.command == "graph":
        graph = build_graph()
        print(f"wrote {len(graph['nodes'])} nodes and {len(graph['edges'])} edges")
        return 0
    if args.command == "obsidian":
        result = write_obsidian_links()
        print(
            f"refreshed Obsidian links on {result['pages']} pages "
            f"({result['changed']} changed)"
        )
        return 0
    report = lint()
    append_log(
        f"Lint completed with {report['counts']['errors']} errors and "
        f"{report['counts']['warnings']} warnings."
    )
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
