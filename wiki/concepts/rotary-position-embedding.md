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

The design goal is a map `f` with `⟨f(q,m), f(k,n)⟩ = g(q,k,n−m)` for positions `m`
and `n`. RoPE is one solution: rotate by an angle proportional to position, so that
`R_mθᵀ = R_−mθ` and `R_αR_β = R_(α+β)` leave the score depending only on `n−m`.
Any other construction with the same property would serve equally well.

It is applied to queries and keys, not values, because position only needs to change
*which* tokens attend to each other, not *what* content is passed forward. Values
carry content only, which is also why cached values stay valid without re-rotation.
Frequencies span local through long-range scales: `H` dimensions form `H/2` pairs
rotated at `θ_i = Θ^(−2i/H)`, an exponential, log-uniform spread borrowed from
sinusoidal encodings. Small `θ_i` (large `i`) rotate slowly and encode long-range
structure, large `θ_i` (small `i`) rotate fast and give local discrimination.

`Θ` (HF's `rotary_base`, typically 10,000) is the only hyperparameter and it sets the
native range: the slowest pair completes one full rotation over `2πΘ` positions.
Scores also decay with distance, so extending far beyond the trained context exposes
angles the model never saw — hence interpolation and schemes such as YaRN that rescale
selected frequency bands. Implementations never build the block-diagonal rotation
matrix; they do element-wise `cos`/`sin` multiplications, equivalent to multiplying
each dimension pair by `e^{iθ}`.
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
