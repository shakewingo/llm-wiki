---
id: jev
title: Jev (TypeSafe Structured Decision Model)
type: concept
domains: [agent-systems, ai-engineering, post-training]
aliases: [TypeSafe, RLCD model, structured decision model]
level: intermediate
relations:
  prerequisites: [reward-modeling]
  enables: [tool-use-function-calling]
  contrasts_with: [direct-preference-optimization]
sources: [yuque:286521159]
---

# Jev (TypeSafe Structured Decision Model)

Jev is a fast, cheap frontier-intelligence model built on RLCD (Reinforcement
Learning from Contrastive Distillation). It maps unstructured state into typed
probabilistic decisions through a constrained output interface.

## Interface

Jev exposes three structured judgment types via `TypeSafeClient`:

- **Noul** — boolean yes/no decisions (e.g., "Does this message request a refund?")
- **Choice** — multi-class selection from predefined criteria
- **Score** — ordinal rating against a rubric (e.g., frustration level 1–3)

Input is a free-form `state` dict; output is always typed and deterministic in
structure, which eliminates parsing errors and reduces hallucination.

## Pricing

$0.04 per million input tokens; output is free. This makes Jev economical for
high-volume classification and filtering workloads where per-call cost matters.

## Key Applications

| Priority | Use Case | Value |
|----------|----------|-------|
| 1 | High-frequency classification & routing (tickets, emails, content tagging) | Bounded answer space, high call volume, measurable cost-per-decision |
| 2 | Large-scale text structuring & feature extraction | Parallel independent judgments on the same text |
| 3 | Agent evaluation & guard layer (output scoring, citation verification, prompt injection detection) | Low-latency checks at every agent step |
| 4 | RAG filtering & validation (relevance, reranking, evidence support) | Clean integration into existing retrieval pipelines |

## Sources

- [Jev](https://www.yuque.com/shakewin/woezs0/snznodh9vqk5xvyg)

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[reward-modeling|Reward Modeling]]
- Enables: [[tool-use-function-calling|Tool Use and Function Calling]]
- Contrasts with: [[direct-preference-optimization|Direct Preference Optimization]]

<!-- END GENERATED OBSIDIAN LINKS -->
