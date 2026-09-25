# guard-audit-log-every-decision

> Log every authorization decision and tool execution (tool, allow/deny, policy matched, context, parameters) as a first-class artifact.

## Why It Matters

- APort writes one audit line per decision (timestamp, tool, allow/deny, policy, context) plus the last decision as a structured `decision.json` in an open format (OAP v1.0) — auditability is what turns deny decisions into reviewable evidence.

- mcp-guardian's audit log records proxied executions with parameters (`include_params: true`), tying every call to the scope that authorized it.

- Auditable decisions are the basis for escalation: an allow/deny trail is what a human reviews when deciding whether to widen or narrow a scope.

- Signed/standardized decision formats matter for portability: evidence must outlive any single harness.

## Scope

- Apply wherever authorization decisions or tool executions are security-relevant: one audit line per decision (timestamp, tool, allow/deny, policy, context) plus a structured decision record is what makes a deny into reviewable evidence and an allow into an accountable one.
- Parameter capture is a knob, not a default: mcp-guardian logs parameters only when `include_params` is enabled — weigh log volume and sensitive values against the audit's purpose.
- Keep the format open and structured (OAP v1.0-style `decision.json`) whenever evidence must outlive the harness that produced it; a local, single-user, read-only agent may be fine with a minimal trail.

## Source

APort Agent Guardrails (https://github.com/aporthq/aport-agent-guardrails); mcp-guardian (https://github.com/S1LV3RJ1NX/mcp-guardian)

## See Also

- [guard-pre-action-deterministic-authorization](guard-pre-action-deterministic-authorization.md) - the hook that decides each call before execution; this rule is the record of what it decided and why
- [guard-scope-based-tool-allowlists](guard-scope-based-tool-allowlists.md) - the per-role scope config whose allow/deny outcomes land in this log
- [obs-portable-trace-conventions](obs-portable-trace-conventions.md) - the same evidence-must-outlive-the-harness concern, applied to execution traces via standard span and attribute names
