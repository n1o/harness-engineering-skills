# ctx-progressive-disclosure-pointers

> Put task- and domain-specific guidance in separate, self-descriptively named files and teach the agent how to find them, so instructions load only when relevant; prefer pointers (file:line references) over copied snippets.

## Why It Matters

- Keep an index (e.g. agent_docs/ with building_the_project.md, running_tests.md, code_conventions.md…) in the always-loaded file with one-line descriptions, and have the agent read the relevant doc before starting work — or ask approval first.

- Path-scoped rule files (e.g. rules applying only to `**/*.sh`) load only when matching files are touched, keeping the root file small (Fowler's "Rules" feature category).

- Prefer pointers to copies: embedded code snippets go stale; `file:line` references keep the codebase authoritative.

- Skills are the same principle generalized: descriptions of resources/instructions the LLM lazy-loads when relevant (Fowler lists skills as context interfaces; HumanLayer notes they're the intended home for this pattern).

## Scope

- Apply when guidance is task- or domain-specific and would bloat the always-loaded file: move it to self-describing files with an index, and prefer `file:line` pointers over copied snippets (copies go stale; the codebase stays authoritative).

- The pointer preference binds wherever the source of truth lives outside context; skip it for static knowledge with no canonical file to point at.

- Skip when guidance must fire every time regardless of task — that belongs in the always-loaded file or on a deterministic trigger, not behind an agent's retrieval decision.

## Source

HumanLayer, "Writing a good CLAUDE.md" (https://www.humanlayer.dev/blog/writing-a-good-claude-md); Martin Fowler, Context Engineering for Coding Agents (https://martinfowler.com/articles/exploring-gen-ai/context-engineering-coding-agents.html)

## See Also

- [ctx-instruction-file-minimal-universal](ctx-instruction-file-minimal-universal.md) - the family root: what stays in the always-loaded file (and how small it must be) — this rule handles everything that moves out.

- [ctx-layered-instruction-files](ctx-layered-instruction-files.md) - the family's structural layer: hierarchy and precedence for the files this rule scatters pointers into.

- [ctx-just-in-time-retrieval](ctx-just-in-time-retrieval.md) - the same disclosure pattern for task data (paths, queries, references) rather than instruction files.

- [ctx-context-load-ownership](ctx-context-load-ownership.md) - assigns who fires each disclosure: agent lazy-load (skills), path-scoped deterministic triggers, or human invocation.
