---
id: llm-compute-and-memory-accounting
title: LLM Compute and Memory Accounting
type: concept
domains: [systems, training, inference]
aliases: [LLM FLOP accounting, training memory accounting, inference memory accounting]
level: advanced
relations:
  prerequisites: [transformer-architecture, backpropagation-and-autodiff, gpu-performance-model]
  used_by: [mixed-precision-training, fully-sharded-data-parallelism, kv-cache]
sources: [notion:388cad4f-b605-8074-8c53-ff558a15beb0, yuque:283802487]
---

# LLM Compute and Memory Accounting

LLM capacity planning separates parameters, optimizer state, gradients, activations,
and persistent inference state. Training retains or recomputes activations for
backpropagation and often keeps higher-precision master weights plus Adam moments.
Inference drops optimizer and gradient state but adds a KV cache that grows with
batch size, context length, layers, KV heads, head dimension, and element width.

For dense Transformers, projection and FFN work scales roughly with tokens times
parameter count, while attention adds a sequence-dependent term. The common
$6\times\text{tokens}\times\text{parameters}$ training estimate combines a dense
forward pass with two comparable backward matrix multiplications; it is a useful
approximation, not a replacement for architecture-specific accounting.

Peak memory, not just totals, determines whether an execution fits. FlashAttention,
activation checkpointing, GQA/MLA, sharding, and reduced precision each remove a
different term, so their savings should not be added blindly.

## Interview answer

“Training memory is weights plus gradients, optimizer state, and saved activations;
inference is weights plus KV cache and peak activations. FLOPs are dominated by
dense projections at ordinary context lengths, while attention and memory movement
become decisive as sequence length and batch size grow.”

## Sources

- [Alisa’s book of LLMs](https://app.notion.com/p/388cad4fb60580748c53ff558a15beb0)
- [Distributed Framework](https://www.yuque.com/shakewin/sysgq3/mhw00hcggbv1scr8)

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[transformer-architecture|Transformer Architecture]], [[backpropagation-and-autodiff|Backpropagation and Automatic Differentiation]], [[gpu-performance-model|GPU Performance Model for LLMs]]
- Used by: [[mixed-precision-training|Mixed-Precision Training]], [[fully-sharded-data-parallelism|Fully Sharded Data Parallelism]], [[kv-cache|KV Cache]]

<!-- END GENERATED OBSIDIAN LINKS -->
