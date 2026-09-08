---
id: prompt-caching
title: Prompt Caching
type: concept
domains: [inference, serving]
aliases: [prefix caching, prefix cache]
level: intermediate
relations:
  prerequisites: [kv-cache]
  implemented_in: [paged-attention, radix-attention]
sources: [yuque:279560513]
legacy_notion_id: 3accad4f-b605-8054-a012-d278d3cd8527
---

# Prompt Caching

Prompt caching reuses prefill work when requests share an identical token prefix,
avoiding repeated computation and KV materialization for that prefix.

The cache key must reflect the exact token sequence, model, and relevant execution
configuration. Stable serialization and placing invariant instructions early in
the prompt improve hit rate; timestamps, request IDs, or non-deterministic JSON near
the front destroy reuse. Paged block hashes and radix trees support partial prefix
sharing with different allocation and lookup tradeoffs.

Operational risks include stale entries, tenant data leakage, false sharing from an
underspecified key, and memory pressure from weak eviction policy.

## Interview answer

“Prompt caching reuses prefill KV state for identical prefixes. It saves first-token
latency and compute only when prompts are serialized deterministically and cache
keys isolate model, version, and tenant-sensitive state.”

## Source

- [Prompt Caching and Prefix Cache](https://www.yuque.com/shakewin/sysgq3/fddexv7e29h99vrl)

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[kv-cache|KV Cache]]
- Implemented in: [[paged-attention|Paged Attention]], [[radix-attention|Radix Attention]]

<!-- END GENERATED OBSIDIAN LINKS -->
