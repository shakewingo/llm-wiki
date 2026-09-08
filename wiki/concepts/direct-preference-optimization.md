---
id: direct-preference-optimization
title: Direct Preference Optimization
type: concept
domains: [post-training, alignment]
aliases: [DPO]
level: intermediate
relations:
  prerequisites: [supervised-fine-tuning, probabilistic-objectives]
  contrasts_with: [reward-modeling, proximal-policy-optimization, rlhf, group-relative-policy-optimization]
sources: [yuque:249024774, yuque:168068842, notion:388cad4f-b605-8074-8c53-ff558a15beb0]
---

# Direct Preference Optimization

DPO trains directly on chosen/rejected response pairs, increasing their relative
log-probability margin while regularizing against a reference policy.

Its derivation substitutes the KL-regularized optimal policy into a pairwise
Bradley–Terry preference model, causing the unknown reward normalizer to cancel. The
result needs neither online rollouts nor an explicit reward and value model. DPO is
simpler and stable, but remains limited by static preference coverage, label quality,
reference choice, and sensitivity to the temperature-like $\beta$ parameter.

## Sources

- [DPO](https://www.yuque.com/shakewin/woezs0/gway2i9nrspb9o7k)
- [RLHF](https://www.yuque.com/shakewin/woezs0/ldm61haxvifpi7bb)
- [Alisa’s book of LLMs](https://app.notion.com/p/388cad4fb60580748c53ff558a15beb0)

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[supervised-fine-tuning|Supervised Fine-Tuning]], [[probabilistic-objectives|Probabilistic Objectives]]
- Contrasts with: [[reward-modeling|Reward Modeling]], [[proximal-policy-optimization|Proximal Policy Optimization]], [[rlhf|Reinforcement Learning from Human Feedback]], [[group-relative-policy-optimization|Group Relative Policy Optimization]]

<!-- END GENERATED OBSIDIAN LINKS -->
