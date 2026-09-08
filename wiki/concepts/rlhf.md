---
id: rlhf
title: Reinforcement Learning from Human Feedback
type: concept
domains: [post-training, alignment]
aliases: [RLHF]
level: intermediate
relations:
  prerequisites: [supervised-fine-tuning, reward-modeling, proximal-policy-optimization]
  contrasts_with: [direct-preference-optimization, group-relative-policy-optimization]
sources: [yuque:168068842, yuque:241299652]
---

# Reinforcement Learning from Human Feedback

RLHF aligns a language model by collecting preference judgments, fitting a reward
model, and optimizing an SFT policy against that reward while constraining drift from
a reference model.

It can optimize nuanced sequence-level behavior beyond token imitation, but it is
expensive and vulnerable to reward hacking, annotator disagreement, distribution
shift, and unstable policy updates. Good systems preserve raw preference provenance,
measure disagreement, test adversarial prompts, and monitor KL and reward trends
alongside human quality.

## Sources

- [RLHF](https://www.yuque.com/shakewin/woezs0/ldm61haxvifpi7bb)
- [DeepSeek Paper Reading](https://www.yuque.com/shakewin/woezs0/agn9y7w2skcvzzrk)

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[supervised-fine-tuning|Supervised Fine-Tuning]], [[reward-modeling|Reward Modeling]], [[proximal-policy-optimization|Proximal Policy Optimization]]
- Contrasts with: [[direct-preference-optimization|Direct Preference Optimization]], [[group-relative-policy-optimization|Group Relative Policy Optimization]]

<!-- END GENERATED OBSIDIAN LINKS -->
