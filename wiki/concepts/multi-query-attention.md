---
id: multi-query-attention
title: Multi-Query Attention
type: concept
domains: [model-architecture, inference]
aliases: [MQA]
level: intermediate
relations:
  prerequisites: [self-attention]
  affects: [kv-cache]
  contrasts_with: [grouped-query-attention, multi-head-latent-attention]
sources: [yuque:145901413, yuque:271488122]
---

# Multi-Query Attention

MQA keeps multiple query heads but shares a single key head and value head across
them, sharply reducing KV-cache size and decode-time memory traffic.

The efficiency gain comes from moving fewer cached bytes per token. The tradeoff is
reduced KV-head diversity, which can cost quality relative to full multi-head
attention. It is the low-memory endpoint of the MHA→GQA→MQA family; MLA pursues a
different compression route with a learned latent representation.

## Interview answer

“MQA shares one K/V head across many query heads. That reduces cache capacity and
bandwidth, but sacrifices some representational diversity.”

## Sources

- [LLaMA](https://www.yuque.com/shakewin/woezs0/avr5nrkaahavwdwv)
- [MLA](https://www.yuque.com/shakewin/woezs0/fz9zd2ttsiywlelx)

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[self-attention|Self-Attention]]
- Contrasts with: [[grouped-query-attention|Grouped-Query Attention]], [[multi-head-latent-attention|Multi-Head Latent Attention]]
- Affects: [[kv-cache|KV Cache]]

<!-- END GENERATED OBSIDIAN LINKS -->
