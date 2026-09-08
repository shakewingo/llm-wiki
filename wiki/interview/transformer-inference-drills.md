---
id: transformer-inference-drills
title: Transformer Inference Drills
type: interview
domains: [inference, serving]
aliases: []
level: mixed
relations:
  prerequisites: [transformer-inference]
sources:
  - yuque:145901413
  - yuque:271488122
  - yuque:267998979
  - yuque:279560513
  - yuque:267998961
  - yuque:283802487
---

# Transformer Inference Drills

## 1. Why does a KV cache speed generation but limit concurrency?

Each decode step reuses stored K/V tensors instead of recomputing the prefix, but
the retained state grows with layers, context, batch, KV heads, and element size.
That consumes capacity and must be read repeatedly. Follow-up: compare
[MQA, GQA, and MLA](../comparisons/attention-cache-strategies.md).

## 2. What differs between prefill and decode?

Prefill processes many prompt queries in parallel and populates the cache. Decode
usually processes one new query per sequence against the full retained prefix, so
it has low arithmetic intensity and is often bandwidth-bound. Follow-up:
[causal attention](../concepts/causal-attention.md).

## 3. How can prompt layout affect infrastructure cost?

Prefix caches require exact, stable token prefixes. Moving invariant system and tool
definitions first, keeping serialization deterministic, and delaying dynamic values
increase reuse. Isolation and complete keys prevent cross-tenant leaks. Follow-up:
[prompt caching](../concepts/prompt-caching.md).

## 4. Why can speculative decoding preserve model quality?

The target model still verifies proposals. Greedy output accepts matching target
choices; probabilistic output uses accept/reject correction so samples retain the
target distribution. Follow-up:
[speculative decoding](../concepts/speculative-decoding.md).

## 5. Does MTP mean the model emits several final tokens in one step?

Not necessarily. MTP primarily adds future-token supervision during training.
Auxiliary heads may later act as drafts, but committed output still needs target
verification. Follow-up:
[multi-token prediction](../concepts/multi-token-prediction.md).

## 6. Compare paged and radix prefix caching.

Paged designs use fixed-size KV blocks and block hashes; radix designs organize
shared token sequences as tree paths. Blocks simplify allocation and partial reuse,
while trees naturally model branching prompts. Follow-ups:
[paged attention](../concepts/paged-attention.md) and
[radix attention](../concepts/radix-attention.md).

## 7. What new failure mode does sparse attention introduce?

The retrieval/indexer stage can omit evidence before expensive attention runs. That
makes recall and indexer training part of model correctness, not only performance.
Follow-up: [dynamic sparse attention](../concepts/dynamic-sparse-attention.md).

## 8. Why might more GPUs make a configuration slower?

Tensor and expert parallelism add collectives or all-to-all traffic. On weak links,
communication, synchronization, and routing imbalance outweigh extra compute and
reduced memory. Follow-ups: [tensor parallelism](../concepts/tensor-parallelism.md)
and [expert parallelism](../concepts/expert-parallelism.md).

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[transformer-inference|Transformer Inference Map]]

<!-- END GENERATED OBSIDIAN LINKS -->
