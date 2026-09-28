# run-harness-optimization-per-model

> Key harness optimization to (model, task-domain) pairs: re-run the improvement loop for each new base model instead of transplanting harnesses, because failure modes are model-specific.

## Why It Matters

- Identical weights, different harness: GPT-5 solves 35.2% of Terminal-Bench 2.1 inside Terminus 2 but 49.6% inside Codex CLI — a 14.4pp gap attributable to the harness alone (HarnessDev, arXiv 2609.01437).
- Each model needs different edits: MiniMax M2.5 needed early-artifact-creation rules and a loop breaker after 50 tool calls; Qwen3.5-35B-A3B needed dependency-prechecking and retry middleware; GLM-5 needed verification of persistent environment changes (e.g., PATH edits). One model's fix is another model's noise (Self-Harness, arXiv 2606.09498).
- Transplants help but must be re-measured: a GPT-5.3-Codex-derived harness transfers to six other models on Terminal-Bench with mean +0.098, but the range is +0.038 to +0.233 — averages hide model-specific variance (MemoHarness, arXiv 2607.14159).
- Mechanism activation degrades on unseen models: SoL-Pi's efficiency mechanisms keep working on a newer Opus model (44.7% token-traffic reduction retained) but at lower activation rates and intensities, which the authors attribute to overfitting the search backend (SoL-Pi, arXiv 2609.20519).
- The per-model harness is a first-class performance lever: Self-Harness lifted Qwen3.5-35B-A3B on SWE-bench Verified from 19.5% to 41.5% (+113% relative) with zero weight changes (Self-Harness, arXiv 2606.09498).

## Scope

- Apply when switching or upgrading base models, porting harnesses between models, deciding between one shared harness and per-model variants, or interpreting cross-model harness-transfer claims.
- Skip for deliberately model-agnostic infrastructure (sandboxing, audit logging, budgets) — those must not vary per model.
- If the budget is too small to re-run the loop, at minimum re-measure the transplanted harness on the new model before trusting it.

## Source

Self-Harness (https://arxiv.org/abs/2606.09498), HarnessDev (https://arxiv.org/abs/2609.01437), MemoHarness (https://arxiv.org/abs/2607.14159), SoL-Pi (https://arxiv.org/abs/2609.20519)

## See Also

- [run-harness-component-attrition-on-model-upgrade](run-harness-component-attrition-on-model-upgrade.md) - that rule prunes components models outgrow; this rule re-derives the components a new model still needs
- [ver-harness-deltas-measured-by-evals](ver-harness-deltas-measured-by-evals.md) - the measurement protocol underlying per-model re-optimization
- [obs-runtime-config-first-class-variable](obs-runtime-config-first-class-variable.md) - infrastructure config as an experimental variable of comparable magnitude
- [eval-pin-harness-with-model](eval-pin-harness-with-model.md) - the reporting duty on the other side: pin (model, harness) pairs in every eval

- [ver-self-edit-non-regression-gate](ver-self-edit-non-regression-gate.md) - every edit this per-model loop proposes must pass that gate before acceptance