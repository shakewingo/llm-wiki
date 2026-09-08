---
id: attention-cache-strategies
title: MHA, MQA, GQA, and MLA
type: comparison
domains: [model-architecture, inference]
aliases: []
level: intermediate
relations:
  prerequisites: [self-attention, kv-cache]
sources: [yuque:145901413, yuque:271488122, yuque:241299652]
---

# MHA, MQA, GQA, and MLA

These designs answer the same serving question differently: how much distinct K/V
state should be retained for many query heads?

| Design | Cached representation | Main advantage | Main tradeoff |
|---|---|---|---|
| MHA | Separate K/V per query head | Maximum per-head diversity | Largest cache and bandwidth |
| [MQA](../concepts/multi-query-attention.md) | One shared K/V head | Smallest head-based cache | Least K/V diversity |
| [GQA](../concepts/grouped-query-attention.md) | One K/V head per query group | Tunable quality/efficiency balance | Group count becomes a model choice |
| [MLA](../concepts/multi-head-latent-attention.md) | Joint low-rank K/V latent plus positional component | Low cache with multi-head reconstruction | More algebra and kernel complexity |

MHA→GQA→MQA changes the number of KV heads. MLA instead changes the representation
stored in the cache. Its absorbed decode path can behave operationally like shared
K/V while retaining learned reconstruction. None of the choices removes the need
for correct [causal attention](../concepts/causal-attention.md), positions, allocation,
or eviction.

## Interview frame

Start from bytes moved per generated token, then discuss quality and kernel support.
A model architecture with a smaller theoretical cache can still underperform if its
runtime materializes large tensors or lacks an optimized attention kernel.

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[self-attention|Self-Attention]], [[kv-cache|KV Cache]]

<!-- END GENERATED OBSIDIAN LINKS -->
