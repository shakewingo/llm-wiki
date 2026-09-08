---
id: knowledge-distillation
title: Knowledge Distillation
type: concept
domains: [training, model-compression]
aliases: [teacher-student distillation]
level: intermediate
relations:
  prerequisites: [probabilistic-objectives]
  enables: [model-quantization]
sources: [yuque:247276544, yuque:253935769, yuque:241299652]
---

# Knowledge Distillation

Distillation trains a smaller student to match a stronger teacher's outputs,
probabilities, representations, or reasoning traces.

Soft targets expose similarities that hard labels omit, while temperature controls
how much probability mass is revealed. A student can inherit useful reasoning data,
but also teacher bias, hallucinations, and formatting artifacts. Distillation lowers
serving cost only when the resulting student is evaluated on real tasks; matching
teacher logits is a training mechanism, not proof of equivalent capability.

## Sources

- [GetHandsDirty](https://www.yuque.com/shakewin/xhs6fk/ym86n135t1744rya)
- [NVIDIA Agentic AI Training](https://www.yuque.com/shakewin/fidaqi/fgv15n9m42qh9m77)
- [DeepSeek Paper Reading](https://www.yuque.com/shakewin/woezs0/agn9y7w2skcvzzrk)

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[probabilistic-objectives|Probabilistic Objectives]]
- Enables: [[model-quantization|Model Quantization]]

<!-- END GENERATED OBSIDIAN LINKS -->
