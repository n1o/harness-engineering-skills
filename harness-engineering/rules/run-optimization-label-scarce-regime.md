# run-optimization-label-scarce-regime

> When representative labeled validation data do not exist, do not stall harness optimization: rank past trajectories by an LLM-judged difficulty × diversity coreset and let the same model self-preference future edits from that experience — no ground-truth labels required.

## Why It Matters

- RHO (Retrospective Harness Optimization) optimizes a deployed harness from past trajectories with no labeled validation data: on held-out SWE-Bench Pro it reaches 0.78 pass rate vs 0.59 for Vanilla Codex, 0.62 Dynamic Cheatsheet, 0.61 ReasoningBank, 0.64 Sleep-time Compute (+0.19 absolute); on Terminal-Bench 2, 0.76 vs 0.71; on GAIA-2, 0.37 vs 0.29 — using 103 agent calls where the matched validation-feedback Meta-Harness needed labeled data (Evolving Agents in the Dark, arXiv 2606.05922).
- The selection mechanism: an LLM judge scores each trajectory's difficulty and an abstract task fingerprint; cosine similarity between fingerprints forms a kernel weighted by difficulty, and a determinant-style diversity objective picks the experience subset — hard and mutually dissimilar tasks carry the optimization signal (arXiv 2606.05922).
- This fills the regime your other optimization rules assume away: [ver-self-edit-non-regression-gate](ver-self-edit-non-regression-gate.md) presupposes a labeled held-out split, [ver-harness-deltas-measured-by-evals](ver-harness-deltas-measured-by-evals.md) an eval suite. Deployed harnesses accumulate unlabeled trajectories far faster than labeled evals.
- Prior experience-based methods (Dynamic Cheatsheet, ReasoningBank, MemMA, Sleep-time Compute) update memory or textual skills only; RHO targets the full harness — prompts, tools, workflows (arXiv 2606.05922).

## Scope

- Apply to self-improvement loops over deployed agent trajectories where future-task labels are scarce or absent: production logs with outcomes but no ground truth.
- Self-preference optimization is unguarded by construction: it ranks and commits edits by the model's own judgment of curated experience. Combine with a non-regression gate the moment any labeled or even proxy signal exists — [ver-self-edit-non-regression-gate](ver-self-edit-non-regression-gate.md) remains the floor for unattended commitment (RSEA's no-gate ablation overfits 33 points in-sample, arXiv 2606.28374).
- LLM-judged difficulty and fingerprints reintroduce a model in the selection path; treat curated experience as provisional evidence, and audit what the judge promoted ([eval-read-transcripts](eval-read-transcripts.md)).
- Not a substitute for evals where evals are affordable — RHO wins on cost and label-freedom, not on ceiling.

## Source

Evolving Agents in the Dark: Retrospective Harness Optimization via Self-Preference (https://arxiv.org/abs/2606.05922)

## See Also

- [ver-self-edit-non-regression-gate](ver-self-edit-non-regression-gate.md) - the labeled-regime counterpart; upgrade to this gate once any held-out signal exists
- [run-dead-end-ledger-scar-tissue](run-dead-end-ledger-scar-tissue.md) - experience curation selects what to learn from; the ledger records what not to retry
- [eval-start-small-grow-from-real-failures](eval-start-small-grow-from-real-failures.md) - the difficulty-and-diversity coreset is the label-scarce analog of growing evals from failures
- [ctx-evolved-knowledge-gated-by-validation](ctx-evolved-knowledge-gated-by-validation.md) - knowledge-layer admission under the same label-scarcity question
