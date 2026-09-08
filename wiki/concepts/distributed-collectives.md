---
id: distributed-collectives
title: Distributed Collective Operations
type: concept
domains: [distributed-systems, training]
aliases: [all-reduce, all-gather, reduce-scatter, all-to-all]
level: advanced
relations:
  prerequisites: [gpu-performance-model]
  used_by: [data-parallelism, fully-sharded-data-parallelism, tensor-parallelism, expert-parallelism, context-parallelism]
sources: [notion:388cad4f-b605-8074-8c53-ff558a15beb0, yuque:283802487]
---

# Distributed Collective Operations

Collectives express how tensor shards move and combine across a process group.
All-gather removes a shard dimension by giving every rank the full value;
reduce-scatter sums replicas and leaves each rank one shard; all-reduce sums and
replicates the result; all-to-all redistributes distinct pieces between every pair.

The backward of all-gather is reduce-scatter because gradients from replicated uses
must sum back onto the owning shard. Conversely, the backward of reduce-scatter is
all-gather. Ring all-reduce can be understood as reduce-scatter followed by
all-gather, avoiding a central coordinator while moving predictable chunks between
neighbors.

Parallelism strategies are largely choices about where these collectives occur.
FSDP gathers parameters and reduce-scatters gradients; tensor parallelism reduces
partial matrix products; expert parallelism uses all-to-all token routing. Their
cost depends on message size, latency, bandwidth, topology, and overlap with compute.

## Interview answer

“All-gather assembles shards, reduce-scatter sums then shards, all-reduce sums and
replicates, and all-to-all redistributes unique pieces. A parallelism plan is useful
only when its saved memory or compute outweighs those communication costs.”

## Sources

- [Alisa’s book of LLMs](https://app.notion.com/p/388cad4fb60580748c53ff558a15beb0)
- [Distributed Framework](https://www.yuque.com/shakewin/sysgq3/mhw00hcggbv1scr8)

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[gpu-performance-model|GPU Performance Model for LLMs]]
- Used by: [[data-parallelism|Data Parallelism]], [[fully-sharded-data-parallelism|Fully Sharded Data Parallelism]], [[tensor-parallelism|Tensor Parallelism]], [[expert-parallelism|Expert Parallelism]], [[context-parallelism|Context Parallelism]]

<!-- END GENERATED OBSIDIAN LINKS -->
