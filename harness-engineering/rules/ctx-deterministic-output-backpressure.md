# ctx-deterministic-output-backpressure

> Wrap noisy build/test/lint commands in a deterministic gate: on success emit only `✓ <description>`; on failure dump the full stashed output — never let the model decide what to truncate.

## Why It Matters

- Take control of output deterministically (a `run_silent`-style wrapper over pytest/jest/go test/cargo/Maven); "success = ✓, failure = full output" — the truncation decision is made once, by the harness, not re-litigated by the model every run.

- Enable fail-fast (`pytest -x`, `--bail`, `-failfast`) so the agent fixes one bug at a time instead of context-switching across five failures or re-reading the same failing-tests block.

- Iterate on noise: strip unhelpful stack frames and timing info, extract just the failed assertion; framework-specific parsers can keep test counts while dropping the spew.

- Anti-pattern: model-driven conservations like `| head -n 50` on a 5-minute suite destroys the tail of output and forces expensive re-runs; piping to /dev/null with an exit-code message can cost more tokens than the output it avoided.

- Rationale: "deterministic is better than non-deterministic — if you already know what matters, don't leave it to a model to churn through thousands of junk tokens to decide."

## Scope

- Apply to any command whose output the agent consumes each iteration — build/test/lint — where runs are frequent and mostly green: the wrapper makes one upfront decision (success = `✓ <description>`, failure = full output) instead of the model re-litigating truncation every run.

- Skip when output is small and information-dense (a single failing assertion), the command is one-shot and its full output is the deliverable, or an interactive investigation genuinely needs the noise.

- Don't let the model do the gating — no `| head -n 50` on a long suite (destroys the tail, forces re-runs) and no /dev/null-with-exit-code (can cost more tokens than it saved).

## Source

HumanLayer, Context-Efficient Backpressure (https://www.humanlayer.dev/blog/context-efficient-backpressure)

## See Also

- [struct-backpressure-verification-gates](struct-backpressure-verification-gates.md) - boundary: this rule gates command *output noise* deterministically; that one makes running verification a *loop gate* (tests for the unit just changed, commit/tag only on green) — complementary, both mechanical.

- [ctx-working-memory-budget](ctx-working-memory-budget.md) - the token economics this rule protects: a green run's 200+ lines vs a <10-token `✓`.

- [ctx-deterministic-tools-before-llm](ctx-deterministic-tools-before-llm.md) - same deterministic-over-model principle applied to enforcement (linters over prose) rather than to output truncation.
