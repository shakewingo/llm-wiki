---
id: applied-ai-drills
title: Applied AI and Evaluation Drills
type: interview
domains: [applied-ai, evaluation, causal-ml]
aliases: []
level: mixed
relations:
  prerequisites: [applied-ai-and-evaluation]
sources: [yuque:145103815, yuque:145103757, yuque:179434725, yuque:241262981, yuque:213041038]
---

# Applied AI and Evaluation Drills

## Why are anomaly metrics easy to game?

Segment adjustment or delay tolerance can turn one late detection into a full true
positive. Always report the matching rule, alert volume, delay, and point/segment
metrics.

## PC versus GES?

PC removes edges using conditional-independence tests; GES greedily optimizes a
fit-complexity score over equivalence classes. Their assumptions and failures differ.

## Why does correlation fail for RCA?

Downstream services often correlate with the same incident. Temporal order, topology,
interventions, and conditional evidence are needed to support causality.

## How do multimodal pipeline errors compound?

ASR, retrieval, language generation, TTS, and rendering each introduce error and
latency; evaluate components and end-to-end behavior.

## What is non-negotiable for synthetic personas?

Consent, repeated disclosure, identity protection, abuse prevention, and appropriate
psychological/legal safeguards.

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[applied-ai-and-evaluation|Applied AI and Evaluation Map]]

<!-- END GENERATED OBSIDIAN LINKS -->
