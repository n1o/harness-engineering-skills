# ctx-memory-substrate-routing

> Pick the memory substrate by task regime, not by fashion: no substrate wins everywhere, retrieval breadth has opposite optimal values in QA vs decision-making, and structural memory buys recall with large write/latency costs — so route or trade accordingly.

## Why It Matters

- No substrate dominates across regimes (Harness the Memory, arXiv 2608.15008): the dual-level graph led recall-heavy QA with 0.648–0.719 across three backbones, beating flat vector retrieval by 0.10–0.15 absolute; but on embodied ALFWorld the best substrate was distilled-strategy refinement (32.1% task success vs 22.4% no-memory), and on BigCodeBench-Hard plain BM25 beat the graph for one backbone (19.6% vs 16.2% Pass@1) at 1/6 the latency (5.0 vs 31.2 s/query).
- Retrieval breadth k reverses sign across regimes (2608.15008): QA score rose monotonically 0.45→0.65 as k went 1→20, but ALFWorld success fell 32.1%→~25% as k went 1→5 — at k=20 the retrieved context absorbed 66% of attention mass and starved the policy's task cues. Retrieval breadth is a regime-conditioned hyperparameter, not a knob to maximize.
- Memory can be net-negative for agentic tasks (2608.15008): a plain vector memory scored −0.5 task success vs the no-memory baseline on ALFWorld — the no-memory control is a mandatory comparison, not an afterthought.
- Structure costs are front-loaded and large (2608.15008): structural/graph substrates spent ~4.4M–10.3M auxiliary write tokens per benchmark run, while the hierarchical substrate that deferred tree construction to first read paid only ~280K and stayed within quality striking distance at 10–30x lower per-query latency; production memory systems (MemGPT, Mem0, Zep) were excluded outright for 2,700–9,000 auxiliary LLM calls per run — overhead that swamps any quality gain.
- The paper's distilled design rule: trade read breadth for write depth — retrieve fewer entries and invest in distilling memory at write time; refinement substrates scaled gracefully while graph rebuilds scaled steeply (9s→45s) (2608.15008).
- Structure is not automatically better even for recall: a knowledge-graph memory lost to plain flat RAG on LongMemEval (token F1 0.417 vs 0.468) — it must beat the boring baseline to justify its cost (Selective Forgetting, arXiv 2608.28978).

## Scope

- Apply when choosing or changing the backing store for agent long-term memory (vector store, graph, hierarchy of summaries, distilled lessons files, KV-cache tricks), setting retrieval breadth k for memory-augmented loops, or budgeting memory write vs read cost.
- Skip for tasks that fit in one context window with no cross-session recall; in-window compaction/summarization is covered by the compaction rules.
- Skip for scratch space with no retrieval step — there is nothing to route.

## Source

Harness the Memory: holistic substrate evaluation (https://arxiv.org/abs/2608.15008), with negative control from Selective Forgetting (https://arxiv.org/abs/2608.28978)

## See Also

- [ctx-filesystem-as-external-memory](ctx-filesystem-as-external-memory.md) - that rule says where durable memory can live; this rule says which structure and retrieval settings to build there per task regime
- [ctx-structured-notes-across-resets](ctx-structured-notes-across-resets.md) - a text-record substrate; this rule adds the routing criterion for when notes beat graph stores and when they lose
- [ctx-working-memory-budget](ctx-working-memory-budget.md) - budgets token spend inside the window; this rule budgets retrieval breadth and memory-op tokens outside it
- [ctx-memory-reconstruct-not-replay](ctx-memory-reconstruct-not-replay.md) - governs what happens to memory after retrieval; this rule governs the store and retrieval settings before it
- [ctx-just-in-time-retrieval](ctx-just-in-time-retrieval.md) - lazy loading must also be bounded, since more retrieved context can actively hurt agentic tasks
- [eval-no-skill-baseline](eval-no-skill-baseline.md) - the no-memory control this rule demands is the same paired-baseline discipline
