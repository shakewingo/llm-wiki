---
id: mixture-of-experts
title: Mixture of Experts
type: concept
domains: [model-architecture, training, inference]
aliases: [MoE, sparse MoE]
level: advanced
relations:
  prerequisites: [transformer-architecture]
  optimized_by: [expert-parallelism]
  contrasts_with: [engram-conditional-memory]
sources: [yuque:241299652, yuque:283802487]
legacy_notion_id: 3e3cad4f-b605-8293-9ae2-815dca1c81cc
---

# Mixture of Experts

Sparse MoE replaces a dense FFN with many expert FFNs while routing each token to
only a small subset, increasing total parameters without proportional active compute.

Routing creates systems costs: tokens must be exchanged to expert-owning devices,
capacity can become imbalanced, and communication may dominate on weak interconnects.
Training must prevent expert collapse or chronic overload. “Tokens per active
parameter” and end-to-end throughput are more useful than total parameter count
alone when comparing deployments.

## Interview answer

“Sparse MoE scales parameter capacity by activating top-k experts per token. The
compute can stay bounded, but routing balance and all-to-all communication become
first-class bottlenecks.”

## Sources

- [DeepSeek Paper Reading](https://www.yuque.com/shakewin/woezs0/agn9y7w2skcvzzrk)
- [Distributed Framework](https://www.yuque.com/shakewin/sysgq3/mhw00hcggbv1scr8)

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[transformer-architecture|Transformer Architecture]]
- Contrasts with: [[engram-conditional-memory|Engram Conditional Memory]]
- Optimized by: [[expert-parallelism|Expert Parallelism]]

<!-- END GENERATED OBSIDIAN LINKS -->
