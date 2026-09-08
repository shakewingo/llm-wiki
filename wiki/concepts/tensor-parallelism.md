---
id: tensor-parallelism
title: Tensor Parallelism
type: concept
domains: [distributed-systems, inference, training]
aliases: [TP]
level: advanced
relations:
  prerequisites: [transformer-architecture]
  affects: [kv-cache]
  contrasts_with: [fully-sharded-data-parallelism]
sources: [yuque:283802487]
---

# Tensor Parallelism

Tensor parallelism shards individual matrix operations across devices, allowing a
layer that is too large for one accelerator to execute collectively.

It reduces per-device parameter and activation storage but introduces collectives
inside each layer. Because these operations occur frequently, fast links such as
NVLink/NVSwitch matter greatly; PCIe-only topology can erase the theoretical gain.
For inference, TP may also shard attention heads or KV state and changes how serving
batches communicate.

## Interview answer

“Tensor parallelism splits each layer's matrices across devices. It solves model
fit and can add compute throughput, but frequent collectives make interconnect
latency and bandwidth decisive.”

## Source

- [Distributed Framework](https://www.yuque.com/shakewin/sysgq3/mhw00hcggbv1scr8)

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[transformer-architecture|Transformer Architecture]]
- Contrasts with: [[fully-sharded-data-parallelism|Fully Sharded Data Parallelism]]
- Affects: [[kv-cache|KV Cache]]

<!-- END GENERATED OBSIDIAN LINKS -->
