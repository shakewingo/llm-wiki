# Wiki Maintenance Instructions

## Ownership and safety

- Yuque and explicitly registered Notion pages are source material for derived
  knowledge. Never copy a complete source body into this directory.
- Keep credentials outside the wiki. Read `YUQUE_API_KEY` and `NOTION_API_KEY`
  from the environment; never print, log, or persist either value.
- Notion is migration evidence for the old graph, not a second canonical graph.
- Markdown frontmatter is canonical. `generated/graph.json`, lint reports, and the
  Markdown sections between `BEGIN/END GENERATED OBSIDIAN LINKS` markers are
  derived and must not be edited by hand.
- Source access does not imply inclusion. Preserve `unreviewed` until a source has
  an intentional scope decision.
- `sync_yuque.py` owns Yuque freshness checks and preserves registry records from
  other providers. `sync_notion.py` owns direct Notion API freshness checks,
  temporary exports, and acknowledgements. Do not use a connector as the routine
  sync path.

## Ingest workflow

1. Run `python scripts/sync_yuque.py plan` and
   `python scripts/sync_notion.py plan`.
2. Review new/changed sources and the affected pages shown in the plan.
3. Fetch only accepted, in-scope source bodies into temporary processing storage.
   For registered Notion pages, use `sync_notion.py export` with an output under a
   temporary directory; see `sources/README.md`.
4. Update synthesis pages, maps, comparisons, drills, and provenance. Do not paste
   the source body.
5. Regenerate Obsidian links, then run graph generation and lint.
6. Only after all three validation commands pass, acknowledge processed versions
   with the matching provider script's `acknowledge` command.

Concept merges, deletions, contradictions, broad scope changes, and high-impact
relationship changes require user review. Never delete knowledge merely because a
source is temporarily inaccessible.

## Query workflow

- Begin at `index.md` or a domain map.
- Use stable frontmatter IDs, aliases, links, and text search before adding an
  embeddings index or graph database.
- Treat interview pages as navigation and rehearsal aids, not independent sources.

## Page conventions

- Filename and `id` use lowercase kebab-case. IDs do not change when titles change.
- Every concept has at least one registry-backed source.
- Allowed relation keys are `prerequisites`, `part_of`, `enables`, `used_by`,
  `contrasts_with`, `affects`, `optimized_by`, and `implemented_in`.
- Keep `contrasts_with` symmetric. Do not infer direction from Notion's legacy
  `Related Concepts` relation.
- Aliases are case-insensitively unique.
- Write plain English. Distinguish sourced claims from an LLM inference.
- Prefer synthesis and mental models over paraphrasing source structure.
- Keep typed relation IDs in frontmatter as plain IDs. Do not replace them with
  wikilinks; `python scripts/wiki_tools.py obsidian` projects them into generated
  `[[target|Title]]` links at the end of every page.
- Never edit inside a generated Obsidian block. The generator replaces the whole
  block and lint rejects missing or stale blocks.

## Conflict handling

- Preserve conflicting claims and identify their sources and dates.
- Prefer a newer source only when it explicitly corrects the older claim.
- Mark unresolved relation semantics in reports; do not force them into a typed
  edge.
- A failed sync must not advance `last_ingested_version`.

## Required validation

Run these after every content or relationship change:

```bash
python scripts/wiki_tools.py obsidian
python scripts/wiki_tools.py graph
python scripts/wiki_tools.py lint
```
