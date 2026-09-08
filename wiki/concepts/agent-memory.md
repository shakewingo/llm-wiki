---
id: agent-memory
title: Agent Memory
type: concept
domains: [agent-systems, memory]
aliases: [long-term agent memory]
level: intermediate
relations:
  prerequisites: [retrieval-augmented-generation]
  optimized_by: [context-compaction]
sources: [yuque:261725390, yuque:263799689, yuque:275632325]
---

# Agent Memory

Agent memory preserves useful information beyond the current model context through
session history, summaries, durable facts, episodic records, or retrievable documents.

Different lifetimes should remain separate: recent conversation, project knowledge,
agent-specific procedures, and user preferences have different ownership and update
rules. Retrieval-based memory scales but can return stale or irrelevant facts;
always-loaded files are predictable but consume tokens. Good memory tracks provenance,
supports correction and deletion, and avoids silently turning sensitive transient
content into permanent state.

## Sources

- [Openclaw/Nanobot](https://www.yuque.com/shakewin/xhs6fk/ks4me3zlgov4ma8g)
- [Nanobot Code Review](https://www.yuque.com/shakewin/xhs6fk/ga5n2frllmdao7c3)
- [Claude Code Analysis](https://www.yuque.com/shakewin/xhs6fk/ru7gng41hd6azwdd)

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[retrieval-augmented-generation|Retrieval-Augmented Generation]]
- Optimized by: [[context-compaction|Context Compaction]]

<!-- END GENERATED OBSIDIAN LINKS -->
