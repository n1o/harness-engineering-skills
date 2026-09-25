# obs-portable-trace-conventions

> Emit harness traces against standardized span names and attribute namespaces (e.g., OpenTelemetry GenAI semantic conventions' `gen_ai.*`) so traces stay portable across observability backends instead of being locked to one vendor's format.

## Why It Matters

- Anchor every span with required attributes `gen_ai.operation.name` and `gen_ai.provider.name`; `gen_ai.request.model` when available, and `error.type` whenever the operation ended in error

- Use the well-known operation-name enum when it applies — `chat`, `execute_tool`, `invoke_agent`, `invoke_workflow`, `plan`, `create_agent`, `embeddings`, `retrieval` — rather than inventing per-harness names; document deviations in system-specific conventions

- Follow the prescribed span-name formats (e.g., `create_agent {gen_ai.agent.name}`, `invoke_agent {gen_ai.agent.name}`) so trace lists group by agent rather than by arbitrary call labels

- Respect requirement levels per attribute: Required / Conditionally Required / Recommended / Opt-In — the spec explicitly distinguishes must-have identity attributes from nice-to-have request parameters (`temperature`, `top_p`, `stop_sequences`)

- Use provider names consistently as a discriminator: Bedrock spans carry `aws.bedrock` plus `aws.bedrock.*` attributes and are not expected to carry `openai.*` attributes

## Scope

- Apply to any harness emitting traces meant to outlive one observability backend — anchor spans with the required `gen_ai.*` identity attributes and the well-known operation-name enum.

- Respect the requirement levels as written (Required / Conditionally Required / Recommended / Opt-In); document deviations in system-specific conventions rather than inventing per-harness names.

- Skip standardization for throwaway local debugging traces; the value is portability and comparability, which only matters once a second consumer exists.

## Source

OpenTelemetry GenAI semantic conventions (https://opentelemetry.io/docs/specs/semconv/gen-ai/ — now https://github.com/open-telemetry/semantic-conventions-genai)

## See Also

- [eval-trace-to-deterministic-checks](eval-trace-to-deterministic-checks.md) - traces as eval input: deterministic checks over the standardized event stream this rule defines
- [obs-agent-span-hierarchy](obs-agent-span-hierarchy.md) - the span-kind taxonomy this convention set names
- [obs-sampling-attrs-at-span-start](obs-sampling-attrs-at-span-start.md) - several of these attributes are also the ones sampling decisions need at span creation
