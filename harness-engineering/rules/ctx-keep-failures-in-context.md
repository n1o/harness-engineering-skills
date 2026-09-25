# ctx-keep-failures-in-context

> Leave failed actions, error observations, and stack traces in the context; erasing them removes the evidence the model needs to shift its prior away from repeating the mistake.

## Why It Matters

- Common anti-pattern: cleaning up the trace, retrying silently, or resetting state and hoping temperature fixes it — "erasing failure removes evidence; without evidence, the model can't adapt."

- Seeing a failed action plus its observation/stack trace implicitly updates the model's beliefs and reduces the chance of the same error again.

- Error recovery is one of the clearest indicators of true agentic behavior, yet is underrepresented in benchmarks that test success under ideal conditions.

## Scope

- Apply by default: leave the failed action plus its observation/stack trace in context so the model's beliefs update and it doesn't repeat the error.

- The boundary is spin: once the agent loops on the same failure, keeping more copies no longer teaches — bound retries and restructure the error context instead.

- Skip for non-informative failure spew (cascading duplicate errors from one root cause): keep the root cause, gate the noise.

## Source

Manus (https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus)

## See Also

- [prin-compact-errors-bounded-retries](prin-compact-errors-bounded-retries.md) - boundary: this rule keeps failures in-context so the model learns from them; that one bounds retries and compacts/removes error context once the agent spins on the same failure — keep first, compact on breach.

- [ctx-deterministic-output-backpressure](ctx-deterministic-output-backpressure.md) - failure output still arrives in full; it's green-run noise that gets gated to `✓`.
