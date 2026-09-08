---
id: human-in-the-loop-agents
title: Human-in-the-Loop Agents
type: concept
domains: [agent-systems, safety]
aliases: [HITL, approval gate]
level: intermediate
relations:
  prerequisites: [agent-loop]
  affects: [tool-use-function-calling, multi-agent-orchestration]
sources: [yuque:241262981, yuque:275632325]
---

# Human-in-the-Loop Agents

Human-in-the-loop design pauses an agent at consequential decision boundaries so a
person can approve, reject, or modify the proposed action.

The approval must bind to an exact plan, target, and version; a vague “continue” is
unsafe if external state changed meanwhile. Read-only discovery can usually proceed
autonomously, while destructive operations, publishing, spending, identity-sensitive
actions, and broad relationship changes deserve review. The system must preserve a
pending state and revalidate it before execution.

## Sources

- [RCA Agent](https://www.yuque.com/shakewin/xhs6fk/igcgrrffw77ehu2z)
- [Claude Code Analysis](https://www.yuque.com/shakewin/xhs6fk/ru7gng41hd6azwdd)

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[agent-loop|Agent Loop]]
- Affects: [[tool-use-function-calling|Tool Use and Function Calling]], [[multi-agent-orchestration|Multi-Agent Orchestration]]

<!-- END GENERATED OBSIDIAN LINKS -->
