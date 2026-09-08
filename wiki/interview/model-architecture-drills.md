---
id: model-architecture-drills
title: Model Architecture Drills
type: interview
domains: [model-architecture, generative-models]
aliases: []
level: mixed
relations:
  prerequisites: [model-architecture-and-generation]
sources: [yuque:145104004, yuque:145950470, yuque:181670371, yuque:260446359, yuque:260283661]
---

# Model Architecture Drills

## Why is BERT better suited to classification than free-form generation?

Its bidirectional encoder and masked objective build representations from both sides,
but do not define causal next-token generation.

## Compare VAE, GAN, and diffusion objectives.

VAE optimizes an approximate likelihood bound, GAN plays an adversarial game, and
diffusion learns iterative denoising. Discuss latent structure, stability, mode
coverage, sharpness, and sampling latency.

## What does CLIP learn?

Separate image and text encoders align paired examples in one vector space using a
bidirectional contrastive loss.

## Why are Engram and MoE complementary?

MoE routes hidden states to computation; Engram deterministically retrieves hashed
n-gram memory from tokens. They scale different resources.

## Why does mHC require systems co-design?

Multiple residual streams increase activation and pipeline communication, so fused
kernels and overlap-aware scheduling are part of the usable architecture.

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[model-architecture-and-generation|Model Architecture and Generation Map]]

<!-- END GENERATED OBSIDIAN LINKS -->
