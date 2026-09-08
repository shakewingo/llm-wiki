---
id: multi-token-prediction
title: Multi-Token Prediction
type: concept
domains: [training, inference]
aliases: [MTP]
level: advanced
relations:
  prerequisites: [transformer-architecture]
  enables: [speculative-decoding]
sources: [yuque:267998979, yuque:241299652]
---

# Multi-Token Prediction

MTP adds auxiliary prediction modules so training supervises multiple future-token
offsets rather than only the immediate next token.

The extra heads supply denser training signal and encourage representations useful
beyond one-step prediction. A serving design may discard auxiliary heads and keep
only the improved main model, or reuse suitable heads as a draft mechanism for
speculative decoding. These are distinct benefits: multi-token training does not by
itself make base autoregressive decode emit several committed tokens at once.

Shared embeddings and hidden features, loss weighting, and inference integration
determine whether the additional training cost produces real quality or latency
benefit.

## Interview answer

“MTP supervises several future offsets during training. It densifies the learning
signal and can supply speculative drafts, but accepted generation still needs a
correct verification path.”

## Sources

- [MTP](https://www.yuque.com/shakewin/woezs0/xsgrva9gef5pwz5n)
- [DeepSeek Paper Reading](https://www.yuque.com/shakewin/woezs0/agn9y7w2skcvzzrk)

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[transformer-architecture|Transformer Architecture]]
- Enables: [[speculative-decoding|Speculative Decoding]]

<!-- END GENERATED OBSIDIAN LINKS -->
