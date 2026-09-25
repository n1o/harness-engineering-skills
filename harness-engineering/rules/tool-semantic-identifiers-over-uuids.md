# tool-semantic-identifiers-over-uuids

> Return natural-language names and interpretable identifiers in tool responses; resolve cryptic IDs before they reach the model.

## Why It Matters

- Agents grapple with natural-language identifiers far better than with arbitrary alphanumeric UUIDs; merely resolving UUIDs to meaningful terms (or a 0-indexed scheme) significantly improved Claude's retrieval precision and reduced hallucinations.

- Prioritize contextual relevance over flexibility: `name`, `image_url`, `file_type` directly inform downstream actions; `uuid`, `256px_image_url`, `mime_type` are low-signal.

- When technical IDs are needed to chain calls, expose a `response_format` enum (`concise` | `detailed`) so the agent controls verbosity; in the source example, `concise` responses used ~1/3 the tokens while `detailed` still returned `thread_ts` and other IDs needed for follow-up calls.

## Scope

- Apply to tool responses that must inform downstream reasoning or chained calls: return natural-language names and interpretable identifiers (the source's UUID-resolution measurably improved retrieval precision and cut hallucinations); prioritize high-signal fields (`name`, `image_url`, `file_type`) over low-signal ones.
- When technical IDs are needed to chain calls, expose a `response_format` enum (`concise` | `detailed`) so the agent controls verbosity — the source measured ~1/3 the tokens on `concise` while `detailed` still returned the IDs follow-ups need.
- Skip when the consumer is machinery rather than the model (a harness reading a stable UUID is fine) — this rule is about what the *model* has to reason over.

## Source

Anthropic, Writing effective tools for agents (https://www.anthropic.com/engineering/writing-tools-for-agents)

## See Also

- [tool-bounded-token-efficient-responses](tool-bounded-token-efficient-responses.md) - the two halves of response economy: this rule picks interpretable identifiers; that one bounds and shapes the response carrying them
- [tool-descriptions-as-prompts](tool-descriptions-as-prompts.md) - the same make-it-interpretable discipline on the input side: parameter names and schemas the model can reason over
- [tool-namespacing-for-selection](tool-namespacing-for-selection.md) - interpretable naming for tools themselves, so selection can happen on meaning rather than opaque handles
