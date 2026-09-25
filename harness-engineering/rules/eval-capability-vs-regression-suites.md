# eval-capability-vs-regression-suites

> Run two kinds of suites: capability evals that start at a low pass rate (a hill to climb) and regression evals near 100% that guard against backsliding — and graduate saturated tasks between them.

## Why It Matters

- Capability/quality evals target tasks the agent struggles with; regression evals verify the agent still handles everything it used to.

- As capability evals saturate, graduate them into the continuously-run regression suite: "can we do this at all?" becomes "can we still do this reliably?"

- Watch for eval saturation: near 100% an eval tracks regressions but gives no improvement signal, and large capability gains show up as tiny score deltas (Qodo initially underestimated Opus 4.5 because their one-shot evals didn't capture long, complex tasks; a new agentic eval framework revealed the progress).

- Descript-style teams run two separate suites on cadence: one for quality benchmarking, one for regression testing.

## Scope

- Apply once an eval program is mature enough to run two suites on cadence; the source's Descript-style teams maintain the split because they have saturated work to protect.

- Graduate capability evals into the regression suite as they saturate — near 100% an eval tracks regressions but gives no improvement signal, and large capability gains show up as tiny score deltas.

- Skip the split when nothing is near saturation yet; a single suite that is still climbing is all capability signal.

## Source

Anthropic 'Demystifying Evals for AI Agents' (https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)

## See Also

- [eval-start-small-grow-from-real-failures](eval-start-small-grow-from-real-failures.md) - the suite lifecycle that precedes this split: small start, grow as effect sizes shrink
- [eval-pass-at-k-vs-pass-cubed-k](eval-pass-at-k-vs-pass-cubed-k.md) - a saturated regression suite still needs multi-trial reporting to stay meaningful under non-determinism
- [ver-harness-deltas-measured-by-evals](ver-harness-deltas-measured-by-evals.md) - the regression suite is the instrument that catches harness changes which fix one task and regress others
