---
id: event-driven-agent-architecture
title: Event-Driven Agent Architecture
type: concept
domains: [agent-systems, ai-engineering]
aliases: [message bus architecture]
level: intermediate
relations:
  prerequisites: [agent-loop]
  enables: [multi-agent-orchestration]
sources: [yuque:261725390, yuque:263799689]
---

# Event-Driven Agent Architecture

An event-driven agent system separates channels, the reasoning loop, and outbound
delivery with typed messages and asynchronous queues.

The message bus absorbs platform differences and backpressure, while session keys
preserve conversational ordering. Provider adapters normalize model APIs, and a tool
registry isolates capabilities from orchestration. This improves extensibility but
requires explicit delivery semantics, cancellation, deduplication, and error handling;
otherwise retries can duplicate user-visible actions.

## Sources

- [Openclaw/Nanobot](https://www.yuque.com/shakewin/xhs6fk/ks4me3zlgov4ma8g)
- [Nanobot Code Review](https://www.yuque.com/shakewin/xhs6fk/ga5n2frllmdao7c3)

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[agent-loop|Agent Loop]]
- Enables: [[multi-agent-orchestration|Multi-Agent Orchestration]]

<!-- END GENERATED OBSIDIAN LINKS -->
