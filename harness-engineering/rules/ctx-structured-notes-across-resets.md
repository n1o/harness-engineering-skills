# ctx-structured-notes-across-resets

> Have the agent persistently write notes/todos to files outside the context window and re-read them after context resets — durable working state that survives summarization.

## Why It Matters

- Structured note-taking (a to-do list, a NOTES.md) tracks progress, dependencies, and critical context that would be lost across dozens of tool calls, with minimal token overhead.

- Anthropic's Pokémon agent maintained precise tallies over thousands of steps (objectives, explored-region maps, combat strategies) and resumed multi-hour sequences after resets by reading its own notes.

- Choose by task shape: compaction for back-and-forth dialogue, note-taking for milestone-driven iterative work, sub-agents for parallel exploration.

## Scope

- Apply to milestone-driven iterative work spanning resets: persist notes/todos to files outside the window and re-read them after each reset, tracking progress, dependencies, and critical context at minimal token cost.

- Choose by task shape (per the source): note-taking for milestone-driven iterative work, compaction for back-and-forth dialogue, sub-agents for parallel exploration — notes are not the universal answer.

- Skip when the task is short or the session never resets — in-window recitation suffices and file I/O is overhead.

## Source

Anthropic, "Effective context engineering for AI agents" (https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents); Manus (https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus)

## See Also

- [struct-externalize-loop-state-files](struct-externalize-loop-state-files.md) - the struct- counterpart: a harness loop that deterministically re-reads/re-writes its plan and learnings files every iteration; this rule is the agent-driven, per-reset version of the same externalization.

- [ctx-filesystem-as-external-memory](ctx-filesystem-as-external-memory.md) - the underlying medium: the file system as unlimited, persistent, agent-operable memory.

- [ctx-recitation-recenter-attention](ctx-recitation-recenter-attention.md) - the in-window complement for loops that don't reset: recite the todo at the tail instead of (only) writing it to a file.
