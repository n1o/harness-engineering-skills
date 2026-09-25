# ctx-context-occupancy-transparency

> Instrument and expose what is taking up how much space in the context window — occupancy transparency is a required harness feature for navigating the size budget.

## Why It Matters

- Even huge windows don't make indiscriminate dumping fine: effectiveness drops and tokens cost money; developers need visibility into which configured context (rules, skills, MCP, history) occupies the budget.

- Fowler cites Claude Code's `/context` command as the model: a breakdown of what consumes the window, so engineers can prune configuration.

- Build rule/context configurations up gradually and prune as models improve — instructions necessary a year ago may be dead weight today; there are no unit tests for context engineering, so iterate against observed occupancy and outcomes.

## Scope

- Apply once a harness carries non-trivial configured context — rules files, skills, MCP tool definitions, history: developers need the occupancy breakdown (the `/context`-command model) to know what to prune.

- Skip when total configured context is trivially small; measurement only pays when the budget is contested.

- Treat the numbers as iteration input, not one-time audit — there are no unit tests for context engineering, so re-check occupancy as models improve and drop instructions that are dead weight today.

## Source

Martin Fowler, "Context Engineering for Coding Agents" (https://martinfowler.com/articles/exploring-gen-ai/context-engineering-coding-agents.html)

## See Also

- [ctx-working-memory-budget](ctx-working-memory-budget.md) - the budget this rule makes visible: occupancy transparency is the measurement instrument, the budget rule is the target.

- [ctx-instruction-file-minimal-universal](ctx-instruction-file-minimal-universal.md) - the always-loaded file is the first thing this measurement should flag when it grows.

- [ctx-just-in-time-retrieval](ctx-just-in-time-retrieval.md) - the main remedy for occupancy problems: keep references, load contents at runtime.
