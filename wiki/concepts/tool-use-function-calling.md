---
id: tool-use-function-calling
title: Tool Use and Function Calling
type: concept
domains: [agent-systems, ai-engineering]
aliases: [function calling, tool calling]
level: foundational
relations:
  prerequisites: [transformer-architecture]
  enables: [agent-loop, model-context-protocol]
sources: [yuque:275632325, yuque:263799689, yuque:230859031]
legacy_notion_id: 6decad4f-b605-823b-a65a-819b9c567c31
---

# Tool Use and Function Calling

Tool use lets a model select a named capability and emit structured arguments that
a runtime validates and executes.

The schema is part of the model interface: concise names, discriminative descriptions,
strict types, and bounded results improve selection. The runtime owns authorization,
timeouts, idempotency, concurrency, redaction, and error handling; model intent is
not a security decision. Parallel calls help independent reads, while ordered state
changes must remain sequential.

## Sources

- [Claude Code Analysis](https://www.yuque.com/shakewin/xhs6fk/ru7gng41hd6azwdd)
- [Nanobot Code Review](https://www.yuque.com/shakewin/xhs6fk/ga5n2frllmdao7c3)
- [AI Agent](https://www.yuque.com/shakewin/xhs6fk/auotaftct11kqk3g)

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[transformer-architecture|Transformer Architecture]]
- Enables: [[agent-loop|Agent Loop]], [[model-context-protocol|Model Context Protocol]]

<!-- END GENERATED OBSIDIAN LINKS -->
