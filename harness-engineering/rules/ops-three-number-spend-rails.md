# ops-three-number-spend-rails

> Give a spending agent three hard numbers, not one: a per-transaction autonomy line, an escalation threshold, and a lifetime ceiling.

## Why It Matters

- Below the autonomy line (e.g., $25/purchase) the agent buys and logs, no approval loop; at or above it, or for any *new recurring charge*, the agent stops, asks, and does other work while waiting — it must not idle burning session time on a blocked item.

- The lifetime ceiling is a hard outer bound the agent can never increase — only a human, in writing, can (e.g., a prepaid card with a fixed cap).

- The gap between the line and the ceiling is where autonomy lives: skip the middle number and you've built a light switch, not a rail.

- Treat recurring charges (subscriptions) as a different risk class from one-offs: they keep costing money after the session ends.

- Give fast-compounding categories their own sub-cap carved out of the ceiling (e.g., "Ads budget: $50 lifetime, hard cap; campaigns capped at the per-transaction line") so a bad ad campaign can't eat the buffer meant for everything else.

- The goal is containment, not better judgment: the worst a single unattended decision can cost is bounded and known in advance.

## Scope

- Apply to any agent that spends money autonomously: three hard numbers, not one — a per-transaction autonomy line (e.g., $25/purchase), an escalation threshold, and a lifetime ceiling only a human can raise in writing; the gap between line and ceiling is where autonomy lives.
- Carve out sub-caps for fast-compounding categories (e.g., an ads budget under the ceiling) and treat recurring charges as a distinct risk class from one-offs — subscriptions keep costing after the session ends.
- The goal is containment, not better judgment: proportion the numbers to how expensive a worst-case unattended decision would be; a purely informational (read-only) agent needs no rails at all.

## Source

Spend rails for autonomous agents (https://joeyycli.github.io/agent-ops-kit-guide/docs/spend-rails-for-autonomous-agents.html)

## See Also

- [ops-ledger-is-the-enforcement-mechanism](ops-ledger-is-the-enforcement-mechanism.md) - family: the three numbers are the caps; the ledger is what makes them enforceable
- [ops-realized-numbers-only-for-escalation](ops-realized-numbers-only-for-escalation.md) - family: what an agent must show (realized ledger numbers, never projections) to move the escalation threshold
- [guard-pre-action-deterministic-authorization](guard-pre-action-deterministic-authorization.md) - enforcement shape: a hard numeric rail is only real if checked deterministically per action, not trusted to model judgment
- [prin-humans-on-the-loop-not-in-it](prin-humans-on-the-loop-not-in-it.md) - only a human, in writing, can raise the ceiling — the human holds the outer gate, not every purchase
