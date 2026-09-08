---
id: temporal-difference-learning
title: Temporal-Difference Learning
type: concept
domains: [foundations, reinforcement-learning]
aliases: [TD learning, Q-learning, SARSA]
level: intermediate
relations:
  prerequisites: [reinforcement-learning]
  enables: [generalized-advantage-estimation]
sources: [yuque:222857934, yuque:168068842]
---

# Temporal-Difference Learning

TD learning updates a value estimate from a bootstrapped target such as
$r+\gamma V(s')$ before an episode finishes. It sits between one-step prediction
and full Monte Carlo return estimation.

Q-learning is off-policy: its target uses the best next action regardless of the
behavior policy. SARSA is on-policy: its target uses the next action actually chosen.
Bootstrapping lowers variance and enables online updates but introduces bias and can
be unstable with function approximation, off-policy data, and aggressive updates.

## Interview answer

“TD methods learn from reward plus an estimated future value. Q-learning targets a
greedy policy; SARSA evaluates the behavior policy actually being followed.”

## Sources

- [CS7641 ML](https://www.yuque.com/shakewin/fidaqi/evbvouf8opoc9aix)
- [RLHF](https://www.yuque.com/shakewin/woezs0/ldm61haxvifpi7bb)

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[reinforcement-learning|Reinforcement Learning]]
- Enables: [[generalized-advantage-estimation|Generalized Advantage Estimation]]

<!-- END GENERATED OBSIDIAN LINKS -->
