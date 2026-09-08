---
id: expert-parallelism
title: Expert Parallelism
type: concept
domains: [distributed-systems, inference, training]
aliases: [EP]
level: advanced
relations:
  prerequisites: [mixture-of-experts]
  part_of: [mixture-of-experts]
sources: [yuque:283802487, yuque:241299652, notion:388cad4f-b605-8074-8c53-ff558a15beb0]
---

# Expert Parallelism

Expert parallelism places different MoE experts on different devices and routes
token representations to the devices selected by the router.

It distributes expert parameters efficiently, but its all-to-all traffic is highly
sensitive to routing skew and network topology. Expert tensor parallelism can shard
one expert further, trading memory for still more communication. A configuration
must be benchmarked as a whole: adding EP may lower memory while reducing tokens per
second on machines without strong device-to-device links.

## Interview answer

“EP distributes experts across devices and exchanges tokens according to routing.
It fits larger MoE models, but load balance and all-to-all communication determine
whether it is actually faster.”

## Sources

- [Distributed Framework](https://www.yuque.com/shakewin/sysgq3/mhw00hcggbv1scr8)
- [DeepSeek Paper Reading](https://www.yuque.com/shakewin/woezs0/agn9y7w2skcvzzrk)
- [Alisa’s book of LLMs](https://app.notion.com/p/388cad4fb60580748c53ff558a15beb0)

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[mixture-of-experts|Mixture of Experts]]
- Part of: [[mixture-of-experts|Mixture of Experts]]

<!-- END GENERATED OBSIDIAN LINKS -->
