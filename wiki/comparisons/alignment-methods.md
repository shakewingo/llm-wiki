---
id: alignment-methods
title: RLHF, DPO, and GRPO
type: comparison
domains: [post-training, alignment]
aliases: []
level: intermediate
relations:
  prerequisites: [supervised-fine-tuning, reward-modeling, policy-gradient]
sources: [yuque:168068842, yuque:249024774, yuque:241299652, yuque:245719568]
legacy_notion_id: 33dcad4f-b605-8310-9dc8-01108f3d93c7
---

# RLHF, DPO, and GRPO

| Method | Data during optimization | Extra models | Strength | Main risk |
|---|---|---|---|---|
| [PPO-RLHF](../concepts/rlhf.md) | Fresh policy rollouts | Reward, value, reference | Flexible arbitrary reward | Expensive and unstable |
| [DPO](../concepts/direct-preference-optimization.md) | Static chosen/rejected pairs | Reference | Simple offline objective | Limited to preference coverage |
| [GRPO](../concepts/group-relative-policy-optimization.md) | Groups of policy samples | Reward/reference; no value model | Relative online signal with fewer models | Rollout cost and group-sensitive signal |

The choice is not “old versus new.” Use PPO when online reward composition and
exploration justify complexity, DPO when a strong offline preference dataset exists,
and GRPO when multiple verifiable samples per prompt provide a useful relative
baseline. All three need drift control and independent evaluation.

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[supervised-fine-tuning|Supervised Fine-Tuning]], [[reward-modeling|Reward Modeling]], [[policy-gradient|Policy Gradient]]

<!-- END GENERATED OBSIDIAN LINKS -->
