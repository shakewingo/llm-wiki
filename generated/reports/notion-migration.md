# Notion Inventory and Migration Map

Verified 2026-09-08 against Notion workspace `ShakewinGo’s Space`.

## Database inventory

- Database: [🧠 AI Knowledge Map](https://app.notion.com/p/3accad4fb605802db9aae71885532d7e)
- Database ID: `3accad4f-b605-802d-b9aa-e71885532d7e`
- Data source: `collection://eb4cad4f-b605-83f3-9b65-0733627e42e4`
- View: `Default view` (`d8acad4f-b605-82c4-b9b1-8879decb2b3d`), table type
- Properties: `Name` (title), `Domain`, `Level`, `Status`, `Tags`, `Type`,
  `Yuque Link`, `Related Concepts`, and `Related Concepts 1`

Select values observed in the schema:

- Domain: Pre-training, Mid-training, Post-training, Inference, RL, Agent Systems,
  Evaluation, MLOps, Foundation
- Level: Foundational, Intermediate, Advanced
- Status: Stub, Draft, Polished
- Type: Concept, Method/Algorithm, Paper Note, Interview Q&A, Practice/Code

## Rows

| Name | Stable Notion page ID | Domain | Type | Status | Yuque link | Migration |
|---|---|---|---|---|---|---|
| [graph](https://app.notion.com/p/3accad4fb60580d8a1cdec78bde5f671) | `3accad4f-b605-80d8-a1cd-ec78bde5f671` | — | — | — | — | Operational page; do not migrate as a concept |
| [Transformer Architecture](https://app.notion.com/p/fa3cad4fb60583e7910981c407243233) | `fa3cad4f-b605-83e7-9109-81c407243233` | Pre-training | Concept | Draft | yes | `transformer-architecture` |
| [RLHF vs DPO vs GRPO](https://app.notion.com/p/33dcad4fb60583109dc801108f3d93c7) | `33dcad4f-b605-8310-9dc8-01108f3d93c7` | Post-training | Interview Q&A | Draft | yes | Defer to post-training slice |
| [KV Cache](https://app.notion.com/p/4c2cad4fb6058288b81081feb1817985) | `4c2cad4f-b605-8288-b810-81feb1817985` | Inference | Concept | Polished | no | `kv-cache` |
| [MoE](https://app.notion.com/p/3e3cad4fb60582939ae2815dca1c81cc) | `3e3cad4f-b605-8293-9ae2-815dca1c81cc` | Pre-training | Concept | Stub | no | `mixture-of-experts` |
| [Tool Use](https://app.notion.com/p/6decad4fb605823ba65a819b9c567c31) | `6decad4f-b605-823b-a65a-819b9c567c31` | Agent Systems | Method/Algorithm | Stub | no | Defer to agent slice |
| [GRPO](https://app.notion.com/p/965cad4fb6058220bb2e81cb441e982f) | `965cad4f-b605-8220-bb2e-81cb441e982f` | Post-training | Method/Algorithm | Draft | yes | Defer to post-training slice |
| [Speculative Decoding](https://app.notion.com/p/0e8cad4fb60582e9ae12813a91ea3581) | `0e8cad4f-b605-82e9-ae12-813a91ea3581` | Inference | Method/Algorithm | Draft | yes | `speculative-decoding` |
| [Multi-Agent Orchestration](https://app.notion.com/p/65ccad4fb605838ea8bb01e26225101f) | `65ccad4f-b605-838e-a8bb-01e26225101f` | Agent Systems | Method/Algorithm | Stub | no | Defer to agent slice |
| [Prompt Caching](https://app.notion.com/p/3accad4fb6058054a012d278d3cd8527) | `3accad4f-b605-8054-a012-d278d3cd8527` | Inference | Method/Algorithm | Polished | yes | `prompt-caching` |

## Legacy edge inventory

The two relation fields are the forward and reciprocal display sides of one
self-relation. The following undirected pairs were observed:

- Transformer Architecture — Prompt Caching
- Transformer Architecture — GRPO
- Transformer Architecture — RLHF vs DPO vs GRPO
- Prompt Caching — KV Cache
- GRPO — RLHF vs DPO vs GRPO

These links mix architecture, association, and interview-navigation semantics. No
field or page content establishes a consistent direction or type. Migration policy:
retain the inventory, derive typed Markdown edges only from concept mechanics and
source evidence, and leave questionable links unresolved.

## Property mapping

| Notion field | Markdown destination | Rule |
|---|---|---|
| Page ID | `legacy_notion_id` | Provenance only; stable concept ID remains canonical |
| Name | `title`; candidate `id` | Normalize ID once, then keep stable across renames |
| Domain | `domains` | Normalize to lowercase kebab-case; permit multiple domains |
| Level | `level` | Lowercase informational metadata |
| Type | `type` | Map concepts/methods to `concept`; Q&A to interview pages |
| Tags | Body/index metadata | Keep only when they support navigation |
| Status | Migration report | Do not treat Notion polish as source authority |
| Yuque Link | Registry-backed `sources` | Resolve document ID; never copy the note body |
| Related Concepts pair | unresolved edge candidates | Do not infer direction or typed semantics |

## Data-quality findings

- No duplicate names or aliases were present among the nine knowledge rows.
- Three Notion rows had no Yuque URL: KV Cache, MoE, and both agent-system stubs.
- The Prompt Caching row was marked Polished but its page body was blank.
- The `graph` row is not a concept and contains server-operational instructions.
- The graph embed uses port `18791`; the older handoff referred to `18793`.
