# ctx-mask-tools-not-remove

> When the action space must change mid-task, mask tool selection at decoding time (logit constraints / response prefill / consistent name prefixes) instead of adding or removing tool definitions from context.

## Why It Matters

- Tool definitions sit near the front of context; adding/removing them mid-iteration invalidates the KV-cache for everything after and breaks references from earlier action-observation pairs, causing schema violations and hallucinated calls.

- Manus constrains action choice via a context-aware state machine plus response prefill (auto / required / specified-function modes), e.g. forcing a text reply when new user input arrives.

- Design tool names with consistent prefixes (all browser tools `browser_*`, shell tools `shell_*`) so whole groups can be enforced or excluded without stateful logits processors.

- Anti-pattern Manus explicitly warns against: RAG-style dynamic tool loading — "unless absolutely necessary, avoid dynamically adding or removing tools mid-iteration"; a bloated action space makes a heavily armed agent dumber.

## Scope

- Apply when the action space must change *mid-task/mid-iteration*: mask tool selection at decoding time (logit constraints, response prefill, name-prefix groups) — never add/remove tool definitions from context.

- The cache constraint is binding exactly when definitions sit near the front of a long prompt: edits there invalidate the KV-cache for everything after and break references from earlier action-observation pairs.

- Skip when the tool set can be frozen for the whole task — masking machinery (state machine, prefix conventions, prefills) is not worth building otherwise; large libraries should be slimmed by progressive discovery instead.

## Source

Manus (https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus)

## See Also

- [tool-progressive-tool-discovery](tool-progressive-tool-discovery.md) - boundary: this rule masks selection of already-present tools mid-task to protect the cache; that one loads definitions on demand so they're never in context — they compose (fixed surface + discovery, never mid-task definition churn).

- [ctx-stable-prefix-kv-cache](ctx-stable-prefix-kv-cache.md) - the cache discipline that makes mid-iteration definition edits so costly; masking is how you change behavior without disturbing it.

- [guard-scope-based-tool-allowlists](guard-scope-based-tool-allowlists.md) - a coarser, static version: per-role allow/blocklists remove tools entirely rather than masking them per-turn.
