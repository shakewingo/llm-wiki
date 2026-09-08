---
id: engram-conditional-memory
title: Engram Conditional Memory
type: concept
domains: [model-architecture, memory]
aliases: [Engram]
level: advanced
relations:
  prerequisites: [sparse-representations, transformer-architecture]
  contrasts_with: [mixture-of-experts]
sources: [yuque:260446359]
---

# Engram Conditional Memory

Engram adds deterministic hashed n-gram lookup to a Transformer as a complementary
sparsity axis to MoE's conditional computation.

Tokenizer compression reduces redundant forms, multi-head hashing mitigates
collisions, and context-aware gating suppresses noisy retrieved embeddings. Because
indices depend on input tokens rather than hidden-state routing, large tables can be
sharded during training or offloaded to host memory during inference. The benefit is
cheap factual-pattern lookup; risks include collisions, stale memorization, and
system bottlenecks when table access is not hidden behind computation.

## Source

- [Engram](https://www.yuque.com/shakewin/woezs0/ef3x6lg83t6od3gi)

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[sparse-representations|Sparse Representations]], [[transformer-architecture|Transformer Architecture]]
- Contrasts with: [[mixture-of-experts|Mixture of Experts]]

<!-- END GENERATED OBSIDIAN LINKS -->
