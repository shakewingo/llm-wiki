---
id: distributed-training-and-mlops
title: Distributed Training and MLOps Map
type: map
domains: [distributed-systems, training, mlops]
aliases: []
level: mixed
entry_points:
  - gpu-performance-model
  - llm-compute-and-memory-accounting
  - distributed-collectives
  - data-parallelism
  - fully-sharded-data-parallelism
  - tensor-parallelism
  - pipeline-parallelism
  - expert-parallelism
  - context-parallelism
  - mixed-precision-training
  - model-quantization
  - llm-evaluation
relations:
  prerequisites: [transformer-architecture, pretraining]
sources: [yuque:283802487, yuque:253935769, yuque:245719568, notion:388cad4f-b605-8074-8c53-ff558a15beb0]
---

# Distributed Training and MLOps Map

Distributed execution trades memory and compute capacity for communication and
coordination.

Begin with the [GPU performance model](../concepts/gpu-performance-model.md),
[compute and memory accounting](../concepts/llm-compute-and-memory-accounting.md),
and [collective operations](../concepts/distributed-collectives.md). They explain
whether a proposed sharding strategy saves the resource that is actually limiting.

[Data parallelism](../concepts/data-parallelism.md) replicates the model;
[FSDP](../concepts/fully-sharded-data-parallelism.md) shards its state;
[tensor parallelism](../concepts/tensor-parallelism.md) splits layer operations;
[pipeline parallelism](../concepts/pipeline-parallelism.md) splits layers; and
[expert parallelism](../concepts/expert-parallelism.md) distributes routed experts.
[Context parallelism](../concepts/context-parallelism.md) splits long sequences.
These dimensions can be combined, but every extra dimension adds collectives,
configuration, and failure modes.

[Mixed precision](../concepts/mixed-precision-training.md) improves training execution,
while [quantization](../concepts/model-quantization.md) targets compact computation or
serving. [Evaluation](../concepts/llm-evaluation.md) closes the lifecycle: throughput
or memory gains are useful only when quality remains acceptable.

Practice with [distributed-systems drills](../interview/distributed-systems-drills.md).

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[transformer-architecture|Transformer Architecture]], [[pretraining|Language-Model Pretraining]]

<!-- END GENERATED OBSIDIAN LINKS -->
