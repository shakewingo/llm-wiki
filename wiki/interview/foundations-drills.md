---
id: foundations-drills
title: AI Foundations Drills
type: interview
domains: [foundations]
aliases: []
level: mixed
relations:
  prerequisites: [foundations]
sources: [yuque:203899196, yuque:222857934, yuque:127456364, yuque:245719568]
---

# AI Foundations Drills

## Why is KL divergence not a distance metric?

It is directional and generally $D_{KL}(P\|Q)\ne D_{KL}(Q\|P)$; it also does not
satisfy the triangle inequality. Explain its expected extra coding-cost intuition.

## When is A* optimal?

With nonnegative path costs and an admissible heuristic; consistency avoids reopening
states in common graph-search implementations.

## Q-learning versus SARSA?

Q-learning uses a greedy next-action target and is off-policy. SARSA uses the action
actually selected and is on-policy.

## Why can a validation score mislead?

Repeated tuning leaks validation information; distribution shift, label leakage, and
an unrepresentative split can also make the score fail to estimate deployment.

## Why is a learned Bayesian graph not automatically causal?

Observational independencies may identify only an equivalence class, and hidden
confounding or incorrect assumptions can produce the same distribution.

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[foundations|AI and ML Foundations Map]]

<!-- END GENERATED OBSIDIAN LINKS -->
