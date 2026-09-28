# eval-pin-harness-with-model

> Pin the harness (identity, version, and configuration) as a declared experimental variable in every agent evaluation — harness choice moves pass rates by model-upgrade-scale amounts and token efficiency by up to 40x, so an unpinned harness makes any model comparison invalid.

## Why It Matters

- Controlled 3×2×50 study (Scaffold Effect, arXiv 2607.22585: 3 harnesses × 2 models × 50 Terminal-Bench Pro tasks): within a single model, harness choice shifted pass rate by 2–8pp, while swapping models within a harness shifted it 4–10pp — harness effects are the same order of magnitude as model upgrades.
- The efficiency effect dwarfs the accuracy effect: within each model, the worst harness burned 40.8–41.9x more tokens per solved task than the best (OpenCode vs Goose; 29.9x for OpenHands-SDK), versus 1.0–1.3x for the model upgrade — and the harness ordering (Goose ≪ OpenHands-SDK < OpenCode) replicated across both models. Pooled across models, the extremes span 28,142 to 1,546,977 tokens (~55x) (2607.22585).
- Failure modes are scaffold properties, not model noise: one harness averaged 2.00–2.16 no-action turns per task vs 0.20–0.30 for another (a 10x ratio replicating across models); each harness showed a distinct failure fingerprint (REASON-dominated vs VERIFY+MAX_TURNS vs TIME/HANG with zero VERIFY) (2607.22585).
- Terminal-Bench 2.0 previously documented the same confound at extreme scale: one model scored 52.1% under one harness and 57.8% under another while consuming 256.9M vs 3.9M tokens — a 65x token difference for a 5.7pp accuracy difference (cited by 2607.22585).
- The effect replicates on a second benchmark: SkillsBench (arXiv 2602.12670, 18 model-harness configurations) found the same model swinging ~8pp across scaffolds (e.g., 60.8% under one CLI vs 52.8% under another) — same weights, different scaffold.
- At n=50 one task equals 2pp, so most pairwise pass-rate differences fall inside bootstrap CIs — pinning the harness is what makes the differences you do report attributable; unpinned deltas of this size cannot be attributed to the model at all.

## Scope

- Apply to any benchmark run, leaderboard submission, model bake-off, or internal eval report — record harness name + version plus the config that drives the failure fingerprint (turn caps, wall-time caps, timeout policy, token-accounting method, no-action-turn behavior).
- Apply to cross-harness portability claims ("model X works well anywhere") — require the same model re-run under each harness before claiming it.
- Skip when comparing runs against your own prior runs on the same pinned harness (the confound is constant; still state the pin).
- Skip for fully deterministic non-agentic pipelines — there is no loop for the harness to mediate.

## Source

The Scaffold Effect in Coding Agents (https://arxiv.org/abs/2607.22585), replicated by SkillsBench (https://arxiv.org/abs/2602.12670)

## See Also

- [obs-runtime-config-first-class-variable](obs-runtime-config-first-class-variable.md) - that rule makes runtime/infrastructure config a controlled variable; this one extends the rigor to the scaffold itself as a reported confounder
- [ver-harness-deltas-measured-by-evals](ver-harness-deltas-measured-by-evals.md) - that rule measures your own harness changes; this rule is the validity precondition for any comparison you publish
- [prin-agent-equals-model-plus-harness](prin-agent-equals-model-plus-harness.md) - defines the boundary of what "harness" covers; you cannot pin what you cannot delimit
- [eval-no-skill-baseline](eval-no-skill-baseline.md) - the same paired-attribution logic applied to skills; this rule applies it to the harness
- [run-harness-optimization-per-model](run-harness-optimization-per-model.md) - the flip side: harness and model must be optimized as a pair, so evals must report them as a pair
