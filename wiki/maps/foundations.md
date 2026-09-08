---
id: foundations
title: AI and ML Foundations Map
type: map
domains: [foundations]
aliases: []
level: mixed
entry_points:
  - neural-network-computation
  - backpropagation-and-autodiff
  - deep-learning-optimization
  - numerical-stability
  - probabilistic-objectives
  - ml-generalization-and-regularization
  - classical-ml-methods
  - sparse-representations
  - search-and-a-star
  - bayesian-networks
  - reinforcement-learning
  - temporal-difference-learning
relations:
  enables: [pretraining, causal-structure-learning]
sources: [yuque:203899196, yuque:222857934, yuque:222458626, yuque:127456364, yuque:245719568, notion:388cad4f-b605-8074-8c53-ff558a15beb0]
---

# AI and ML Foundations Map

This slice connects the assumptions beneath modern AI systems.

## Learning path

1. Ground the computation in [neural-network layers](../concepts/neural-network-computation.md),
   [backpropagation](../concepts/backpropagation-and-autodiff.md), and
   [deep-learning optimization](../concepts/deep-learning-optimization.md).
2. Learn objectives with [probabilistic objectives](../concepts/probabilistic-objectives.md),
   then connect the math to [numerical stability](../concepts/numerical-stability.md)
   and why validation needs [generalization and regularization](../concepts/ml-generalization-and-regularization.md).
3. Review [classical ML](../concepts/classical-ml-methods.md) and
   [sparse representations](../concepts/sparse-representations.md) as practical baselines.
4. Understand symbolic planning through [search and A*](../concepts/search-and-a-star.md)
   and uncertainty through [Bayesian networks](../concepts/bayesian-networks.md).
5. Move to sequential decisions with [reinforcement learning](../concepts/reinforcement-learning.md)
   and [temporal-difference learning](../concepts/temporal-difference-learning.md).

The recurring question is: what assumptions make a method work? Independence,
stationarity, representativeness, graph structure, reward quality, and evaluation
protocol are often more important than the model name.

Practice with [foundations drills](../interview/foundations-drills.md).

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Enables: [[pretraining|Language-Model Pretraining]], [[causal-structure-learning|Causal Structure Learning]]

<!-- END GENERATED OBSIDIAN LINKS -->
