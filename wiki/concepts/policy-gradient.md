---
id: policy-gradient
title: Policy Gradient
type: concept
domains: [reinforcement-learning, post-training]
aliases: [REINFORCE]
level: intermediate
relations:
  prerequisites: [reinforcement-learning]
  enables: [proximal-policy-optimization, rlhf]
sources: [yuque:168068842, yuque:222857934]
---

# Policy Gradient

Policy-gradient methods optimize expected return directly by increasing the log
probability of sampled actions in proportion to their estimated advantage.

The score-function estimator is unbiased but high variance. Reward-to-go removes
irrelevant past rewards; a value baseline reduces variance without changing the
expectation; entropy bonuses preserve exploration. In language models, actions are
tokens and a trajectory is a completion. Long sequences, expensive sampling, and
sparse sequence-level rewards make credit assignment difficult.

## Sources

- [RLHF](https://www.yuque.com/shakewin/woezs0/ldm61haxvifpi7bb)
- [CS7641 ML](https://www.yuque.com/shakewin/fidaqi/evbvouf8opoc9aix)

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[reinforcement-learning|Reinforcement Learning]]
- Enables: [[proximal-policy-optimization|Proximal Policy Optimization]], [[rlhf|Reinforcement Learning from Human Feedback]]

<!-- END GENERATED OBSIDIAN LINKS -->
