# ctx-condensation-threshold-cache-friendly

> Trigger condensation only at a size threshold, summarize the old span (goals, progress made, remaining work, critical files, failing tests) while keeping recent turns verbatim — this keeps per-turn cost bounded and linear instead of quadratic while amortizing cache rebuilds.

## Why It Matters

- Baseline un-condensed context scales quadratically over a long session (every turn re-transmits full history); threshold-triggered condensation makes cost scale linearly, settling at under half the per-turn cost.

- Preserve task-critical specifics for coding work: user goals, agent progress, critical files, failing tests — not just generic summaries.

- Triggering at a threshold (rather than every turn) preserves prompt-cache efficiency by spreading the rebuild cost across many turns.

- Measured outcome: ~2x per-turn cost reduction with equal-or-better SWE-bench Verified solve rate (54% vs 53%); the only cost is an occasional turn spent condensing.

## Scope

- Apply on long sessions with many-turn histories where uncondensed context grows quadratically: threshold-triggered condensation (summarize old span, keep recent turns verbatim) is what makes per-turn cost settle linear instead.

- Skip for short sessions or when KV-cache efficiency is the binding constraint on the loop's cost — summarizing mid-session invalidates the prompt cache; triggering at a threshold rather than every turn is the mitigation.

- The ~2x per-turn cost reduction and threshold choice are OpenHands' measured defaults from their stack, not universal constants — re-measure on your agent and task mix.

## Source

OpenHands, Context Condensensation for More Efficient AI Agents (https://www.openhands.dev/blog/openhands-context-condensensation-for-more-efficient-ai-agents)

## See Also

- [ctx-frequent-intentional-compaction](ctx-frequent-intentional-compaction.md) - complementary: this rule condenses in-window at a threshold; that one compacts into durable artifacts at phase boundaries and restarts fresh — cite both, choosing per phase structure and cache needs.

- [ctx-compaction-recall-then-precision](ctx-compaction-recall-then-precision.md) - how to tune what the condensation summary keeps: recall first, then precision, with tool-result clearing as the lightest lever.

- [ctx-stable-prefix-kv-cache](ctx-stable-prefix-kv-cache.md) - the cache-efficiency lens that motivates threshold (not every-turn) triggering here.
