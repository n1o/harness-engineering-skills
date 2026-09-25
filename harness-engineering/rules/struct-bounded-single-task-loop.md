# struct-bounded-single-task-loop

> Drive long-running autonomy with a bounded outer loop that hands the agent exactly one task per iteration in a fresh context window — not one mega-session with an unbounded mandate.

## Why It Matters

- Ralph's core loop is `while :; do cat PROMPT.md | claude-code; done` — each iteration is a complete, fresh session; "ask Ralph to do one thing per loop. Only one thing... You may relax this restriction as the project progresses, but if it starts going off the rails, then you need to narrow it down"

- Each loop deterministically re-allocates the same stack every time — plan file plus specs are re-read per iteration, so iteration N has the same grounding as iteration 1 despite the fresh context

- completely runs the same shape with more governance: "a fresh `claude -p` per task over `bd ready` until empty", one fresh-context worker per queued task

- Why: the effective context budget is ~170k tokens; the more of it a session burns, the worse the outcomes — small bounded loops with fresh windows beat one long degrading session

- Anti-example: a single long-horizon session that keeps working "until done" — quality degrades as the window fills and a mid-run crash loses everything not yet externalized

## Scope

- Apply to long-running autonomy: one task per bounded outer-loop iteration in a fresh context window, with the plan file plus specs deterministically re-read each time.

- Relax the one-task restriction only as the project progresses; if it starts going off the rails, narrow it back down.

- Skip the loop shape for interactive or short tasks that fit one window — the pattern exists because the effective context budget (~170k tokens in the source) degrades outcomes as a session burns it.

## Source

Ralph (https://ghuntley.com/ralph/); completely (https://github.com/23ag1/completely)

## See Also

- [prin-small-focused-agents](prin-small-focused-agents.md) - the same context-degradation argument at agent granularity (3–10, maybe 20 steps); this rule is the loop-level expression
- [run-incremental-one-feature-at-a-time](run-incremental-one-feature-at-a-time.md) - the task-size constraint from the human-in-the-loop side: one feature, mergeable clean state
- [struct-externalize-loop-state-files](struct-externalize-loop-state-files.md) - fresh windows only work because state lives in files, not conversation memory
