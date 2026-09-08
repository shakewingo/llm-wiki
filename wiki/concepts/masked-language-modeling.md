---
id: masked-language-modeling
title: Masked Language Modeling
type: concept
domains: [pretraining, model-architecture]
aliases: [MLM]
level: foundational
relations:
  prerequisites: [transformer-architecture]
  enables: [bert]
sources: [yuque:145104004, yuque:222458626]
---

# Masked Language Modeling

Masked-language modeling corrupts selected input tokens and trains an encoder to
recover them using context on both sides.

The objective learns contextual representations suited to understanding tasks, but
pretraining sees artificial mask tokens that downstream inputs usually lack. Masking
too little wastes context; masking too much removes the evidence required for
reconstruction. MLM differs from causal language modeling, which predicts each next
token using only the left prefix and aligns directly with autoregressive generation.

## Sources

- [BERT](https://www.yuque.com/shakewin/woezs0/havcwgm88z0449od)
- [Deep Learning PyTorch](https://www.yuque.com/shakewin/fidaqi/rwg53sz1y5tcidkw)

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[transformer-architecture|Transformer Architecture]]
- Enables: [[bert|BERT]]

<!-- END GENERATED OBSIDIAN LINKS -->
