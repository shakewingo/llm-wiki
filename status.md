# Current Status

Last verified: 2026-09-08, Asia/Shanghai.

## Complete

- Migrated the reviewed AI-related Yuque material into seven connected vertical
  slices: foundations; model architecture and generation; Transformer inference;
  post-training and alignment; retrieval and agent systems; applied AI and
  evaluation; and distributed training and MLOps.
- Built 75 derived concept pages, seven domain maps, two comparison pages, and
  seven interview drill sets.
- Generated a deterministic knowledge graph with 91 nodes and 246 typed edges.
- Refreshed the 68-document metadata registry and marked all 34 sources used by
  wiki concepts as processed at their current Yuque versions.
- Reviewed source scopes now total 20 `core`, 7 `project-evidence`, 9 `reference`,
  25 `excluded`, and 7 `unreviewed`.
- Kept Yuque as the canonical store for full notes. No Yuque note body is persisted
  anywhere under this wiki.
- Preserved the legacy Notion inventory as migration evidence without treating its
  reciprocal, untyped relations as directional concept edges.
- Added native Obsidian Graph View compatibility by projecting typed relations into
  generated wikilink blocks on all 91 pages. Generation is deterministic,
  idempotent, and checked by lint.
- Verified graph generation and linting with zero errors and zero warnings, Ruff
  with no findings, all six automated tests passing, and a live sync preview with
  zero pending changes.

## Scope boundary

The seven remaining `unreviewed` records are ambiguous or primarily non-AI topics
(`Mixed`, `Clickhouse`, `Playaround`, `App Dev`, `MoneyInOne`, `Python`, and
`Gatech CS8903 - ODC`). Empty AI placeholders and personal planning material stay
excluded because they provide no usable technical evidence. These are not gaps in
the reviewed AI vertical slices.

## Deferred by current decision

- ~~Build a custom graph UI with visual styling for different relation types. Native
  Obsidian Graph View support is complete.~~
- Run a daily nanobot sync that presents detected changes for approval before
  implementation; automatic application remains disabled.
- Add embeddings or a graph database.

## Maintenance

Run `python scripts/sync_yuque.py plan` for a metadata-only change preview. For an
approved change, fetch only the selected source bodies into temporary storage,
update derived pages, regenerate Obsidian links and the JSON graph, lint, then
acknowledge the processed source versions.
