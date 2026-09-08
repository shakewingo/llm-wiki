---
id: bert
title: BERT
type: concept
domains: [model-architecture, pretraining]
aliases: [Bidirectional Encoder Representations from Transformers]
level: foundational
relations:
  prerequisites: [transformer-architecture, masked-language-modeling]
  implemented_in: [sentence-embeddings]
sources: [yuque:145104004, yuque:222458626, yuque:204005901]
---

# BERT

BERT is an encoder-only Transformer pretrained to build bidirectional token
representations and then fine-tuned for downstream understanding tasks.

Masked-language modeling hides selected tokens and predicts them from both left and
right context. The original model also used next-sentence prediction. Task-specific
heads adapt the representation to classification, span-based question answering,
and other discriminative tasks. Unlike a causal decoder, BERT does not naturally
generate long text token by token.

## Sources

- [BERT](https://www.yuque.com/shakewin/woezs0/havcwgm88z0449od)
- [Deep Learning PyTorch](https://www.yuque.com/shakewin/fidaqi/rwg53sz1y5tcidkw)
- [MLi Paper Reading](https://www.yuque.com/shakewin/woezs0/hhoofowylkt3t2id)

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[transformer-architecture|Transformer Architecture]], [[masked-language-modeling|Masked Language Modeling]]
- Implemented in: [[sentence-embeddings|Sentence Embeddings]]

<!-- END GENERATED OBSIDIAN LINKS -->
