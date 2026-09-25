# guard-pre-action-deterministic-authorization

> Put authorization in a host-emitted pre-tool-call hook that verifies each action against policy before execution — not in prompt instructions the model may ignore.

## Why It Matters

- Policy enforced via runtime hook runs *before* the tool executes; AGENTS.md/instruction-file policy runs only after the model decides to comply — high bypass risk, best used as documentation or fallback only.

- In APort's live adversarial testbed, permissive (instruction-based) policy succeeded 74.6% of the time for attackers vs 0% under restrictive deterministic policy across 879 top-tier attempts.

- Fail closed: if the evaluator cannot find a passport/config, or receives malformed hook input, or hits evaluator integrity failure, it denies the call — you cannot default-allow what you cannot prove would have been authorized.

- Keep an explicit report-only rollout mode (`--enforcement=warn`) for tuning policy, but never let warn mode downgrade malformed-input or misconfiguration cases.

- Prevent policy swap attacks: repo-controlled instruction files must not be able to substitute a permissive passport (APort ignores repo-level policy by default).

## Scope

- Apply wherever a policy claim must actually bind: a host-emitted pre-tool-call hook that verifies each action against policy before execution; AGENTS.md/instruction-file policy only runs after the model decides to comply, so keep it as documentation or fallback, not enforcement.
- The 74.6% vs 0% attacker-success comparison is one adversarial testbed's measured result (permissive instruction-based policy vs restrictive deterministic policy, 879 attempts) — evidence that deterministic hooks beat instructions there, not a universal guarantee for every harness.
- Keep the non-negotiables: fail closed on missing config, malformed hook input, or evaluator integrity failure; keep a report-only (`--enforcement=warn`) mode for tuning, but never let warn mode downgrade malformed-input or misconfiguration cases; ignore repo-controlled policy by default to block policy-swap attacks.

## Source

APort Agent Guardrails (https://github.com/aporthq/aport-agent-guardrails); mcp-guardian (https://github.com/S1LV3RJ1NX/mcp-guardian)

## See Also

- [guard-hard-policies-over-model-judgment](guard-hard-policies-over-model-judgment.md) - why the hook must exist at all: model refusals are a soft block, so enforcement cannot live in prompt instructions
- [guard-scope-based-tool-allowlists](guard-scope-based-tool-allowlists.md) - the per-role allow/blocklist that the hook's policy language should encode
- [guard-audit-log-every-decision](guard-audit-log-every-decision.md) - each allow/deny the hook produces should land in the audit trail as reviewable evidence
