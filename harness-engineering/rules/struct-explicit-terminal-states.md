# struct-explicit-terminal-states

> Model the harness as a small public state machine with explicit terminal/paused states, and never report success from missing evidence.

## Why It Matters

- Citadel's loop has five public states — Request, Run, Evidence, Needs You, Resume — where Needs You stops with "the exact approval, conflict, or missing evidence required" and Resume leaves repo-local state naming the next action for a fresh session

- Evidence verdicts are four-valued — `passed`, `failed`, `blocked`, or `unknown` — and "missing evidence is not promoted to success"

- completely's DONE is compositional: reported "only when the queue is empty, there are zero orphaned tasks, the tree is clean, and the union of the batch actually composes"; its run-report "never reports a half-done run as finished"

- Agent AFK's daemon pings the human only when work "lands in a terminal state" — the notification contract depends on terminal states being defined, not vibes

- Anti-example: "the agent said it's done" as a terminal state — assertion is not a state; only an independently verified (or explicitly blocked/unknown) outcome is

## Scope

- Apply to any harness with unattended or cross-session runs: model the loop as a small public state machine (Request/Run/Evidence/Needs You/Resume) with four-valued evidence verdicts (`passed`/`failed`/`blocked`/`unknown`).

- Missing evidence is never promoted to success — "the agent said it's done" is not a state; only an independently verified (or explicitly blocked/unknown) outcome is.

- The notification contract ("ping the human only on terminal state") only works if terminal states are defined; skip the formal machine for single-session interactive tools with no cross-session handoff.

## Source

Citadel (https://github.com/SethGammon/Citadel); completely (https://github.com/23ag1/completely); Agent AFK (https://github.com/griffinwork40/agent-afk)

## See Also

- [struct-append-only-trace-receipt](struct-append-only-trace-receipt.md) - states and verdicts are only auditable because the receipt records how each was reached
- [struct-default-fail-evaluator](struct-default-fail-evaluator.md) - what produces the `passed` verdict: independent evidence, default-FAIL
- [ver-self-verification-before-exit](ver-self-verification-before-exit.md) - the in-run verification pass that feeds the state machine's Evidence state
