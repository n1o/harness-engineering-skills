# ctx-deterministic-tools-before-llm

> Never send an LLM to do a linter's job: enforce style, formatting, and mechanical checks with deterministic tools (auto-fixing linters, lifecycle hooks), not instruction-file prose.

## Why It Matters

- LLMs are expensive, slow substitutes for linters/formatters; style rules bloat instruction count and context with mostly-irrelevant snippets, degrading instruction-following overall.

- LLMs are in-context learners: with a few codebase searches (or a research doc) they follow existing conventions without being told.

- If style matters, wire a Stop/lifecycle hook that runs the formatter and feeds errors back for the agent to fix, or a slash command pointing at the diff — handle implementation and formatting separately for better results on both.

## Scope

- Apply to style, formatting, and mechanical checks: wire a formatter/linter via a Stop/lifecycle hook (or a slash command pointing at the diff) instead of encoding them as instruction-file prose.

- Skip for conventions the model can pick up in-context — with a few codebase searches (or a research doc) it follows existing patterns without being told.

- The boundary is enforcement vs orientation: if the rule describes *what the codebase is like* (map, stack, verification commands), it stays in the instruction file; if it must *fire every time*, it becomes a deterministic tool.

## Source

HumanLayer, "Writing a good CLAUDE.md" (https://www.humanlayer.dev/blog/writing-a-good-claude-md)

## See Also

- [run-mechanical-invariants-linter-messages-as-injections](run-mechanical-invariants-linter-messages-as-injections.md) - the architectural variant: custom linters enforce structural invariants and their error messages inject remediation instructions into context; this rule is the style/formatting instance of the same move.

- [ctx-deterministic-output-backpressure](ctx-deterministic-output-backpressure.md) - the companion deterministic gate on the output side, once the linter/test runs are wired.

- [ctx-instruction-file-minimal-universal](ctx-instruction-file-minimal-universal.md) - keeping mechanical rules out of the file is one lever for keeping it minimal.

- [guard-hard-policies-over-model-judgment](guard-hard-policies-over-model-judgment.md) - the same deterministic-over-probabilistic principle at the security boundary.
