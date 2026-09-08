---
id: data-parallelism
title: Data Parallelism
type: concept
domains: [distributed-systems, training]
aliases: [DP, distributed data parallel]
level: intermediate
relations:
  prerequisites: [pretraining]
  enables: [fully-sharded-data-parallelism]
sources: [yuque:283802487]
---

# Data Parallelism

Data parallelism replicates a model across workers, processes different mini-batch
shards, and synchronizes gradients so replicas remain equivalent.

All-reduce communication grows with parameter size, while useful compute grows with
local batch size. Small microbatches, slow links, stragglers, or incorrect loss
scaling reduce efficiency. DDP keeps complete parameters and optimizer state on every
worker; sharded variants reduce that redundancy at the cost of more communication
and lifecycle complexity.

## Source

- [Distributed Framework](https://www.yuque.com/shakewin/sysgq3/mhw00hcggbv1scr8)

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[pretraining|Language-Model Pretraining]]
- Enables: [[fully-sharded-data-parallelism|Fully Sharded Data Parallelism]]

<!-- END GENERATED OBSIDIAN LINKS -->
