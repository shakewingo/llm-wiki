---
id: speculative-decoding
title: Speculative Decoding
type: concept
domains: [inference]
aliases: [speculative sampling]
level: intermediate
relations:
  prerequisites: [causal-attention]
  affects: [kv-cache]
sources: [yuque:267998979, yuque:241299652]
legacy_notion_id: 0e8cad4f-b605-82e9-ae12-813a91ea3581
---

# Speculative Decoding

Speculative decoding lets a cheap draft model propose several tokens and asks the
target model to verify them in one parallel forward pass.

For greedy decoding, matching target choices can be accepted directly. For sampling,
accept/reject and correction distributions are required so the final samples still
follow the target model distribution. Speedup depends on acceptance length and the
draft-to-target cost ratio; a slow or poorly aligned draft can make the method lose.

Verification also complicates KV-cache rollback and branching. The core result is
lower latency without changing the target distribution, not fewer target parameters.

## Interview answer

“A draft proposes multiple tokens, and the target verifies them in parallel. The
method helps when acceptance is high and drafting is cheap; sampling needs rejection
correction to preserve the target distribution.”

## Sources

- [MTP](https://www.yuque.com/shakewin/woezs0/xsgrva9gef5pwz5n)
- [DeepSeek Paper Reading](https://www.yuque.com/shakewin/woezs0/agn9y7w2skcvzzrk)

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[causal-attention|Causal Attention]]
- Affects: [[kv-cache|KV Cache]]

<!-- END GENERATED OBSIDIAN LINKS -->
