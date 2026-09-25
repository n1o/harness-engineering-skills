# struct-orphan-recovery-heartbeat

> Assume unattended workers die mid-task; detect orphans via heartbeats and reopen their claims on the next run instead of losing or duplicating the work.

## Why It Matters

- completely: "`worker_id` + heartbeat orphan recovery (a session that dies mid-task is auto-reopened on the next run)" — `cmpl orphans` lists and `--reap` reopens tasks a dead run left claimed; the repo reports it "survives session limits / crashes via heartbeat-based orphan recovery"

- Stall detection must be activity-based so "a busy worker is never false-killed" — liveness is evidenced by observable work, not wall-clock silence alone

- Ralph's recovery posture for the broken-codebase case: judge whether to `git reset --hard` to the last committed checkpoint and restart the loop, or craft new prompts to rescue — possible only because the loop commits on green (see struct-backpressure rule)

- Citadel measured the failure mode this guards against: "journaled recovery produced 0 duplicate effects versus 3 for naive restart across six injected boundaries"

- Anti-example: task claims held only in a live session's memory — a crash orphans the task invisibly and the next run either skips it or redoes it with side effects

## Scope

- Apply to any fleet where workers hold task claims: heartbeats detect orphans, the next run reopens their claims (`cmpl orphans` / `--reap`), so a dead session neither skips nor duplicates work.

- Stall detection must be activity-based — a busy worker is never false-killed; liveness is observable work, not wall-clock silence alone.

- This is work-queue recovery (claims in shared state); it does not itself make external side effects safe — that's the idempotency rule's job.

## Source

completely (https://github.com/23ag1/completely); Agent AFK (https://github.com/griffinwork40/agent-afk); Ralph (https://ghuntley.com/ralph/)

## See Also

- [ops-idempotent-side-effects-for-retry-resume](ops-idempotent-side-effects-for-retry-resume.md) - the boundary: this rule recovers the work queue; that rule makes the re-executed external side effects safe
- [struct-isolated-worktrees-per-worker](struct-isolated-worktrees-per-worker.md) - the parallel-worker population this recovery exists for
- [struct-backpressure-verification-gates](struct-backpressure-verification-gates.md) - commit-on-green checkpoints are what make `git reset --hard` recovery to a known state possible
- [struct-explicit-terminal-states](struct-explicit-terminal-states.md) - orphaned tasks must land in an explicit state (reopened), never silently vanish
