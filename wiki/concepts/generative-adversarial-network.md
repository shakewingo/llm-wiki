---
id: generative-adversarial-network
title: Generative Adversarial Networks
type: concept
domains: [generative-models]
aliases: [GAN]
level: intermediate
relations:
  prerequisites: [probabilistic-objectives]
  contrasts_with: [diffusion-model, variational-autoencoder]
sources: [yuque:204005901]
---

# Generative Adversarial Networks

A GAN trains a generator to fool a discriminator while the discriminator learns to
separate real from generated samples.

Adversarial learning can produce sharp samples without an explicit likelihood, but
the coupled game is unstable and may collapse to limited modes. Balance between the
two networks, objective choice, normalization, and evaluation all matter. VAEs offer
a structured latent likelihood objective but often blur; diffusion models trade many
denoising steps for stable high-quality generation.

## Source

- [MLi Paper Reading](https://www.yuque.com/shakewin/woezs0/hhoofowylkt3t2id)

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[probabilistic-objectives|Probabilistic Objectives]]
- Contrasts with: [[diffusion-model|Diffusion Models]], [[variational-autoencoder|Variational Autoencoder]]

<!-- END GENERATED OBSIDIAN LINKS -->
