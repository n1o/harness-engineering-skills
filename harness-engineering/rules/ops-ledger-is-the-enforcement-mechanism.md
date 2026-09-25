# ops-ledger-is-the-enforcement-mechanism

> A cap without a ledger is unenforceable; the ledger and the cap must ship together, and entries must be written the moment the transaction is learned of.

## Why It Matters

- Nobody — human or model — can tell whether a cap has been hit without a record; record every transaction (revenue or expense, any amount) immediately, and keep summary totals current.

- "The moment you learn of it" is load-bearing: a transaction logged after a batch of other work is one distraction away from never being logged.

- An honest "$0 today" is a valid entry; an invented number poisons every decision made after it — a drifted ledger is worse than no ledger because it looks authoritative until someone spends real money trusting it.

- Generalizes beyond money: any quantitative rail (token budgets, retry caps, tool-call limits) needs a contemporaneous, trusted record to be an actual control.

## Scope

- Apply to every cap you expect anyone (human or model) to honor: the ledger and the cap ship together, entries are written the moment the transaction is learned of, and summary totals stay current — a record logged after a batch of other work is one distraction away from never being logged.
- Generalizes beyond money to any quantitative rail — token budgets, retry caps, tool-call limits: without a contemporaneous record the "cap" is an aspiration, so this rule is the enforcement half of every numeric limit in this set.
- An honest "$0 today" is a valid entry; an invented number poisons every later decision, and a drifted ledger is worse than none because it looks authoritative.

## Source

Spend rails for autonomous agents (https://joeyycli.github.io/agent-ops-kit-guide/docs/spend-rails-for-autonomous-agents.html)

## See Also

- [ops-three-number-spend-rails](ops-three-number-spend-rails.md) - family: the three hard numbers are the caps; this rule is the record that makes them enforceable at all
- [ops-realized-numbers-only-for-escalation](ops-realized-numbers-only-for-escalation.md) - family: the escalation rule only works because the ledger it cites is contemporaneous and trusted
- [ops-shared-retry-budget](ops-shared-retry-budget.md) - the generalization in action: the budget is a retry cap, and the shared token bucket is its contemporaneous ledger
- [ctx-working-memory-budget](ctx-working-memory-budget.md) - the token-budget instance of the same principle: a cap without a running record is not a control
