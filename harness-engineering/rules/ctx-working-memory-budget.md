# ctx-working-memory-budget

> Treat the context window as a finite attention budget with diminishing returns — engineer for the smallest set of high-signal tokens that achieves the outcome, not for "fits in the window".

## Why It Matters

- Context rot is real across all models: as token count grows, recall and long-range reasoning degrade (n² attention relationships stretched thin); degradation is a gradient, not a cliff.

- The engineering goal is the minimal token set that fully outlines expected behavior — "minimal" does not mean "short"; include what's needed, cut what's noise.

- Operate in the model's "smart zone" (~75k tokens for Claude-class models per HumanLayer); HumanLayer targets 40–60% window utilization for complex work.

- Anti-example from HumanLayer: a green jest/pytest run dumping 200+ lines burns 2–3% of the window to convey an "all good" that costs <10 tokens as `✓`.

## Scope

- Apply whenever content competes for the window — context rot is a gradient across all models (recall and long-range reasoning degrade as tokens grow), so engineer for the smallest high-signal set, not "fits in the window".

- "Minimal" is not "short": include what's needed, cut what's noise — the goal is the minimal token set that fully outlines expected behavior.

- The ~75k smart-zone figure and 40–60% utilization targets are HumanLayer's measured defaults for Claude-class models, not universal constants — re-derive for your model and task, and skip the aggressive pruning when recall of long-range detail is the priority and the budget allows.

## Source

Anthropic, Effective context engineering for AI agents (https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents); HumanLayer, Context-Efficient Backpressure (https://www.humanlayer.dev/blog/context-efficient-backpressure)

## See Also

- [ctx-context-occupancy-transparency](ctx-context-occupancy-transparency.md) - you can't hold this budget without measuring what occupies it; that rule is the required instrumentation.

- [ctx-deterministic-output-backpressure](ctx-deterministic-output-backpressure.md) - the deterministic enforcement side of the same anti-noise stance (green runs as `✓`, not 200+ lines).

- [ctx-subagent-context-isolation](ctx-subagent-context-isolation.md) - the structural escape valve: when the budget won't fit the work, move it to another window.
