# prin-internalize-harness-into-model

> Once a harness mechanism is validated and stable, internalize it — distill into model weights or fold into shipped defaults — instead of letting runtime scaffolding accumulate.

## Why It Matters

- Harness-Zero distills an evolved harness into a Qwen3.5-9B student via reviewed-rollout LoRA SFT: macro-average rises 23.3%→44.3% (90.1% relative), exceeding the 41.7% the same base model reaches with the evolved harness still attached; deployment ships (model, minimal harness) alone — no evolved harness, no private reference harness, no reviewer agent (Harness-Zero, arXiv 2609.24974).
- Internalization is behavioral, not just score: distilled students recover 82.3% of 28 harness-exclusive behavior patterns on average (Harness-Zero, arXiv 2609.24974).
- Data volume does not predict distillation value: teacher rollouts with 98.6% collection success distilled to only 15.0 pass@1 on USPTO, while Harness-Zero's 59.4%-collection-success reviewed rollouts reached 30.0 — corrective signal quality, not yield, drives internalization (Harness-Zero, arXiv 2609.24974).
- The alternative — routing among an ever-growing set of specialized harnesses — incurs recurring context, model-call, tool-call, and orchestration costs on every deployment; MemoHarness's per-case retrieval mitigates but still pays these costs per task (Harness-Zero, arXiv 2609.24974; MemoHarness, arXiv 2607.14159).
- Measured caveat: internalization is incomplete in some domains — USPTO distilled performance (30.0) trails the evolved harness attached (38.0) — so keep the original mechanism documented as a fallback rather than deleting it (Harness-Zero, arXiv 2609.24974).

## Scope

- Apply when you control model training (SFT/LoRA) or shipped default prompts, and a mechanism is validated, stable, and exercised on every run.
- Skip when there is no training budget.
- Never internalize environment-specific policy — sandboxing, budgets, hard gates stay deterministic and out of the weights.
- Skip when the mechanism is changing faster than a training cycle can follow.

## Source

Harness-Zero: Harness Distillation via Agent-as-Harness (https://arxiv.org/abs/2609.24974), with motivation from MemoHarness (https://arxiv.org/abs/2607.14159)

## See Also

- [run-harness-component-attrition-on-model-upgrade](run-harness-component-attrition-on-model-upgrade.md) - removes components models outgrow; this rule moves still-needed behavior into the model itself
- [ver-harness-deltas-measured-by-evals](ver-harness-deltas-measured-by-evals.md) - the validation that must precede internalization
- [ctx-deterministic-tools-before-llm](ctx-deterministic-tools-before-llm.md) - boundary: deterministic enforcement stays deterministic; weights only absorb probabilistic behavior
- [guard-hard-policies-over-model-judgment](guard-hard-policies-over-model-judgment.md) - same boundary on the safety side
