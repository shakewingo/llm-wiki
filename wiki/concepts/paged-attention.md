---
id: paged-attention
title: Paged Attention
type: concept
domains: [inference, serving]
aliases: [PagedAttention]
level: intermediate
relations:
  prerequisites: [kv-cache]
  part_of: [prompt-caching]
  affects: [kv-cache]
sources: [yuque:279560513]
---

# Paged Attention

Paged attention manages KV state in fixed-size blocks rather than requiring one
contiguous allocation per sequence, reducing fragmentation and enabling flexible
sharing and eviction.

For automatic prefix caching, a block can be addressed by a hash incorporating all
tokens up to that block. Matching blocks are reused, so shared prefixes need not
end at a whole request boundary. Smaller blocks improve granularity but add metadata
and lookup overhead; larger blocks can waste capacity at sequence tails.

## Interview answer

“Paged attention brings virtual-memory-style blocks to the KV cache. It reduces
fragmentation and enables block-level prefix reuse, at the cost of indirection and
block-management overhead.”

## Source

- [Prompt Caching and Prefix Cache](https://www.yuque.com/shakewin/sysgq3/fddexv7e29h99vrl)

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[kv-cache|KV Cache]]
- Part of: [[prompt-caching|Prompt Caching]]
- Affects: [[kv-cache|KV Cache]]

<!-- END GENERATED OBSIDIAN LINKS -->
