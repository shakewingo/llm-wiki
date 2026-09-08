# Design

## Goal and ownership

The wiki is a compounding AI-domain knowledge system for big-picture navigation,
technical review, and interview practice. Yuque owns complete notes; the local
registry owns source metadata; Markdown owns synthesized knowledge and typed
relationships; generated files provide graph and health-check views.

## Evidence from the legacy Notion graph

The Notion database `🧠 AI Knowledge Map` has one data source, one table view, nine
knowledge rows, and one operational `graph` row. Its fields are `Name`, `Domain`,
`Level`, `Status`, `Tags`, `Type`, `Yuque Link`, and two reciprocal sides of the
same self-relation: `Related Concepts` and `Related Concepts 1`.

The relation has no declared direction or semantics. Therefore Notion page IDs are
retained in the migration inventory, but legacy links are not promoted to
`prerequisites`, `enables`, or another typed relation without content evidence.

## Structure

```text
llm-wiki/
├── AGENTS.md
├── index.md
├── log.md
├── sources/registry.json
├── wiki/{maps,concepts,comparisons,interview}/
├── generated/{graph.json,reports/}
├── templates/
├── scripts/
└── tests/
```

## Canonical frontmatter

Concept IDs are stable lowercase kebab-case. Relations use only:
`prerequisites`, `part_of`, `enables`, `used_by`, `contrasts_with`, `affects`,
`optimized_by`, and `implemented_in`. `contrasts_with` is symmetric. Source IDs
have the form `yuque:<document-id>` and must exist in the registry.

## Incremental sync transaction

`sync_yuque.py plan` compares provider metadata with the registry and reports new,
changed, renamed, or inaccessible sources plus affected pages. An LLM maintainer
then fetches accepted bodies into temporary storage, updates derived pages, and
runs graph generation and lint. `acknowledge` advances processed versions only
after those checks pass and records the operation in `log.md`.

This keeps reruns idempotent and prevents partial failures from claiming a source
version was processed. The approval boundary is deliberate: a sync preview may
identify source changes, but derived wiki pages are changed only after review.

## Visualization and automation boundary

`generated/graph.json` is the stable machine-readable visualization input. For
Obsidian's native Graph View, `wiki_tools.py obsidian` deterministically projects
each page's typed frontmatter relations into a generated wikilink block on that
page. Frontmatter remains canonical, and lint rejects a missing or stale projection.

A custom graph UI with styled relation types, a daily nanobot sync that asks for
approval, embeddings, and a graph database remain postponed. None is required to
browse or maintain the Markdown knowledge graph.
