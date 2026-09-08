---
id: context-parallelism
title: Context Parallelism
type: concept
domains: [distributed-systems, training, inference]
aliases: [CP, sequence parallelism, ring attention]
level: advanced
relations:
  prerequisites: [self-attention, flash-attention, distributed-collectives]
  affects: [kv-cache, llm-compute-and-memory-accounting]
sources: [notion:388cad4f-b605-8074-8c53-ff558a15beb0, yuque:283802487]
---

# Context Parallelism

Context parallelism shards the sequence dimension across devices so no rank owns
all long-context activations or attention state. Each rank holds a query block and
must combine it with every required key/value block while preserving causal masking
and the numerically stable softmax reduction.

Ring attention rotates K/V blocks between neighboring ranks. For each arriving tile,
a rank updates the running maximum, denominator, and weighted-value accumulator for
its local queries—the distributed analogue of FlashAttention's online softmax.
Other layouts use all-to-all transformations or sequence-parallel sublayers.

The method extends feasible context length but adds communication proportional to
the circulated state. Load balance, topology, overlap, position handling, and causal
tile scheduling determine whether memory savings translate into speed.

## Interview answer

“Context parallelism partitions tokens rather than layers or matrix dimensions.
Ring attention circulates K/V tiles and combines them with online softmax, reducing
per-device context memory while paying communication and scheduling overhead.”

## Sources

- [Alisa’s book of LLMs](https://app.notion.com/p/388cad4fb60580748c53ff558a15beb0)
- [Distributed Framework](https://www.yuque.com/shakewin/sysgq3/mhw00hcggbv1scr8)

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[self-attention|Self-Attention]], [[flash-attention|FlashAttention]], [[distributed-collectives|Distributed Collective Operations]]
- Affects: [[kv-cache|KV Cache]], [[llm-compute-and-memory-accounting|LLM Compute and Memory Accounting]]

<!-- END GENERATED OBSIDIAN LINKS -->
