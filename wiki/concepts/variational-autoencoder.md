---
id: variational-autoencoder
title: Variational Autoencoder
type: concept
domains: [generative-models, applied-ml]
aliases: [VAE]
level: intermediate
relations:
  prerequisites: [probabilistic-objectives]
  enables: [diffusion-model, vae-lof-anomaly-detection]
  contrasts_with: [generative-adversarial-network]
sources: [yuque:145950470, yuque:145103757]
---

# Variational Autoencoder

A VAE learns a probabilistic latent space by encoding an input into a distribution,
sampling a latent with the reparameterization trick, and decoding it back to data.

Its evidence lower bound combines reconstruction quality with a KL penalty that
keeps the approximate posterior near a prior. This produces a smooth sampleable
latent space but can blur outputs or suffer posterior collapse when the decoder
ignores the latent. VAE encoders also support anomaly scoring when unusual samples
reconstruct poorly or have low latent likelihood.

## Sources

- [Diffusion Model](https://www.yuque.com/shakewin/woezs0/ppbpaxtvhppyvtse)
- [VAE + LOF Anomaly Detection](https://www.yuque.com/shakewin/woezs0/oucahnztr1pbh5qn)

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[probabilistic-objectives|Probabilistic Objectives]]
- Enables: [[diffusion-model|Diffusion Models]], [[vae-lof-anomaly-detection|VAE–LOF Anomaly Detection]]
- Contrasts with: [[generative-adversarial-network|Generative Adversarial Networks]]

<!-- END GENERATED OBSIDIAN LINKS -->
