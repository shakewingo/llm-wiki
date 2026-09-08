---
id: probabilistic-objectives
title: Probabilistic Objectives
type: concept
domains: [foundations, training]
aliases: [maximum likelihood estimation, MLE, KL divergence]
level: foundational
relations:
  enables: [variational-autoencoder, reward-modeling]
sources: [yuque:245719568, yuque:222857934, notion:388cad4f-b605-8074-8c53-ff558a15beb0]
---

# Probabilistic Objectives

Maximum likelihood chooses parameters that make observed data probable. Taking logs
turns products over conditionally independent examples into sums, and minimizing
negative log-likelihood yields familiar losses such as cross-entropy.

KL divergence $D_{KL}(P\|Q)=\mathbb{E}_P[\log P-\log Q]$ measures the extra coding
cost of representing samples from $P$ with $Q$. It is directional, not a metric.
KL appears in variational inference, distillation, and policy regularization.

Both tools inherit assumptions: a misspecified likelihood gives confident but wrong
parameters, and the direction of KL determines whether optimization tends to cover
multiple modes or concentrate on one.

## Sources

- [Knowledge Puzzle](https://www.yuque.com/shakewin/woezs0/fvhczuilmmhpf6t4)
- [CS7641 ML](https://www.yuque.com/shakewin/fidaqi/evbvouf8opoc9aix)
- [Alisa’s book of LLMs](https://app.notion.com/p/388cad4fb60580748c53ff558a15beb0)

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Enables: [[variational-autoencoder|Variational Autoencoder]], [[reward-modeling|Reward Modeling]]

<!-- END GENERATED OBSIDIAN LINKS -->
