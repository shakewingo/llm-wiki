---
id: chain-of-thought-reasoning
title: Chain-of-Thought Reasoning
type: concept
domains: [reasoning, post-training]
aliases: [CoT, reasoning trace]
level: intermediate
relations:
  prerequisites: [supervised-fine-tuning, reinforcement-learning]
  affects: [llm-evaluation, knowledge-distillation]
sources: [yuque:204005901, yuque:241299652]
---

# Chain-of-Thought Reasoning

Chain-of-thought prompting or training elicits intermediate reasoning steps before a
final answer, often improving multi-step tasks in sufficiently capable models.

Reasoning traces can be supplied through demonstrations, generated and filtered for
SFT, optimized with outcome or process rewards, or distilled into smaller models.
Visible explanations are not guaranteed to be faithful to internal computation and
may contain plausible mistakes. Evaluation should therefore verify the final result
and critical steps rather than treating length as reasoning quality.

## Sources

- [MLi Paper Reading](https://www.yuque.com/shakewin/woezs0/hhoofowylkt3t2id)
- [DeepSeek Paper Reading](https://www.yuque.com/shakewin/woezs0/agn9y7w2skcvzzrk)

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[supervised-fine-tuning|Supervised Fine-Tuning]], [[reinforcement-learning|Reinforcement Learning]]
- Affects: [[llm-evaluation|LLM Evaluation]], [[knowledge-distillation|Knowledge Distillation]]

<!-- END GENERATED OBSIDIAN LINKS -->
