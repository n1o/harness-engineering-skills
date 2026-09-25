# ctx-frequent-intentional-compaction

> Design the whole workflow around context management: compact conversation into durable artifacts (research docs, plans, progress files) at phase boundaries and restart with fresh context, keeping utilization in the 40–60% range.

## Why It Matters

- Context killers are searching, code-flow reading, edits, test/build logs, and huge tool JSON; compaction distills them into structured artifacts instead of letting them accumulate.

- Structured as research → plan → implement, where each phase runs in fresh context and hands a distilled artifact to the next; after each verified implementation phase, compact status back into the plan file.

- Compaction prompt example: "Write everything we did so far to progress.md: end goal, approach, steps done, current failure" — commit messages can serve the same role.

- This makes sessions resumable and fights context drift: the artifact, not the decaying chat history, is the source of truth; enabled non-experts to ship merged PRs into a 300k LOC brownfield Rust codebase.

## Scope

- Apply to phase-shaped engineering work (research → plan → implement) where the heavy context generators — searching, code-flow reading, edits, test/build logs, huge tool JSON — accumulate across phases.

- Skip when work is short-lived or genuinely conversational in one window, or when orchestration overhead (restarts, handoff artifacts) outweighs drift risk.

- The 40–60% utilization range is HumanLayer's working target for complex coding sessions, not a universal constant — and it presupposes artifacts worth compacting into (progress files, plans) rather than free-form summary text.

## Source

HumanLayer, Advanced Context Engineering for Coding Agents (https://www.humanlayer.dev/blog/advanced-context-engineering)

## See Also

- [ctx-condensation-threshold-cache-friendly](ctx-condensation-threshold-cache-friendly.md) - complementary and cite both: this rule compacts into durable artifacts at phase boundaries and restarts fresh; that one condenses in-window at a size threshold and keeps recent turns verbatim — prefer the threshold style when cache efficiency and per-turn cost matter most.

- [run-context-reset-handoff-artifacts-across-windows](run-context-reset-handoff-artifacts-across-windows.md) - the reset half of this pattern: structured handoff artifacts (progress file + git history + feature states) bridge sessions when compaction alone isn't enough.

- [ctx-compaction-recall-then-precision](ctx-compaction-recall-then-precision.md) - how to tune what the compaction artifact keeps: recall first, then precision.

- [ctx-subagent-context-isolation](ctx-subagent-context-isolation.md) - the parallel-decomposition variant: exploration burns tokens in a sub-agent window and returns a distilled summary instead of compacting the lead window.
