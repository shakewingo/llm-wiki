---
id: agent-safety-boundaries
title: Agent Safety Boundaries
type: concept
domains: [agent-systems, safety]
aliases: [agent permissions, least privilege]
level: advanced
relations:
  prerequisites: [tool-use-function-calling, human-in-the-loop-agents]
  affects: [agent-loop]
sources: [yuque:275632325, yuque:263799689]
---

# Agent Safety Boundaries

Agent safety begins below the model: permissions, sandboxing, validation, and policy
must constrain every tool invocation even when the model asks confidently.

Least privilege limits tools and filesystem/network scope; fail-closed defaults block
unknown cases; explicit user rules override permissive modes. Untrusted repository
text and tool results can contain prompt injection, so context inclusion itself is a
security boundary. Logs should record decisions without leaking secrets, and remote
or policy kill switches can contain newly discovered hazards.

## Sources

- [Claude Code Analysis](https://www.yuque.com/shakewin/xhs6fk/ru7gng41hd6azwdd)
- [Nanobot Code Review](https://www.yuque.com/shakewin/xhs6fk/ga5n2frllmdao7c3)

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[tool-use-function-calling|Tool Use and Function Calling]], [[human-in-the-loop-agents|Human-in-the-Loop Agents]]
- Affects: [[agent-loop|Agent Loop]]

<!-- END GENERATED OBSIDIAN LINKS -->
