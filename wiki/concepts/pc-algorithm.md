---
id: pc-algorithm
title: PC Algorithm
type: concept
domains: [causal-ml]
aliases: [Peter-Clark algorithm]
level: advanced
relations:
  prerequisites: [causal-structure-learning]
  contrasts_with: [greedy-equivalence-search]
sources: [yuque:179434725]
---

# PC Algorithm

PC is a constraint-based causal-discovery algorithm that starts from a dense
undirected graph, removes edges when conditional independence is found, identifies
unshielded colliders, and applies orientation rules without creating contradictions.

Its result is generally a partially directed equivalence class. Accuracy depends
strongly on sample size, significance thresholds, conditioning-set growth, and the
chosen test—Fisher Z for linear Gaussian relationships, chi-square or G-tests for
categorical variables, or kernel tests for nonlinear dependence. Errors early in
skeleton discovery propagate into edge orientations.

## Source

- [Causal Structure Learning](https://www.yuque.com/shakewin/woezs0/zbne4d5yhpdwnasv)

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[causal-structure-learning|Causal Structure Learning]]
- Contrasts with: [[greedy-equivalence-search|Greedy Equivalence Search]]

<!-- END GENERATED OBSIDIAN LINKS -->
