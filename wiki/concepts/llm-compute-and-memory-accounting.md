---
id: llm-compute-and-memory-accounting
title: LLM Compute and Memory Accounting
type: concept
domains: [systems, training, inference]
aliases: [LLM FLOP accounting, training memory accounting, inference memory accounting]
level: advanced
relations:
  prerequisites: [transformer-architecture, backpropagation-and-autodiff, gpu-performance-model]
  used_by: [mixed-precision-training, fully-sharded-data-parallelism, kv-cache]
sources: [notion:388cad4f-b605-8074-8c53-ff558a15beb0, yuque:283802487]
---

# LLM Compute and Memory Accounting

LLM capacity planning separates parameters, optimizer state, gradients, activations,
and persistent inference state. Training retains or recomputes activations for
backpropagation and often keeps higher-precision master weights plus Adam moments.
Inference drops optimizer and gradient state but adds a KV cache that grows with
batch size, context length, layers, KV heads, head dimension, and element width.

For dense Transformers, projection and FFN work scales roughly with tokens times
parameter count, while attention adds a sequence-dependent term. The common
$6\times\text{tokens}\times\text{parameters}$ training estimate combines a dense
forward pass with two comparable backward matrix multiplications; it is a useful
approximation, not a replacement for architecture-specific accounting.

## Counting parameters and FLOPs

With `D = d_model`, `F = d_ff`, `L` layers, `V` vocab, head dimension `H` and `N`
heads, the per-layer parameter split is roughly: attention `4D²` (Q, K, V, O
projections, assuming `K = N` KV heads), FFN `3DF` (up, gate, down), and norms `2D`.
Adding embeddings `2VD` gives `2VD + L(4D² + 2D + 3DF)`, which is about
`2VD + 12LD²` once `F = 8D/3`.

Forward FLOPs per layer at prefill (`S` tokens, batch `B`) are `8BSD² + 4BS²D` for
attention (four `2BSD²` projections plus two `S²`-sized products) and `6BSDF`, about
`16BSD²`, for the FFN — so `2BSD(12D + 2S)` per layer, or roughly
`2BSD(12LD + 2LS + V)` for the whole model. Backward costs about twice forward
because gradients are taken with respect to both parameters and layer inputs. That
factor is where the `6` in `6 · tokens · params` comes from: `2` forward plus `4`
backward per token-parameter pair.

Two crossover rules follow from the arithmetic. The MLP block dominates both the
parameter count and the FLOPs budget as long as sequence length stays below about
`8D`; past that, the quadratic attention term takes over. And for a dense GLU-style
FFN the FLOPs are small per parameter but large in aggregate, which is why FLOPs and
parameters can be treated as roughly proportional at ordinary context lengths.

## Where memory actually goes

Inference: weights plus KV cache plus peak activations. The cache is `2 · B · S · L
· K · H` elements (the `2` accounts for K and V), which is where GQA's reduction in
`K` pays off directly. Activations are `O(BNS² + BSF)` at prefill but only
`O(BNS + BF)` during decode, since one query attends over the cache; FlashAttention
means the `S × S` score matrix is never materialized, so the quadratic term collapses
to linear and peak activation memory tracks total tokens.

Training: weights, optimizer state, gradients, activations. Under mixed precision
with Adam, FP32 master weights cost `4P` (plus a transient BF16 copy at `2P`),
gradients `4P` (accumulated in FP32 even when computed in BF16), and the two Adam
moments `8P` — roughly `18P` before activations, which mirrors the famous order-of-`16P`
rule of thumb. Activations dominate next: `14BSD + BNS²` per layer without
FlashAttention, reduced to `BS`-scaling with it, and cut further by gradient
checkpointing.

Peak memory, not just totals, determines whether an execution fits. FlashAttention,
activation checkpointing, GQA/MLA, sharding, and reduced precision each remove a
different term, so their savings should not be added blindly.

## Interview answer

“Training memory is weights plus gradients, optimizer state, and saved activations;
inference is weights plus KV cache and peak activations. FLOPs are dominated by
dense projections at ordinary context lengths, while attention and memory movement
become decisive as sequence length and batch size grow.”

## Sources

- [Alisa’s book of LLMs](https://app.notion.com/p/388cad4fb60580748c53ff558a15beb0)
- [Distributed Framework](https://www.yuque.com/shakewin/sysgq3/mhw00hcggbv1scr8)

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[transformer-architecture|Transformer Architecture]], [[backpropagation-and-autodiff|Backpropagation and Automatic Differentiation]], [[gpu-performance-model|GPU Performance Model for LLMs]]
- Used by: [[mixed-precision-training|Mixed-Precision Training]], [[fully-sharded-data-parallelism|Fully Sharded Data Parallelism]], [[kv-cache|KV Cache]]

<!-- END GENERATED OBSIDIAN LINKS -->
