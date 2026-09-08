---
id: context-compaction
title: Context Compaction
type: concept
domains: [agent-systems, memory]
aliases: [conversation summarization, context compression]
level: intermediate
relations:
  prerequisites: [agent-memory]
  affects: [agent-loop]
sources: [yuque:261725390, yuque:263799689, yuque:275632325]
---

# Context Compaction

Context compaction replaces older conversation detail with a smaller representation
so an agent can continue within the model's context limit.

A safe compactor preserves user instructions, decisions, unresolved work, tool
results needed for verification, and references to durable artifacts. Progressive
layers—recent verbatim messages, older summaries, and long-term indexed facts—lose
less than one all-or-nothing summary. Compaction must be idempotent and auditable;
otherwise repeated summaries amplify mistakes and discard evidence.

## Sources

- [Openclaw/Nanobot](https://www.yuque.com/shakewin/xhs6fk/ks4me3zlgov4ma8g)
- [Nanobot Code Review](https://www.yuque.com/shakewin/xhs6fk/ga5n2frllmdao7c3)
- [Claude Code Analysis](https://www.yuque.com/shakewin/xhs6fk/ru7gng41hd6azwdd)

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[agent-memory|Agent Memory]]
- Affects: [[agent-loop|Agent Loop]]

<!-- END GENERATED OBSIDIAN LINKS -->
