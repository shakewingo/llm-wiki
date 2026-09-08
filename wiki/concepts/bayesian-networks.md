---
id: bayesian-networks
title: Bayesian Networks
type: concept
domains: [foundations, causal-ml]
aliases: [Bayes net, belief network]
level: intermediate
relations:
  prerequisites: [probabilistic-objectives]
  enables: [causal-structure-learning]
sources: [yuque:203899196, yuque:179434725]
---

# Bayesian Networks

A Bayesian network represents a joint distribution with a directed acyclic graph:
each node is conditionally distributed given its parents, and the joint probability
factorizes into those local conditional distributions.

The graph encodes conditional independencies, which makes inference and learning
more tractable than an unconstrained joint table. Variable elimination answers
queries by summing out irrelevant variables. A graph learned from observational
data is not automatically causal: equivalence classes, hidden confounders, data
scarcity, and incorrect independence tests can leave directions unidentified.
Expert constraints or interventions provide stronger evidence.

## Interview answer

“A Bayes net factorizes a joint distribution according to a DAG. It supports compact
probabilistic inference, while causal interpretation requires additional assumptions
or interventions.”

## Sources

- [Gatech CS6601 - AI](https://www.yuque.com/shakewin/fidaqi/dlm2n18clgtdxppy)
- [Causal Structure Learning](https://www.yuque.com/shakewin/woezs0/zbne4d5yhpdwnasv)

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[probabilistic-objectives|Probabilistic Objectives]]
- Enables: [[causal-structure-learning|Causal Structure Learning]]

<!-- END GENERATED OBSIDIAN LINKS -->
