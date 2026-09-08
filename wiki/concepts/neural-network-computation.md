---
id: neural-network-computation
title: Neural Network Computation
type: concept
domains: [foundations, model-architecture]
aliases: [multi-layer perceptron, MLP, feed-forward neural network]
level: foundational
relations:
  enables: [backpropagation-and-autodiff, transformer-architecture, recurrent-neural-network]
sources: [notion:388cad4f-b605-8074-8c53-ff558a15beb0, yuque:222458626]
---

# Neural Network Computation

A neural-network layer applies an affine transformation followed by a nonlinear
function. For a batch stored by rows, $H=f(XW+b)$ maps
$X\in\mathbb{R}^{B\times d_{in}}$ through
$W\in\mathbb{R}^{d_{in}\times d_{out}}$; the bias is broadcast across examples.

Stacked linear maps without nonlinearities collapse into one linear map. Activation
functions therefore provide the representational gain from depth. ReLU is cheap but
can create permanently inactive units; sigmoid and tanh saturate; gated activations
such as SwiGLU let one projection modulate another.

Shape reasoning is as important as the equation. Frameworks may store weights
transposed relative to mathematical notation, while the batch dimension is preserved
for activation gradients and reduced when accumulating gradients for shared weights.

## Interview answer

“An MLP alternates affine maps with nonlinearities. Batching turns neuron-wise dot
products into matrix multiplication; during backpropagation, activation gradients
retain the batch axis while gradients of shared parameters sum over it.”

## Sources

- [Alisa’s book of LLMs](https://app.notion.com/p/388cad4fb60580748c53ff558a15beb0)
- [Deep Learning with PyTorch](https://www.yuque.com/shakewin/fidaqi/rwg53sz1y5tcidkw)

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Enables: [[backpropagation-and-autodiff|Backpropagation and Automatic Differentiation]], [[transformer-architecture|Transformer Architecture]], [[recurrent-neural-network|Recurrent Neural Networks]]

<!-- END GENERATED OBSIDIAN LINKS -->
