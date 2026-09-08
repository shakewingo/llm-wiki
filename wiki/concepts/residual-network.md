---
id: residual-network
title: Residual Networks
type: concept
domains: [model-architecture, training]
aliases: [ResNet, residual connection]
level: foundational
relations:
  part_of: [transformer-architecture]
  enables: [manifold-constrained-hyper-connections]
sources: [yuque:222458626, yuque:204005901, yuque:260283661]
---

# Residual Networks

A residual connection writes a block as $x_{l+1}=x_l+F(x_l)$, giving information
and gradients a direct path through depth.

The identity path makes it easier for a layer to learn a small refinement instead
of reconstructing the full representation. Residuals underpin deep CNNs and
Transformers, usually together with normalization. Shape mismatches require a
projection, and poorly scaled residual branches can still destabilize very deep
models. Hyper-connections generalize the single stream into several interacting
residual streams.

## Sources

- [Deep Learning PyTorch](https://www.yuque.com/shakewin/fidaqi/rwg53sz1y5tcidkw)
- [MLi Paper Reading](https://www.yuque.com/shakewin/woezs0/hhoofowylkt3t2id)
- [mHC](https://www.yuque.com/shakewin/woezs0/qcd8g69ec9wrft2a)

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Part of: [[transformer-architecture|Transformer Architecture]]
- Enables: [[manifold-constrained-hyper-connections|Manifold-Constrained Hyper-Connections]]

<!-- END GENERATED OBSIDIAN LINKS -->
