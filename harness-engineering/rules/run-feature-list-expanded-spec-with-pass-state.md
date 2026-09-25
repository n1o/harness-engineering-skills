# run-feature-list-expanded-spec-with-pass-state

> Have the initializer expand the user's prompt into a comprehensive structured feature list, all initially marked failing, so later agents have a mechanical definition of "done" and cannot declare premature victory.

## Why It Matters

- In the source example, a one-line prompt expanded to 200+ features like "a user can open a new chat, type a query, press enter, and see an AI response."

- Each feature is a JSON entry with a description, test steps, and a `passes: false` field; coding agents edit the file only by flipping `passes` after careful testing.

- Use strongly-worded instructions ("It is unacceptable to remove or edit tests") and prefer JSON over Markdown — the model is less likely to inappropriately overwrite structured JSON files.

- This directly counters the observed failure mode where a later agent sees prior progress and declares the whole project done.

## Scope

- Apply to long-running, multi-session builds: expand the user's prompt into a structured feature list (JSON with description, test steps, `passes: false`) so later agents get a mechanical definition of "done" and can't declare premature victory on inherited progress.
- Prefer JSON over Markdown and use strongly-worded instructions ("unacceptable to remove or edit tests") — per the source, the model is less likely to inappropriately overwrite structured JSON.
- Weight against breadth: the source's example expanded one line to 200+ features — worth it precisely because later agents saw prior progress and declared the project done; for single-session or already-precise specs the list adds mechanical overhead without new signal.

## Source

Anthropic, "Effective harnesses for long-running agents" (https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)

## See Also

- [run-incremental-one-feature-at-a-time](run-incremental-one-feature-at-a-time.md) - same source harness: each session makes incremental progress on exactly one feature; the feature list is what picks "which one" and carries pass state between sessions
- [run-self-verify-before-marking-done](run-self-verify-before-marking-done.md) - the gate on the `passes` flip: status changes only after careful end-to-end testing as a real user, not on the agent's say-so
- [run-initializer-agent-bootstrap-session-zero](run-initializer-agent-bootstrap-session-zero.md) - the initializer session that produces the expanded feature list before any feature work begins

