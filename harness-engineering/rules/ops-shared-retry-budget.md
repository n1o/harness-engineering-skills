# ops-shared-retry-budget

> Bound fleet-wide retries with a shared budget pinned to the success rate, not per-call caps that multiply into unbounded fleet waste.

## Why It Matters

- A per-step retry cap bounds a step, never a run and never a fleet: N workers × per-worker cap is unbounded in practice; local caps compose into global disaster (the source's $200 postmortem: every layer retried politely, the limits multiplied into a bill).

- Implement as a token bucket the whole fleet draws from: each success earns partial retry credit, plus a slow ambient refill; retries are allowed only while they remain a small fraction of real traffic.

- Self-throttling property: when the downstream is healthy, successes refill the bucket and retries flow; when it's broken, failures stop refilling and retries choke off automatically — no human, no alert, no config change.

- Agent-specific urgency: each retry is a full transcript re-read plus a model call, so the unit of waste is dollars, not milliseconds.

- Ask of any harness: what is the maximum an entire fleet can spend retrying a dependency that will never recover? If the answer isn't a number, it's whatever the provider bills before someone wakes up.

## Scope

- Apply at fleet scale: a shared budget is the only bound on total retry volume, because per-step caps multiply (N workers × per-worker cap is unbounded — the source's $200 postmortem had every layer retrying politely).
- A single-agent setup can start with a simple per-tool retry counter and adopt the token-bucket mechanics (successes earn partial retry credit plus slow ambient refill) when more workers or dependencies arrive; the question "what is the maximum the entire fleet can spend retrying a dependency that will never recover?" must have a numeric answer either way.
- Keep the self-throttling property intact: when the dependency is healthy, retries flow; when it's broken, failures stop refilling and retries choke off without human intervention — the unit of waste is dollars per retry (transcript re-read plus model call), not milliseconds.

## Source

Distributed retry patterns (https://loopandretry.github.io/posts/fleet-retry-patterns/)

## See Also

- [ops-circuit-breaker-per-dependency-shared-fleet](ops-circuit-breaker-per-dependency-shared-fleet.md) - composes: the breaker stops attempts at a down dependency; the budget caps total volume across dependencies and workers
- [ops-decorrelated-backoff-jitter](ops-decorrelated-backoff-jitter.md) - composes: the budget decides *how many* retries happen; jitter decides they don't all happen at once
- [ops-quarantine-poison-dont-recirculate](ops-quarantine-poison-dont-recirculate.md) - composes: the budget bounds transient-failure retries; permanently-failing items leave the loop instead of draining it
- [ops-ledger-is-the-enforcement-mechanism](ops-ledger-is-the-enforcement-mechanism.md) - the token bucket is the contemporaneous ledger that makes the fleet-wide cap an actual control
