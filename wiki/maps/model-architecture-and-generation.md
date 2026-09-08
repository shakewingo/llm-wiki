---
id: model-architecture-and-generation
title: Model Architecture and Generation Map
type: map
domains: [model-architecture, generative-models, multimodal]
aliases: []
level: mixed
entry_points:
  - rms-normalization
  - swiglu-feed-forward-network
  - encoder-decoder
  - bert
  - masked-language-modeling
  - residual-network
  - graph-neural-network
  - variational-autoencoder
  - generative-adversarial-network
  - diffusion-model
  - contrastive-language-image-pretraining
  - engram-conditional-memory
  - manifold-constrained-hyper-connections
  - recurrent-neural-network
  - state-space-model
relations:
  prerequisites: [foundations, transformer-architecture]
sources: [yuque:145104004, yuque:145950470, yuque:181670371, yuque:204005901, yuque:260446359, yuque:260283661, notion:388cad4f-b605-8074-8c53-ff558a15beb0]
---

# Model Architecture and Generation Map

Architecture determines which interactions are cheap, what information is retained,
and which inductive bias the model receives.

For a modern decoder block, connect [RMSNorm](../concepts/rms-normalization.md) and
the [SwiGLU FFN](../concepts/swiglu-feed-forward-network.md) to attention and the
residual stream. These details control scale, parameter count, and computation even
though the high-level architecture diagram often hides them.

Start with [encoder–decoder models](../concepts/encoder-decoder.md),
[BERT](../concepts/bert.md), and [masked-language modeling](../concepts/masked-language-modeling.md).
Then connect depth through [residual networks](../concepts/residual-network.md) and
explicit topology through [graph neural networks](../concepts/graph-neural-network.md).

For generation, compare the probabilistic latent of a
[VAE](../concepts/variational-autoencoder.md), the adversarial game of a
[GAN](../concepts/generative-adversarial-network.md), and iterative denoising in a
[diffusion model](../concepts/diffusion-model.md). [CLIP](../concepts/contrastive-language-image-pretraining.md)
bridges image and text spaces. Finally, [Engram](../concepts/engram-conditional-memory.md)
and [mHC](../concepts/manifold-constrained-hyper-connections.md) show current attempts
to change memory lookup and residual topology.

Finally compare [recurrent networks](../concepts/recurrent-neural-network.md),
[Transformers](../concepts/transformer-architecture.md), and
[state-space models](../concepts/state-space-model.md) by training parallelism,
inference state, and long-range access. The concise tradeoff table is in
[sequence-model families](../comparisons/sequence-model-families.md).

Practice with [architecture drills](../interview/model-architecture-drills.md).

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[foundations|AI and ML Foundations Map]], [[transformer-architecture|Transformer Architecture]]

<!-- END GENERATED OBSIDIAN LINKS -->
