---
id: encoder-decoder
title: Encoder–Decoder Models
type: concept
domains: [model-architecture]
aliases: [sequence-to-sequence, seq2seq]
level: foundational
relations:
  prerequisites: [self-attention]
  part_of: [transformer-architecture]
sources: [yuque:145104021, yuque:222458626]
---

# Encoder–Decoder Models

An encoder converts an input sequence into contextual states; a decoder generates
an output sequence while attending to its own prefix and the encoder states.

In a Transformer, encoder self-attention is bidirectional, decoder self-attention is
causal, and cross-attention uses decoder queries with encoder keys and values. This
fits translation and summarization where input and output lengths differ. Decoder-only
models instead place instructions and source material in one causal context, gaining
a uniform interface at the cost of recomputing or caching that context.

## Sources

- [Attention is All You Need](https://www.yuque.com/shakewin/woezs0/wfnf4pb8yxth3i36)
- [Deep Learning PyTorch](https://www.yuque.com/shakewin/fidaqi/rwg53sz1y5tcidkw)

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[self-attention|Self-Attention]]
- Part of: [[transformer-architecture|Transformer Architecture]]

<!-- END GENERATED OBSIDIAN LINKS -->
