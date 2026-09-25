# obs-sampling-attrs-at-span-start

> Populate the attributes needed for trace-sampling decisions at span creation time, not at span end — head-based sampling can't use attributes that arrive after the decision point, and late-filled attributes force you to either keep everything or drop blindly.

## Why It Matters

- The spec calls out which attributes "can be important for making sampling decisions and SHOULD be provided at span creation time": `gen_ai.agent.name`, `gen_ai.operation.name`, `gen_ai.provider.name`, `gen_ai.request.model`, `server.address`, `server.port`

- Design consequence for harnesses: if your instrumentation fills identity attributes lazily, head-based sampling can't route by model/agent/provider and you will either keep everything (cost blowup) or drop blindly. (Tail-based sampling evaluates completed spans and can use late attributes, but pays the cost of buffering the full span stream first; early attribute availability still keeps head sampling viable.)

- Use stable, provider-assigned identifiers for `gen_ai.agent.id` (e.g., agent ARNs) — the spec explicitly warns against recording transient in-memory instance IDs

## Scope

- Apply when your sampling policy routes by these attributes under head-based sampling: `gen_ai.agent.name`, `gen_ai.operation.name`, `gen_ai.provider.name`, `gen_ai.request.model`, `server.address`, `server.port` need to be populated at span creation time or the decision point can't use them (the spec marks this SHOULD, not MUST).

- Skip under tail-based sampling (it evaluates completed spans and can use late attributes, at the cost of buffering the full stream), or when your head sampler doesn't use these attributes at all (e.g. fixed-rate) — early population is then harmless but not load-bearing.

- Use stable provider-assigned identifiers for `gen_ai.agent.id` — never transient in-memory instance IDs, which defeat sampling routing across sessions.

## Source

OpenTelemetry GenAI semantic conventions (docs/gen-ai/gen-ai-agent-spans.md, https://github.com/open-telemetry/semantic-conventions-genai)

## See Also

- [obs-portable-trace-conventions](obs-portable-trace-conventions.md) - the attribute namespaces and requirement levels these sampling attributes come from
- [obs-agent-span-hierarchy](obs-agent-span-hierarchy.md) - identity attributes ride on the session/agent spans that carry them
- [obs-record-token-usage-and-duration-metrics](obs-record-token-usage-and-duration-metrics.md) - what you keep after sampling must include usage and duration signals
