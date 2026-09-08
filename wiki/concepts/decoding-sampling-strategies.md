---
id: decoding-sampling-strategies
title: Decoding and Sampling Strategies
type: concept
domains: [inference, evaluation]
aliases: [top-k, top-p, nucleus sampling]
level: foundational
relations:
  prerequisites: [causal-attention]
  affects: [llm-evaluation]
sources: [yuque:145901413, yuque:245719568, notion:388cad4f-b605-8074-8c53-ff558a15beb0]
---

# Decoding and Sampling Strategies

Decoding converts next-token probabilities into output. Greedy decoding always picks
the maximum; beam search keeps several high-scoring sequences; temperature rescales
logits; top-k samples among a fixed number of tokens; top-p samples from the smallest
set whose cumulative mass reaches a threshold.

Lower temperature is more deterministic, while higher temperature increases diversity
and error risk. Beam search can favor generic sequences and is expensive for open-ended
dialogue. Sampling settings are part of an evaluation configuration: comparing models
under different decoding policies confounds model quality with search behavior.

## Sources

- [LLaMA](https://www.yuque.com/shakewin/woezs0/avr5nrkaahavwdwv)
- [Knowledge Puzzle](https://www.yuque.com/shakewin/woezs0/fvhczuilmmhpf6t4)
- [Alisa’s book of LLMs](https://app.notion.com/p/388cad4fb60580748c53ff558a15beb0)

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[causal-attention|Causal Attention]]
- Affects: [[llm-evaluation|LLM Evaluation]]

<!-- END GENERATED OBSIDIAN LINKS -->
