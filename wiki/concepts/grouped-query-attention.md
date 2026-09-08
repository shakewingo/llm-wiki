---
id: grouped-query-attention
title: Grouped-Query Attention
type: concept
domains: [model-architecture, inference]
aliases: [GQA, grouped multi-query attention]
level: intermediate
relations:
  prerequisites: [self-attention]
  affects: [kv-cache]
  contrasts_with: [multi-query-attention, multi-head-latent-attention]
sources: [yuque:145901413, yuque:271488122]
---

# Grouped-Query Attention

GQA partitions query heads into groups whose members share a key/value head, giving
a tunable middle ground between MHA quality and MQA cache efficiency.

Fewer KV heads mean a proportionally smaller cache and less decode-time bandwidth.
More groups retain greater K/V diversity. The chosen group count is therefore a
model-quality versus serving-cost decision, not merely a kernel option.

## Interview answer

“GQA shares K/V heads within groups of query heads. It preserves more diversity
than MQA while reducing KV-cache memory compared with full MHA.”

## Sources

- [LLaMA](https://www.yuque.com/shakewin/woezs0/avr5nrkaahavwdwv)
- [MLA](https://www.yuque.com/shakewin/woezs0/fz9zd2ttsiywlelx)

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[self-attention|Self-Attention]]
- Contrasts with: [[multi-query-attention|Multi-Query Attention]], [[multi-head-latent-attention|Multi-Head Latent Attention]]
- Affects: [[kv-cache|KV Cache]]

<!-- END GENERATED OBSIDIAN LINKS -->
