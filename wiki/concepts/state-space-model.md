---
id: state-space-model
title: State Space Models
type: concept
domains: [model-architecture, sequence-modeling]
aliases: [SSM, selective state space model, Mamba]
level: advanced
relations:
  prerequisites: [recurrent-neural-network]
  contrasts_with: [transformer-architecture, recurrent-neural-network]
sources: [notion:388cad4f-b605-8074-8c53-ff558a15beb0]
---

# State Space Models

A state-space sequence model evolves a compact latent state and reads an output from
it. In discrete form, $x_k=Ax_{k-1}+Bu_k$ separates state transition from input
injection. Structured parameterizations allow the recurrence to be evaluated with
parallel scans or convolutions during training while retaining constant-state,
linear-time streaming inference.

Selective models such as Mamba make input, output, or timescale parameters depend on
the current token. This lets the system decide what to write, retain, and expose,
addressing the content-insensitive compression of a fixed linear recurrence.

Unlike attention, the state is a bottleneck rather than an explicit store of prior
tokens. That improves asymptotic memory but can lose exact recall; practical results
depend on scan kernels, initialization, state dimension, and hybridization with
attention.

## Interview answer

“An SSM turns a sequence into updates of a compact latent state. Its structured
recurrence can train in parallel and decode with constant state; selective SSMs make
the write/read dynamics input-dependent, trading attention's explicit history for
efficient compression.”

## Sources

- [Alisa’s book of LLMs](https://app.notion.com/p/388cad4fb60580748c53ff558a15beb0)

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[recurrent-neural-network|Recurrent Neural Networks]]
- Contrasts with: [[transformer-architecture|Transformer Architecture]], [[recurrent-neural-network|Recurrent Neural Networks]]

<!-- END GENERATED OBSIDIAN LINKS -->
