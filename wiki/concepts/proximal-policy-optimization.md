---
id: proximal-policy-optimization
title: Proximal Policy Optimization
type: concept
domains: [reinforcement-learning, post-training]
aliases: [PPO]
level: advanced
relations:
  prerequisites: [policy-gradient, generalized-advantage-estimation, reward-modeling]
  used_by: [rlhf]
  contrasts_with: [direct-preference-optimization, group-relative-policy-optimization]
sources: [yuque:168068842, yuque:241299652]
---

# Proximal Policy Optimization

PPO reuses on-policy samples for several gradient steps while clipping the policy
probability ratio so updates do not move too far at once.

An actor generates responses, a reward signal scores them, a critic estimates value,
and a frozen reference policy supplies a KL penalty. This flexibility supports
arbitrary rewards, but the multi-model pipeline is expensive and sensitive to reward
scale, advantage estimation, clipping, KL control, and stale trajectories.

## Interview answer

“PPO is a clipped policy-gradient method. In RLHF it is flexible but operationally
heavy because rollout, reward, value, and reference models must remain coordinated.”

## Sources

- [RLHF](https://www.yuque.com/shakewin/woezs0/ldm61haxvifpi7bb)
- [DeepSeek Paper Reading](https://www.yuque.com/shakewin/woezs0/agn9y7w2skcvzzrk)

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[policy-gradient|Policy Gradient]], [[generalized-advantage-estimation|Generalized Advantage Estimation]], [[reward-modeling|Reward Modeling]]
- Used by: [[rlhf|Reinforcement Learning from Human Feedback]]
- Contrasts with: [[direct-preference-optimization|Direct Preference Optimization]], [[group-relative-policy-optimization|Group Relative Policy Optimization]]

<!-- END GENERATED OBSIDIAN LINKS -->
