---
id: kv-cache
title: KV Cache
type: concept
domains: [inference, transformer]
aliases: [key-value cache, attention cache]
level: foundational
relations:
  prerequisites: [causal-attention]
  used_by: [continuous-batching-and-sequence-packing]
  optimized_by:
    - multi-query-attention
    - grouped-query-attention
    - multi-head-latent-attention
    - paged-attention
sources: [yuque:145901413, yuque:279560513, notion:388cad4f-b605-8074-8c53-ff558a15beb0]
legacy_notion_id: 4c2cad4f-b605-8288-b810-81feb1817985
---

# KV Cache

A KV cache stores each layer's prior key and value tensors so autoregressive decode
computes projections only for the new token instead of recomputing the full prefix.

For a simplified dense layout, storage grows with batch size, layers, sequence
length, KV-head count, head dimension, and bytes per element. Decode trades compute
for state: one new query attends over an ever-growing cache. Long contexts and large
batches therefore make capacity, memory bandwidth, fragmentation, and eviction
central systems concerns.

MQA/GQA reduce the number of KV heads, MLA stores a compressed latent, quantization
reduces bytes, and paged layouts manage allocation. A stale or wrongly indexed
cache silently changes model output.

## Interview answer

“The KV cache removes repeated K/V projection work for the prefix. It speeds decode
but introduces memory growth and bandwidth pressure, so attention architecture and
cache management determine serving capacity.”

## Sources

- [LLaMA](https://www.yuque.com/shakewin/woezs0/avr5nrkaahavwdwv)
- [Prompt Caching and Prefix Cache](https://www.yuque.com/shakewin/sysgq3/fddexv7e29h99vrl)
- [Alisa’s book of LLMs](https://app.notion.com/p/388cad4fb60580748c53ff558a15beb0)

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[causal-attention|Causal Attention]]
- Used by: [[continuous-batching-and-sequence-packing|Continuous Batching and Sequence Packing]]
- Optimized by: [[multi-query-attention|Multi-Query Attention]], [[grouped-query-attention|Grouped-Query Attention]], [[multi-head-latent-attention|Multi-Head Latent Attention]], [[paged-attention|Paged Attention]]

<!-- END GENERATED OBSIDIAN LINKS -->
