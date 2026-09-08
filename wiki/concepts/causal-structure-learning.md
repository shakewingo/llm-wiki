---
id: causal-structure-learning
title: Causal Structure Learning
type: concept
domains: [causal-ml, applied-ml]
aliases: [causal discovery]
level: advanced
relations:
  prerequisites: [bayesian-networks]
  implemented_in: [pc-algorithm, greedy-equivalence-search]
  used_by: [root-cause-analysis]
sources: [yuque:179434725]
---

# Causal Structure Learning

Causal structure learning infers graph structure from statistical dependencies,
independencies, scores, interventions, and domain constraints.

Constraint-based algorithms remove edges using conditional-independence tests and
orient identifiable colliders. Score-based algorithms search graph equivalence
classes for a fit-complexity objective such as BIC. Observational data often identifies
only a Markov-equivalence class, not one causal DAG. Hidden confounders, selection
bias, nonstationarity, and weak tests make confident arrows dangerous; expert knowledge
and interventions should be recorded as separate evidence.

## Source

- [Causal Structure Learning](https://www.yuque.com/shakewin/woezs0/zbne4d5yhpdwnasv)

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[bayesian-networks|Bayesian Networks]]
- Used by: [[root-cause-analysis|AI-Assisted Root Cause Analysis]]
- Implemented in: [[pc-algorithm|PC Algorithm]], [[greedy-equivalence-search|Greedy Equivalence Search]]

<!-- END GENERATED OBSIDIAN LINKS -->
