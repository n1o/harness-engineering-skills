# ops-realized-numbers-only-for-escalation

> Require agents requesting more budget to cite realized ledger numbers, never projections; silence means no.

## Why It Matters

- Define what a budget-increase request must contain *before* the agent needs to ask: exact dollar amount, current spend-to-return ratio from the ledger, and the specific number that justifies it — no spend without an explicit reply naming the new amount.

- An agent motivated to keep working will always produce an optimistic projection; only money already spent and results already measured survive contact with an agent that wants to say yes to itself.

- This makes escalation mechanical: a human approving sees facts, not persuasion.

## Scope

- Apply to every budget-increase request in an autonomous spending loop: define before the agent needs to ask what the request must contain — exact amount, current spend-to-return ratio from the ledger, the specific realized number that justifies it — and require an explicit reply naming the new amount.
- The point is adversarial: an agent motivated to keep working will always produce an optimistic projection, so only realized numbers survive; this shapes escalation requests, it does not replace the caps themselves.
- Silence means no — the rule presupposes a pre-existing escalation threshold (e.g., the three-number rails) that gives the agent something to escalate from and a human to answer.

## Source

Spend rails for autonomous agents (https://joeyycli.github.io/agent-ops-kit-guide/docs/spend-rails-for-autonomous-agents.html)

## See Also

- [ops-three-number-spend-rails](ops-three-number-spend-rails.md) - family: the rails define the autonomy line and threshold being escalated; this rule governs the escalation request itself
- [ops-ledger-is-the-enforcement-mechanism](ops-ledger-is-the-enforcement-mechanism.md) - family: the realized numbers cited in a request are only trustworthy because the ledger records them the moment they're learned of
- [guard-audit-log-every-decision](guard-audit-log-every-decision.md) - the same decisions-as-evidence posture: approvals and denials become reviewable artifacts, not vibes
- [prin-humans-on-the-loop-not-in-it](prin-humans-on-the-loop-not-in-it.md) - the human's role in this gate: responding to a mechanical escalation with facts, not inspecting every artifact
