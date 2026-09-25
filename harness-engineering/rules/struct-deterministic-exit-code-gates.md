# struct-deterministic-exit-code-gates

> Enforce the quality floor with deterministic hooks that exit non-zero — gates the model cannot talk its way past — covering edits, dangerous commands, write scopes, commits, and budget.

## Why It Matters

- completely's gates: lint + types on **every edit**; a dangerous-command block (`rm -rf`, force-push); a commit-before-close rule (`bd close` refused while the tree is dirty); an edit-time write-zone fence (a worker cannot write outside its declared files); binding reviewer findings (no closure over unresolved CRITICAL/HIGH) — all exit-2 hooks the agent can't skip

- Prompts alone don't enforce: "a longer `CLAUDE.md` doesn't fix it (an essay nobody execute)" — completely fixes the failure modes "by engineering the environment so they can't happen"

- Bound spend mechanically too: Agent AFK's per-task `AFK_MAX_BUDGET_USD` rail stops a runaway task, and `--max-turns` caps loop iterations — resource ceilings are harness state, not model judgment

- Ship a doctor/self-check (`cmpl doctor`, `afk doctor`) that verifies the gates and dependencies actually work before an unattended run depends on them

## Scope

- Apply wherever the model could otherwise talk its way past a rule: lint + types on every edit, dangerous-command blocks, commit-before-close, edit-time write-zone fences, binding reviewer findings, budget ceilings.

- Prompts alone don't enforce — "a longer `CLAUDE.md` doesn't fix it (an essay nobody executes)"; if a rule can be enforced as an exit-2 hook, engineering the environment beats asking the model.

- Ship a doctor/self-check before an unattended run depends on the gates — skip gating only for fully human-supervised sessions where the operator is the enforcement.

## Source

completely (https://github.com/23ag1/completely); Agent AFK (https://github.com/griffinwork40/agent-afk)

## See Also

- [struct-backpressure-verification-gates](struct-backpressure-verification-gates.md) - the boundary: tests-as-backpressure inside the loop (fast, per-unit, commit on green) vs these hooks-as-hard-gates the model can't skip
- [struct-isolated-worktrees-per-worker](struct-isolated-worktrees-per-worker.md) - the write-zone fence is one of these gates, applied per parallel worker
- [guard-pre-action-deterministic-authorization](guard-pre-action-deterministic-authorization.md) - the security-side expression: authorize deterministically before the action, not by model judgment
