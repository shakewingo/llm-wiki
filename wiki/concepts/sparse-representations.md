---
id: sparse-representations
title: Sparse Representations
type: concept
domains: [foundations, systems]
aliases: [sparse matrix]
level: foundational
relations:
  enables: [vector-database, mixture-of-experts]
sources: [yuque:224766388]
---

# Sparse Representations

A sparse representation stores only nonzero values and their indices instead of a
full dense array. One-hot features are the simplest example: dimensionality may be
large while each row contains only a few active entries.

Formats such as CSR favor row slicing and matrix multiplication, while CSC favors
column access. Sparsity saves memory and compute only when kernels can exploit the
pattern; irregular access, indexing overhead, or conversion to dense form can erase
the benefit. Modern AI uses several kinds of sparsity, from retrieval and expert
routing to sparse attention, but their hardware behavior differs.

## Source

- [ML Knowledge](https://www.yuque.com/shakewin/aqegd7/hbm8c659b0bm0bf8)

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Enables: [[vector-database|Vector Databases and HNSW]], [[mixture-of-experts|Mixture of Experts]]

<!-- END GENERATED OBSIDIAN LINKS -->
