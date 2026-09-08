---
id: vector-database
title: Vector Databases and HNSW
type: concept
domains: [retrieval, systems]
aliases: [vector store, HNSW, approximate nearest-neighbor search]
level: intermediate
relations:
  prerequisites: [sentence-embeddings, sparse-representations]
  enables: [retrieval-augmented-generation]
sources: [yuque:150979527, yuque:253935769]
---

# Vector Databases and HNSW

A vector database stores embeddings plus metadata and serves similarity search.
Approximate nearest-neighbor indexes trade exactness for latency and scale.

HNSW builds a multilayer proximity graph: sparse upper layers provide long jumps,
and dense lower layers refine local neighbors. Search breadth controls a recall versus
latency tradeoff; construction parameters affect memory and index quality. Production
systems also need metadata filtering, versioned embeddings, deletion, tenancy, and
reindexing. High vector recall is useful only if retrieved chunks are relevant to the
downstream answer.

## Sources

- [RAG](https://www.yuque.com/shakewin/woezs0/kurmygcgi69wb5kv)
- [NVIDIA Agentic AI Training](https://www.yuque.com/shakewin/fidaqi/fgv15n9m42qh9m77)

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[sentence-embeddings|Sentence Embeddings]], [[sparse-representations|Sparse Representations]]
- Enables: [[retrieval-augmented-generation|Retrieval-Augmented Generation]]

<!-- END GENERATED OBSIDIAN LINKS -->
