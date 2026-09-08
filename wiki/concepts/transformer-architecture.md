---
id: transformer-architecture
title: Transformer Architecture
type: concept
domains: [model-architecture, inference]
aliases: [transformer]
level: foundational
relations:
  prerequisites: [self-attention]
  enables: [causal-attention, kv-cache]
  contrasts_with: [graph-neural-network]
sources: [yuque:145104021, yuque:145901413]
legacy_notion_id: fa3cad4f-b605-83e7-9109-81c407243233
---

# Transformer Architecture

A Transformer alternates token-to-token communication through attention with
per-token computation through a feed-forward network, stabilized by residual paths
and normalization.

## Mechanics and mental model

Attention lets each position retrieve information from other positions; the FFN
then transforms the retrieved representation independently at each position.
Stacking these blocks repeatedly alternates communication and computation. A
decoder-only language model masks future tokens and predicts the next token from
the visible prefix.

The original scaled dot-product attention is
$\operatorname{softmax}(QK^T/\sqrt{d_k})V$. The scale keeps logits from growing
with key dimension, while multiple heads learn distinct projections and patterns.

## Tradeoffs and failure modes

- Training parallelizes across sequence positions, but dense attention costs
  quadratic work and memory in sequence length.
- Decode remains sequential across generated tokens and often becomes memory-bandwidth
  bound.
- Architecture details such as RoPE, RMSNorm, SwiGLU, grouped-query attention, and
  cache layout strongly affect modern implementations.

## Interview answer

“A Transformer block mixes information across tokens with attention, transforms
each token with an FFN, and uses residuals plus normalization for stable depth. In
autoregressive inference, causal masking and repeated next-token decoding make KV
caching essential.”

## Sources

- [Attention is All You Need](https://www.yuque.com/shakewin/woezs0/wfnf4pb8yxth3i36)
- [LLaMA](https://www.yuque.com/shakewin/woezs0/avr5nrkaahavwdwv)

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[self-attention|Self-Attention]]
- Enables: [[causal-attention|Causal Attention]], [[kv-cache|KV Cache]]
- Contrasts with: [[graph-neural-network|Graph Neural Networks]]

<!-- END GENERATED OBSIDIAN LINKS -->
