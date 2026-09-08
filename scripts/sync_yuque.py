#!/usr/bin/env python3
"""Metadata-only Yuque inventory, change planning, and version acknowledgement."""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from typing import Any

from wiki_tools import ROOT, build_graph, lint, load_pages


API = "https://www.yuque.com/api/v2"
REGISTRY = ROOT / "sources" / "registry.json"
REPORT = ROOT / "generated" / "reports" / "sync-plan.json"
PILOT_IDS = {
    145104021,
    145901413,
    241299652,
    267998961,
    267998979,
    271488122,
    279560513,
    283802487,
}
CORE_TITLES = {
    "Attention is All You Need",
    "BERT",
    "Causal Structure Learning Algo",
    "DSA / CSA/ HCA",
    "DeepSeek Paper Reading",
    "Diffusion Model",
    "Direct Preference Optimization (DPO)",
    "Engram",
    "Knowledge Puzzle",
    "LLaMA",
    "MLA",
    "ML Knowledge",
    "MTP",
    "Prompt Caching and Prefix Cache",
    "Reinforcement Learning from Human Feedback (RLHF)",
    "Retrieval Augmented Generation (RAG）",
    "Stats / ML Algorithm Overview",
    "Time-Series Anomaly Detection Service at Microsoft (SR-CNN)",
    "Unsupervised Anomaly Detection with Variational Auto-Encoder and Local Outliers Factor for KPIs",
    "mHC",
}
PROJECT_TITLES = {
    "AI Agent",
    "CC源码解读 - 0331v",
    "Code Vision Multimodel from Scratch",
    "Nanobot Code Review",
    "Openclaw/Nanobot",
    "RCA Agent w langgraph",
    "VoiceChatBot for the Dead (仿真已故亲人聊天机器人)",
}
REFERENCE_TITLES = {
    "Distributed Framework",
    "For AI Engineer Interview",
    "Gatech EIC",
    "Gatech CS6601 - AI",
    "Gatech CS7641 - ML",
    "GetHandsDirty",
    "MLi Paper Reading",
    "Nvidia Agentic AI Training",
    "动手学深度学习pytorch版",
}
EXCLUDED_TITLES = {
    "(TBC) Threshold-free Anomaly Detection for Streaming Time Series through Deep Learning (Jingdong)",
    "AI 4 Alzheimer's",
    "AI Engineer Roadmap",
    "Agent Architecture",
    "Articles",
    "Cost",
    "Gatech CS6457 - VGD",
    "Google Tunix Hack",
    "Hackathon",
    "JD - Data Engineer",
    "LLM",
    "Mila",
    "My Game-Style Blog",
    "Paper to read",
    "Practice on Kaggle",
    "Roadmap Progress Hint",
    "School AI Lab",
    "Supplementary",
    "Team Project",
    "Weekly Priority Tracker",
    "离职冲刺日记",
    "💡 1 分钟玩转语雀文档",
}


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


def token() -> str:
    value = os.environ.get("YUQUE_API_KEY")
    if not value:
        raise RuntimeError("YUQUE_API_KEY is not set")
    return value


def api_get(path: str) -> dict[str, Any]:
    request = urllib.request.Request(
        API + path,
        headers={"X-Auth-Token": token(), "User-Agent": "llm-wiki-sync/1"},
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)["data"]


def fetch_detail(doc: dict[str, Any]) -> dict[str, Any]:
    detail = api_get(f"/repos/{doc['namespace']}/docs/{doc['slug']}")
    return {
        **doc,
        "latest_version_id": detail.get("latest_version_id"),
        "content_updated_at": detail.get("content_updated_at"),
        "word_count": detail.get("word_count", 0),
    }


def list_documents() -> list[dict[str, Any]]:
    repos = api_get("/users/shakewin/repos?offset=0")
    documents: list[dict[str, Any]] = []
    for repo in repos:
        namespace = repo["namespace"]
        for doc in api_get(f"/repos/{namespace}/docs?limit=100"):
            documents.append(
                {
                    "namespace": namespace,
                    "knowledge_base_name": repo["name"],
                    "id": doc["id"],
                    "slug": doc["slug"],
                    "title": doc["title"],
                    "status": doc.get("status"),
                    "public": bool(doc.get("public")),
                    "content_updated_at": doc.get("content_updated_at"),
                    "word_count": doc.get("word_count", 0),
                }
            )
    return documents


def fetch_details(documents: list[dict[str, Any]]) -> list[dict[str, Any]]:
    results = []
    with ThreadPoolExecutor(max_workers=8) as pool:
        futures = {pool.submit(fetch_detail, doc): doc for doc in documents}
        for future in as_completed(futures):
            results.append(future.result())
    return sorted(results, key=lambda doc: (doc["namespace"], doc["title"], doc["id"]))


def scope_for(doc: dict[str, Any]) -> tuple[str, str]:
    title = doc["title"]
    if title in CORE_TITLES:
        return "core", "Direct AI/LLM concept material; provisional pending user review."
    if title in PROJECT_TITLES:
        return "project-evidence", "Implementation evidence; provisional pending user review."
    if title in REFERENCE_TITLES:
        return "reference", "Useful context or curriculum; provisional pending user review."
    if title in EXCLUDED_TITLES or not doc.get("word_count"):
        return "excluded", "Empty, personal, administrative, or out of pilot scope."
    return "unreviewed", "Content must be reviewed before inclusion."


def source_concepts() -> dict[str, list[str]]:
    concepts: dict[str, list[str]] = {}
    pages, _ = load_pages()
    for page in pages:
        for source_id in page.get("sources") or []:
            concepts.setdefault(source_id, []).append(page["id"])
    return {key: sorted(set(value)) for key, value in concepts.items()}


def atomic_write_registry(registry: dict[str, Any]) -> None:
    REGISTRY.parent.mkdir(parents=True, exist_ok=True)
    temporary = REGISTRY.with_suffix(".json.tmp")
    temporary.write_text(json.dumps(registry, ensure_ascii=False, indent=2) + "\n")
    temporary.replace(REGISTRY)


def bootstrap(mark_pilot: bool) -> dict[str, Any]:
    previous = {}
    if REGISTRY.exists():
        previous = {
            item["source_id"]: item
            for item in json.loads(REGISTRY.read_text()).get("sources", [])
        }
    concepts = source_concepts()
    records = []
    for doc in fetch_details(list_documents()):
        source_id = f"yuque:{doc['id']}"
        old = previous.get(source_id, {})
        scope, reason = scope_for(doc)
        latest = doc.get("latest_version_id")
        ingested = old.get("last_ingested_version")
        if mark_pilot and doc["id"] in PILOT_IDS:
            ingested = latest
        records.append(
            {
                "source_id": source_id,
                "provider": "yuque",
                "knowledge_base": doc["namespace"],
                "knowledge_base_name": doc["knowledge_base_name"],
                "slug": doc["slug"],
                "title": doc["title"],
                "url": f"https://www.yuque.com/{doc['namespace']}/{doc['slug']}",
                "content_updated_at": doc.get("content_updated_at"),
                "latest_version_id": latest,
                "last_ingested_version": ingested,
                "scope": old.get("scope", scope),
                "scope_reason": old.get("scope_reason", reason),
                "concepts": concepts.get(source_id, []),
                "public": doc["public"],
                "status": doc["status"],
                "word_count": doc["word_count"],
            }
        )
    registry = {
        "schema_version": 1,
        "generated_at": now(),
        "scope_review": "provisional",
        "sources": sorted(records, key=lambda item: item["source_id"]),
    }
    atomic_write_registry(registry)
    return registry


def plan(write_report: bool) -> dict[str, Any]:
    registry = json.loads(REGISTRY.read_text())
    old_by_id = {item["source_id"]: item for item in registry["sources"]}
    live = list_documents()
    included = {"core", "project-evidence", "reference"}
    detailed = fetch_details(
        [
            doc
            for doc in live
            if old_by_id.get(f"yuque:{doc['id']}", {}).get("scope") in included
        ]
    )
    details_by_id = {doc["id"]: doc for doc in detailed}
    live = [{**doc, **details_by_id.get(doc["id"], {})} for doc in live]
    live_by_id = {f"yuque:{doc['id']}": doc for doc in live}
    changes = []
    for source_id, doc in sorted(live_by_id.items()):
        old = old_by_id.get(source_id)
        if old is None:
            changes.append({"source_id": source_id, "change": "new", "title": doc["title"]})
            continue
        kinds = []
        if doc["title"] != old["title"]:
            kinds.append("renamed")
        if (
            doc.get("latest_version_id") is not None
            and doc.get("latest_version_id") != old.get("latest_version_id")
        ):
            kinds.append("version-changed")
        if doc.get("content_updated_at") != old.get("content_updated_at"):
            kinds.append("content-changed")
        if kinds:
            changes.append(
                {
                    "source_id": source_id,
                    "change": kinds,
                    "scope": old["scope"],
                    "title": doc["title"],
                    "latest_version_id": doc.get("latest_version_id"),
                    "affected_pages": old.get("concepts", []),
                }
            )
    for source_id, old in sorted(old_by_id.items()):
        if source_id not in live_by_id:
            changes.append(
                {
                    "source_id": source_id,
                    "change": "inaccessible-or-deleted",
                    "scope": old["scope"],
                    "title": old["title"],
                    "affected_pages": old.get("concepts", []),
                }
            )
    result = {"planned_at": now(), "changes": changes, "change_count": len(changes)}
    if write_report:
        REPORT.parent.mkdir(parents=True, exist_ok=True)
        REPORT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    return result


def acknowledge(source_ids: list[str]) -> None:
    build_graph()
    report = lint()
    if not report["ok"]:
        raise RuntimeError("lint failed; registry versions were not advanced")
    registry = json.loads(REGISTRY.read_text())
    records = {item["source_id"]: item for item in registry["sources"]}
    wanted = [records[source_id] for source_id in source_ids]
    docs = [
        {
            "namespace": item["knowledge_base"],
            "knowledge_base_name": item["knowledge_base_name"],
            "id": int(item["source_id"].split(":", 1)[1]),
            "slug": item["slug"],
            "title": item["title"],
            "status": item["status"],
            "public": item["public"],
            "word_count": item["word_count"],
        }
        for item in wanted
    ]
    for detail in fetch_details(docs):
        item = records[f"yuque:{detail['id']}"]
        item["latest_version_id"] = detail["latest_version_id"]
        item["last_ingested_version"] = detail["latest_version_id"]
        item["content_updated_at"] = detail["content_updated_at"]
        item["last_ingested_at"] = now()
    registry["generated_at"] = now()
    atomic_write_registry(registry)
    with (ROOT / "log.md").open("a") as handle:
        handle.write(f"\n- Acknowledged processed versions: {', '.join(source_ids)}.\n")


def main() -> int:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    bootstrap_parser = sub.add_parser("bootstrap")
    bootstrap_parser.add_argument("--mark-pilot", action="store_true")
    plan_parser = sub.add_parser("plan")
    plan_parser.add_argument("--write-report", action="store_true")
    acknowledge_parser = sub.add_parser("acknowledge")
    acknowledge_parser.add_argument("--source-id", action="append", required=True)
    args = parser.parse_args()
    try:
        if args.command == "bootstrap":
            registry = bootstrap(args.mark_pilot)
            print(f"wrote {len(registry['sources'])} source records")
        elif args.command == "plan":
            print(json.dumps(plan(args.write_report), ensure_ascii=False, indent=2))
        else:
            acknowledge(args.source_id)
            print(f"acknowledged {len(args.source_id)} source versions")
        return 0
    except (RuntimeError, KeyError, urllib.error.URLError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
