---
id: multi-agent-orchestration
title: Multi-Agent Orchestration
type: concept
domains: [agent-systems, ai-engineering]
aliases: [agent teams, supervisor-worker agents]
level: advanced
relations:
  prerequisites: [agent-loop, tool-use-function-calling]
  optimized_by: [human-in-the-loop-agents]
sources: [yuque:241262981, yuque:275632325]
legacy_notion_id: 65ccad4f-b605-838e-a8bb-01e26225101f
---

# Multi-Agent Orchestration

Multi-agent orchestration decomposes work among specialized model loops and combines
their results through supervisor/worker, handoff, debate, or hierarchical patterns.

Parallelism helps only for independent subtasks. Shared files, vague ownership, and
duplicated context cause conflicts and token waste. A coordinator should send concrete
evidence and acceptance criteria rather than asking workers to rediscover context.
Lifecycle cleanup, cancellation, budgets, and structured messages are essential.

## Sources

- [RCA Agent](https://www.yuque.com/shakewin/xhs6fk/igcgrrffw77ehu2z)
- [Claude Code Analysis](https://www.yuque.com/shakewin/xhs6fk/ru7gng41hd6azwdd)

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[agent-loop|Agent Loop]], [[tool-use-function-calling|Tool Use and Function Calling]]
- Optimized by: [[human-in-the-loop-agents|Human-in-the-Loop Agents]]

<!-- END GENERATED OBSIDIAN LINKS -->
