---
id: recurrent-neural-network
title: Recurrent Neural Networks
type: concept
domains: [model-architecture, sequence-modeling]
aliases: [RNN, LSTM, GRU]
level: foundational
relations:
  prerequisites: [neural-network-computation, backpropagation-and-autodiff]
  contrasts_with: [transformer-architecture, state-space-model]
sources: [notion:388cad4f-b605-8074-8c53-ff558a15beb0, yuque:222458626]
---

# Recurrent Neural Networks

An RNN processes a sequence by repeatedly updating a fixed-size hidden state with
shared weights. This gives linear sequence work and constant recurrent state at
inference, but training is sequential across positions and long-range information
must survive every intermediate update.

Repeated Jacobian products cause gradients to vanish or explode. LSTMs introduce a
cell-state highway controlled by forget, input, and output gates; when the forget
gate remains near one, information and gradients can travel farther. GRUs simplify
the same gated-memory idea.

Attention gives direct paths between token pairs and trains across positions in
parallel, at the cost of dense pairwise work and a growing cache. RNNs retain a
useful mental model for streaming systems and motivate modern state-space models.

## Interview answer

“An RNN compresses the prefix into a recurrent hidden state. It is cheap to stream,
but sequential training and repeated Jacobians hurt parallelism and long-range
credit assignment; LSTM gates create a more stable memory path.”

## Sources

- [Alisa’s book of LLMs](https://app.notion.com/p/388cad4fb60580748c53ff558a15beb0)
- [Deep Learning with PyTorch](https://www.yuque.com/shakewin/fidaqi/rwg53sz1y5tcidkw)

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[neural-network-computation|Neural Network Computation]], [[backpropagation-and-autodiff|Backpropagation and Automatic Differentiation]]
- Contrasts with: [[transformer-architecture|Transformer Architecture]], [[state-space-model|State Space Models]]

<!-- END GENERATED OBSIDIAN LINKS -->
