---
id: radix-attention
title: Radix Attention
type: concept
domains: [inference, serving]
aliases: [RadixAttention]
level: intermediate
relations:
  prerequisites: [kv-cache]
  part_of: [prompt-caching]
  affects: [kv-cache]
sources: [yuque:279560513]
---

# Radix Attention

Radix attention organizes cached prefixes in a radix tree whose branches mirror
shared and diverging token sequences.

It naturally represents many conversations that share a system prompt and then
branch. Longest-prefix lookup finds reusable KV state; eviction can remove cold
branches. The tree is powerful for multi-turn and branching workloads but requires
careful concurrency, reference counting, and tenant isolation.

## Interview answer

“Radix attention stores prefix KV state in a radix tree. Shared prompt segments map
to shared paths, making longest-prefix reuse efficient for branching workloads.”

## Source

- [Prompt Caching and Prefix Cache](https://www.yuque.com/shakewin/sysgq3/fddexv7e29h99vrl)

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[kv-cache|KV Cache]]
- Part of: [[prompt-caching|Prompt Caching]]
- Affects: [[kv-cache|KV Cache]]

<!-- END GENERATED OBSIDIAN LINKS -->
