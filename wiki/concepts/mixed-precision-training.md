---
id: mixed-precision-training
title: Mixed-Precision Training
type: concept
domains: [training, systems]
aliases: [BF16 training, FP16 training]
level: intermediate
relations:
  prerequisites: [ml-generalization-and-regularization]
  contrasts_with: [model-quantization]
sources: [yuque:245719568, yuque:283802487, notion:388cad4f-b605-8074-8c53-ff558a15beb0]
---

# Mixed-Precision Training

Mixed-precision training uses low-precision tensors for expensive operations while
retaining higher precision where accumulation or updates need stability.

BF16 keeps FP32-like exponent range with fewer mantissa bits; FP16 offers more
mantissa precision but a narrower range and often needs loss scaling. FP8 can improve
throughput further with stricter scaling and kernel requirements. This is primarily
a training execution strategy; quantization usually targets a compact stored or
served model. Numeric overflow, underflow, and reduction error require monitoring.

## Sources

- [Knowledge Puzzle](https://www.yuque.com/shakewin/woezs0/fvhczuilmmhpf6t4)
- [Distributed Framework](https://www.yuque.com/shakewin/sysgq3/mhw00hcggbv1scr8)
- [Alisa’s book of LLMs](https://app.notion.com/p/388cad4fb60580748c53ff558a15beb0)

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[ml-generalization-and-regularization|ML Generalization and Regularization]]
- Contrasts with: [[model-quantization|Model Quantization]]

<!-- END GENERATED OBSIDIAN LINKS -->
