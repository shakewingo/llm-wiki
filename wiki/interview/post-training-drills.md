---
id: post-training-drills
title: Post-Training and Alignment Drills
type: interview
domains: [post-training, alignment]
aliases: []
level: mixed
relations:
  prerequisites: [post-training-and-alignment]
sources: [yuque:168068842, yuque:249024774, yuque:241299652, yuque:245719568]
---

# Post-Training and Alignment Drills

## Why start with SFT before preference optimization?

SFT establishes instruction-following behavior and a reasonable rollout distribution;
preference methods then refine relative quality instead of discovering the interface
from sparse rewards.

## How does DPO remove the reward model?

Substituting the KL-regularized optimal policy into the pairwise preference model
cancels the unknown normalization term and yields a chosen/rejected log-ratio loss.

## What does GRPO remove relative to PPO?

It replaces the learned value baseline with reward normalization across a group of
responses to the same prompt. It still needs rollout generation and reward signals.

## What is reward hacking?

The policy exploits flaws in the reward proxy rather than satisfying the intended
behavior. Independent human evaluation and adversarial tests are required.

## Can visible chain-of-thought be trusted as an explanation?

No. It can improve task solving but may rationalize rather than faithfully describe
internal computation; verify critical steps and the answer.

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[post-training-and-alignment|Post-Training and Alignment Map]]

<!-- END GENERATED OBSIDIAN LINKS -->
