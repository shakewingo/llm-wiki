---
id: root-cause-analysis
title: AI-Assisted Root Cause Analysis
type: concept
domains: [applied-ml, agent-systems, observability]
aliases: [RCA agent]
level: advanced
relations:
  prerequisites: [causal-structure-learning, retrieval-augmented-generation, agent-loop]
  implemented_in: [event-driven-agent-architecture]
sources: [yuque:241262981, yuque:179434725]
---

# AI-Assisted Root Cause Analysis

An RCA agent collects traces, logs, metrics, topology, and runbooks, then proposes
and verifies explanations for an incident.

RED metrics—rate, errors, and duration—locate symptoms, while trace structure and
causal hypotheses distinguish correlation from plausible propagation. A state graph
can split evidence collection, diagnosis, and verification, and MCP can standardize
observability tools. The system should show evidence for each claim, preserve human
approval for remediation, and avoid treating the most correlated service as causal.

## Sources

- [RCA Agent with LangGraph](https://www.yuque.com/shakewin/xhs6fk/igcgrrffw77ehu2z)
- [Causal Structure Learning](https://www.yuque.com/shakewin/woezs0/zbne4d5yhpdwnasv)

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[causal-structure-learning|Causal Structure Learning]], [[retrieval-augmented-generation|Retrieval-Augmented Generation]], [[agent-loop|Agent Loop]]
- Implemented in: [[event-driven-agent-architecture|Event-Driven Agent Architecture]]

<!-- END GENERATED OBSIDIAN LINKS -->
