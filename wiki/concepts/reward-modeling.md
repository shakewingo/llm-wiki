---
id: reward-modeling
title: Reward Modeling
type: concept
domains: [post-training, evaluation]
aliases: [preference model, reward model]
level: intermediate
relations:
  prerequisites: [supervised-fine-tuning, probabilistic-objectives]
  enables: [rlhf, proximal-policy-optimization]
  contrasts_with: [direct-preference-optimization]
sources: [yuque:168068842, yuque:249024774, yuque:241299652]
---

# Reward Modeling

A reward model converts human preferences or verifiable rules into a scalar signal
for candidate responses.

For pairwise preferences, a Bradley–Terry objective raises the score of a chosen
response relative to a rejected one. Learned rewards generalize beyond labeled
pairs but can be exploited: the policy may discover high-scoring behavior that
violates the evaluator's intent. Rule-based rewards avoid a learned predictor for
verifiable tasks but cover fewer behaviors. Reward evaluation therefore needs held-out
human checks, adversarial testing, and monitoring for length or style shortcuts.

## Sources

- [RLHF](https://www.yuque.com/shakewin/woezs0/ldm61haxvifpi7bb)
- [DPO](https://www.yuque.com/shakewin/woezs0/gway2i9nrspb9o7k)
- [DeepSeek Paper Reading](https://www.yuque.com/shakewin/woezs0/agn9y7w2skcvzzrk)

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[supervised-fine-tuning|Supervised Fine-Tuning]], [[probabilistic-objectives|Probabilistic Objectives]]
- Enables: [[rlhf|Reinforcement Learning from Human Feedback]], [[proximal-policy-optimization|Proximal Policy Optimization]]
- Contrasts with: [[direct-preference-optimization|Direct Preference Optimization]]

<!-- END GENERATED OBSIDIAN LINKS -->
