---
id: supervised-fine-tuning
title: Supervised Fine-Tuning
type: concept
domains: [training, post-training]
aliases: [SFT, instruction tuning]
level: foundational
relations:
  prerequisites: [pretraining]
  enables: [rlhf, direct-preference-optimization]
sources: [yuque:253935769, yuque:168068842, yuque:241299652]
---

# Supervised Fine-Tuning

SFT trains a pretrained model on labeled input-output examples to teach instruction
following, task format, style, or domain behavior.

Cross-entropy is usually computed only on the desired response tokens. Dataset
quality, coverage, and consistency dominate: contradictory templates teach unstable
behavior, while narrow data may overwrite general capabilities. Parameter-efficient
methods such as LoRA lower training memory and storage but do not remove the need
for careful evaluation. SFT commonly creates the starting policy for preference
optimization.

## Sources

- [NVIDIA Agentic AI Training](https://www.yuque.com/shakewin/fidaqi/fgv15n9m42qh9m77)
- [RLHF](https://www.yuque.com/shakewin/woezs0/ldm61haxvifpi7bb)
- [DeepSeek Paper Reading](https://www.yuque.com/shakewin/woezs0/agn9y7w2skcvzzrk)

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[pretraining|Language-Model Pretraining]]
- Enables: [[rlhf|Reinforcement Learning from Human Feedback]], [[direct-preference-optimization|Direct Preference Optimization]]

<!-- END GENERATED OBSIDIAN LINKS -->
