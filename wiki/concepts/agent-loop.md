---
id: agent-loop
title: Agent Loop
type: concept
domains: [agent-systems, ai-engineering]
aliases: [tool-calling loop, reason-act-observe loop]
level: foundational
relations:
  prerequisites: [tool-use-function-calling]
  enables: [multi-agent-orchestration, human-in-the-loop-agents]
sources: [yuque:263799689, yuque:261725390, yuque:275632325]
---

# Agent Loop

An agent loop repeatedly builds context, asks a model for a response or tool calls,
executes allowed tools, returns observations, and stops when the task is complete.

Reliable loops need iteration and token budgets, cancellation, retries, tool-result
normalization, context compaction, session persistence, and clear termination. Local
preprocessing should happen before expensive model calls, while intermediate errors
can remain inside the loop when recovery is possible. Unbounded iteration, hidden
state mutation, or ambiguous tool results make agents expensive and difficult to
debug.

## Sources

- [Nanobot Code Review](https://www.yuque.com/shakewin/xhs6fk/ga5n2frllmdao7c3)
- [Openclaw/Nanobot](https://www.yuque.com/shakewin/xhs6fk/ks4me3zlgov4ma8g)
- [Claude Code Analysis](https://www.yuque.com/shakewin/xhs6fk/ru7gng41hd6azwdd)

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[tool-use-function-calling|Tool Use and Function Calling]]
- Enables: [[multi-agent-orchestration|Multi-Agent Orchestration]], [[human-in-the-loop-agents|Human-in-the-Loop Agents]]

<!-- END GENERATED OBSIDIAN LINKS -->
