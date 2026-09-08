---
id: distributed-systems-drills
title: Distributed Training and MLOps Drills
type: interview
domains: [distributed-systems, training, mlops]
aliases: []
level: mixed
relations:
  prerequisites: [distributed-training-and-mlops]
sources: [yuque:283802487, yuque:253935769, yuque:245719568]
---

# Distributed Training and MLOps Drills

## Compare DP, FSDP, TP, PP, and EP.

DP replicates models; FSDP shards state; TP splits layer tensors; PP splits layers;
EP places routed experts. Compare what each saves and which collective it adds.

## Why can eight GPUs be slower than one?

Small workloads, PCIe topology, frequent collectives, pipeline bubbles, imbalance,
and synchronization can exceed the saved computation.

## BF16 versus FP16?

BF16 has wider exponent range and is easier to train; FP16 has more mantissa precision
but often needs loss scaling. Kernel support determines realized benefit.

## Mixed precision versus quantization?

Mixed precision usually preserves higher-precision master/accumulation paths during
training. Quantization targets compact weight, activation, or cache representation,
often for inference.

## What belongs in a distributed smoke-test matrix?

Single CPU/GPU baselines, each parallel dimension, representative combinations,
loss parity, memory, throughput, utilization, checkpoint recovery, and multi-node runs.

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[distributed-training-and-mlops|Distributed Training and MLOps Map]]

<!-- END GENERATED OBSIDIAN LINKS -->
