---
id: retrieval-and-agent-systems
title: Retrieval and Agent Systems Map
type: map
domains: [retrieval, agent-systems, ai-engineering]
aliases: []
level: mixed
entry_points:
  - sentence-embeddings
  - vector-database
  - retrieval-augmented-generation
  - tool-use-function-calling
  - model-context-protocol
  - agent-loop
  - agent-memory
  - context-compaction
  - event-driven-agent-architecture
  - multi-agent-orchestration
  - human-in-the-loop-agents
  - agent-safety-boundaries
relations:
  prerequisites: [transformer-architecture]
  enables: [root-cause-analysis]
sources: [yuque:150979527, yuque:253935769, yuque:241262981, yuque:261725390, yuque:263799689, yuque:275632325]
---

# Retrieval and Agent Systems Map

Agent systems combine model reasoning with external knowledge, tools, state, and
control flow.

The retrieval path is [sentence embeddings](../concepts/sentence-embeddings.md) →
[vector database](../concepts/vector-database.md) →
[RAG](../concepts/retrieval-augmented-generation.md). The action path is
[tool use](../concepts/tool-use-function-calling.md) →
[MCP](../concepts/model-context-protocol.md) →
[agent loop](../concepts/agent-loop.md).

Long-running behavior needs [agent memory](../concepts/agent-memory.md),
[context compaction](../concepts/context-compaction.md), and an
[event-driven architecture](../concepts/event-driven-agent-architecture.md).
[Multi-agent orchestration](../concepts/multi-agent-orchestration.md) adds
coordination, while [human approval](../concepts/human-in-the-loop-agents.md) and
[safety boundaries](../concepts/agent-safety-boundaries.md) constrain consequences.

Practice with [agent-system drills](../interview/agent-systems-drills.md).

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[transformer-architecture|Transformer Architecture]]
- Enables: [[root-cause-analysis|AI-Assisted Root Cause Analysis]]

<!-- END GENERATED OBSIDIAN LINKS -->
