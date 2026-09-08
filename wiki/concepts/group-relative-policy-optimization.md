---
id: group-relative-policy-optimization
title: Group Relative Policy Optimization
type: concept
domains: [post-training, reinforcement-learning]
aliases: [GRPO]
level: advanced
relations:
  prerequisites: [policy-gradient, reward-modeling]
  contrasts_with: [proximal-policy-optimization, rlhf, direct-preference-optimization]
sources: [yuque:241299652, yuque:245719568, notion:388cad4f-b605-8074-8c53-ff558a15beb0]
legacy_notion_id: 965cad4f-b605-8220-bb2e-81cb441e982f
---

# Group Relative Policy Optimization

GRPO estimates advantage by comparing rewards among several responses sampled for
the same prompt, removing PPO's separately trained value model.

Group normalization supplies a relative baseline; a clipped policy objective and KL
control limit drift. Verifiable rule-based rewards work particularly well for math
or code, but group quality depends on sample diversity and reward resolution. Nearly
identical rewards give a weak signal, while noisy rewards can rank the group
incorrectly. GRPO reduces model count, not the cost of generating multiple rollouts.

## Sources

- [DeepSeek Paper Reading](https://www.yuque.com/shakewin/woezs0/agn9y7w2skcvzzrk)
- [Knowledge Puzzle](https://www.yuque.com/shakewin/woezs0/fvhczuilmmhpf6t4)
- [Alisa’s book of LLMs](https://app.notion.com/p/388cad4fb60580748c53ff558a15beb0)

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[policy-gradient|Policy Gradient]], [[reward-modeling|Reward Modeling]]
- Contrasts with: [[proximal-policy-optimization|Proximal Policy Optimization]], [[rlhf|Reinforcement Learning from Human Feedback]], [[direct-preference-optimization|Direct Preference Optimization]]

<!-- END GENERATED OBSIDIAN LINKS -->
