---
id: backpropagation-and-autodiff
title: Backpropagation and Automatic Differentiation
type: concept
domains: [foundations, training]
aliases: [backpropagation, backprop, automatic differentiation, autodiff]
level: foundational
relations:
  prerequisites: [neural-network-computation]
  enables: [deep-learning-optimization, llm-compute-and-memory-accounting]
sources: [notion:388cad4f-b605-8074-8c53-ff558a15beb0, yuque:222458626]
---

# Backpropagation and Automatic Differentiation

Backpropagation computes parameter gradients by applying the chain rule through a
computation graph in reverse topological order. Each operation combines an incoming
gradient with its local derivative; gradients add when one value feeds multiple
downstream branches.

Reverse-mode automatic differentiation is efficient for a scalar loss with many
parameters because one reverse traversal produces every parameter gradient. Its
compute is of the same order as the forward pass, but it needs intermediate
activations. Activation checkpointing stores selected boundaries and recomputes the
missing forward segments during backward, exchanging extra compute for lower memory.

Gradient checking with centered finite differences is useful for small tests, but
it scales poorly and is sensitive to step size and floating-point error.

## Interview answer

“Backprop is reverse-mode autodiff over a computation graph. It multiplies upstream
and local derivatives, sums at fan-out points, and normally retains forward
activations; checkpointing saves memory by recomputing some of them.”

## Sources

- [Alisa’s book of LLMs](https://app.notion.com/p/388cad4fb60580748c53ff558a15beb0)
- [Deep Learning with PyTorch](https://www.yuque.com/shakewin/fidaqi/rwg53sz1y5tcidkw)

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[neural-network-computation|Neural Network Computation]]
- Enables: [[deep-learning-optimization|Deep Learning Optimization]], [[llm-compute-and-memory-accounting|LLM Compute and Memory Accounting]]

<!-- END GENERATED OBSIDIAN LINKS -->
