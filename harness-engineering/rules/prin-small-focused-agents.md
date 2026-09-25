# prin-small-focused-agents

> Keep each agent small and focused — roughly 3–10, maybe 20 steps — because performance degrades as context grows; agents are one building block in a larger, mostly deterministic system.

## Why It Matters

- The core problem with "loop until you solve it": agents get lost when the context window gets too long, spinning out retrying the same broken approach; anything past 10–20 turns becomes a mess the LLM can't recover from.

- Even at 90% per-step reliability, compounding error is far from "good enough for customers" — the source's analogy: imagine a web app that crashed on 10% of page loads.

- The working pattern is micro-agents sprinkled into deterministic DAGs: LLM steps manage well-scoped task sets, which makes live human feedback easy to incorporate without context-error spirals.

- Deliberately grow agent scope only as model reliability increases, verifying quality is maintained at each size — the most magical results come from operating consistently just at the edge of model capability.

## Scope

- Apply to agents embedded in a larger system: the step figure (roughly 3–10, maybe 20) is the source's starting hypothesis to evaluate per model and task, not a universal cap — the working pattern is micro-agents sprinkled into deterministic DAGs, so the bound is on one agent's task set, not the whole job.
- Deliberately grow agent scope only as model reliability increases, verifying quality is maintained at each size; agents operating just at the edge of capability give the best results, so the right size is empirical, not doctrinal.
- Skip when a well-scoped task reliably finishes within budget — the failure mode this rule guards against (context too long, retry spirals past 10–20 turns) appears only as scope grows.

## Source

HumanLayer, "12 Factor Agents" (https://www.humanlayer.dev/blog/12-factor-agents)

## See Also

- [struct-bounded-single-task-loop](struct-bounded-single-task-loop.md) - boundary: session-level scoping here vs the outer-loop architecture there — a deterministic loop handing out one task per fresh window is the system-level design this rule's small agents fit into
- [ctx-subagent-context-isolation](ctx-subagent-context-isolation.md) - same small-window discipline applied to exploration: subagents burn tokens in their own window and return condensed summaries, keeping the lead agent small
- [run-unify-state-own-your-context](run-unify-state-own-your-context.md) - same 12FA source: agents are one building block in a mostly deterministic system whose state lives in the serializable thread
- [ctx-working-memory-budget](ctx-working-memory-budget.md) - the attention-budget rationale behind step limits: degradation is a gradient, so "small" is about tokens of working context, not only turn count
