---
id: fully-sharded-data-parallelism
title: Fully Sharded Data Parallelism
type: concept
domains: [distributed-systems, training]
aliases: [FSDP, ZeRO]
level: advanced
relations:
  prerequisites: [data-parallelism]
  contrasts_with: [tensor-parallelism]
sources: [yuque:283802487, notion:388cad4f-b605-8074-8c53-ff558a15beb0]
---

# Fully Sharded Data Parallelism

FSDP shards parameters, gradients, and optimizer state across data-parallel workers,
materializing layer parameters only when needed.

It reduces per-device memory enough to train much larger models while preserving the
data-parallel programming model. The cost is repeated all-gather and reduce-scatter,
plus careful wrapping, checkpointing, mixed precision, and overlap. FSDP shards model
state over time; tensor parallelism splits the computation inside each layer.

## Source

- [Distributed Framework](https://www.yuque.com/shakewin/sysgq3/mhw00hcggbv1scr8)
- [Alisa’s book of LLMs](https://app.notion.com/p/388cad4fb60580748c53ff558a15beb0)

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[data-parallelism|Data Parallelism]]
- Contrasts with: [[tensor-parallelism|Tensor Parallelism]]

<!-- END GENERATED OBSIDIAN LINKS -->
