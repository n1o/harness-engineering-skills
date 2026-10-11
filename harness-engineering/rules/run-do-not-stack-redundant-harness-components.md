# run-do-not-stack-redundant-harness-components

> Harness component gains are not additive: when multiple components encode the same mitigation (e.g., several layers all pushing toward closure-style verification), stacking them spends the finite turn budget on redundant re-checks — evaluate components jointly, not one at a time in isolation.

## Why It Matters

- In the AHE observability-driven evolution loop on Terminal-Bench 2, the three positive single-component gains sum to +11.1pp while full AHE with all components combined yields only +7.3pp; on the Hard slice, the memory-only variant exceeds the full stack — memory, middleware, and system prompt all push toward the same closure-style verification, so together they spend turns on redundant re-checks within the long-horizon budget (Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses, arXiv 2604.25850).
- The components of an agent interact through a shared finite budget — context window and turn count — so a second component mitigating an already-mitigated failure mode pays its cost (tokens, turns, latency) for near-zero marginal benefit (arXiv 2604.25850).
- Aggregative evolution optimizes the mean over a task mix (in AHE, 55 Medium tasks dominate) and converges to that mix's trade-off, giving back part of a component's effect on harder slices — another reason per-component wins measured separately cannot be extrapolated to the stack (arXiv 2604.25850).
- This is the quantitative counterpart to [run-harness-component-attrition-on-model-upgrade](run-harness-component-attrition-on-model-upgrade.md): attrition removes components whose assumptions expired; this rule refuses to *add* components whose job is already done.

## Scope

- Apply when composing a harness from multiple independently-motivated components (memory files, middleware, prompt sections, verification layers): before shipping the union, measure the stack end-to-end, and check for components that mitigate the same failure class.
- Distinguish two failure shapes: *redundancy* (components overlap, net gain < sum of parts — merge or drop one) from *true interaction* (components conflict on a shared budget trade-off — pick per task mix). The AHE evidence covers both; interaction-aware evolution remains open.
- The one-at-a-time, measure-each-change discipline of [ver-harness-deltas-measured-by-evals](ver-harness-deltas-measured-by-evals.md) and [run-incremental-one-feature-at-a-time](run-incremental-one-feature-at-a-time.md) is for *attribution during development*; this rule governs the *shipping decision* — the union of individually-green components must itself pass the eval before cutover.
- Skip for components on disjoint resources (e.g., a sandbox guard and a context compactor) — no shared-budget interaction to worry about.

## Source

Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses (https://arxiv.org/abs/2604.25850)

## See Also

- [run-harness-component-attrition-on-model-upgrade](run-harness-component-attrition-on-model-upgrade.md) - removal-side counterpart: strip components that stopped earning their cost
- [ver-harness-deltas-measured-by-evals](ver-harness-deltas-measured-by-evals.md) - the measurement discipline; this rule adds that the final union also needs its own delta
- [eval-capability-vs-regression-suites](eval-capability-vs-regression-suites.md) - per-slice results (Hard vs Medium) diverge; gate the stack on each slice you care about
- [prin-simplest-solution-that-works](prin-simplest-solution-that-works.md) - the prescriptive ancestor: don't add complexity without demonstrated joint benefit
