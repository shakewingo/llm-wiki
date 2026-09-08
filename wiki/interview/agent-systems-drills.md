---
id: agent-systems-drills
title: Retrieval and Agent Systems Drills
type: interview
domains: [retrieval, agent-systems, ai-engineering]
aliases: []
level: mixed
relations:
  prerequisites: [retrieval-and-agent-systems]
sources: [yuque:150979527, yuque:241262981, yuque:261725390, yuque:263799689, yuque:275632325]
---

# Retrieval and Agent Systems Drills

## Diagnose a bad RAG answer.

Separate ingestion, retrieval, reranking, prompt construction, and generation. Check
whether the answer lacked evidence, retrieved the wrong evidence, or ignored it.

## Why are tool schemas part of model quality?

Names and descriptions guide selection, while strict arguments prevent ambiguity.
The runtime—not the model—must enforce authorization and side-effect rules.

## When should agents run in parallel?

Only for independent work with distinct ownership. Shared mutable state or dependent
results require sequencing or coordination.

## What must compaction preserve?

User instructions, decisions, unresolved work, critical tool evidence, and artifact
references. Repeated lossy summaries should remain auditable.

## How should an approval gate work?

Bind approval to an exact plan, targets, and versions, then revalidate immediately
before execution.

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[retrieval-and-agent-systems|Retrieval and Agent Systems Map]]

<!-- END GENERATED OBSIDIAN LINKS -->
