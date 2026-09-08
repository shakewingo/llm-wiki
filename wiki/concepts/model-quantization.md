---
id: model-quantization
title: Model Quantization
type: concept
domains: [model-compression, inference, training]
aliases: [INT8, FP8, low-precision inference]
level: intermediate
relations:
  affects: [kv-cache, mixed-precision-training]
  contrasts_with: [mixed-precision-training]
sources: [yuque:245719568, yuque:253935769, notion:388cad4f-b605-8074-8c53-ff558a15beb0]
---

# Model Quantization

Quantization represents weights, activations, or cache values with fewer bits to
reduce memory, bandwidth, and sometimes compute cost.

Post-training quantization calibrates an existing model; quantization-aware training
adapts parameters to simulated low precision. Per-channel scales handle outliers
better than one global scale, while weights, activations, and KV cache have different
error sensitivity. A smaller representation helps only when the target hardware has
efficient kernels and conversion overhead does not dominate.

## Sources

- [Knowledge Puzzle](https://www.yuque.com/shakewin/woezs0/fvhczuilmmhpf6t4)
- [NVIDIA Agentic AI Training](https://www.yuque.com/shakewin/fidaqi/fgv15n9m42qh9m77)
- [Alisa’s book of LLMs](https://app.notion.com/p/388cad4fb60580748c53ff558a15beb0)

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Contrasts with: [[mixed-precision-training|Mixed-Precision Training]]
- Affects: [[kv-cache|KV Cache]], [[mixed-precision-training|Mixed-Precision Training]]

<!-- END GENERATED OBSIDIAN LINKS -->
