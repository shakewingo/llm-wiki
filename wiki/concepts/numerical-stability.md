---
id: numerical-stability
title: Numerical Stability in Neural Networks
type: concept
domains: [foundations, training, systems]
aliases: [log-sum-exp trick, stable softmax, online softmax]
level: intermediate
relations:
  prerequisites: [probabilistic-objectives, neural-network-computation]
  affects: [self-attention, mixed-precision-training, flash-attention]
sources: [notion:388cad4f-b605-8074-8c53-ff558a15beb0, yuque:245719568]
---

# Numerical Stability in Neural Networks

Mathematically equivalent expressions can behave very differently in finite
precision. Exponentials overflow for large logits, tiny probabilities underflow,
and reductions can lose small contributions when scales differ greatly.

Stable softmax subtracts the maximum logit because softmax is invariant to a common
shift. Log-softmax uses $x_i-\operatorname{logsumexp}(x)$ so it never materializes a
near-zero probability before taking its logarithm. Online softmax carries a running
maximum and rescales the accumulated denominator whenever that maximum changes,
which makes tiled exact attention possible.

Precision policy is operation-specific: matrix multiplication tolerates reduced
precision better than exponentials, normalization, or long reductions. Stability
bugs often produce plausible tensor shapes but NaNs, silent saturation, or divergent
training.

## Interview answer

“Subtracting the maximum makes softmax and log-sum-exp stable without changing their
values. Online softmax extends the same invariant to streamed tiles, rescaling prior
partial sums when a new maximum appears.”

## Sources

- [Alisa’s book of LLMs](https://app.notion.com/p/388cad4fb60580748c53ff558a15beb0)
- [Knowledge Puzzle](https://www.yuque.com/shakewin/woezs0/fvhczuilmmhpf6t4)

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[probabilistic-objectives|Probabilistic Objectives]], [[neural-network-computation|Neural Network Computation]]
- Affects: [[self-attention|Self-Attention]], [[mixed-precision-training|Mixed-Precision Training]], [[flash-attention|FlashAttention]]

<!-- END GENERATED OBSIDIAN LINKS -->
