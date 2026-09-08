---
id: deep-learning-optimization
title: Deep Learning Optimization
type: concept
domains: [foundations, training]
aliases: [AdamW, gradient clipping, learning-rate schedule]
level: intermediate
relations:
  prerequisites: [backpropagation-and-autodiff, ml-generalization-and-regularization]
  used_by: [pretraining, supervised-fine-tuning, rlhf]
sources: [notion:388cad4f-b605-8074-8c53-ff558a15beb0, yuque:245719568, yuque:222458626]
---

# Deep Learning Optimization

An optimizer converts gradients into parameter updates. SGD follows the current
gradient; Adam tracks exponential moving averages of the gradient and its square,
then bias-corrects and normalizes the update. AdamW decouples weight decay from that
adaptive gradient step so regularization is not distorted by per-parameter scaling.

Learning-rate schedules control the global step size over time. Warmup avoids large,
poorly calibrated early updates; later decay supports convergence. Gradient clipping
rescales an excessive global gradient norm without changing its direction, limiting
catastrophic steps but not fixing persistently bad data or objectives.

Adam-family training carries material state: parameters, gradients, and two moment
buffers, often with higher-precision master weights. That cost is one reason optimizer
state sharding matters in large-model training.

## Interview answer

“Adam adapts updates with first and second gradient moments; AdamW applies decay
directly to parameters. Warmup and decay control the time-dependent step size, while
global-norm clipping is a guardrail against isolated explosive updates.”

## Sources

- [Alisa’s book of LLMs](https://app.notion.com/p/388cad4fb60580748c53ff558a15beb0)
- [Knowledge Puzzle](https://www.yuque.com/shakewin/woezs0/fvhczuilmmhpf6t4)
- [Deep Learning with PyTorch](https://www.yuque.com/shakewin/fidaqi/rwg53sz1y5tcidkw)

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[backpropagation-and-autodiff|Backpropagation and Automatic Differentiation]], [[ml-generalization-and-regularization|ML Generalization and Regularization]]
- Used by: [[pretraining|Language-Model Pretraining]], [[supervised-fine-tuning|Supervised Fine-Tuning]], [[rlhf|Reinforcement Learning from Human Feedback]]

<!-- END GENERATED OBSIDIAN LINKS -->
