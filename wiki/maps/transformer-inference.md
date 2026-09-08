---
id: transformer-inference
title: Transformer Inference Map
type: map
domains: [inference, model-architecture, serving]
aliases: []
level: mixed
entry_points:
  - transformer-architecture
  - kv-cache
  - prompt-caching
  - speculative-decoding
  - continuous-batching-and-sequence-packing
  - flash-attention
relations:
  prerequisites: [transformer-architecture]
sources:
  - yuque:145104021
  - yuque:145901413
  - yuque:271488122
  - yuque:267998979
  - yuque:279560513
  - yuque:267998961
  - yuque:283802487
  - yuque:241299652
  - notion:388cad4f-b605-8074-8c53-ff558a15beb0
---

# Transformer Inference Map

Transformer inference is easiest to reason about as four interacting levers:
what each token must compute, what state is retained, what work can be reused or
skipped, and how the work is placed across hardware.

## Suggested learning path

1. Begin with [Transformer architecture](../concepts/transformer-architecture.md),
   [self-attention](../concepts/self-attention.md), and
   [causal attention](../concepts/causal-attention.md).
2. Learn why sequential decode creates a [KV cache](../concepts/kv-cache.md) and
   why [RoPE](../concepts/rotary-position-embedding.md) must agree with cache positions.
3. Compare architectural cache reduction:
   [MQA](../concepts/multi-query-attention.md),
   [GQA](../concepts/grouped-query-attention.md), and
   [MLA](../concepts/multi-head-latent-attention.md).
4. Study serving-time state reuse with
   [prompt caching](../concepts/prompt-caching.md),
   [paged attention](../concepts/paged-attention.md), and
   [radix attention](../concepts/radix-attention.md).
5. Study work avoidance and parallel verification through
   [speculative decoding](../concepts/speculative-decoding.md),
   [multi-token prediction](../concepts/multi-token-prediction.md), and
   [dynamic sparse attention](../concepts/dynamic-sparse-attention.md).
6. Connect kernels and scheduling through
   [FlashAttention](../concepts/flash-attention.md) and
   [continuous batching](../concepts/continuous-batching-and-sequence-packing.md).
7. Finish with placement: [tensor parallelism](../concepts/tensor-parallelism.md),
   [mixture of experts](../concepts/mixture-of-experts.md), and
   [expert parallelism](../concepts/expert-parallelism.md).

## The big picture

| Lever | Main benefit | Main cost or risk |
|---|---|---|
| Cache K/V | Avoid prefix reprojection | Memory grows with context and batch |
| Reduce KV heads or dimensions | Lower cache bytes and bandwidth | Quality or implementation complexity |
| Reuse shared prefixes | Lower prefill time and cost | Key correctness, privacy, eviction |
| Draft and verify | Parallelize several token checks | Low acceptance can erase gains |
| Select sparse history | Avoid full-context attention | Retrieval misses become quality errors |
| Tile exact attention | Avoid quadratic HBM intermediates | Kernel and hardware constraints |
| Continuously refill batches | Improve serving utilization | Scheduler and latency complexity |
| Shard computation | Fit and serve larger models | Communication and topology bottlenecks |

The common systems thread is arithmetic intensity. Modern accelerators can multiply
quickly, while parameter and cache movement is expensive. An optimization is useful
only when its saved bytes or parallel work exceed its lookup, communication, or
verification overhead.

## Practice

Use [Transformer inference drills](../interview/transformer-inference-drills.md) to
rehearse the map as design tradeoffs rather than isolated definitions.

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[transformer-architecture|Transformer Architecture]]

<!-- END GENERATED OBSIDIAN LINKS -->
