---
id: self-attention
title: Self-Attention
type: concept
domains: [model-architecture]
aliases: [scaled dot-product attention]
level: foundational
relations:
  part_of: [transformer-architecture]
  enables: [causal-attention]
sources: [yuque:145104021]
---

# Self-Attention

Self-attention lets each token build a context-dependent representation by
weighting values from tokens in the same sequence.

Queries describe what a token seeks, keys describe what each position offers for
matching, and values carry the information to aggregate. For sequence length
$L$, dense attention materializes an $L\times L$ interaction pattern and therefore
has $O(L^2)$ pairwise work. Multi-head projections let the model represent several
relationship patterns at once.

The chief advantage over recurrence is a short path between arbitrary positions
and parallel computation during training. Its chief weakness is quadratic scaling
for long contexts, motivating cache-aware and sparse variants.

## Interview answer

“Self-attention computes content-dependent weighted combinations of tokens using
query-key similarities. It parallelizes well and models long-range dependencies,
but dense attention scales quadratically with sequence length.”

## Source

- [Attention is All You Need](https://www.yuque.com/shakewin/woezs0/wfnf4pb8yxth3i36)

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Part of: [[transformer-architecture|Transformer Architecture]]
- Enables: [[causal-attention|Causal Attention]]

<!-- END GENERATED OBSIDIAN LINKS -->
