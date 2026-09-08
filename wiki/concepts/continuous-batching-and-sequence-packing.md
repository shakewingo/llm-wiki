---
id: continuous-batching-and-sequence-packing
title: Continuous Batching and Sequence Packing
type: concept
domains: [inference, serving, training]
aliases: [continuous batching, in-flight batching, sequence packing, token-budget batching]
level: intermediate
relations:
  prerequisites: [kv-cache]
  optimized_by: [paged-attention]
  affects: [llm-compute-and-memory-accounting]
sources: [notion:388cad4f-b605-8074-8c53-ff558a15beb0, yuque:279560513]
---

# Continuous Batching and Sequence Packing

Static batching waits for every sequence in a batch to finish, wasting slots when
generation lengths differ. Continuous batching removes completed requests and
admits new work at iteration boundaries, keeping more of the accelerator occupied.
Schedulers may also mix compute-heavy prefill with bandwidth-heavy decode, subject
to latency and memory budgets.

Sequence packing concatenates shorter examples into a fixed token budget and masks
cross-example attention. It is common in training and fine-tuning; serving engines
instead maintain independent request states while dynamically assembling each step.
Both reduce padding waste, but incorrect masks or position IDs can leak information
between sequences.

Paged KV-cache allocation complements continuous batching because request slots can
grow, finish, and be reclaimed without requiring one contiguous maximum-sized cache.

## Interview answer

“Continuous batching replaces finished generation requests immediately instead of
waiting for the longest sequence. Sequence packing reduces padding by sharing a
token budget, but must preserve independent masks and positions.”

## Sources

- [Alisa’s book of LLMs](https://app.notion.com/p/388cad4fb60580748c53ff558a15beb0)
- [Prompt Caching and Prefix Cache](https://www.yuque.com/shakewin/sysgq3/fddexv7e29h99vrl)

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[kv-cache|KV Cache]]
- Affects: [[llm-compute-and-memory-accounting|LLM Compute and Memory Accounting]]
- Optimized by: [[paged-attention|Paged Attention]]

<!-- END GENERATED OBSIDIAN LINKS -->
