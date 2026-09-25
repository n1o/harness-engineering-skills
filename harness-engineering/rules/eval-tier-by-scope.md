# eval-tier-by-scope

> Tier evals by scope: use trace grading while debugging behavior, then promote to repeatable datasets; within a suite, use single-step, full-run, and multi-turn evals for different questions.

## Why It Matters

- Trace grading is the fastest way to find workflow-level issues (right tool? handoff happened? policy violated?); move to datasets and eval runs once you know what "good" looks like and need repeatability for benchmarking changes.

- Single-step evals constrain the agent loop to one decision point (e.g. interrupt before the tool node) — cheap, token-saving "unit tests" for decision-making; LangChain found ~half their test cases were single-step, because regressions often occur at individual decision points, not across full runs.

- Full-run evals test end state across trajectory (a required tool was called at some point), final response (quality for open-ended tasks), and other state/artifacts (files the coding agent wrote, sources the research agent found).

- Multi-turn evals simulate user conversations but must be kept on rails: add conditional checks after each turn — if output is expected, continue to the next turn; if not, fail early — rather than naively hardcoding a full input sequence that breaks when the agent deviates.

- To test a later turn in isolation, construct a test starting from that point with appropriate initial state.

## Scope

- Apply across the whole eval lifecycle: trace grading while debugging behavior, then promote to repeatable datasets once "good" is known.

- Within a suite, mix tiers by question: single-step evals (~half of the source's cases) for decision-point regressions, full-run for end state, multi-turn for conversation — not one-size-fits-all.

- Multi-turn evals must be kept on rails with conditional per-turn checks; a hardcoded full input sequence breaks when the agent deviates, so skip multi-turn when the interaction isn't genuinely conversational.

## Source

OpenAI 'Evaluate agent workflows' (https://platform.openai.com/docs/guides/agent-evals); LangChain 'Evaluating Deep Agents: Our Learnings' (https://blog.langchain.com/evaluating-deep-agents-our-learnings/)

## See Also

- [eval-bespoke-assertions-per-case](eval-bespoke-assertions-per-case.md) - the other axis: same tiers, but success criteria vary per datapoint
- [eval-trace-to-deterministic-checks](eval-trace-to-deterministic-checks.md) - how the trace-grading tier gets operationalized
- [eval-grade-outcome-not-path](eval-grade-outcome-not-path.md) - full-run tiering still needs outcome-first grading to avoid path brittleness
