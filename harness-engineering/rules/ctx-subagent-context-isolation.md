# ctx-subagent-context-isolation

> Run exploration and deep work in sub-agent context windows and return only condensed, distilled summaries to the lead agent — context control, not role-playing.

## Why It Matters

- Sub-agents may burn tens of thousands of tokens on search but return 1,000–2,000-token summaries; the lead agent's window stays clean for synthesis.

- Straightforward use: a fresh window for finding/searching/summarizing so the parent skips clouding its context with grep/read chatter; ideally the subagent output looks like a good compaction artifact (goal, findings, files, next steps).

- Getting quality condensed returns from subagents is non-trivial (HumanLayer's "telephone" problem); sub-agents with wrong context need steering, and bad summaries propagate.

- Also a cost/quality lever (per Fowler): tasks worth running in their own context, with a different model for a second opinion, or with tool sets you don't want in the default context.

## Scope

- Apply to exploration/search/summarization that would cloud the lead agent's window with grep/read chatter: run it in a sub-agent window and return a 1,000–2,000-token distilled summary (goal, findings, files, next steps).

- Also a cost/quality lever per the source: tasks worth their own context, a different model for a second opinion, or tool sets you don't want in the default context.

- Skip when the task is small enough that spawning costs more than it saves, or when the "telephone" problem bites — getting quality condensed returns is non-trivial, and bad summaries propagate; sub-agents with wrong context need steering.

## Source

Anthropic, "Effective context engineering for AI agents" (https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents); HumanLayer, "Advanced Context Engineering" (https://www.humanlayer.dev/blog/advanced-context-engineering)

## See Also

- [ctx-frequent-intentional-compaction](ctx-frequent-intentional-compaction.md) - the sequential counterpart: compact the lead window into durable artifacts at phase boundaries, vs isolating parallel exploration in sub-agent windows here.

- [ctx-compaction-recall-then-precision](ctx-compaction-recall-then-precision.md) - what a good subagent return looks like: recall-max first, then precision — tune the summary prompt like a compaction prompt.

- [prin-small-focused-agents](prin-small-focused-agents.md) - the decomposition principle behind keeping each window small in the first place.
