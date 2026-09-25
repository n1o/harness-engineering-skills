# run-harness-component-attrition-on-model-upgrade

> Every harness component encodes an assumption about what the model can't do on its own — stress-test those assumptions and remove components that are no longer load-bearing when models improve, one at a time.

## Why It Matters

- The source's radical-cut attempt to simplify the harness failed and made it impossible to tell which pieces were load-bearing; the methodical approach — remove one component at a time, review the impact — worked.

- Concrete example: the sprint construct was removed once Opus 4.6 could natively sustain 2+ hour builds; the planner and evaluator were kept because each still added visible value.

- The evaluator becomes a cost/benefit decision, not a fixed yes/no: it's worth it when the task sits beyond what the current model does reliably solo; as the capability boundary moves outward, it becomes overhead for in-boundary tasks but keeps lifting edge-of-capability work.

- Matches the "find the simplest solution possible, and only increase complexity when needed" principle; the space of useful harness combinations doesn't shrink as models improve, it moves.

## Scope

- Apply on model upgrades (or any capability shift): every component encodes an assumption about what the model can't do solo — stress-test those assumptions and remove components that are no longer load-bearing.
- Method matters: one component at a time with impact review — the source's radical-cut attempt failed and made it impossible to tell which pieces were load-bearing.
- Per-component, not all-or-nothing: the evaluator stays a cost/benefit call — worth it beyond what the model does reliably solo, overhead for in-boundary tasks, still lifting edge-of-capability work; the useful-combination space moves outward, it doesn't shrink.

## Source

Anthropic, "Harness design for long-running application development" (https://www.anthropic.com/engineering/harness-design-long-running-apps); Anthropic, "Building effective agents" (https://www.anthropic.com/engineering/building-effective-agents)

## See Also

- [prin-simplest-solution-that-works](prin-simplest-solution-that-works.md) - boundary: simplicity-first at design time vs attrition on model upgrades — the source cites the same principle, but this rule starts minimal while attrition keeps the harness honest as capability boundaries move
- [ver-harness-deltas-measured-by-evals](ver-harness-deltas-measured-by-evals.md) - how to review impact objectively: harness deltas measured as eval changes with the model fixed, not by feel
- [ver-layered-verification-stack](ver-layered-verification-stack.md) - same "temporary engineering" stance: process guardrails are explicitly built around current model weaknesses and likely dissolve as models improve

