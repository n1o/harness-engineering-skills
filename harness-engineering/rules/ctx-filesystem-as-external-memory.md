# ctx-filesystem-as-external-memory

> Use the file system as the ultimate context — unlimited, persistent, agent-operable — and make every compression restorable by keeping a pointer (URL, path) to re-fetch dropped content.

## Why It Matters

- Big windows don't solve agentic context: observations (web pages, PDFs) blow the limit, performance degrades with length, and long prefills stay expensive even when cached.

- Any irreversible compression carries risk because you cannot predict which observation becomes critical ten steps later; Manus's rule: drop a page's content only if the URL is preserved, drop a document only if its sandbox path remains.

- The model should read and write files on demand, using them as structured externalized memory (Anthropic's memory tool / file-based system follows the same pattern).

- Long-horizon coherence comes from re-reading own notes after resets, not from holding everything in window.

## Scope

- Apply whenever content is dropped from context in any form — compaction, truncation, or summarization: keep a pointer (URL, path) so the drop is restorable, and let the model read/write files on demand as structured external memory.

- The rule becomes binding as observations grow (web pages, PDFs) and long-horizon coherence across resets becomes the goal; for short sessions with small payloads, holding content in-window is fine.

- Skip for content that cannot be re-fetched or re-derived at reasonable cost — keep it in-window instead.

## Source

Manus, "Context Engineering for AI Agents: Lessons from Building Manus" (https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus); Anthropic, "Effective context engineering for AI agents" (https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)

## See Also

- [ctx-just-in-time-retrieval](ctx-just-in-time-retrieval.md) - the retrieval mechanism for these pointers: agents maintain references and pull contents in via tools at runtime.

- [ctx-structured-notes-across-resets](ctx-structured-notes-across-resets.md) - applies the same file-based external memory to working state that must survive resets.

- [ctx-compaction-recall-then-precision](ctx-compaction-recall-then-precision.md) - pointers make aggressive compaction safe: dropped observations stay re-fetchable.
