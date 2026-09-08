---
id: contrastive-language-image-pretraining
title: Contrastive Language–Image Pretraining
type: concept
domains: [multimodal, model-architecture]
aliases: [CLIP]
level: intermediate
relations:
  prerequisites: [encoder-decoder]
  enables: [multimodal-ai-systems, diffusion-model]
sources: [yuque:181670371, yuque:145950470]
---

# Contrastive Language–Image Pretraining

CLIP trains image and text encoders so matched pairs have high similarity and
mismatched pairs have low similarity in a shared embedding space.

A batch supplies many negatives, and losses are normally computed in both
image-to-text and text-to-image directions. Normalized embeddings and a learned
temperature control similarity scale. The shared space enables zero-shot
classification, retrieval, and text conditioning for image generation, but it can
inherit dataset bias and learn shortcuts from captions.

## Sources

- [Code Vision Multimodel from Scratch](https://www.yuque.com/shakewin/nigzu8/kq9vzdczzx6w9b2t)
- [Diffusion Model](https://www.yuque.com/shakewin/woezs0/ppbpaxtvhppyvtse)

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[encoder-decoder|Encoder–Decoder Models]]
- Enables: [[multimodal-ai-systems|Multimodal AI Systems]], [[diffusion-model|Diffusion Models]]

<!-- END GENERATED OBSIDIAN LINKS -->
