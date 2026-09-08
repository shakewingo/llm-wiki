# Current Status

Last verified: 2026-09-08, Asia/Shanghai.

## Complete

- Migrated the reviewed AI-related Yuque material and the registered Notion source
  `Alisa’s book of LLMs` into seven connected vertical
  slices: foundations; model architecture and generation; Transformer inference;
  post-training and alignment; retrieval and agent systems; applied AI and
  evaluation; and distributed training and MLOps.
- Built 89 derived concept pages, seven domain maps, three comparison pages, and
  seven interview drill sets.
- Generated a deterministic knowledge graph with 106 nodes and 307 typed edges;
  graph nodes now carry source IDs for provenance-aware consumers.
- Refreshed the 69-source metadata registry: 68 Yuque documents plus one Notion
  page. All 35 sources used by wiki pages are recorded at their reviewed versions.
- Reviewed source scopes now total 20 `core`, 7 `project-evidence`, 10 `reference`,
  25 `excluded`, and 7 `unreviewed`.
- Kept source systems as the canonical stores for complete content. No complete
  Yuque or Notion body is persisted anywhere under this wiki.
- Preserved the legacy Notion inventory as migration evidence without treating its
  reciprocal, untyped relations as directional concept edges.
- Added native Obsidian Graph View compatibility by projecting typed relations into
  generated wikilink blocks on all 106 pages. Generation is deterministic,
  idempotent, and checked by lint.
- Verified direct Notion API access from `NOTION_API_KEY` against the exact Alisa
  page: page metadata, block children, and page-Markdown endpoints returned HTTP
  200. The full content arrived in one untruncated Markdown part with zero unknown
  blocks.
- Added `sync_notion.py` for metadata previews, fast Notion-flavored Markdown
  exports to guarded temporary storage, and post-validation version
  acknowledgement. The routine workflow no longer depends on a Notion connector.
- Final verification: 106 nodes, 307 edges, zero lint errors or warnings, Ruff
  clean, all 13 automated tests passing, and zero pending Notion changes.

## Scope boundary

The seven remaining `unreviewed` records are ambiguous or primarily non-AI topics
(`Mixed`, `Clickhouse`, `Playaround`, `App Dev`, `MoneyInOne`, `Python`, and
`Gatech CS8903 - ODC`). Empty AI placeholders and personal planning material stay
excluded because they provide no usable technical evidence. These are not gaps in
the reviewed AI vertical slices.

## Deferred by current decision

- ~~Build a custom graph UI with visual styling for different relation types. Native
  Obsidian Graph View support is complete.~~
- ~~Run a daily nanobot sync that presents detected changes for approval before
  implementation.~~ Implemented 2026-09-08: cron job `llm-wiki-daily-check` runs
  daily at 09:00 CST, calls `scripts/daily_check.sh`, and reports both Yuque and
  Notion sync plans for approval. The scheduler must expose both API keys in its
  process environment. Automatic content application remains disabled; only
  approved changes are applied interactively.
- Add embeddings or a graph database.

## Git backup

- This folder is a private GitHub repo: `github.com/shakewingo/llm-wiki` (default
  branch `main`). Initialized 2026-09-08.
- The daily cron job commits and pushes any local changes (e.g. approved wiki
  updates applied earlier) after each check. No automatic content changes are
  made by the cron job itself — it only syncs already-approved, already-applied
  local commits to the remote.
- Push authentication uses a scoped credential helper at
  `scripts/git-credential-helper.sh`, which reads the GitHub token from the
  `gh` CLI's local config (`~/.config/gh/hosts.yml`) at push time. The token is
  never stored in this repo or printed to logs.

## Maintenance

Run `python scripts/sync_yuque.py plan` and `python scripts/sync_notion.py plan` for
metadata-only change previews. For an approved change, fetch only the selected
source bodies into temporary storage, update derived pages, regenerate Obsidian
links and the JSON graph, lint, then acknowledge with the matching provider script.
Exact Notion setup and commands are documented in `sources/README.md`.
