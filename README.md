# AI Engineer LLM Wiki

This is a local, LLM-maintained interview-preparation wiki. Yuque and explicitly
registered Notion pages remain the homes of complete source content; this directory stores metadata,
derived explanations, cross-source synthesis, typed concept relationships, domain
maps, comparisons, and interview drills.

Start with [index.md](./index.md). The migrated AI scope spans foundations, model
architecture and generation, Transformer inference, post-training and alignment,
retrieval and agent systems, applied AI and evaluation, and distributed training
and MLOps. Source bodies are fetched only into temporary processing storage and
are never persisted here.

## Commands

```bash
python scripts/wiki_tools.py obsidian
python scripts/wiki_tools.py graph
python scripts/wiki_tools.py lint
python scripts/sync_yuque.py plan
python scripts/sync_notion.py plan
```

Both sync scripts use provider API credentials from environment variables. See
[sources/README.md](./sources/README.md) for the direct Notion API workflow,
including temporary page-Markdown export and post-validation acknowledgement.

To use the native Obsidian graph, open this directory as a vault. The `obsidian`
command projects canonical typed frontmatter relations into generated wikilink
blocks; rerunning it is safe and idempotent.

See [AGENTS.md](./AGENTS.md) before maintaining the wiki and [status.md](./status.md)
for the current implementation state.
