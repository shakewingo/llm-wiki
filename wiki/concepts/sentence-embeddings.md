---
id: sentence-embeddings
title: Sentence Embeddings
type: concept
domains: [retrieval, representation-learning]
aliases: [semantic embeddings, Sentence-BERT]
level: foundational
relations:
  prerequisites: [bert]
  enables: [vector-database, retrieval-augmented-generation]
sources: [yuque:150979527]
---

# Sentence Embeddings

A sentence embedding maps variable-length text into a fixed-size vector whose
geometry approximates semantic similarity.

Siamese or dual-encoder training processes two texts independently and optimizes
their similarity, making retrieval far cheaper than running cross-attention over
every pair. Pooling choice, normalization, domain data, and negative examples shape
the space. Embeddings are fast candidate generators, but a single vector loses token
detail and similarity may reflect topic rather than answer relevance.

## Source

- [RAG](https://www.yuque.com/shakewin/woezs0/kurmygcgi69wb5kv)

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[bert|BERT]]
- Enables: [[vector-database|Vector Databases and HNSW]], [[retrieval-augmented-generation|Retrieval-Augmented Generation]]

<!-- END GENERATED OBSIDIAN LINKS -->
