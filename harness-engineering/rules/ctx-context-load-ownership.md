# ctx-context-load-ownership

> Be explicit about who decides when each context feature loads — LLM (lazy, non-deterministic), human (controlled, less automated), or agent software at deterministic lifecycle points — and match the trigger to how critical the load is.

## Why It Matters

- LLM-decided loading (skills) is a prerequisite for unsupervised operation but carries uncertainty that the context actually gets loaded when expected.

- Human-invoked context (slash commands) buys control at the cost of automation.

- Agent-software triggers (hooks, always-loaded rules files) fire deterministically at session start or file events — use these for guidance that must never be missed.

## Scope

- Apply when deciding, per context feature, what happens if it silently fails to load: guidance that must never be missed belongs on deterministic agent-software triggers (hooks, always-loaded rules files); optional capability can be LLM-decided (skills); human-invoked loading trades automation for control.

- Skip the deliberation for content whose absence is harmless in one session — any trigger works, so pick the cheapest.

- Match trigger reliability to criticality, not convenience: the more catastrophic a missed load, the more deterministic the trigger must be.

## Source

Martin Fowler, "Context Engineering for Coding Agents" (https://martinfowler.com/articles/exploring-gen-ai/context-engineering-coding-agents.html)

## See Also

- [ctx-instruction-file-minimal-universal](ctx-instruction-file-minimal-universal.md) - governs the content of the always-loaded slot this rule's deterministic trigger fires on; this rule governs the trigger mechanism.

- [ctx-progressive-disclosure-pointers](ctx-progressive-disclosure-pointers.md) - the pattern for the LLM-decided (lazy, non-deterministic) tier of this rule's loading decision.

- [ctx-illusion-of-control-probabilities](ctx-illusion-of-control-probabilities.md) - the probabilistic framing behind reserving deterministic triggers for must-fire loads.
