# ver-harness-deltas-measured-by-evals

> Measure every harness change as an eval delta with the model held fixed — and use automated trace analysis as the outer improvement loop that proposes the changes.

## Why It Matters

- LangChain improved their coding agent 13.7 points (52.8 → 66.5) on Terminal Bench 2.0 changing *only* the harness, model fixed (gpt-5.2-codex) — evidence that harness deltas are first-class, benchmark-visible improvements.

- Improvement loop (the "Trace Analyzer Skill"): fetch experiment traces, spawn parallel error-analysis agents, synthesize findings, make targeted harness changes — boosting-style, focusing on previous mistakes. A human verifies proposed changes (watch for changes that overfit one task and regress others).

- Compress the optimization space to three knob families — system prompt, tools, middleware — and evaluate each change against the benchmark (e.g. reasoning-budget "sandwich": xhigh planning, high build, xhigh verification scored 66.5% vs 53.9% for all-xhigh, which timed out).

- Tailor the harness per model: the same harness scored competitively-but-worse on Claude Opus 4.6 because the improvement loop hadn't been run for it — principles generalize, but iterations are model-specific.

- Frameworks make this loop runnable: Harbor orchestrates sandboxes, agent interaction, verification, and scoring; Inspect provides task/dataset/solver/scorer decomposition, sandboxes, a log viewer, and offline re-scoring of saved logs so harness changes can be re-evaluated without re-running agents.

## Scope

- Apply to every harness change — system prompt, tools, middleware — measured as an eval delta with the model held fixed; harness deltas are benchmark-visible (13.7 points in the source's run).

- A human verifies proposed changes in the loop: watch for changes that overfit one task and regress others.

- Iterations are model-specific — the same harness scored worse on a model the improvement loop hadn't been run for; skip the full loop for quick fixes you can A/B on a handful of tasks.

## Source

LangChain 'Improving Deep Agents with harness engineering' (https://blog.langchain.com/improving-deep-agents-with-harness-engineering/)

## See Also

- [struct-harness-as-declared-config](struct-harness-as-declared-config.md) - declared, versioned config is what makes two harness states diffable so the delta is well-defined
- [eval-capability-vs-regression-suites](eval-capability-vs-regression-suites.md) - the regression suite is what catches a harness change that fixes one task and regresses others
- [eval-trace-to-deterministic-checks](eval-trace-to-deterministic-checks.md) - the trace analysis that proposes which harness change to try
- [obs-runtime-config-first-class-variable](obs-runtime-config-first-class-variable.md) - infra noise is the confound to hold fixed while measuring a harness delta
