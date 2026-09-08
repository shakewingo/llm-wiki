---
id: gpu-performance-model
title: GPU Performance Model for LLMs
type: concept
domains: [systems, training, inference]
aliases: [roofline model, arithmetic intensity, model FLOP utilization, MFU]
level: intermediate
relations:
  enables: [flash-attention, distributed-collectives, llm-compute-and-memory-accounting]
sources: [notion:388cad4f-b605-8074-8c53-ff558a15beb0, yuque:283802487]
---

# GPU Performance Model for LLMs

Accelerator performance is bounded either by arithmetic throughput or by moving
bytes through the memory hierarchy. High-bandwidth memory is large but distant from
the compute units; registers and on-chip SRAM are far smaller and faster. Arithmetic
intensity—FLOPs performed per byte moved—predicts which resource is limiting under
the roofline model.

Large, well-shaped matrix multiplications can approach the compute roof because
loaded operands are reused. Autoregressive decode at small batch sizes often streams
many parameter and KV-cache bytes for comparatively little work, making bandwidth
the roof. Kernel fusion, batching, quantization, and cache-aware algorithms help by
increasing reuse or reducing traffic.

Model FLOP utilization compares achieved model FLOPs per second with hardware peak.
It is useful only with a consistent FLOP convention and should be read alongside
tokens per second, latency, memory usage, and communication overhead.

## Interview answer

“The roofline model compares arithmetic intensity with the GPU's compute-to-bandwidth
ratio. Training matmuls are often compute-friendly, while small-batch decode is
frequently bandwidth-bound; the optimization target is therefore bytes moved, not
just FLOPs.”

## Sources

- [Alisa’s book of LLMs](https://app.notion.com/p/388cad4fb60580748c53ff558a15beb0)
- [Distributed Framework](https://www.yuque.com/shakewin/sysgq3/mhw00hcggbv1scr8)

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Enables: [[flash-attention|FlashAttention]], [[distributed-collectives|Distributed Collective Operations]], [[llm-compute-and-memory-accounting|LLM Compute and Memory Accounting]]

<!-- END GENERATED OBSIDIAN LINKS -->
