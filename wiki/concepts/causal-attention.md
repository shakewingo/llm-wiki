---
id: causal-attention
title: Causal Attention
type: concept
domains: [model-architecture, inference]
aliases: [masked self-attention]
level: foundational
relations:
  prerequisites: [self-attention]
  part_of: [transformer-architecture]
  enables: [kv-cache]
sources: [yuque:145104021, yuque:145901413]
---

# Causal Attention

Causal attention masks future positions so token $t$ can depend only on tokens at
positions $\leq t$, matching autoregressive generation.

During training and prefill, all query positions can be processed in parallel under
the triangular mask. During decode, the new query length is one while keys and
values span the existing prefix. This asymmetry is why cached prefix state saves
recomputation but grows with context length.

An incorrect mask leaks future tokens during training; a cache position error makes
the model attend with the wrong chronology.

## Interview answer

“Causal attention is self-attention with a future-token mask. Training is parallel
over positions, but generation is sequential; each decode step queries the entire
visible prefix.”

## Sources

- [Attention is All You Need](https://www.yuque.com/shakewin/woezs0/wfnf4pb8yxth3i36)
- [LLaMA](https://www.yuque.com/shakewin/woezs0/avr5nrkaahavwdwv)

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[self-attention|Self-Attention]]
- Part of: [[transformer-architecture|Transformer Architecture]]
- Enables: [[kv-cache|KV Cache]]

<!-- END GENERATED OBSIDIAN LINKS -->
