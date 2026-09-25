# run-context-reset-handoff-artifacts-across-windows

> When work spans many context windows, bridge sessions with structured handoff artifacts (progress file + git history + feature states) rather than relying on compaction alone; use full context resets when the model exhibits "context anxiety."

## Why It Matters

- Compaction summarizes in place but doesn't give a clean slate; models can lose coherence on lengthy tasks and start wrapping up prematurely as they approach their perceived limit (context anxiety).

- A context reset — fresh agent plus a structured handoff carrying previous state and next steps — addresses both, at the cost of orchestration complexity, token overhead, and latency; the handoff artifact must carry enough state for the next agent to pick up cleanly.

- The source team found Sonnet 4.5 exhibited context anxiety strongly enough that compaction alone was insufficient, so resets became essential; Opus 4.5 removed the behavior, letting them drop resets entirely.

- Concrete session-start evidence from source: agent runs `pwd`, reads `claude-progress.txt`, reads `feature_list.json`, checks `git log --oneline -20`, runs `init.sh`, and smoke-tests core functionality before starting new work.

## Scope

- Apply to work that spans many context windows — long-running builds where sessions must pick up cleanly from a prior one via a structured handoff (progress file + git history + feature states).
- Reset vs compaction-in-place: per the source, full resets with handoff artifacts are for models exhibiting context anxiety (wrapping up prematurely near the perceived limit); when the model doesn't show it, compaction alone suffices — Opus 4.5 dropped resets entirely once the behavior was gone.
- Weigh the overhead: resets cost orchestration complexity, tokens, and latency, and the handoff must carry enough state for a clean pickup — skip them for single-window tasks and models without the failure mode.

## Source

Anthropic, "Effective harnesses for long-running agents" (https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents); Anthropic, "Harness design for long-running application development" (https://www.anthropic.com/engineering/harness-design-long-running-apps)

## See Also

- [ctx-frequent-intentional-compaction](ctx-frequent-intentional-compaction.md) - boundary: compaction-in-place vs full resets with handoff artifacts; resets when the model shows context anxiety, compaction when it doesn't — per the source
- [ctx-structured-notes-across-resets](ctx-structured-notes-across-resets.md) - the durable state inside the handoff: notes/progress files written before the reset and re-read after it
- [struct-externalize-loop-state-files](struct-externalize-loop-state-files.md) - the loop-architecture version of the same discipline: plan and specs re-read by every fresh iteration so N has the same grounding as 1
- [run-incremental-one-feature-at-a-time](run-incremental-one-feature-at-a-time.md) - same source harness: sessions end mergeable with a progress summary, which is exactly the artifact the next session's startup reads

