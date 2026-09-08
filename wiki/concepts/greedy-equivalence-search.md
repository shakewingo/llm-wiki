---
id: greedy-equivalence-search
title: Greedy Equivalence Search
type: concept
domains: [causal-ml]
aliases: [GES]
level: advanced
relations:
  prerequisites: [causal-structure-learning, probabilistic-objectives]
  contrasts_with: [pc-algorithm]
sources: [yuque:179434725]
---

# Greedy Equivalence Search

GES is a score-based causal structure learner that greedily adds edges while a
decomposable score improves, then greedily removes edges for further improvement.

It searches equivalence classes rather than treating every DAG independently. BIC
balances log-likelihood fit with a penalty for parameter count, discouraging dense
overfit graphs. Greedy search is scalable but can stop at a local optimum; the score's
assumptions and hidden confounding still limit causal interpretation.

## Source

- [Causal Structure Learning](https://www.yuque.com/shakewin/woezs0/zbne4d5yhpdwnasv)

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[causal-structure-learning|Causal Structure Learning]], [[probabilistic-objectives|Probabilistic Objectives]]
- Contrasts with: [[pc-algorithm|PC Algorithm]]

<!-- END GENERATED OBSIDIAN LINKS -->
