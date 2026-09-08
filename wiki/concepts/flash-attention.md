---
id: flash-attention
title: FlashAttention
type: concept
domains: [inference, training, systems]
aliases: [Flash Attention, IO-aware exact attention]
level: advanced
relations:
  prerequisites: [self-attention, numerical-stability, gpu-performance-model]
  affects: [llm-compute-and-memory-accounting]
sources: [notion:388cad4f-b605-8074-8c53-ff558a15beb0]
---

# FlashAttention

FlashAttention computes exact scaled dot-product attention in tiles sized for fast
on-chip memory. Standard eager attention materializes the full score and probability
matrices in high-bandwidth memory; repeatedly writing and reading those quadratic
intermediates can cost more time than the arithmetic itself.

Each query tile streams through key/value tiles while maintaining a running maximum,
softmax denominator, and weighted value accumulator. When a later tile contains a
larger maximum, previous partial sums are rescaled. This online-softmax invariant
produces the same mathematical result as dense attention without storing the full
$N\times N$ matrix.

It reduces attention activation memory from quadratic to linear in sequence length
and improves speed by reducing memory traffic. It does not change dense attention's
quadratic arithmetic complexity, and kernel eligibility still depends on hardware,
dtype, head dimension, masking, and framework support.

## Interview answer

“FlashAttention is an exact IO-aware attention algorithm. It tiles Q, K, and V into
on-chip memory and uses online softmax, avoiding the quadratic score-matrix traffic;
memory falls to linear even though dense attention FLOPs remain quadratic.”

## Sources

- [Alisa’s book of LLMs](https://app.notion.com/p/388cad4fb60580748c53ff558a15beb0)

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[self-attention|Self-Attention]], [[numerical-stability|Numerical Stability in Neural Networks]], [[gpu-performance-model|GPU Performance Model for LLMs]]
- Affects: [[llm-compute-and-memory-accounting|LLM Compute and Memory Accounting]]

<!-- END GENERATED OBSIDIAN LINKS -->
