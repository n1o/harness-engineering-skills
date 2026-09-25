# ops-decorrelated-backoff-jitter

> Add decorrelated jitter to exponential backoff so fleet retries don't arrive in synchronized waves that stampede the recovering dependency.

## Why It Matters

- Fleet bug in plain exponential backoff: if all N workers fail at the same moment, they all follow the same schedule and retry in lockstep; the recovering service gets slammed, falls over again, and the retries become the outage (self-sustaining thundering herd).

- Fix: decorrelated jitter — each worker's next delay randomized against its own previous delay (`min(cap, random.uniform(base, prev * 3))`), spreading retries across a smooth band instead of stacking on tick boundaries.

- Costs nothing and removes an entire class of "our retries caused the second outage" incidents; agent fleets are small enough that people skip it, and twelve workers is plenty to stampede an internal API.

## Scope

- Apply whenever more than one worker retries the same dependency: plain exponential backoff makes all N workers that failed together retry in lockstep, and the synchronized wave (not the original outage) takes the dependency down again.
- The source's point that "twelve workers is plenty to stampede an internal API" sets the scale: this stops being optional well before large fleet sizes, because a fleet small enough to skip jitter is also small enough to self-inflict the second outage.
- Effectively free to implement (`min(cap, random.uniform(base, prev * 3))`) but it only addresses *synchronized transient* retries; permanently-failing items need quarantine, and total volume still needs a shared budget.

## Source

Distributed retry patterns (https://loopandretry.github.io/posts/fleet-retry-patterns/)

## See Also

- [ops-shared-retry-budget](ops-shared-retry-budget.md) - composes: jitter spreads retries the schedule doesn't; the budget caps how many retries exist to spread
- [ops-circuit-breaker-per-dependency-shared-fleet](ops-circuit-breaker-per-dependency-shared-fleet.md) - composes: once recovery probes resume, the breaker admits one; jitter keeps the resumed traffic from re-stampeding
- [ops-quarantine-poison-dont-recirculate](ops-quarantine-poison-dont-recirculate.md) - composes: jitter smooths transient-failure retries; permanently-failing items should leave the retry loop entirely
