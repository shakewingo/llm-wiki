---
id: post-training
title: Post-Training
type: concept
domains: [post-training, alignment, agent-engineering]
aliases: [post-training pipeline, agent post-training]
level: intermediate
relations:
  prerequisites: [pretraining, supervised-fine-tuning]
  enables: [rlhf, direct-preference-optimization, group-relative-policy-optimization, knowledge-distillation, recursive-self-improvement]
  contrasts_with: [pretraining]
sources: [yuque:286000095]
---

# Post-Training

Post-training transforms a pretrained base model into a useful policy through
supervised fine-tuning, preference optimization, and reinforcement learning.
For agent systems, the pipeline adds environment-grounded verification and
programmatic task generation.

## Agent Post-Training Pipeline

The standard industrial pipeline for agent post-training:

1. **Resettable environment + programmatic verifier** — the most expensive and
   core component. A deterministic harness (fixtures + verify script) that can
   reset state and score agent trajectories.
2. **Task generator** — programmatically generates training variants from
   skeleton templates, varying layout, distractor files, numeric values,
   dependency chain length, and fault injection positions.
3. **Rollout** — sample trajectories from a teacher model or the policy itself
   within the harness.
4. **Verifier filtering → dedup → loss mask** — keep only passing trajectories;
   compute loss only on assistant tokens (tool observations excluded).
5. **SFT (LoRA/QLoRA)** — fine-tune on filtered trajectories.
6. **Optional RL** — GRPO/RLVR with verifiable rewards, or offline DPO on
   success/failure pairs.
7. **Evaluation** — freeze the adapter, run paired comparison on held-out test
   skeletons, report win/loss, regression, and cost.

## Algorithm Tiers (by cost, all under $100)

| Tier | Method | Description | Cost |
|------|--------|-------------|------|
| L0 | Rejection Sampling Fine-Tuning (RFT / STaR / expert iteration) | Base model samples N trajectories per task; keep only verifier-passing ones for SFT. No teacher needed. | Lowest |
| L1 | Teacher Distillation | Strong model API runs in your harness; filter by execution results. Inject faults to collect recovery trajectories. | ~$10–25 API |
| L2 | DPO / KTO | Pair one success and one failure trajectory per task for offline preference training. | Very low, but multi-turn DPO alignment details are error-prone |
| L3 | GRPO Online RL | Reward = verifier pass/fail + format + recovery bonuses. Frameworks: TRL, verl, OpenPipe ART. | Rollout cost dominates; 7B is tight, 1.5–4B realistic |

GRPO requires pass@k between 0 and 1 — tasks where the model always succeeds or
always fails produce zero advantage and no learning signal.

## Training Data Strategy

- **Primary**: self-generated from the environment. Programmatically generate
  variants from train skeletons covering layout, distractor files, numeric
  values, dependency chain length, and fault injection positions.
- **Public datasets** (≤20% mix, to prevent general function-calling regression):
  Salesforce/xlam-function-calling-60k (APIGen), APIGen-MT (multi-turn),
  NousResearch/hermes-function-calling-v1, THUDM/AgentInstruct.
  Note: these are mostly single-turn API calls — distribution differs
  significantly from multi-step file/shell environments.

## Evaluation Strategy

1. **Primary**: reserved test skeletons (50–100), never used in prompt tuning.
2. **External reference** (optional): BFCL multi-turn subset for general tool-use
   regression check. Terminal-Bench is closest to the environment but requires
   Docker. τ-bench is customer-service oriented, limited reference value.
   Always report as "locally adapted subset, not official scores."
3. **Regression check**: IFEval subset or general QA to confirm the model
   hasn't degraded.

## Evaluation Backend

For fair comparison: same HF checkpoint, same backend, same precision, only
comparing adapter on/off. vLLM with `--enable-lora` for both rollout and eval
is ~10x faster than llama.cpp. Requires an OpenAI-compatible backend
implementation and exact token-level consistency between training chat/tool
templates and inference.

## Recursive Self-Improvement (RSI)

RSI strictly means: after system improvement, the *ability to improve itself*
also becomes stronger. Score improvement alone ≠ RSI.

### Classification

| Category | Examples | What is improved | Is it RSI? |
|----------|----------|------------------|------------|
| Model self-training loop | STaR, ReST/ReST-EM, expert iteration, Self-Rewarding LM, SPIN, R-Zero | Model weights: M_t → M_{t+1} | Yes |
| Agent improves training code | GEPA, Dream-RSI, ModularRSI, RRSI | Another object (algorithm, training code) | Usually no |
| Automated research | Karpathy's autoresearch | A smaller model's training recipe | No |

Karpathy's autoresearch: a fixed strong model agent modifies a small LLM's
training script per `program.md`, limited to ~5 min per experiment. Metric
(val_bpb) improves → keep; degrades → git revert. The research agent itself
doesn't improve, so it's "automated research + hill-climbing search," not RSI.
Its value is the experimental protocol: fixed evaluator, limited modification
scope, keep/discard, experiment log, time budget.

### Reading Roadmap (4 hours)

| Time | Material | Focus |
|------|----------|-------|
| 25 min | [autoresearch](https://github.com/karpathy/autoresearch) README + program.md | Allowed modifications, fixed metrics, experiment budget, keep/discard, logging |
| 25 min | [GEPA](https://arxiv.org/abs/2507.19457) paper | Abstract, method diagram, one update instance. What information in trajectories enables effective modification? |
| 40 min | [ModularRSI](https://arxiv.org/html/2609.14857v1) + [RRSI](https://arxiv.org/html/2609.24972v2) | §3 of each. Module boundaries, success/failure comparison, overfitting, candidate selection |
| 65 min | [Dream-RSI](https://dream-rsi.com/) demo + [paper](https://arxiv.org/html/2609.14858v1) | Demo 10 min; §2–3 ~30 min; §4–5 ~25 min. Skip domain algorithm details and long code appendices |
| 35 min | [STaR](https://arxiv.org/abs/2203.14465) + skim [NeoHorse-1](https://arxiv.org/abs/2609.08183) | Generate→verify→train→new model generates again; how recent work preserves tool trajectories and harness context for training |
| 50 min | Design your own experiment | Define: what is being improved, what is the fixed evaluator, what is the modification budget |

## Sources

- [Post-Training (Yuque)](https://www.yuque.com/shakewin/xhs6fk/enzhwl32t9wfe9ib)

<!-- BEGIN GENERATED OBSIDIAN LINKS -->
## Obsidian relationships

- Prerequisites: [[pretraining|Language-Model Pretraining]], [[supervised-fine-tuning|Supervised Fine-Tuning]]
- Enables: [[rlhf|Reinforcement Learning from Human Feedback]], [[direct-preference-optimization|Direct Preference Optimization]], [[group-relative-policy-optimization|Group Relative Policy Optimization]], [[knowledge-distillation|Knowledge Distillation]], [[recursive-self-improvement|Recursive Self-Improvement]]
- Contrasts with: [[pretraining|Language-Model Pretraining]]

<!-- END GENERATED OBSIDIAN LINKS -->
