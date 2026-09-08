---
id: rms-normalization
title: Root Mean Square Normalization
type: concept
domains: [model-architecture, training]
aliases: [RMSNorm]
level: intermediate
relations:
  part_of: [transformer-architecture]
  affects: [mixed-precision-training]
sources: [notion:388cad4f-b605-8074-8c53-ff558a15beb0, yuque:145901413]
---

# Root Mean Square Normalization

RMSNorm scales a hidden vector by its root mean square and then applies a learned
per-feature gain:

$$
\operatorname{RMSNorm}(x)=\gamma\odot
\frac{x}{\sqrt{\frac{1}{d}\sum_i x_i^2+\epsilon}}.
$$

Unlike LayerNorm, it does not subtract the feature mean. The normalization controls
the overall activation scale, while $\gamma$ restores the model's ability to amplify
or suppress individual dimensions. Pre-norm Transformer blocks place it before
attention and the feed-forward sublayer so the residual stream retains a stable
identity path.

Reductions and the choice of $\epsilon$ make implementation precision important.
Normalization can stabilize scale, but it does not by itself prevent every source
of exploding gradients or guarantee healthy optimization.

## Interview answer

“RMSNorm divides by root-mean-square magnitude and learns a per-dimension gain. It
omits LayerNorm's mean-centering, giving modern Transformers a simpler scale-control
mechanism, commonly in a pre-norm residual layout.”

## Sources

- [Alisa’s book of LLMs](https://app.notion.com/p/388cad4fb60580748c53ff558a15beb0)
- [LLaMA](https://www.yuque.com/shakewin/woezs0/avr5nrkaahavwdwv)

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Part of: [[transformer-architecture|Transformer Architecture]]
- Affects: [[mixed-precision-training|Mixed-Precision Training]]

<!-- END GENERATED OBSIDIAN LINKS -->
