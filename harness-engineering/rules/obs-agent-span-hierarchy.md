# obs-agent-span-hierarchy

> Structure traces as an explicit hierarchy — session → agent → operation/task → tool — rather than a flat event stream, so replay and drill-down follow the actual delegation structure.

## Why It Matters

- OTel defines distinct span kinds for each agent phase: `plan` for "agent planning or task decomposition phase", `execute_tool` for tool execution, `invoke_workflow` for multi-step workflows — model each loop phase as its own span type

- AgentOps mirrors this as decorators: `@session` is the root span for all others; `@agent`, `@operation`/`@task`, `@workflow` nest to form the execution graph; every decorator supports input/output recording and exception capture so a session can be replayed step-by-step

- Carry `gen_ai.conversation.id` when the framework has one readily available (chat stores, session IDs, hosted-agent threads) so multi-turn runs correlate across spans

- This is what makes "session replay" possible at all: without the parent/child structure, an unattended run's trace cannot be walked back as a narrative

## Scope

- Apply to any instrumented agent whose sessions will be replayed, triaged, or audited — the session → agent → operation/task → tool hierarchy is what makes drill-down and step-by-step replay possible at all.

- Model each loop phase as its own span type (`plan`, `execute_tool`, `invoke_workflow`); carry `gen_ai.conversation.id` only when the framework has one readily available.

- Overkill for single-shot, non-delegating calls where a flat stream suffices — the hierarchy earns its keep when there is actual delegation structure to walk.

## Source

OpenTelemetry GenAI agent-span taxonomy (create_agent / invoke_agent client+internal / invoke_workflow / plan / execute_tool spans, https://github.com/open-telemetry/semantic-conventions-genai); AgentOps (https://github.com/AgentOps-AI/agentops)

## See Also

- [obs-portable-trace-conventions](obs-portable-trace-conventions.md) - names and attributes that keep this hierarchy portable across backends
- [struct-append-only-trace-receipt](struct-append-only-trace-receipt.md) - the parent/child structure is what makes an append-only receipt walkable as a narrative
- [eval-trace-to-deterministic-checks](eval-trace-to-deterministic-checks.md) - hierarchical spans are the event stream those checks consume
