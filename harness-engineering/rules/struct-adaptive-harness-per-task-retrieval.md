# struct-adaptive-harness-per-task-retrieval

> For heterogeneous task mixes, retrieve a task-adapted harness configuration at runtime from a case-indexed experience bank instead of serving one static harness.

## Why It Matters

- MemoHarness adapts a globally optimized harness to each unlabeled test case by retrieving K similar successes and failures: 0.806 mean success on its Terminal-Bench evaluation split (89 tasks, 80/20 train/evaluation; the paper does not state the Terminal-Bench version — do not compare directly with Terminal-Bench 2.x numbers from other papers) vs 0.722 for the strongest static baseline (Codex), and vs Claude Code 0.556, Terminus 0.361, OpenCode 0.389 (MemoHarness, arXiv 2607.14159).
- Per-case adaptation generalizes and stays cheap: the Terminal-Bench-derived configuration improves unseen suites (SWE-Bench Pro 0.706→0.765; StrongReject 0.879→0.909) at $6.89 total cost vs Codex's $10.28 — provided retrieved experience is cacheable (MemoHarness, arXiv 2607.14159).
- JIT-Agent generates an executable per-task harness (memory/planning/action/orchestration modules) from a compact retrieved context of prior harnesses: +7.7 average on GLM-5.2 and +8.8 on DeepSeek-V4-Flash across all 18 matched backbone–benchmark pairs, peaking at +24.8 (DeepPlanning-Shopping 59.1→83.9) (JIT-Agent, arXiv 2608.25593).
- The ahead-of-time assumption is the failure mode: AOT harness compilation presumes the deployment distribution is stable and known before seeing each task's structure; per-task synthesis removes that assumption, which matters exactly when task mixes are heterogeneous (JIT-Agent, arXiv 2608.25593).
- Cost control is built into selection: MemoHarness's correctness-first lexicographic rule (mean reward, then lower mean token cost) prevents adaptation from buying accuracy with unbounded token spend (MemoHarness, arXiv 2607.14159).

## Scope

- Apply to heterogeneous task mixes (mixed domains/tools/skills) and deployments that log per-case outcomes and can maintain a retrieval index of prior runs.
- Boundary with [prin-internalize-harness-into-model](prin-internalize-harness-into-model.md): when you control training and a mechanism is validated, stable, and exercised every run, internalize it into weights/defaults instead of paying per-task retrieval forever — this rule is the fallback for heterogeneous mixes you cannot cover by retraining, and the two compose (distill the stable common core, retrieve residual variants).
- Every bank entry must itself be a declared, versioned config artifact per [struct-harness-as-declared-config](struct-harness-as-declared-config.md) — the bank retrieves among declared configs, never outside the declared surface.
- Skip for homogeneous task families — one tuned static harness is simpler and usually wins.
- Skip when per-case retrieval overhead exceeds its measured gains.
- Safety-critical policy dimensions must stay fixed for all tasks; retrieval may vary prompts and tool wiring, never authorization.

## Source

MemoHarness (https://arxiv.org/abs/2607.14159), JIT-Agent (https://arxiv.org/abs/2608.25593)

## See Also

- [prin-simplest-solution-that-works](prin-simplest-solution-that-works.md) - add per-task adaptation only when a static harness measurably underperforms
- [ctx-just-in-time-retrieval](ctx-just-in-time-retrieval.md) - retrieving task data at runtime; this rule retrieves configuration
- [ver-harness-deltas-measured-by-evals](ver-harness-deltas-measured-by-evals.md) - measure the adaptive layer against the static baseline before keeping it
- [run-dead-end-ledger-scar-tissue](run-dead-end-ledger-scar-tissue.md) - the failure half of the bank this rule retrieves from
- [ctx-memory-reconstruct-not-replay](ctx-memory-reconstruct-not-replay.md) - retrieved harness experience is likewise input to critique, not instructions to replay
- [prin-internalize-harness-into-model](prin-internalize-harness-into-model.md) - the internalization alternative when you control training; both rules cite MemoHarness from opposite sides — read both before choosing
- [struct-harness-as-declared-config](struct-harness-as-declared-config.md) - every retrieved bank entry must be a declared, diffable config
