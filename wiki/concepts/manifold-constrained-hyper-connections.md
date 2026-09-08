---
id: manifold-constrained-hyper-connections
title: Manifold-Constrained Hyper-Connections
type: concept
domains: [model-architecture, distributed-systems]
aliases: [mHC, hyper-connections]
level: advanced
relations:
  prerequisites: [residual-network]
  affects: [pipeline-parallelism]
sources: [yuque:260283661]
---

# Manifold-Constrained Hyper-Connections

mHC generalizes one residual stream into multiple streams connected by learned
pre-, post-, and residual mixing matrices, while constraining the mixing to improve
training stability.

The manifold constraint maps residual mixing toward doubly stochastic structure so
signals do not grow or collapse arbitrarily. Multiple streams increase activation,
I/O, and pipeline communication, so the design also depends on fused kernels and
overlap-aware scheduling. It illustrates a recurring lesson: an architectural gain
must be co-designed with memory movement and distributed execution.

## Source

- [mHC](https://www.yuque.com/shakewin/woezs0/qcd8g69ec9wrft2a)

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[residual-network|Residual Networks]]
- Affects: [[pipeline-parallelism|Pipeline Parallelism]]

<!-- END GENERATED OBSIDIAN LINKS -->
