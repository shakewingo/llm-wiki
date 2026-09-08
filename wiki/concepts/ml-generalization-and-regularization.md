---
id: ml-generalization-and-regularization
title: ML Generalization and Regularization
type: concept
domains: [foundations, training]
aliases: [bias-variance tradeoff, weight decay]
level: foundational
relations:
  affects: [pretraining, supervised-fine-tuning]
sources: [yuque:222857934, yuque:222458626, yuque:245719568]
---

# ML Generalization and Regularization

Generalization is performance on unseen data rather than optimization of the
training set. Underfitting reflects excessive bias; overfitting reflects excessive
variance or memorization of noise.

Controls include representative validation splits, early stopping, data augmentation,
capacity limits, dropout, and penalties on weights. L2 regularization adds
$\lambda\lVert w\rVert_2^2$ to the objective; in simple SGD this resembles multiplying
weights by a decay factor before the gradient step. With adaptive optimizers,
decoupled weight decay is not identical to adding an L2 gradient term.

The main failure mode is tuning repeatedly against the test set, which turns it
into another training signal and makes the final estimate optimistic.

## Sources

- [CS7641 ML](https://www.yuque.com/shakewin/fidaqi/evbvouf8opoc9aix)
- [Deep Learning PyTorch](https://www.yuque.com/shakewin/fidaqi/rwg53sz1y5tcidkw)
- [Knowledge Puzzle](https://www.yuque.com/shakewin/woezs0/fvhczuilmmhpf6t4)

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Affects: [[pretraining|Language-Model Pretraining]], [[supervised-fine-tuning|Supervised Fine-Tuning]]

<!-- END GENERATED OBSIDIAN LINKS -->
