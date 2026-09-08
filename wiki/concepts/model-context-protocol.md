---
id: model-context-protocol
title: Model Context Protocol
type: concept
domains: [agent-systems, integration]
aliases: [MCP]
level: intermediate
relations:
  prerequisites: [tool-use-function-calling]
  enables: [retrieval-augmented-generation, multimodal-ai-systems]
sources: [yuque:241262981, yuque:213041038, yuque:275632325]
---

# Model Context Protocol

MCP standardizes how an AI host discovers and calls external tools and accesses
context resources through separately managed servers.

It reduces one-off connector code and lets integrations expose typed capabilities,
but it does not remove trust boundaries. Hosts must authenticate servers, restrict
available capabilities, validate tool arguments, contain local processes, and treat
returned content as untrusted. A good server keeps operations narrow and makes
read-only versus mutating behavior explicit.

## Sources

- [RCA Agent](https://www.yuque.com/shakewin/xhs6fk/igcgrrffw77ehu2z)
- [Voice Chatbot](https://www.yuque.com/shakewin/xhs6fk/smzsma1rag73ei59)
- [Claude Code Analysis](https://www.yuque.com/shakewin/xhs6fk/ru7gng41hd6azwdd)

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[tool-use-function-calling|Tool Use and Function Calling]]
- Enables: [[retrieval-augmented-generation|Retrieval-Augmented Generation]], [[multimodal-ai-systems|Multimodal AI Systems]]

<!-- END GENERATED OBSIDIAN LINKS -->
