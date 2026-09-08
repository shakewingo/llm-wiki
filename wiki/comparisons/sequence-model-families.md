---
id: sequence-model-families
title: RNNs, Transformers, and State Space Models
type: comparison
domains: [model-architecture, sequence-modeling]
aliases: []
level: intermediate
relations:
  prerequisites: [recurrent-neural-network, transformer-architecture, state-space-model]
sources: [notion:388cad4f-b605-8074-8c53-ff558a15beb0]
---

# RNNs, Transformers, and State Space Models

| Family | Training across positions | Inference state | Long-range access | Primary tradeoff |
|---|---|---|---|---|
| RNN/LSTM | Sequential | Fixed-size hidden/cell state | Information passes through every step | Cheap streaming, difficult parallelism and long credit paths |
| Transformer | Parallel | KV cache grows with context | Direct content-based lookup | Strong recall and hardware utilization, quadratic dense attention |
| Selective SSM | Parallel scan/convolution | Fixed-size latent state | Compressed into learned dynamics | Linear scaling, but state bottleneck may lose exact history |

The asymptotic comparison is not the whole engineering decision. Kernel maturity,
hardware utilization, hybrid layers, task length, and whether exact retrieval is
needed often dominate. Transformers exchange memory for direct access; recurrent
families exchange direct access for compression.

## Sources

- [Alisa’s book of LLMs](https://app.notion.com/p/388cad4fb60580748c53ff558a15beb0)

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[recurrent-neural-network|Recurrent Neural Networks]], [[transformer-architecture|Transformer Architecture]], [[state-space-model|State Space Models]]

<!-- END GENERATED OBSIDIAN LINKS -->
