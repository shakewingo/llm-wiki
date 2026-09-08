---
id: multi-head-latent-attention
title: Multi-Head Latent Attention
type: concept
domains: [model-architecture, inference]
aliases: [MLA]
level: advanced
relations:
  prerequisites: [self-attention, rotary-position-embedding]
  affects: [kv-cache]
  contrasts_with: [multi-query-attention, grouped-query-attention]
sources: [yuque:271488122, yuque:241299652]
---

# Multi-Head Latent Attention

MLA jointly compresses keys and values into a low-rank latent cache, then performs
attention in a form that preserves multi-head expressiveness while moving less
decode-time state.

The key systems idea is weight absorption: matrix multiplication can be regrouped
so the large up-projected K/V tensors need not be materialized during one-token
decode. Decoupled RoPE keeps positional components separate so that regrouping
remains valid. Implementations may use an MHA-like path for training/prefill and an
absorbed MQA-like path for decode.

The design adds architectural and kernel complexity. Compression rank, positional
handling, and the selected execution mode must agree or the theoretical cache
saving will not translate into real throughput.

## Interview answer

“MLA caches a learned low-rank K/V latent. Weight absorption avoids reconstructing
large K/V tensors during decode, while decoupled RoPE preserves valid positional
attention.”

## Sources

- [MLA](https://www.yuque.com/shakewin/woezs0/fz9zd2ttsiywlelx)
- [DeepSeek Paper Reading](https://www.yuque.com/shakewin/woezs0/agn9y7w2skcvzzrk)

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[self-attention|Self-Attention]], [[rotary-position-embedding|Rotary Position Embedding]]
- Contrasts with: [[multi-query-attention|Multi-Query Attention]], [[grouped-query-attention|Grouped-Query Attention]]
- Affects: [[kv-cache|KV Cache]]

<!-- END GENERATED OBSIDIAN LINKS -->
