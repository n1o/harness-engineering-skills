# tool-eval-driven-tool-iteration

> Improve tools with an evaluation loop: realistic multi-call tasks, verifiable outcomes, held-out test sets, and transcript analysis — not one-off vibes.

## Why It Matters

- Generate eval tasks grounded in real-world uses and realistic data; strong tasks require potentially dozens of tool calls; avoid toy sandbox environments.

- Pair each task with a verifiable outcome, but avoid over-strict verifiers that reject correct answers over formatting; don't overspecify expected tool sequences since multiple valid paths exist.

- Track per-call runtime, number of tool calls, token consumption, and tool errors; read raw transcripts (not just agent self-reports — what agents omit matters more than what they include).

- Use held-out test sets to avoid overfitting; the source reports beating expert human-written tools with agent-optimized ones verified this way.

## Scope

- Apply to any tool-surface change worth trusting: eval tasks grounded in real-world uses and realistic data (potentially dozens of tool calls, no toy sandboxes), each paired with a verifiable outcome.
- Avoid the two measurement traps from the source: over-strict verifiers that reject correct answers over formatting, and overspecified expected tool sequences when multiple valid paths exist.
- Read raw transcripts, not agent self-reports — what agents omit matters more than what they include; track per-call runtime, tool-call count, token consumption, and tool errors, and keep a held-out set to avoid overfitting.

- **When to skip**: Applies once tools are used at scale or errors are costly; early prototypes can iterate on vibes.

## Source

Anthropic, Writing effective tools for agents (https://www.anthropic.com/engineering/writing-tools-for-agents)

## See Also

- [eval-no-skill-baseline](eval-no-skill-baseline.md) - the baseline discipline applies to tool changes too: without a pre-change baseline, an improved score says almost nothing
- [eval-read-transcripts](eval-read-transcripts.md) - the transcript-reading half of the loop: scores say whether, transcripts say why and what to fix
- [tool-descriptions-as-prompts](tool-descriptions-as-prompts.md) - description edits are the smallest tool changes this loop should measure — never tuned by intuition
- [ver-harness-deltas-measured-by-evals](ver-harness-deltas-measured-by-evals.md) - the harness-level version of the same measure-the-delta discipline
