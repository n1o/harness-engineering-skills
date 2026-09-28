# run-dead-end-ledger-scar-tissue

> Persist every failed harness configuration, rejected edit, and operational dead end as a searchable ledger consulted before each new proposal — the improvement loop must never re-propose what already failed.

## Why It Matters

- Playbooks that record dead ends as natural-language rules ("DO NOT use GPU generation X due to hardware instability") cut major fix steps per iteration from 4.0 (bootstrap) to 0.5, with the zero-fix rate rising from 0% to 83%; after an architecture transition spiked fixes back to 5 consecutive iterations, recovery surpassed pre-transition levels (Auto-RecSys, arXiv 2609.10922).
- Dead-end records eliminated whole error classes, not just instances: after one recorded GPU-hardware failure pattern, that failure class disappeared from all subsequent job submissions (Auto-RecSys, arXiv 2609.10922).
- MemoHarness's dual-layer bank stores per-case entries (config, trajectory, reward, token cost, diagnosis) plus cross-case "global patterns" distilled every 5 new entries or 3 consecutive failures; the controller retrieves bounded slices of both before proposing the next harness (MemoHarness, arXiv 2607.14159).
- Failures are retrieval targets, not just successes: MemoHarness's test-time adaptation conditions on the K nearest successful AND failed cases; Self-Harness logs every rejected edit so the next iteration's proposer sees what was already tried (MemoHarness, arXiv 2607.14159; Self-Harness, arXiv 2606.09498).
- Discarded attempts remain available evidence: the Darwin Gödel Machine keeps functional-but-worse agents in its archive and biases selection toward underexplored ones — nothing learned is thrown away (DGM, arXiv 2505.22954).

## Scope

- Apply to any iterative harness/agent-improvement loop spanning multiple sessions or agents; operational playbooks; experiment portfolios; anywhere the same class of proposal can recur.
- Skip for single-shot loops with no repetition risk.
- Prune entries whose preconditions have changed — stale dead ends mislead as surely as missing ones.

## Source

Auto-RecSys (https://arxiv.org/abs/2609.10922), MemoHarness (https://arxiv.org/abs/2607.14159), Self-Harness (https://arxiv.org/abs/2606.09498), Darwin Godel Machine (https://arxiv.org/abs/2505.22954)

## See Also

- [struct-externalize-loop-state-files](struct-externalize-loop-state-files.md) - working state; this ledger is the failure memory of that loop
- [ctx-keep-failures-in-context](ctx-keep-failures-in-context.md) - keeps failure evidence in-window; this rule persists it across loops and sessions
- [ctx-memory-curation-scored-forgetting](ctx-memory-curation-scored-forgetting.md) - the pruning policy that keeps this ledger from degrading into noise
- [ops-quarantine-poison-dont-recirculate](ops-quarantine-poison-dont-recirculate.md) - runtime error quarantine; this rule is the design-level dead-end analogue
