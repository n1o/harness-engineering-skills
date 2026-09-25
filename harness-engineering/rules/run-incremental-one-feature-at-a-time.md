# run-incremental-one-feature-at-a-time

> Constrain each coding session to make incremental progress on exactly one feature, and require the session to end in a mergeable clean state.

## Why It Matters

- "Clean state" means code appropriate for merging to main: no major bugs, orderly and documented, so a developer (or agent) can start a new feature without cleaning up an unrelated mess first.

- Elicit clean endings mechanically: commit to git with descriptive messages and write a progress summary at session end — this lets agents revert bad changes and recover working states.

- The incremental approach was "critical" to fixing the agent's tendency to attempt too much at once (one-shotting).

- Efficiency side effect: no session wastes tokens guessing what happened or repairing an undocumented broken state.

## Scope

- Apply to long unattended builds: constrain each session to incremental progress on exactly one feature, ending in a mergeable clean state — no major bugs, orderly and documented, so the next session starts clean.
- "One feature per session" is a measured default from the source for unsupervised long-running builds, not a universal cap — relax under supervision when the model reliably maintains quality, and re-tighten if sessions go off the rails.
- The mechanical ending is the enforcement: descriptive git commit plus a progress summary at session end, which is what lets agents revert bad changes and keeps later sessions from guessing at undocumented half-work.

## Source

Anthropic, "Effective harnesses for long-running agents" (https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)

## See Also

- [struct-bounded-single-task-loop](struct-bounded-single-task-loop.md) - boundary: session-level feature scoping vs the outer loop architecture; the loop hands the agent one task per fresh window, and its sources say the one-thing restriction is itself relaxable as the project progresses
- [run-feature-list-expanded-spec-with-pass-state](run-feature-list-expanded-spec-with-pass-state.md) - same source harness: the feature list defines "one feature" and its pass state; this rule constrains how much of it a session may touch
- [run-context-reset-handoff-artifacts-across-windows](run-context-reset-handoff-artifacts-across-windows.md) - the session-end summary and commit are the handoff artifacts the next window's startup reads

