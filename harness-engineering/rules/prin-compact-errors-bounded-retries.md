# prin-compact-errors-bounded-retries

> Feed tool errors back into the context window so the agent can self-heal, but bound retries deterministically and restructure/remove error context when the agent spins.

## Why It Matters

- LLMs are good at reading an error message or stack trace and adjusting the next tool call — this is the cheapest self-healing mechanism and works standalone.

- Implement a consecutive-error counter per tool call (~3 attempts); on breach, break the loop: reset parts of the context window, escalate to a human via tool call, or take deterministic control.

- Doing error-feeding "TOO much" makes the agent repeat the same error over and over — the harness owns how errors are represented: compact them, drop prior failed events, or rewrite context to get back on track.

- Consider hiding resolved errors and failed calls from context entirely once they no longer inform the next step.

## Scope

- Apply to any harness that runs tool calls in a loop: feed errors back for self-healing, but keep a per-tool consecutive-error counter (the source's default is ~3 attempts, not a law) and act on breach.
- On breach, the harness — not the model — owns the response: reset parts of the context window, escalate to a human via tool call, or take deterministic control.
- Error-feeding needs no machinery; the counter and restructuring earn their keep only where an agent can spin — if retry volume is already bounded fleet-wide (ops-shared-retry-budget), this rule's job is the single agent's loop, not the fleet's economics.

## Source

HumanLayer, "12 Factor Agents" (https://www.humanlayer.dev/blog/12-factor-agents)

## See Also

- [ops-shared-retry-budget](ops-shared-retry-budget.md) - boundary: this rule's per-tool counter bounds one agent's spin; the shared budget bounds fleet-wide retry economics — they compose, catching different waste
- [ctx-keep-failures-in-context](ctx-keep-failures-in-context.md) - boundary: keep the failure and its stack trace visible while it is unresolved evidence; this rule's hiding/removal applies only once errors no longer inform the next step
- [ver-layered-verification-stack](ver-layered-verification-stack.md) - loop-detection middleware injecting "reconsider your approach" after N repeats is the same deterministic spin-breaker at trajectory level
- [run-unify-state-own-your-context](run-unify-state-own-your-context.md) - same 12FA source: owning the context format includes deciding how errors are represented and which failed calls stay
