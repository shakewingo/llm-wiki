---
id: post-training-and-alignment
title: Post-Training and Alignment Map
type: map
domains: [post-training, alignment, reasoning]
aliases: []
level: mixed
entry_points:
  - pretraining
  - supervised-fine-tuning
  - reward-modeling
  - policy-gradient
  - generalized-advantage-estimation
  - proximal-policy-optimization
  - rlhf
  - direct-preference-optimization
  - group-relative-policy-optimization
  - chain-of-thought-reasoning
  - knowledge-distillation
  - model-quantization
relations:
  prerequisites: [foundations, transformer-architecture]
sources: [yuque:168068842, yuque:249024774, yuque:241299652, yuque:245719568, yuque:253935769, yuque:247276544, notion:388cad4f-b605-8074-8c53-ff558a15beb0]
---

# Post-Training and Alignment Map

Post-training transforms a broad next-token model into a useful policy.

The typical path is [pretraining](../concepts/pretraining.md) →
[SFT](../concepts/supervised-fine-tuning.md) → preference or reinforcement learning.
[Reward modeling](../concepts/reward-modeling.md), [policy gradients](../concepts/policy-gradient.md),
[GAE](../concepts/generalized-advantage-estimation.md), and
[PPO](../concepts/proximal-policy-optimization.md) explain classic
[RLHF](../concepts/rlhf.md). [DPO](../concepts/direct-preference-optimization.md)
removes the explicit reward/rollout loop, while
[GRPO](../concepts/group-relative-policy-optimization.md) removes PPO's value model
and compares samples within a prompt group.

[Chain-of-thought](../concepts/chain-of-thought-reasoning.md) can be trained or rewarded;
[distillation](../concepts/knowledge-distillation.md) and
[quantization](../concepts/model-quantization.md) transfer or compress the result.

Use [the alignment comparison](../comparisons/alignment-methods.md) and
[post-training drills](../interview/post-training-drills.md).

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[foundations|AI and ML Foundations Map]], [[transformer-architecture|Transformer Architecture]]

<!-- END GENERATED OBSIDIAN LINKS -->
