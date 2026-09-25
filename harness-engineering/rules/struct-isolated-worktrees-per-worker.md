# struct-isolated-worktrees-per-worker

> Give each parallel agent its own isolated git worktree with a declared write scope, then select results by evidence — tests pass plus smallest net change.

## Why It Matters

- `afk farm` "spawns N isolated git worktrees, runs an agent on each in parallel, scores the results (tests + lint + LoC delta), and prints a ranked summary"; "the winner (branch that passes tests and makes the smallest net change) is surfaced; the rest are left for manual cherry-pick or deletion"; a commit-count escape check confirms each agent did real work

- completely serializes by write scope: "tasks with disjoint write-zones run concurrently; same-file ones serialize", enforced by the edit-time write-zone fence — isolation is declared up front, not discovered at merge time

- An integration gate runs after each parallel batch before the batch's union is accepted as done

- Citadel coordinates fleets the same way: "isolated worktrees, ownership, and shared discoveries" for "several agents or branches", keeping operational state (`.planning/`) separate from application code

- Why worktrees rather than branches-in-place: a shared checkout means parallel agents corrupt each other's working state; the worktree is the cheap, disposable isolation unit

## Scope

- Apply whenever agents run in parallel on one repo: each worker gets its own worktree plus a declared write scope; disjoint zones run concurrently, same-file tasks serialize.

- Select by evidence — tests pass plus smallest net change — with a commit-count escape check that each agent did real work; an integration gate runs after each batch before its union is accepted.

- Skip parallel worktrees when tasks touch the same files anyway (serialization dominates) or for a single agent — a shared checkout only corrupts state when two writers exist.

## Source

Agent AFK (https://github.com/griffinwork40/agent-afk); completely (https://github.com/23ag1/completely); Citadel (https://github.com/SethGammon/Citadel)

## See Also

- [struct-deterministic-exit-code-gates](struct-deterministic-exit-code-gates.md) - the write-zone fence is an edit-time exit-code gate, not a convention
- [struct-orphan-recovery-heartbeat](struct-orphan-recovery-heartbeat.md) - parallel workers are exactly the population that dies mid-task and needs claim recovery
- [struct-append-only-trace-receipt](struct-append-only-trace-receipt.md) - per-worker traces are how the ranked summary and cherry-pick decisions stay auditable
