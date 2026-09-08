---
id: llm-evaluation
title: LLM Evaluation
type: concept
domains: [evaluation, ai-engineering]
aliases: [LLM evals]
level: intermediate
relations:
  affects: [pretraining, supervised-fine-tuning, rlhf, retrieval-augmented-generation]
sources: [yuque:253935769, yuque:245719568, yuque:222857934]
---

# LLM Evaluation

LLM evaluation measures capability, reliability, safety, latency, and cost with a
mixture of automated tests and human judgment.

Training-data contamination can invalidate benchmarks, and one aggregate score hides
important slices. RAG requires separate retrieval and grounded-answer metrics; agents
need task completion, tool correctness, side-effect, and recovery checks. Pairwise
preference is useful for open-ended quality but inherits judge bias. A good evaluation
suite is versioned, reproducible, resistant to leakage, and tied to deployment
decisions rather than leaderboard optimization.

## Sources

- [NVIDIA Agentic AI Training](https://www.yuque.com/shakewin/fidaqi/fgv15n9m42qh9m77)
- [Knowledge Puzzle](https://www.yuque.com/shakewin/woezs0/fvhczuilmmhpf6t4)
- [CS7641 ML](https://www.yuque.com/shakewin/fidaqi/evbvouf8opoc9aix)

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Affects: [[pretraining|Language-Model Pretraining]], [[supervised-fine-tuning|Supervised Fine-Tuning]], [[rlhf|Reinforcement Learning from Human Feedback]], [[retrieval-augmented-generation|Retrieval-Augmented Generation]]

<!-- END GENERATED OBSIDIAN LINKS -->
