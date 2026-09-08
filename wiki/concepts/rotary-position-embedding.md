---
id: rotary-position-embedding
title: Rotary Position Embedding
type: concept
domains: [model-architecture, inference]
aliases: [RoPE, rotary embedding]
level: intermediate
relations:
  part_of: [transformer-architecture]
  affects: [multi-head-latent-attention, kv-cache]
sources: [yuque:145901413, yuque:271488122, notion:388cad4f-b605-8074-8c53-ff558a15beb0]
---

# Rotary Position Embedding

RoPE injects position by rotating query and key components so their dot product
depends on relative displacement as well as content.

It is applied to queries and keys, not values. Frequencies span local through
long-range scales; extending far beyond the trained context can expose unseen
angles, so interpolation and schemes such as YaRN modify selected frequency bands.
In ordinary attention, cached keys
already contain their positional rotation. In MLA, position handling must be split
carefully: mixing RoPE into the compressed latent can prevent the weight-absorption
algebra used for efficient decode, so DeepSeek separates positional and compressed
content components.

The failure mode to remember is cache inconsistency: wrong position indices or
different RoPE scaling between prefill and decode corrupt attention even when tensor
shapes remain valid.

## Interview answer

“RoPE rotates Q and K by position so attention scores encode relative distance. Its
placement matters for KV-cache reuse and especially for MLA's absorb-mode algebra.”

## Sources

- [LLaMA](https://www.yuque.com/shakewin/woezs0/avr5nrkaahavwdwv)
- [MLA](https://www.yuque.com/shakewin/woezs0/fz9zd2ttsiywlelx)
- [Alisa’s book of LLMs](https://app.notion.com/p/388cad4fb60580748c53ff558a15beb0)

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Part of: [[transformer-architecture|Transformer Architecture]]
- Affects: [[multi-head-latent-attention|Multi-Head Latent Attention]], [[kv-cache|KV Cache]]

<!-- END GENERATED OBSIDIAN LINKS -->
