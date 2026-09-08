---
id: retrieval-augmented-generation
title: Retrieval-Augmented Generation
type: concept
domains: [retrieval, agent-systems]
aliases: [RAG]
level: foundational
relations:
  prerequisites: [sentence-embeddings, vector-database]
  used_by: [agent-memory, root-cause-analysis]
sources: [yuque:150979527, yuque:253935769, yuque:213041038]
---

# Retrieval-Augmented Generation

RAG retrieves external evidence for a query and places it in the model context before
generation, separating mutable knowledge from model parameters.

An ingestion path parses, chunks, embeds, and indexes documents. A query path embeds
the question, retrieves candidates, optionally filters or reranks them, and builds a
grounded prompt. Failures arise from bad chunk boundaries, low retrieval recall,
stale indexes, misleading sources, or a generator that ignores evidence. Evaluation
must separate retrieval quality from answer quality and verify citations.

## Sources

- [RAG](https://www.yuque.com/shakewin/woezs0/kurmygcgi69wb5kv)
- [NVIDIA Agentic AI Training](https://www.yuque.com/shakewin/fidaqi/fgv15n9m42qh9m77)
- [Voice Chatbot](https://www.yuque.com/shakewin/xhs6fk/smzsma1rag73ei59)

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[sentence-embeddings|Sentence Embeddings]], [[vector-database|Vector Databases and HNSW]]
- Used by: [[agent-memory|Agent Memory]], [[root-cause-analysis|AI-Assisted Root Cause Analysis]]

<!-- END GENERATED OBSIDIAN LINKS -->
