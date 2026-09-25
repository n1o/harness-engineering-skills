# struct-backpressure-verification-gates

> Wire verification into the loop as mechanical backpressure the agent must satisfy each iteration — run the tests for the unit just changed, use static analyzers for dynamic languages, and commit/tag only on green.

## Why It Matters

- Standing instruction: "After implementing functionality or resolving problems, run the tests for that unit of code that was improved" — per-unit, per-loop, not a big-bang test run at the end

- For dynamically typed languages, wire in a static analyzer/type checker (Ralph names dialyzer, pyrefly) or "you will run into a bonfire of outcomes"; type systems and linters are backpressure that rejects invalid generation without model judgment

- Anything can serve as backpressure — security scanners, static analyzers — "but the key collective sum is that the wheel has got to turn fast" (Rust's compile cost vs. correctness is an explicit tradeoff to weigh, not a default)

- Persist verified progress mechanically: "when the tests pass... git commit... git push", and "as soon as there are no build or test errors create a git tag" — the git history becomes the loop's checkpoint series, enabling `git reset --hard` recovery to the last good state

- Anti-example the source names: models are "trained to chase their reward function, and the reward function is compiling code", so expect placeholder implementations until an explicit no-stub/no-placeholder contract plus tests pushes back

## Scope

- Apply inside any agent coding loop: run the tests for the unit just changed each iteration, wire static analyzers/type checkers for dynamic languages, commit/tag only on green.

- Backpressure must stay fast — "the wheel has got to turn fast"; weigh each checker's cost against correctness explicitly (Rust's compile cost vs. correctness is a tradeoff to weigh, not a default).

- Expect placeholder implementations until an explicit no-stub/no-placeholder contract plus tests pushes back — the reward function is compiling code.

- **When to skip**: Applies to any loop that writes code; skip only for read-only analysis loops with nothing to gate.

## Source

Ralph (https://ghuntley.com/ralph/)

## See Also

- [struct-deterministic-exit-code-gates](struct-deterministic-exit-code-gates.md) - the boundary: this rule is tests-as-backpressure the loop negotiates with each iteration; that rule is hooks-as-hard-gates (exit non-zero) the model can't talk past
- [ver-in-loop-internal-quality](ver-in-loop-internal-quality.md) - type systems and tests pass while semantic damage accumulates — backpressure must include convention checks
- [struct-bounded-single-task-loop](struct-bounded-single-task-loop.md) - the loop this backpressure lives inside, one task per fresh iteration
