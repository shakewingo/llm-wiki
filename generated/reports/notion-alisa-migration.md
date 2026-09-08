# Alisa’s Book of LLMs — Integration Review

Reviewed source: [Alisa’s book of LLMs](https://app.notion.com/p/388cad4fb60580748c53ff558a15beb0)

- Notion page ID: `388cad4f-b605-8074-8c53-ff558a15beb0`
- Parent: `Docs`
- Last edited at review: `2026-09-04T09:44:00.000Z` (official API timestamp)
- Approximate size: 22,764 words, 64 detected headings
- Verification state reported by Notion: unverified

## Integration judgment

The page is broad and technically detailed, but much of its LLM content overlaps
the existing Yuque-derived wiki. It is integrated as a registered `reference`
source rather than copied as a parallel book. Existing pages receive additional
provenance where the source strengthens them; new pages are limited to important
gaps with enough source depth to support a useful synthesis.

The source mixes polished explanations, implementation notes, personal annotations,
and a few explicitly uncertain statements. The wiki therefore preserves the useful
mechanics while avoiding source-specific hardware numbers, tentative wording, and
claims that would require independent verification.

## New concepts justified by the gap review

### Training foundations

- `neural-network-computation`
- `backpropagation-and-autodiff`
- `deep-learning-optimization`
- `numerical-stability`

### Modern Transformer and serving internals

- `rms-normalization`
- `swiglu-feed-forward-network`
- `llm-compute-and-memory-accounting`
- `continuous-batching-and-sequence-packing`
- `flash-attention`

### Alternative sequence architectures

- `recurrent-neural-network`
- `state-space-model`
- comparison: `sequence-model-families`

### Hardware and distributed execution

- `gpu-performance-model`
- `distributed-collectives`
- `context-parallelism`

## Existing areas reinforced instead of duplicated

- Transformer architecture, self-attention, RoPE, KV cache, speculative decoding,
  and decoding strategies.
- Probabilistic objectives and numerical precision.
- Policy gradients, PPO, RLHF, GRPO, and DPO.
- Data, fully sharded, tensor, pipeline, and expert parallelism.
- Multimodal systems.

## Material deliberately not split into new pages

- Activation functions stay inside `neural-network-computation`; a separate catalog
  would add vocabulary without improving navigation.
- Entropy, cross-entropy, and KL extend `probabilistic-objectives` rather than
  creating overlapping pages.
- Scaling laws were marked skipped in the source and lacked enough material for a
  supported concept page.
- Gumbel-Softmax and straight-through estimation are useful but peripheral to the
  current interview map; they can be promoted later if another source or project
  creates a concrete need.
- Volatile device capacity and throughput examples were generalized into a durable
  roofline/performance model.
- The similarly titled Notion page `81ccad4f-b605-82ad-986c-8103273ac19d` was not
  ingested because the user supplied the exact `388cad4f-...` source page.

## Persistence and synchronization

The full Notion body was fetched for review and was not saved in the wiki. The
registry stores metadata, the reviewed version timestamp, and affected page IDs.
`sync_yuque.py` preserves non-Yuque records during bootstrap and reports them
separately instead of marking them deleted. Routine Notion access now uses the
official API directly: `sync_notion.py` reads `NOTION_API_KEY` from the process
environment, checks registered pages, and exports Notion-flavored Markdown only to
temporary storage. The API token is never stored in this repository.
