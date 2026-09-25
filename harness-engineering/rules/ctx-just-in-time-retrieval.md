# ctx-just-in-time-retrieval

> Give agents lightweight identifiers (file paths, queries, links) plus navigation tools, and let them load data at runtime — progressive disclosure over pre-embedding everything into context.

## Why It Matters

- Agents maintain references, not contents, and pull data in via tools when needed — mirroring human use of file systems, inboxes, and bookmarks instead of memorization.

- Reference metadata is itself behavioral signal: `test_utils.py` under `tests/` vs `src/core_logic/` implies different purpose; file sizes, naming conventions, and timestamps proxy complexity and relevance.

- Explore layer by layer: each interaction's context informs the next retrieval decision, keeping working memory on relevant subsets.

- Hybrid where it pays: Claude Code drops CLAUDE.md up front (fast, static) while glob/grep retrieve just-in-time (fresh, precise); runtime exploration is slower, so pre-retrieve where speed matters and guard against dead-end tool misuse.

## Scope

- Apply when data is large relative to the window or would sit unused most turns: give the agent lightweight identifiers (paths, queries, links) and load contents at runtime, layer by layer.

- Keep the hybrid split where it pays: static, always-relevant context (a CLAUDE.md) drops up front; everything else retrieves just-in-time; pre-retrieve only where runtime exploration is too slow for the task.

- Skip when the payload is small and always needed — pre-embedding beats a retrieval round-trip.

## Source

Anthropic, "Effective context engineering for AI agents" (https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)

## See Also

- [ctx-progressive-disclosure-pointers](ctx-progressive-disclosure-pointers.md) - the instruction-side twin: same references-not-copies principle for guidance files rather than task data.

- [ctx-filesystem-as-external-memory](ctx-filesystem-as-external-memory.md) - the storage side of the contract: the filesystem holds contents, pointers keep drops restorable.

- [ctx-context-occupancy-transparency](ctx-context-occupancy-transparency.md) - tells you when indiscriminate pre-embedding has made the budget worth reclaiming.
