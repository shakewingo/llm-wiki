---
id: pretraining
title: Language-Model Pretraining
type: concept
domains: [training, pretraining]
aliases: [foundation-model training]
level: foundational
relations:
  prerequisites: [transformer-architecture, probabilistic-objectives]
  enables: [supervised-fine-tuning]
sources: [yuque:145104021, yuque:253935769, yuque:247276544]
---

# Language-Model Pretraining

Pretraining learns broad representations and next-token behavior from large,
mostly unlabeled corpora before task-specific adaptation.

The data pipeline matters as much as architecture: normalization, exact and fuzzy
deduplication, quality filtering, contamination checks, tokenizer training, and
mixture weighting determine what the model can learn. The objective is usually
token-level cross-entropy. Continued pretraining can add domain knowledge, but an
imbalanced corpus may cause catastrophic forgetting or narrow the model.

## Interview answer

“Pretraining is large-scale self-supervised representation learning. Its critical
engineering problems are data quality, contamination, compute efficiency, and
stable optimization—not merely collecting more text.”

## Sources

- [Attention is All You Need](https://www.yuque.com/shakewin/woezs0/wfnf4pb8yxth3i36)
- [NVIDIA Agentic AI Training](https://www.yuque.com/shakewin/fidaqi/fgv15n9m42qh9m77)
- [GetHandsDirty](https://www.yuque.com/shakewin/xhs6fk/ym86n135t1744rya)

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[transformer-architecture|Transformer Architecture]], [[probabilistic-objectives|Probabilistic Objectives]]
- Enables: [[supervised-fine-tuning|Supervised Fine-Tuning]]

<!-- END GENERATED OBSIDIAN LINKS -->
