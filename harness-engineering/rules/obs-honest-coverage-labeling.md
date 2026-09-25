# obs-honest-coverage-labeling

> Every trace-derived report must state what the evidence actually covers: per-session capability levels, parse coverage, pricing confidence, and explicit estimate flags — missing evidence is never presented as a complete trace.

## Why It Matters

- Report a capability level per session — `Detailed`, `Aggregate`, or `Limited` — "so missing event-level evidence is never presented as a complete trace"

- Surface data confidence explicitly: report scope, per-source coverage, parse skips, cache hits, unknown sources/models, and pricing fallbacks alongside the numbers

- Label derived numbers for what they are: "All cost and delivery fields are explicitly estimates or heuristics; they are not provider billing or proof that a commit reached `main`"; allow local price overrides but keep the pricing source/status visible in the audit

- Anti-example the design guards against: a cost dashboard that silently falls back to a default model price and presents the result as exact billing

## Scope

- Apply to every trace-derived report — capability level per session, parse coverage, pricing confidence, estimate flags; missing evidence is never presented as a complete trace.

- Skip only for reports derived solely from fully-structured sources with no fallbacks to label; the moment any field is estimated, heuristic, or partially parsed, the label is required.

- Local price overrides are fine, but keep the pricing source/status visible in the audit — the anti-example is a dashboard that silently falls back to a default price and presents it as exact billing.

## Source

agenttrace (https://github.com/luoyuctl/agenttrace)

## See Also

- [obs-latency-gap-diagnostics](obs-latency-gap-diagnostics.md) - the other agenttrace-derived report; gap analysis is only as honest as its stated parse coverage
- [obs-record-token-usage-and-duration-metrics](obs-record-token-usage-and-duration-metrics.md) - the usage/cost numbers this rule forces to be labeled as estimates
- [struct-explicit-terminal-states](struct-explicit-terminal-states.md) - "missing evidence is not promoted to success" is the same discipline at the state-machine level
