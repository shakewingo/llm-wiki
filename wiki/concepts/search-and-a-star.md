---
id: search-and-a-star
title: Search and A*
type: concept
domains: [foundations]
aliases: [A-star search, graph search]
level: foundational
relations:
  enables: [agent-loop]
sources: [yuque:203899196]
---

# Search and A*

Search explores a state space by maintaining a frontier of candidate paths and an
explored set that prevents repeated work. Uniform-cost search expands the lowest
known path cost $g(n)$; greedy best-first search uses only an estimated remaining
cost $h(n)$; A* combines them as $f(n)=g(n)+h(n)$.

An admissible heuristic never overestimates the remaining cost, which lets A* retain
optimality under the usual assumptions. A weak heuristic degenerates toward
uniform-cost search, while an overconfident heuristic may be fast but lose the best
solution. The same pattern appears in agent planning: proposal order, state
deduplication, cost accounting, and termination rules matter as much as generation.

## Interview answer

“A* expands the state with the smallest known cost plus admissible estimate. It is
optimal with the right heuristic, but memory and branching still limit scale.”

## Source

- [Gatech CS6601 - AI](https://www.yuque.com/shakewin/fidaqi/dlm2n18clgtdxppy)

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Enables: [[agent-loop|Agent Loop]]

<!-- END GENERATED OBSIDIAN LINKS -->
