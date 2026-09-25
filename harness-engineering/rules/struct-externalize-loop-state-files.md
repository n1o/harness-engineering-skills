# struct-externalize-loop-state-files

> Keep the loop's working state — plan, learnings, how-to-run knowledge — in files that every fresh iteration re-reads and re-writes, instead of in conversation memory.

## Why It Matters

- The prompt stack deterministically loads `fix_plan.md` (prioritized remaining work) and `specs/*` every loop; Ralph must "ALWAYS KEEP @fix_plan.md up to date with your learnings... especially after wrapping up/finishing your turn" and update `AGENT.md` when he learns a better way to run the build — so the next context window inherits the reasoning

- The primary context window acts as a scheduler: "spawn subagents" for expensive allocation work, with explicitly bounded parallelism — "only 1 subagent for build/tests" to avoid back-pressure, while search/write work may fan out

- Capture in-the-moment rationale: ask the agent to write why each test exists and matters when it writes the test, "leaving little notes for future iterations... because future loops will not have the reasoning in their context window" — this documentation later steers delete/modify/fix decisions on failing tests

- Document discovered bugs into the plan file even when unrelated to the current task, so nothing observed is lost when the window closes

- Anti-example: a plan that lives only in the session transcript — every crash or window rollover silently drops the plan

## Scope

- Apply to any loop with fresh context windows: the prompt stack must deterministically re-read the plan file and specs every iteration, and re-write them with learnings before the turn ends.

- Capture in-the-moment rationale (why each test exists, discovered bugs even when unrelated to the current task) — future loops will not have the reasoning in their context window.

- Skip for single-session interactive work where the conversation is the state — the discipline exists because every crash or window rollover silently drops unwritten plans.

## Source

Ralph (https://ghuntley.com/ralph/)

## See Also

- [ctx-structured-notes-across-resets](ctx-structured-notes-across-resets.md) - the same durable-state idea at context-engineering granularity: agent-written notes re-read after resets
- [run-context-reset-handoff-artifacts-across-windows](run-context-reset-handoff-artifacts-across-windows.md) - the bridge-session variant: structured handoff artifacts (progress file + git history + feature states) instead of compaction alone
- [struct-bounded-single-task-loop](struct-bounded-single-task-loop.md) - the loop that makes these files load-bearing — fresh windows inherit state only through them
