---
id: diffusion-model
title: Diffusion Models
type: concept
domains: [generative-models, multimodal]
aliases: [DDPM, denoising diffusion]
level: intermediate
relations:
  prerequisites: [probabilistic-objectives]
  used_by: [multimodal-ai-systems]
  contrasts_with: [generative-adversarial-network]
sources: [yuque:145950470]
---

# Diffusion Models

A diffusion model learns to reverse a gradual noising process, turning random noise
into samples through repeated denoising steps.

The forward process has fixed Gaussian transitions; the neural network predicts
noise, score, or a related parameterization for the reverse process. Stable Diffusion
operates in a compressed VAE latent space and conditions a U-Net on text embeddings,
reducing pixel-space cost. Diffusion offers stable training and high sample quality,
but iterative sampling is slower than a single autoregressive or GAN forward pass.

## Source

- [Diffusion Model](https://www.yuque.com/shakewin/woezs0/ppbpaxtvhppyvtse)

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[probabilistic-objectives|Probabilistic Objectives]]
- Used by: [[multimodal-ai-systems|Multimodal AI Systems]]
- Contrasts with: [[generative-adversarial-network|Generative Adversarial Networks]]

<!-- END GENERATED OBSIDIAN LINKS -->
