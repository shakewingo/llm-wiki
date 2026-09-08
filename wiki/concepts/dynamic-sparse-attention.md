---
id: dynamic-sparse-attention
title: Dynamic Sparse Attention
type: concept
domains: [model-architecture, inference, training]
aliases: [DSA]
level: advanced
relations:
  prerequisites: [self-attention, multi-head-latent-attention]
  affects: [kv-cache]
sources: [yuque:267998961, yuque:241299652]
---

# Dynamic Sparse Attention

DSA uses a lightweight learned indexer to select the top-$k$ relevant cached
positions before the main attention computation.

After dense warm-up, sparse training co-trains the indexer toward the main model's
attention distribution while the main model attends only to selected entries. The
main attention work changes from $O(L^2)$ to approximately $O(Lk)$ in training and
from reading $L$ cache rows to $k$ rows per decode query, plus the cheaper indexer
scan. DeepSeek's implementation builds on MLA's absorbed decode representation.

Quality depends on retrieval recall. An indexer that misses an important token saves
compute but irreversibly removes that evidence from the main attention calculation.

## Interview answer

“DSA learns a cheap indexer that retrieves top-k positions, then runs expensive
attention only on them. It reduces long-context compute and cache reads, but turns
retrieval recall into a model-quality risk.”

## Sources

- [DSA / CSA / HCA](https://www.yuque.com/shakewin/woezs0/kh0uap4zmflsimws)
- [DeepSeek Paper Reading](https://www.yuque.com/shakewin/woezs0/agn9y7w2skcvzzrk)

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[self-attention|Self-Attention]], [[multi-head-latent-attention|Multi-Head Latent Attention]]
- Affects: [[kv-cache|KV Cache]]

<!-- END GENERATED OBSIDIAN LINKS -->
