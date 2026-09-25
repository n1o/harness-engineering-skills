# ctx-compaction-recall-then-precision

> When compacting, first maximize recall (capture every relevant detail from real agent traces), then tighten precision (drop superfluous content); start with the lightest-touch lever — tool-result clearing.

## Why It Matters

- Compaction reinitiates a window from a summary; the art is what to keep. Overly aggressive compaction loses subtle-but-critical context whose importance only shows later.

- Tune compaction prompts on complex agent traces, not synthetic examples; iterate from recall-max to precision.

- Once a tool call is deep in history, the raw result is rarely needed again — tool-result clearing is the safest, cheapest compaction form.

- Compaction preserves architectural decisions, unresolved bugs, and implementation details while discarding redundant tool outputs; pair with the most recently accessed files for continuity.

## Scope

- Apply when your compaction path exists and you're tuning what its summaries keep: iterate recall-max first (capture every relevant detail from real agent traces), then tighten precision; synthetic examples won't expose what matters later.

- Skip when the loss mode is large raw observations, not summarization quality — tool-result clearing is the safest, cheapest first lever and needs no prompt tuning.

- Before any of it, keep dropped content re-fetchable (paths, URLs) so an over-tight summary is recoverable.

## Source

Anthropic, "Effective context engineering for AI agents" (https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)

## See Also

- [ctx-condensation-threshold-cache-friendly](ctx-condensation-threshold-cache-friendly.md) - when to trigger this tuning (threshold) and the cache/cost payoff; this rule covers what the summary keeps.

- [ctx-frequent-intentional-compaction](ctx-frequent-intentional-compaction.md) - boundary: in-window summary quality vs compacting into durable artifacts at phase boundaries and restarting fresh.

- [ctx-filesystem-as-external-memory](ctx-filesystem-as-external-memory.md) - makes compaction reversible: keep pointers so dropped observations can be re-fetched.
