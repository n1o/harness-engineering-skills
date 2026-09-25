# ops-idempotent-side-effects-for-retry-resume

> Make side-effecting tool calls idempotent (server-recognized idempotency keys, upserts) and record their completion durably, so retries, resumes, and crash recovery don't duplicate real-world actions.

## Why It Matters

- Retry controls assume a failed call had no effect — but with external side effects (payments, emails, deploys, API writes) a timeout can mean "done but unconfirmed"; retrying then duplicates the action, and duplicating is not a model-judgment problem, it's a call-design problem.
- Give each side-effecting request an idempotency key the *server* recognizes atomically on replay (Stripe/AWS-style) — client-side check-before-act can race another worker and appends are a counterexample to 'running it twice is fine'.
- Separate "attempted" from "confirmed": a run that dies between the side effect and the record is exactly the window where naive restart duplicates work — Citadel measured 0 duplicate effects with journaled recovery versus 3 for naive restart across six injected boundaries (local fixtures; directionally indicative, not a general guarantee).
- Recovery reads the journal, not memory: on restart, check what was already confirmed done before re-attempting anything (the same discipline as `struct-orphan-recovery-heartbeat`, applied to the world outside the agent).
- Cancellation and deadlines are part of the same contract: a side-effecting call that can be retried must also be cancellable before the effect, and a run with a deadline must not start an effect it cannot wait to confirm.
- Compose with the failure controls: `ops-shared-retry-budget` caps retry volume, `ops-quarantine-poison-dont-recirculate` removes permanent failures — this rule makes the *individual retry* safe so those caps can run without human fear of duplication.

## Scope

- Apply to any tool call with external, non-undoable effects: payments, emails, deploys, third-party API writes, production mutations.
- Skip for work whose effects are recoverable by other means (git-tracked file edits, reads, local compute) — there the retry controls alone suffice. 'Recoverable' means a duplicate or lost effect is cheap to detect and undo, not that duplicates are impossible.
- Most valuable exactly where autonomous retry/resume is also enabled: unattended loops, fleet workers, crash-recovery paths.

## Source

Distributed retry patterns: bounding blast radius across a fleet (https://loopandretry.github.io/posts/fleet-retry-patterns/); Citadel (https://github.com/SethGammon/Citadel) - journaled-recovery duplicate-effect measurement

## See Also

- [ops-shared-retry-budget](ops-shared-retry-budget.md) - fleet-wide ceiling on retry volume
- [ops-quarantine-poison-dont-recirculate](ops-quarantine-poison-dont-recirculate.md) - classify errors before retrying; permanent failures leave the loop
- [struct-orphan-recovery-heartbeat](struct-orphan-recovery-heartbeat.md) - crash recovery for the work queue; this rule extends it to external side effects
- [struct-explicit-terminal-states](struct-explicit-terminal-states.md) - "unknown" is a valid verdict; never promote an unconfirmed effect to success
