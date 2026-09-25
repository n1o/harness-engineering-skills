# obs-record-token-usage-and-duration-metrics

> Capture per-call token usage (split by modality and cache) and standardized duration metrics so cost and latency are measured signals, not guesses reconstructed after the fact.

## Why It Matters

- Record `gen_ai.usage.input_tokens` / `output_tokens`, plus cache dimensions (`cache_read.input_tokens`, `cache_write.input_tokens`) and modality splits (`.text.*`, `.image.*`, `.audio.*`) — cache reads and writes price differently and dominate long-horizon agent costs

- Emit standard histogram metrics: `gen_ai.client.operation.duration`, `gen_ai.invoke_agent.duration`, `gen_ai.invoke_agent.inference_calls` / `tool_calls`, `gen_ai.execute_tool.duration`, with the spec's recommended explicit bucket boundaries (0.01s…81.92s) so distributions are comparable across backends

- Report `gen_ai.client.operation.time_to_first_chunk` for streaming calls only — SHOULD NOT be reported for non-streaming calls

- Token-usage attributes are Recommended, not opt-in, on agent/invocation spans — treat usage capture as part of the trace contract (agenttrace ranks sessions by input/output/cache tokens and estimated cost precisely because sources record them)

## Scope

- Apply to any instrumented agent call: token usage split by modality and cache (cache reads/writes price differently and dominate long-horizon costs), plus standard duration histograms with the spec's bucket boundaries.

- Usage capture is part of the trace contract (Recommended, not opt-in, on agent/invocation spans); `time_to_first_chunk` is for streaming calls only.

- Skip per-call metrics only where the provider exposes none — then record what's available and say so, rather than reconstructing costs after the fact.

## Source

OpenTelemetry GenAI semantic conventions (gen-ai-spans.md / gen-ai-metrics.md, https://github.com/open-telemetry/semantic-conventions-genai); corroborated by AgentOps (https://github.com/AgentOps-AI/agentops) and agenttrace (https://github.com/luoyuctl/agenttrace)

## See Also

- [eval-clean-environment-per-trial](eval-clean-environment-per-trial.md) - cost and runtime are measured signals here (secondary metrics in a skill eval); environment control there keeps them comparable
- [obs-honest-coverage-labeling](obs-honest-coverage-labeling.md) - token/cost numbers derived from traces must be labeled as estimates, not billing
- [obs-latency-gap-diagnostics](obs-latency-gap-diagnostics.md) - duration metrics flag which sessions need gap-level diagnosis
