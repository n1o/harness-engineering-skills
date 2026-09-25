# ver-train-verifiers-on-production-traces

> Verifiers trained only on benchmark traces translate poorly to production: ground them in real user–agent interactions, using sparse outcome signals plus rubric-derived dense supervision, then deploy them for reranking and early stopping.

## Why It Matters

- Benchmark-trained critics scored AUC ~0.45–0.48 on production outcomes — worse than random — because verified rewards (unit tests) exist on benchmarks but not in messy human-in-the-loop sessions where goals evolve and success is "did it survive review and merge."

- Production supervision pipeline: segment interactions (user request → agent actions → finish; segments are the unit, since one chat contains many tries), annotate every segment with trace-observable rubric features (24 features: misunderstood intent, ignored instructions, scope creep, …) giving ~100% dense coverage, then ground with sparse outcome proxies — code survival (~4% coverage, AUC 0.69) beat PR merge (~6%, AUC 0.58).

- Validate rubrics by regressing rubric features against sparse outcomes — what's predictive differs between benchmarks and production, so the taxonomy must earn its keep.

- Payoff at inference time: critic-guided Best-of-N selection lifted Best@8 on mixed-outcome SWE-bench Verified from 57.9% (random) to 73.8%; early stopping accepted at 1.35 attempts average vs 8.0, at +17.7 over random.

- The critic score is a harness primitive: call it in your own loops for reranking, early stopping (accept above threshold), and iterative refinement.

## Scope

- Apply when critics must score real sessions: benchmark-trained verifiers scored AUC ~0.45–0.48 on production outcomes (worse than random) because verified rewards exist on benchmarks but not in messy human-in-the-loop sessions.

- Requires both signals: dense rubric-feature annotation (~100% coverage) grounded by sparse outcome proxies (code survival ~4%/AUC 0.69 beat PR merge ~6%/AUC 0.58); validate rubrics by regressing features against outcomes.

- Skip the training pipeline while you're benchmark-only — the payoff (reranking Best-of-N, early stopping at 1.35 vs 8 attempts) comes when the critic gates production-adjacent work.

## Source

OpenHands 'Learning to Verify AI-Generated Code' (https://openhands.dev/blog/20260305-learning-to-verify-ai-generated-code)

## See Also

- [ver-layered-verification-stack](ver-layered-verification-stack.md) - where the trained critic sits: layer 1, scoring the whole trajectory
- [eval-read-transcripts](eval-read-transcripts.md) - the benchmark-side discipline this rule's production counterpart
- [eval-trace-to-deterministic-checks](eval-trace-to-deterministic-checks.md) - rubric features are trace-observable by construction; deterministic checks are the next step for repeatable ones
