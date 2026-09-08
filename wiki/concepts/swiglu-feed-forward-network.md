---
id: swiglu-feed-forward-network
title: SwiGLU Feed-Forward Network
type: concept
domains: [model-architecture]
aliases: [SwiGLU, gated feed-forward network]
level: intermediate
relations:
  prerequisites: [neural-network-computation]
  part_of: [transformer-architecture]
sources: [notion:388cad4f-b605-8074-8c53-ff558a15beb0, yuque:145901413]
---

# SwiGLU Feed-Forward Network

SwiGLU is the gated feed-forward sublayer used by many modern decoder-only
Transformers. Two projections create an up branch and a gate branch; the gate uses
the SiLU/Swish activation, their elementwise product is formed, and a down projection
returns to the model dimension:

$$
\operatorname{SwiGLU}(x)=
\bigl(\operatorname{SiLU}(xW_g)\odot xW_u\bigr)W_d.
$$

The gate is not just a scalar switch: both projections are learned feature vectors,
so their product provides conditional, multiplicative computation per token. The
extra projection increases parameter and FLOP accounting relative to a two-matrix
MLP, so implementations often adjust the intermediate width.

## Interview answer

“SwiGLU uses one learned projection, passed through SiLU, to gate another learned
projection elementwise before the down projection. It gives the per-token FFN a
multiplicative conditional pathway.”

## Sources

- [Alisa’s book of LLMs](https://app.notion.com/p/388cad4fb60580748c53ff558a15beb0)
- [LLaMA](https://www.yuque.com/shakewin/woezs0/avr5nrkaahavwdwv)

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[neural-network-computation|Neural Network Computation]]
- Part of: [[transformer-architecture|Transformer Architecture]]

<!-- END GENERATED OBSIDIAN LINKS -->
