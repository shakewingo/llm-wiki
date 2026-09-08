---
id: foundations-drills
title: AI Foundations Drills
type: interview
domains: [foundations]
aliases: []
level: mixed
relations:
  prerequisites: [foundations]
sources: [yuque:203899196, yuque:222857934, yuque:127456364, yuque:245719568, notion:388cad4f-b605-8074-8c53-ff558a15beb0]
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

## Why do gradients sum at a computation-graph branch?

The shared value influences the loss through every downstream path, so the
multivariable chain rule adds each path's contribution. This is also why gradients
from replicated distributed uses must reduce back to the owner.

## Adam versus AdamW?

Adam normalizes with running first and second moments. AdamW applies weight decay
directly to parameters instead of mixing an L2 term into the adaptive gradient.

## Why subtract the maximum before softmax?

Softmax is invariant to a common shift. Subtracting the largest logit makes every
exponent at most one, avoiding overflow without changing the distribution.

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[foundations|AI and ML Foundations Map]]

<!-- END GENERATED OBSIDIAN LINKS -->
