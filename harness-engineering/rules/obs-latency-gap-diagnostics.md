# obs-latency-gap-diagnostics

> Diagnose slow agent runs from the trace's time structure — long gaps, hangs, retry loops, slow tools, oversized parameters, context pressure — rather than only total duration.

## Why It Matters

- The tool's stated second job: "diagnose why a task ran slowly" by catching "long gaps, hanging sessions, retry loops, slow tool calls, large parameters, and context pressure"

- Rank sessions by cost, duration, turns, health, failures, and anomalies so triage starts at the worst sessions instead of chronological browsing

- Compare runs against a local baseline when supplied to produce regression evidence, with incident timelines and attempt-to-attempt diffs

- Design implication for any harness: emit timestamps and call IDs on tool steps (the minimum metadata agenttrace consumes), or gap/retry analysis is impossible after the fact

## Scope

- Apply when diagnosing slow runs: rank sessions by cost, duration, turns, health, failures, anomalies instead of chronological browsing — triage starts at the worst sessions.

- Requires the minimum metadata up front (timestamps and call IDs on tool steps) — emit them or gap/retry analysis is impossible after the fact.

- Skip deep diagnostics for runs where total duration alone answers the question; the gap structure matters when you need *why slow*, not just *how slow*.

## Source

agenttrace (https://github.com/luoyuctl/agenttrace)

## See Also

- [obs-honest-coverage-labeling](obs-honest-coverage-labeling.md) - every gap report must state what the trace actually covers; missing evidence is not a complete trace
- [obs-record-token-usage-and-duration-metrics](obs-record-token-usage-and-duration-metrics.md) - standardized duration metrics are the aggregate signal that tells you which sessions to diagnose
- [obs-low-cardinality-error-type](obs-low-cardinality-error-type.md) - retry-loop detection feeds on aggregatable error classes, not stack-trace strings
