# ver-self-edit-non-regression-gate

> In an automated harness-improvement loop, accept a proposed harness edit only if it regresses on neither a held-in development split nor a held-out split and improves on at least one — and keep every rejected edit logged.

## Why It Matters

- Self-Harness's conservative acceptance rule (Δ_held-in ≥ 0 AND Δ_held-out ≥ 0 AND max(Δ) > 0, evaluated with 2 attempts per task) produced consistent gains across all nine model–benchmark combinations: the largest absolute gain was +40.6pp (GLM-5 on AppWorld, 44.4%→85.0%) and the largest relative gain +132% (Qwen3.5-35B-A3B on AppWorld, 22.5%→52.2%), with held-out gains (e.g., 20.0%→44.4%) confirming generalization rather than split overfitting (Self-Harness, arXiv 2606.09498).
- Without a gate, evolution degrades over time: Evo-Bench observes "early saturation" — evolvers rapidly discover high-quality harness structures, then introduce detrimental modifications in later rounds; Qwen3.7-Max improves Overall (+11.8) while regressing Office tasks (−0.6) (Evo-Bench, arXiv 2608.09096).
- Greedy acceptance loses to keeping alternatives: in the Darwin Gödel Machine ablation, always selecting the best-performing parent reaches 39.7% on SWE-bench versus 50.0% for archive-based selection with a novelty bonus, and removing open-ended exploration drops it to 23.0% (DGM, arXiv 2505.22954).
- Minimality matters as much as the gate: Self-Harness constrains the proposer to minimal edits (a single instruction or tool) targeting one clustered failure signature, preserving unrelated harness behaviors — so regressions stay attributable and reversible (Self-Harness, arXiv 2606.09498).
- The measured trade-off: Self-Harness itself notes the non-regression rule rejects beneficial trade-off edits (one split up, other down); accept that conservatism as the price of never shipping a regression from an unattended loop (Self-Harness, arXiv 2606.09498).
- Automated loops with validation beat manual tuning at scale: AutoSaddler's offline mini-batch loop reaches 62.0±1.2 on GAIA2 (vs 53.0±1.5 default) and 50.0±0.0 on Terminal-Bench 2.0 (vs expert-tuned Terminus KIRA 47.5±2.5) — the acceptance criterion, not the search machinery, is the load-bearing part (AutoSaddler, arXiv 2608.23041).

## Scope

- Apply to self-improving harness loops where an agent edits its own prompts/tools/middleware under a verifier signal; prompt-optimization pipelines; any automated mutation of harness configuration.
- This rule governs *acceptance* in unattended loops (split deltas decide, no human in the accept path). Loops with human-verified acceptance follow `ver-harness-deltas-measured-by-evals` ("A human verifies proposed changes"); when both could apply, the unattended gate is the floor and human review may still override it.
- Skip for one-off human harness edits reviewed directly by an engineer — `ver-harness-deltas-measured-by-evals` covers measurement there.
- Loops with no held-out tasks: treat accepted edits as provisional; the gate's generalization guarantee does not exist without a held-out split.
- State whether gate deltas are pass@k or pass^k (all-k-must-pass) — the two diverge sharply, and an acceptance gate is exactly where the choice binds ([eval-pass-at-k-vs-pass-cubed-k](eval-pass-at-k-vs-pass-cubed-k.md)); Self-Harness used 2 attempts per task as its measured default.

## Source

Self-Harness: Harnesses That Improve Themselves (https://arxiv.org/abs/2606.09498), with evidence from Evo-Bench (https://arxiv.org/abs/2608.09096), Darwin Godel Machine (https://arxiv.org/abs/2505.22954), AutoSaddler (https://arxiv.org/abs/2608.23041)

## See Also

- [ver-harness-deltas-measured-by-evals](ver-harness-deltas-measured-by-evals.md) - that rule measures each change as an eval delta; this rule fixes the accept/reject criterion inside the automated loop
- [eval-capability-vs-regression-suites](eval-capability-vs-regression-suites.md) - suite composition; this rule is the per-edit acceptance gate applied to that suite
- [run-harness-component-attrition-on-model-upgrade](run-harness-component-attrition-on-model-upgrade.md) - component removal decisions also need non-regression evidence
- [run-dead-end-ledger-scar-tissue](run-dead-end-ledger-scar-tissue.md) - the log of rejected edits this gate produces is the input to that ledger
- [eval-pass-at-k-vs-pass-cubed-k](eval-pass-at-k-vs-pass-cubed-k.md) - the metric choice (at least one success vs all succeed) that a 2-attempt acceptance gate must declare
- [run-harness-optimization-per-model](run-harness-optimization-per-model.md) - the per-model improvement loop whose edits must pass this gate
- [ctx-evolved-knowledge-gated-by-validation](ctx-evolved-knowledge-gated-by-validation.md) - the same-shaped gate applied to knowledge-entry admission instead of harness edits
