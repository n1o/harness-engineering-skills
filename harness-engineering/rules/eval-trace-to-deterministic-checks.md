# eval-trace-to-deterministic-checks

> Convert captured agent traces (structured event streams) into deterministic, debuggable checks over what actually happened — not just the final output.

## Why It Matters

- Run the agent in a mode that emits a JSONL event stream (e.g. `codex exec --json`), save traces to disk, and write small deterministic checks over events: did it run `npm install`, did it create `package.json`, did commands run in the expected order.

- Everything is deterministic and debuggable: when a check fails, open the trace and see exactly what happened; regressions become explainable.

- Trace grading = assigning structured scores to the end-to-end record of decisions, tool calls, and reasoning steps; unlike black-box output evals it tells you *why* an agent succeeded or failed, and scales error identification across many runs.

- Extend gradually with heavier trace-derived checks only when they reduce risk: command-count/thrashing detection, token budgets, build checks, runtime smoke checks, repo cleanliness (`git status --porcelain` empty or allow-listed), and least-privilege/permission-escalation regressions.

- Start with fast checks that explain behavior; add slower, heavier checks selectively.

## Scope

- Apply whenever the harness can emit a JSONL event stream (e.g. `codex exec --json`) — save traces to disk and write small deterministic checks over events, not just final output.

- Extend gradually and only when a check reduces risk: command-count/thrashing, token budgets, build and runtime smoke checks, repo cleanliness; start with fast checks that explain behavior, add slower ones selectively.

- Keep checks over *what happened* (tool ran, file created), not exact orderings — path-sequence assertions are the known brittleness failure mode.

## Source

OpenAI 'Testing Agent Skills Systematically with Evals' (https://developers.openai.com/blog/eval-skills/); OpenAI 'Trace grading' (https://platform.openai.com/docs/guides/trace-grading)

## See Also

- [obs-portable-trace-conventions](obs-portable-trace-conventions.md) - traces as eval input here vs standardized traces as portable telemetry there; the same stream serves both
- [eval-grade-outcome-not-path](eval-grade-outcome-not-path.md) - outcome-first grading is the guardrail that keeps trace checks from hardening into rigid path-sequence assertions
- [eval-read-transcripts](eval-read-transcripts.md) - the manual counterpart: read traces to decide which checks deserve to become deterministic
- [struct-append-only-trace-receipt](struct-append-only-trace-receipt.md) - trace-on-disk is also the audit receipt; deterministic checks mine the same artifact
