# struct-append-only-trace-receipt

> Write every run's actions as an append-only trace that doubles as a human-readable receipt — the audit artifact and the run record are the same file.

## Why It Matters

- "Every run writes an append-only record of what the agent did" and `afk trace show` prints it back as a receipt — tool calls, gate decisions, subagent lifecycles, cost — "so you can audit a run without reaching for `jq`"

- Append-only matters: an unattended run you walk away from must be reconstructable after the fact, and mutable logs can be rewritten by the very process under audit

- The trace is the substrate for self-improvement: `afk improve` is a "zero-LLM, deterministic pipeline that mines session traces for ranked failure patterns" (repeated-tool-use, subagent-block, closure-anomaly, tool-failure-density detectors), produces failure cards, and generates replayable eval cases from them

- Keep telemetry local-first and inspectable: "What telemetry exists is local JSONL under `~/.afk/` that you can read or delete" — no phone-home required to get the receipt

- Design implication: gate decisions and costs belong in the same stream as tool calls, or the receipt can't answer "why did the harness allow/block this?"

## Scope

- Apply to any unattended run you must be able to reconstruct after the fact — append-only matters precisely because mutable logs can be rewritten by the process under audit.

- Gate decisions and costs belong in the same stream as tool calls, or the receipt can't answer "why did the harness allow/block this?"; keep it local-first and inspectable (plain JSONL, no phone-home required).

- The trace is also the substrate for `afk improve`-style mining — skip the full receipt only for interactive, human-watched sessions where the operator *is* the record.

## Source

Agent AFK (https://github.com/griffinwork40/agent-afk)

## See Also

- [struct-explicit-terminal-states](struct-explicit-terminal-states.md) - terminal/paused states and evidence verdicts are only auditable if this receipt records them
- [eval-trace-to-deterministic-checks](eval-trace-to-deterministic-checks.md) - deterministic checks and failure-pattern mining consume this same trace
- [obs-agent-span-hierarchy](obs-agent-span-hierarchy.md) - parent/child span structure is what makes the receipt walkable as a narrative
- [guard-audit-log-every-decision](guard-audit-log-every-decision.md) - the security-audit variant: every authorization decision logged
