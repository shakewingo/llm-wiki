# AI Engineer LLM Wiki

This is a local, LLM-maintained interview-preparation wiki. Yuque remains the
canonical home of complete personal notes; this directory stores metadata,
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
```

To use the native Obsidian graph, open this directory as a vault. The `obsidian`
command projects canonical typed frontmatter relations into generated wikilink
blocks; rerunning it is safe and idempotent.

See [AGENTS.md](./AGENTS.md) before maintaining the wiki and [status.md](./status.md)
for the current implementation state.
