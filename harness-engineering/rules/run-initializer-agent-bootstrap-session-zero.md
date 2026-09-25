# run-initializer-agent-bootstrap-session-zero

> Give the very first agent session a different, specialized prompt whose only job is to set up the environment all later sessions will inherit — before any feature work begins.

## Why It Matters

- The initializer agent creates: an `init.sh` script that runs the dev server, a progress file logging what agents have done, an initial git commit, and an expanded feature list from the user's prompt.

- Rationale: a fresh high-level prompt ("build a claude.ai clone") makes agents one-shot the app and run out of context mid-feature, leaving undocumented half-work for the next session to guess at.

- The initializer and coding agents differ only in initial user prompt — system prompt, tools, and harness were otherwise identical; no special runtime needed.

- Anti-example from source: out of the box, even a frontier model (Opus 4.5) with compaction in a loop falls short of a production-quality app from a high-level prompt alone.

## Scope

- Apply when bootstrapping long-running multi-session builds: give session zero a specialized prompt whose only job is environment setup — init.sh, progress file, initial commit, expanded feature list — before any feature work.
- The initializer is a prompt-level distinction only: system prompt, tools, and harness were identical to coding sessions in the source — no special runtime needed.
- Skip for single-session or already-initialized work: the rationale (fresh high-level prompts make agents one-shot and run out of context mid-feature) doesn't apply once environment and feature list exist.

## Source

Anthropic, "Effective harnesses for long-running agents" (https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)

## See Also

- [run-feature-list-expanded-spec-with-pass-state](run-feature-list-expanded-spec-with-pass-state.md) - the initializer's key artifact: the expanded feature list with `passes: false` state that defines later sessions' work
- [run-make-the-app-legible-and-runnable-init-script](run-make-the-app-legible-and-runnable-init-script.md) - the other initializer artifact: init.sh makes every later session's smoke test and end-to-end verification possible
- [run-incremental-one-feature-at-a-time](run-incremental-one-feature-at-a-time.md) - what the initializer enables: one feature per session, each ending mergeable, instead of one-shotting the app
- [struct-bounded-single-task-loop](struct-bounded-single-task-loop.md) - the loop-architecture counterpart: same fresh-context, one-thing-per-iteration discipline, driven deterministically by an outer loop
