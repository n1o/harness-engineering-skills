# obs-low-cardinality-error-type

> Report failures with a low-cardinality `error.type` attribute (provider error code, canonical exception name, or other low-cardinality identifier), not free-form exception strings or stack traces.

## Why It Matters

- `error.type` is Conditionally Required on every span and metric whenever the operation ended in an error — error visibility is not optional telemetry

- Instrumentations SHOULD document the list of error values they report; `_OTHER` is the defined fallback when no custom value applies

- This keeps error dimensions aggregatable across sessions/models; high-cardinality values (full exception text, request IDs) poison metrics dashboards

- Same convention applies to metrics: `gen_ai.client.operation.duration` carries `error.type`, so failure rates and latency-by-error-class come from one signal definition

## Scope

- Apply to every span and metric that ends in error — `error.type` is Conditionally Required, not optional telemetry; document the value list, `_OTHER` is the fallback.

- Keep it low-cardinality (provider error code, canonical exception name); full exception text and request IDs poison metrics dashboards — they may live in logs, not in error dimensions.

- Skip only for operations that cannot error; the same convention applies to metrics (`gen_ai.client.operation.duration` carries `error.type`).

## Source

OpenTelemetry GenAI semantic conventions (https://github.com/open-telemetry/semantic-conventions-genai, docs/gen-ai/gen-ai-agent-spans.md and gen-ai-metrics.md)

## See Also

- [prin-compact-errors-bounded-retries](prin-compact-errors-bounded-retries.md) - compact low-cardinality errors here for aggregation; full error text there, fed back to the agent for self-healing
- [obs-portable-trace-conventions](obs-portable-trace-conventions.md) - `error.type` is one of the required attributes that keep traces portable
- [obs-latency-gap-diagnostics](obs-latency-gap-diagnostics.md) - retry-loop detection consumes the error classes this rule standardizes
