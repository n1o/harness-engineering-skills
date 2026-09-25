# eval-read-transcripts

> Don't take eval scores at face value: read transcripts from many trials to verify graders are measuring what matters — the verifier says whether you won, the trace says why and what to fix.

## Why It Matters

- When a task fails, the transcript distinguishes a genuine agent mistake from a grader rejecting a valid solution; failures should seem fair — clear what the agent got wrong and why.

- Anthropic's rule: no eval score is trusted until someone digs into details and reads transcripts — unfair grading, ambiguous tasks, penalized valid solutions, or over-constraining harnesses mean the eval must be revised.

- Trace inspection after the first eval round reveals the fixable patterns: unnecessary exploration in baseline runs, clean direct workflows when guidance works, overconstraint or brittle recovery when it doesn't.

- Production observability (OTEL-compatible tracing, tools like Laminar/LangSmith) serves this loop without locking the eval to one tracing stack.

## Scope

- Apply to every eval round, especially failures and surprising passes — the verifier says whether you won, the trace says why and what to fix.

- No eval score is trusted (per the source) until someone digs into transcripts; unfair grading, ambiguous tasks, penalized valid solutions, or over-constraining harnesses mean the eval must be revised.

- Scales with tooling (OTEL-compatible tracing, Laminar/LangSmith-class tools) — but the reading itself stays manual judgment, so budget it for eval rounds, not every run.

## Source

Anthropic 'Demystifying Evals for AI Agents' (https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents); OpenHands 'How to Evaluate Agent Skills' (https://openhands.dev/blog/evaluating-agent-skills)

## See Also

- [eval-unambiguous-tasks-reference-solutions](eval-unambiguous-tasks-reference-solutions.md) - the two ways an eval is broken: bad task vs bad grader; transcripts reveal which
- [eval-combine-grader-types](eval-combine-grader-types.md) - transcript findings are what calibrate graders and justify adding model judges
- [eval-trace-to-deterministic-checks](eval-trace-to-deterministic-checks.md) - turn recurring transcript observations into deterministic checks
- [ver-train-verifiers-on-production-traces](ver-train-verifiers-on-production-traces.md) - the production-trace counterpart of this benchmark-transcript discipline
