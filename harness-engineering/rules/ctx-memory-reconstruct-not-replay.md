# ctx-memory-reconstruct-not-replay

> Never replay retrieved memories verbatim into the prompt: insert an explicit critique-and-reconstruct step that compares each memory's source state against the current state, and give the agent a first-class reject option — semantic relevance does not equal action-level applicability.

## Why It Matters

- Removing the reconstruction stage and replaying raw retrieved memory dropped ALFWorld success from 85.2% to 70.1% — a −15.1-point penalty for verbatim replay; reconstruction is what closes the applicability gap between abstract stored experience and the concrete current state (MemHarness, arXiv 2607.28272).
- Reconstruction must be state-conditioned, not generic: swapping the policy's internal reconstruction for a generic LLM (same backbone, not trained on the task) fell to 77.7% on ALFWorld — critique quality is task-grounded, so a bolt-on summarizer is not a substitute (2607.28272).
- Store the memory's source state alongside the abstraction: stripping the source observation from reconstruction degraded ALFWorld 85.2%→80.0%, and counterfactual edits to the current state measurably shifted rejection rates (0.6%→6.4% on ALFWorld, 72.1%→78.8% on WebShop) — the agent actively diffs history against present (2607.28272).
- Rejection is a healthy outcome, not a failure: WebShop reconstructions rejected 56–72% of retrieved memories, and trained agents converged to 2–3 retrievals per trajectory with sparse filtering — a memory system needs an explicit no-op/reject path that falls back to self-reasoning (2607.28272).
- Reconstruction pays off out-of-distribution: 85.9% success on unseen ALFWorld layouts vs 76.3% for raw replay — yesterday's playbook is most likely wrong exactly where generalization is tested (2607.28272).
- Practicing reconstruction improves the agent even when memory is absent at test time: the no-memory variant still scored 83.0% vs 76.4% for plain RL (2607.28272).

## Scope

- Apply to harnesses that inject retrieved prior experience (past trajectories, distilled lessons, memory files, skill notes) into an agent's working context; prompt design for memory-augmented loops; deciding whether to retrieve at all.
- Skip for exact-fact recall where verbatim fidelity is the point (API signatures, commands, numbers) — the critique step risks paraphrasing away token identity.
- Skip for the current window's own history — it is the present state, not retrieved memory — and for one-shot tasks with no memory bank.

## Source

MemHarness: Memory Is Reconstructed, Not Replayed (https://arxiv.org/abs/2607.28272)

## See Also

- [ctx-keep-failures-in-context](ctx-keep-failures-in-context.md) - keeps failures as in-window evidence; this rule governs retrieved past experience, where stale entries must be filtered by applicability
- [ctx-illusion-of-control-probabilities](ctx-illusion-of-control-probabilities.md) - injected "relevant" memory is a probability-shifter: measure retrieval quality, don't assume it
- [ctx-memory-substrate-routing](ctx-memory-substrate-routing.md) - governs store choice and breadth before retrieval; this rule governs use after retrieval
- [guard-untrusted-content-as-data](guard-untrusted-content-as-data.md) - retrieved memory is input to evaluate, not instructions to follow
- [ctx-just-in-time-retrieval](ctx-just-in-time-retrieval.md) - gets content into context; the critique-against-current-state step is where the value is realized
