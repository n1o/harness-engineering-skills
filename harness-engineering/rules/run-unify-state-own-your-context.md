# run-unify-state-own-your-context

> Keep one source of truth for agent state — the thread/context window as a serializable event log — so that execution state, business state, pausing, resuming, forking, and debugging all fall out trivially.

## Why It Matters

- Execution state (current step, waiting status, retry counts) is usually just metadata about what has happened; engineer the app so it can be inferred from the context window instead of maintaining a parallel state machine.

- Benefits listed in source: one source of truth, trivial serialization, full history visible in one place, easy new-event types, resume from any point by loading the thread, fork by copying a subset of events, and easy rendering into human-readable UI for observability.

- Own the context format itself (don't accept the framework's default message layout): structure events into the most token- and attention-efficient representation, and consider hiding resolved errors/failed calls from context once they're no longer useful.

- Minimize things that can't live in context (session IDs, secrets), but don't aim for zero — the goal is one reviewable, replayable record.

## Scope

- Apply to any agent application with meaningful execution state: make the thread/context window the serializable event log and single source of truth — pausing, resuming, forking, and debugging fall out of it.
- Owning the context format is part of it: structure events into the most token- and attention-efficient representation, including hiding resolved errors and failed calls once they're no longer useful.
- Don't aim for zero things outside context (session IDs, secrets can't live there) — the goal is one reviewable, replayable record; skip the discipline only where execution state is trivial enough to re-derive from scratch.

## Source

HumanLayer, "12 Factor Agents" (https://www.humanlayer.dev/blog/12-factor-agents)

## See Also

- [run-pause-resume-between-selection-and-execution](run-pause-resume-between-selection-and-execution.md) - same 12FA source: interrupting between selection and execution is only cheap because the thread is the resumable record
- [prin-compact-errors-bounded-retries](prin-compact-errors-bounded-retries.md) - same 12FA source: error representation — what stays, what's compacted, what's hidden — is part of owning the context format
- [ctx-structured-notes-across-resets](ctx-structured-notes-across-resets.md) - boundary: the thread is the source of truth inside a run; durable notes/files carry working state across resets and summaries
- [struct-externalize-loop-state-files](struct-externalize-loop-state-files.md) - the bounded-loop application: plan and specs re-read from files each fresh iteration because a fresh window re-derives state from artifacts
