# ops-circuit-breaker-per-dependency-shared-fleet

> Key a circuit breaker per dependency (per tool, per API) and share it across all workers so the fleet learns a failure once.

## Why It Matters

- When a dependency crosses a failure threshold, open the circuit: fail fast without attempting the call (no attempt, no spend) for a cool-down window, then admit exactly one probe (half-open) to test recovery.

- Shared, not per-worker: in the postmortem, twelve workers each independently rediscovered that the API was down; a shared breaker means the first few failures open it once and the other eleven fail fast for free instead of each paying to relearn the same fact.

- Fail-fast is a feature, not a degradation: a run that gives up in 50ms costs nothing and ends in a labeled `hard_error` outcome you can actually observe and alert on.

- Layering: the breaker stops attempts against a *currently down* dependency; the retry budget caps total retry volume; they catch different failures and compose.

## Scope

- Apply when many workers share dependencies: key the breaker per dependency (per tool, per API) and share it across the fleet so the first few failures open it once and the rest fail fast for free.
- This is fleet-scale machinery — with one or two workers against a healthy internal API the breaker saves little; it earns its keep when a down dependency would otherwise be rediscovered (and re-billed) worker by worker.
- Layer, don't substitute: the breaker stops attempts against a currently-down dependency while the retry budget caps total volume — they catch different failures and compose; fail-fast outcomes (`hard_error`) should stay observable and alertable.

## Source

Distributed retry patterns (https://loopandretry.github.io/posts/fleet-retry-patterns/)

## See Also

- [ops-shared-retry-budget](ops-shared-retry-budget.md) - composes: the breaker stops attempts against a currently-down dependency; the budget caps total retry volume across the fleet
- [ops-quarantine-poison-dont-recirculate](ops-quarantine-poison-dont-recirculate.md) - composes: the breaker bounds transient-failure cost per dependency; the DLQ removes permanently-failing items from circulation
- [ops-decorrelated-backoff-jitter](ops-decorrelated-backoff-jitter.md) - composes: once half-open probes and retries resume, jitter keeps them from re-stampeding the recovering dependency
- [ops-ledger-is-the-enforcement-mechanism](ops-ledger-is-the-enforcement-mechanism.md) - the failure counts that open the circuit are only real if recorded the moment they are learned of
