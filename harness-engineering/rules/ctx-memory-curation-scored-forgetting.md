# ctx-memory-curation-scored-forgetting

> Give every persistent memory entry a cheap, deterministic importance score (recency, access frequency, structural centrality, age) and prune below a threshold on a fixed cadence — memory stores need an explicit forgetting policy, and the bookkeeping must not be done by generative LLM calls.

## Why It Matters

- Scored forgetting was quality-neutral at meaningful compression (Selective Forgetting, arXiv 2608.28978): pruning every 400 turns below importance 0.10 removed 9.8% of nodes and 5.5% of edges with token F1 unchanged (0.292→0.293, 95% CI [−0.015, +0.016]) — retention noise costs nothing to delete but costs retrieval precision to keep.
- The scoring formula is cheap and fully deterministic (2608.28978): importance = 0.35·recency (90-day half-life) + 0.25·log access frequency + 0.20·log edge centrality + 0.20·turns-decay (1,000-turn half-life) — no LLM in the retention decision; these weights are measured defaults from this one study, not universal constants, and were never swept.
- Dedup before write, cheaply (2608.28978): an O(1) title-index check runs first, falling back to a vector cosine scan only at threshold 0.92 — the write path doesn't need a model call either; MemHarness used the same pattern with semantic dedup at θ=0.85 plus a Laplace-smoothed success-per-use pruning score (arXiv 2607.28272).
- Memory control by generative LLM is a cost trap (Harness the Memory, arXiv 2608.15008): production memory systems (MemGPT, Mem0, Zep) were excluded from evaluation because their autoregressive memory operations cost 2,700–9,000 auxiliary LLM calls per benchmark run — 1–2 orders of magnitude overhead that dominates any quality metric.
- Non-generative control also wins on quality where tested (Jev-Mem, arXiv 2609.23986): a typed, non-autoregressive controller for memory decisions scored 0.777 overall on LoCoMo vs 0.700 for the best generative baseline, with the largest gain on adversarial questions (0.962 vs 0.742) — memory bookkeeping is a classification problem, not a generation problem.
- Unpruned stores measurably hurt: with all 500 haystacks in one 27,021-node graph, scores dropped versus per-question graphs (F1 0.292 vs 0.417) (2608.28978) — accumulation without curation degrades retrieval, mirroring how instruction bloat degrades instruction-following.

## Scope

- Apply to persistent agent memory stores that grow across sessions/tasks (preference stores, experience banks, project knowledge bases); any harness deciding what to keep, merge, or delete.
- Skip for session-scoped scratch state deleted wholesale at reset.
- Skip for retention-mandated records — audit trails where deletion is prohibited (see `guard-audit-log-every-decision`); score and archive them separately.
- In-window compaction is a different mechanism (recall/precision over live context) — covered by the compaction rules.

## Source

Selective Forgetting (https://arxiv.org/abs/2608.28978); MemHarness (https://arxiv.org/abs/2607.28272); Harness the Memory (https://arxiv.org/abs/2608.15008); Jev-Mem (https://arxiv.org/abs/2609.23986)

## See Also

- [ctx-structured-notes-across-resets](ctx-structured-notes-across-resets.md) - notes persist by default; this rule adds the pruning half so the note store doesn't degrade into noise
- [run-entropy-garbage-collection-cadence](run-entropy-garbage-collection-cadence.md) - GC for repo code patterns; this rule is GC for the memory store, with an explicit scoring function
- [ctx-deterministic-tools-before-llm](ctx-deterministic-tools-before-llm.md) - the general principle; this rule applies it to memory bookkeeping with measured thresholds
- [ctx-compaction-recall-then-precision](ctx-compaction-recall-then-precision.md) - in-window compaction order; this rule is the store-level complement: once recall is captured durably, prune by measured importance
- [ops-quarantine-poison-dont-recirculate](ops-quarantine-poison-dont-recirculate.md) - classify before retrying for a fleet; importance scoring is the memory-side analogue: score before keeping
