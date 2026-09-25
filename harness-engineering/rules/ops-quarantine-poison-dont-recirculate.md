# ops-quarantine-poison-dont-recirculate

> Classify the error before retrying it; after bounded attempts, move permanently-failing items to a dead-letter quarantine and keep the fleet processing.

## Why It Matters

- Some failures are permanent — the 400 that will always be a 400, the record that will always be malformed; retrying them is pure waste no matter how well you throttle, and poison at the head of a queue blocks good work behind it.

- Retryability is a property of the specific error, not a default; a per-step cap on a permanent failure did nothing in the postmortem because transient-failure controls don't bound permanent failures.

- The dead-letter queue doubles as a signal: a growing DLQ is a labeled, alertable failure count, instead of an invisible retry storm.

- Composition across all four patterns: decorrelated backoff and the circuit breaker bound the cost of *transient* failure; the retry budget adds the global ceiling; the DLQ bounds the cost of *permanent* failure — each layer catches what the previous one misses.

## Scope

- Apply once any retry path exists: classify the error before retrying it, because a per-step cap does nothing against a permanent failure (the 400 that will always be a 400) — after bounded attempts, permanently-failing items move to a dead-letter quarantine so the fleet keeps processing.
- The DLQ is also a signal, not just a bin: a growing dead-letter count is a labeled, alertable failure signal, which is the payoff over an invisible retry storm.
- Skip the full quarantine machinery only when every failure class is transient by construction; if the queue can hold poison, it needs an exit for poison.

## Source

Distributed retry patterns (https://loopandretry.github.io/posts/fleet-retry-patterns/)

## See Also

- [ops-circuit-breaker-per-dependency-shared-fleet](ops-circuit-breaker-per-dependency-shared-fleet.md) - composes: the breaker bounds transient-failure cost; the DLQ bounds permanent-failure cost — each catches what the other misses
- [ops-shared-retry-budget](ops-shared-retry-budget.md) - composes: the budget is the global ceiling on retry volume; quarantine shrinks what's left to spend it on
- [ops-idempotent-side-effects-for-retry-resume](ops-idempotent-side-effects-for-retry-resume.md) - the safety precondition for retries that do run: an idempotent, journaled side effect can be retried without duplicating real-world actions
- [struct-orphan-recovery-heartbeat](struct-orphan-recovery-heartbeat.md) - crash-side counterpart: recovery re-reads confirmed state instead of assuming in-flight work is undone
