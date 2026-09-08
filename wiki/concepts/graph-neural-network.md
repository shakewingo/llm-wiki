---
id: graph-neural-network
title: Graph Neural Networks
type: concept
domains: [model-architecture, graph-ml]
aliases: [GNN, GCN]
level: intermediate
relations:
  prerequisites: [ml-generalization-and-regularization]
  contrasts_with: [transformer-architecture]
sources: [yuque:204005901]
---

# Graph Neural Networks

A GNN updates each node by aggregating messages from its neighbors, allowing learned
representations to reflect graph structure and node or edge features.

Message passing is permutation-invariant over neighbors and can support node,
edge, or graph prediction. More layers expand the receptive field but can cause
over-smoothing, over-squashing, and expensive neighborhood expansion. Unlike a
Transformer's dense content-based connectivity, a basic GNN begins from an explicit
graph; hybrid graph Transformers can learn additional long-range interactions.

## Source

- [MLi Paper Reading](https://www.yuque.com/shakewin/woezs0/hhoofowylkt3t2id)

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[ml-generalization-and-regularization|ML Generalization and Regularization]]
- Contrasts with: [[transformer-architecture|Transformer Architecture]]

<!-- END GENERATED OBSIDIAN LINKS -->
