---
id: pipeline-parallelism
title: Pipeline Parallelism
type: concept
domains: [distributed-systems, training]
aliases: [PP]
level: advanced
relations:
  prerequisites: [transformer-architecture]
  affects: [manifold-constrained-hyper-connections]
sources: [yuque:283802487, yuque:260283661]
---

# Pipeline Parallelism

Pipeline parallelism assigns consecutive layer stages to different devices and
streams microbatches through them.

It fits deep models without splitting every matrix, but idle “bubbles,” activation
transfers, and stage imbalance reduce utilization. More microbatches shrink the
bubble but increase scheduling and memory pressure. Multi-stream architectures such
as mHC enlarge stage communication, motivating fused kernels and schedules that
overlap transfers with computation.

## Sources

- [Distributed Framework](https://www.yuque.com/shakewin/sysgq3/mhw00hcggbv1scr8)
- [mHC](https://www.yuque.com/shakewin/woezs0/qcd8g69ec9wrft2a)

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[transformer-architecture|Transformer Architecture]]
- Affects: [[manifold-constrained-hyper-connections|Manifold-Constrained Hyper-Connections]]

<!-- END GENERATED OBSIDIAN LINKS -->
