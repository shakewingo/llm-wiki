---
id: generalized-advantage-estimation
title: Generalized Advantage Estimation
type: concept
domains: [reinforcement-learning, post-training]
aliases: [GAE]
level: advanced
relations:
  prerequisites: [policy-gradient, temporal-difference-learning]
  used_by: [proximal-policy-optimization]
sources: [yuque:245719568, yuque:168068842]
---

# Generalized Advantage Estimation

GAE combines multi-step temporal-difference residuals to estimate how much better an
action was than the value baseline predicted.

The parameter $\lambda$ interpolates between low-variance, biased one-step TD and
high-variance, lower-bias Monte Carlo returns. Discount $\gamma$ controls planning
horizon. GAE improves policy-gradient stability, but it inherits value-model error
and requires correct episode boundaries and masking; a bootstrapped terminal state
can systematically corrupt training.

## Sources

- [Knowledge Puzzle](https://www.yuque.com/shakewin/woezs0/fvhczuilmmhpf6t4)
- [RLHF](https://www.yuque.com/shakewin/woezs0/ldm61haxvifpi7bb)

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[policy-gradient|Policy Gradient]], [[temporal-difference-learning|Temporal-Difference Learning]]
- Used by: [[proximal-policy-optimization|Proximal Policy Optimization]]

<!-- END GENERATED OBSIDIAN LINKS -->
