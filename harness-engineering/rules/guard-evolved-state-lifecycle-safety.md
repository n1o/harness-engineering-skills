# guard-evolved-state-lifecycle-safety

> Treat persistent evolved state — memories, skills, workflow rules, playbooks — as a safety-relevant substrate with a full lifecycle: tag provenance at write, constrain the authority it can carry, verify deletion, and quarantine on violation. Untrusted-content rules cover injection at read time; this covers what the agent itself persists.

## Why It Matters

- A systematic survey (683 coded papers, SAVER framework) shows conventional LLM safety evaluates single responses and agent safety evaluates single actions — both miss the causal role of state that persists, migrates, or activates in a later context. It organizes the space as Substrate (memory item, skill, workflow rule, shared artifact) × Adaptation operation (add, abstract, activate, modify, forget, propagate, migrate) → Violation (provenance, authority, scope, privacy, recoverability) → Exposure → Response (Safety in Self-Evolving Agents, arXiv 2610.00093).
- Persistence itself amplifies failure: on the Personal Agent Sycophancy Benchmark, downstream-failure mean is 45.0% for session-only episodes vs 71.9% when behavior is committed to persistent state across twelve models — a 27.0pp gap from committing, not from generating (arXiv 2610.00093, association not causation per the authors).
- Evolution loops can preserve harmful lessons: studies of harness self-evolution report persistent harnesses retaining incorrect lessons, unsafe tool-use rules, and biased instructions across generations (arXiv 2610.00093; Harness Updating Is Not Harness Benefit, arXiv 2605.30621).
- The survey finds the field strongest at admission, retrieval, activation, and local containment — and weakest at descendant-wide repair (purging a poisoned entry from every state descended from it), deletion verification, and post-evolution evaluation. Those weakest points are where harness engineering must compensate (arXiv 2610.00093).

## Scope

- Apply to any harness with persistent, agent-written state that influences later behavior: memory stores, skill libraries, evolved prompts/workflow rules, shared team artifacts, learned playbooks.
- Provenance: every evolved entry records its origin (which trajectories, which run, which model) so a later violation can be traced and reverted.
- Authority and scope: an evolved entry inherits no tool privileges by existing — evaluate it under [guard-scope-based-tool-allowlists](guard-scope-based-tool-allowlists.md) and [guard-pre-action-deterministic-authorization](guard-pre-action-deterministic-authorization.md) at activation, not just at write.
- Recoverability: keep the pre-evolution state reachable (versioned harness config, [struct-harness-as-declared-config](struct-harness-as-declared-config.md)); a committed regression must be revertible, and "deleted" must be verifiable.
- Admission gates for evolved state remain [ver-self-edit-non-regression-gate](ver-self-edit-non-regression-gate.md) / [ctx-evolved-knowledge-gated-by-validation](ctx-evolved-knowledge-gated-by-validation.md); this rule adds the lifecycle after admission.
- Skip for stateless harnesses or human-only edits — [guard-untrusted-content-as-data](guard-untrusted-content-as-data.md) covers the read-side threat there.

## Source

Safety in Self-Evolving Agents: A Survey (SAVER framework) (https://arxiv.org/abs/2610.00093); persistence-amplification evidence from Harness Updating Is Not Harness Benefit (https://arxiv.org/abs/2605.30621)

## See Also

- [guard-untrusted-content-as-data](guard-untrusted-content-as-data.md) - the read-time counterpart: retrieved state is untrusted input; this rule governs what gets written and what it can carry
- [ctx-evolved-knowledge-gated-by-validation](ctx-evolved-knowledge-gated-by-validation.md) - admission gate for knowledge entries; this rule extends the lifecycle past admission
- [ver-self-edit-non-regression-gate](ver-self-edit-non-regression-gate.md) - the accept/reject gate whose accepted outputs become evolved state
- [run-dead-end-ledger-scar-tissue](run-dead-end-ledger-scar-tissue.md) - the ledger is an evolved state whose integrity this rule protects
- [guard-audit-log-every-decision](guard-audit-log-every-decision.md) - provenance is audit logging applied to the evolution loop
