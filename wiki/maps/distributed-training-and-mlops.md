---
id: distributed-training-and-mlops
title: Distributed Training and MLOps Map
type: map
domains: [distributed-systems, training, mlops]
aliases: []
level: mixed
entry_points:
  - data-parallelism
  - fully-sharded-data-parallelism
  - tensor-parallelism
  - pipeline-parallelism
  - expert-parallelism
  - mixed-precision-training
  - model-quantization
  - llm-evaluation
relations:
  prerequisites: [transformer-architecture, pretraining]
sources: [yuque:283802487, yuque:253935769, yuque:245719568]
---

# Distributed Training and MLOps Map

Distributed execution trades memory and compute capacity for communication and
coordination.

[Data parallelism](../concepts/data-parallelism.md) replicates the model;
[FSDP](../concepts/fully-sharded-data-parallelism.md) shards its state;
[tensor parallelism](../concepts/tensor-parallelism.md) splits layer operations;
[pipeline parallelism](../concepts/pipeline-parallelism.md) splits layers; and
[expert parallelism](../concepts/expert-parallelism.md) distributes routed experts.
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
