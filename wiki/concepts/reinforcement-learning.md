---
id: reinforcement-learning
title: Reinforcement Learning
type: concept
domains: [foundations, post-training]
aliases: [RL]
level: foundational
relations:
  prerequisites: [probabilistic-objectives]
  enables: [policy-gradient, temporal-difference-learning, rlhf]
sources: [yuque:222857934, yuque:168068842, yuque:241299652]
---

# Reinforcement Learning

Reinforcement learning optimizes a policy through interaction: an agent observes a
state, takes an action, receives reward, and seeks high discounted return.

Model-based methods use transition and reward dynamics for planning; model-free
methods estimate values or policies directly. Exploration gathers information but
can reduce immediate reward. Delayed credit, high-variance returns, distribution
shift, and reward misspecification make RL harder than supervised prediction.

LLM post-training casts token generation as a policy, but its environment is unusual:
trajectories are expensive, rewards may be learned or rule-based, and a reference
policy is often used to limit destructive drift.

## Sources

- [CS7641 ML](https://www.yuque.com/shakewin/fidaqi/evbvouf8opoc9aix)
- [RLHF](https://www.yuque.com/shakewin/woezs0/ldm61haxvifpi7bb)
- [DeepSeek Paper Reading](https://www.yuque.com/shakewin/woezs0/agn9y7w2skcvzzrk)

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[probabilistic-objectives|Probabilistic Objectives]]
- Enables: [[policy-gradient|Policy Gradient]], [[temporal-difference-learning|Temporal-Difference Learning]], [[rlhf|Reinforcement Learning from Human Feedback]]

<!-- END GENERATED OBSIDIAN LINKS -->
