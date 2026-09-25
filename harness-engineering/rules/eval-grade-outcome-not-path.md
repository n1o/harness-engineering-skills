# eval-grade-outcome-not-path

> Grade what the agent produced, not the exact path it took; rigid step-sequence checks punish valid unanticipated solutions.

## Why It Matters

- The common instinct — assert a precise sequence of tool calls in order — is too rigid and brittle: agents regularly find valid approaches eval designers didn't anticipate.

- Alternative that preserves signal: assert that a required tool was called at some point, or verify the end state, rather than the ordering.

- Frontier models can legitimately exceed the eval (Opus 4.5 "failed" a tau2-bench flight-booking task by finding a policy loophole that was a better outcome for the user).

- Build in partial credit for multi-component tasks: an agent that identifies the problem and verifies the customer but fails the refund is meaningfully better than one that fails immediately — represent the continuum of success.

- Scoring per task can be weighted (combined grader scores vs threshold), binary (all pass), or hybrid.

## Scope

- Apply to open-ended tasks where valid solutions vary; assert a required tool was called at some point, or verify the end state, instead of exact orderings.

- Skip outcome-only grading where the path is itself the contract (least-privilege and permission-escalation regressions are path questions by nature).

- Use partial credit for multi-component tasks so near-misses aren't indistinguishable from immediate failures.

## Source

Anthropic 'Demystifying Evals for AI Agents' (https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)

## See Also

- [eval-trace-to-deterministic-checks](eval-trace-to-deterministic-checks.md) - deterministic checks over trace events; the boundary is keeping them from hardening into rigid path-sequence assertions
- [eval-tier-by-scope](eval-tier-by-scope.md) - single-step evals test one decision point; outcome grading belongs to full runs
- [eval-bespoke-assertions-per-case](eval-bespoke-assertions-per-case.md) - per-case criteria are where the outcome/process mix gets decided
