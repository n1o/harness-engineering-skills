# obs-prompt-content-opt-in

> Raw prompts, completions, and tool arguments are opt-in telemetry; default traces carry structured metadata, not content bodies.

## Why It Matters

- The semconv marks content-bearing attributes as Opt-In and mandates a published JSON schema for their structure when recorded; system instructions MUST be structured on events

- agenttrace operationalizes the same boundary: it stores "tool-step metadata and duration when the source provides call IDs and timestamps; no prompt, response, result, or tool-argument body is stored in steps" — everything runs locally so "prompts, code, and logs do not need to leave your machine"

- Anti-example: a harness that dumps full conversation text into span attributes by default creates privacy exposure and trace bloat that makes audits harder, not easier

- When you do need content for debugging, gate it behind explicit opt-in and record it in the structured form the schema defines

## Scope

- Apply by default to all telemetry: traces carry structured metadata, not prompt/completion/tool-argument bodies; content-bearing attributes are Opt-In with a published JSON schema.

- Opt in only when content is needed for debugging, and record it in the structured form the schema defines — never dump full conversation text into span attributes by default.

- The boundary is privacy and auditability (trace bloat makes audits harder, not easier); local-first storage eases but does not remove it.

## Source

OpenTelemetry GenAI semantic conventions, Opt-In requirement level for `gen_ai.input.messages`, `gen_ai.output.messages`, `gen_ai.tool.definitions`, `gen_ai.system_instructions` (https://github.com/open-telemetry/semantic-conventions-genai); agenttrace (https://github.com/luoyuctl/agenttrace)

## See Also

- [obs-portable-trace-conventions](obs-portable-trace-conventions.md) - the requirement-level system (Opt-In etc.) this rule leans on
- [guard-untrusted-content-as-data](guard-untrusted-content-as-data.md) - the security-side counterpart: treat recorded content as data, never as instructions
- [obs-agent-span-hierarchy](obs-agent-span-hierarchy.md) - the hierarchy that keeps metadata (not content) sufficient for replay
