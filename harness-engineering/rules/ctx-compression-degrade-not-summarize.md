# ctx-compression-degrade-not-summarize

> When compressing agent history, prefer rule-based lossy primitives — tool-result clearing with placeholders — over LLM summarization of history: clearing preserves near-full-context accuracy at a fraction of the cost, while LLM summarization costs accuracy and adds latency.

## Why It Matters

- A controlled study of 65 compression policies (primitive × trigger × depth) across three open-weight models on SWE-bench Verified and Terminal-Bench 1.0, ~35,000 runs: tool-result clearing (TRC) reaches approximately full-context resolve rate while using 0.57× the tokens, 0.79× the latency, and 0.71× the billed cost; LLM summarization (SU) uses a similar 0.59× tokens but drops resolve rate by 11.0 points (Beyond Token Savings: A Systematic Study of Context Compression in LLM Agents, arXiv 2609.32961).
- Token savings do not reliably translate into latency or cost savings: policies at similar token counts diverge — TRC bills 0.71× full context where OTRC (its partial variant) bills 0.95× — because summarization calls add their own wall-clock overhead (28–46% of solved-run time in some settings) (arXiv 2609.32961).
- LLM compression injects new generated content in place of observed evidence, so a summary error silently rewrites the agent's record of what happened; placeholder clearing keeps the true residue and marks the elision honestly (arXiv 2609.32961).
- Policy effects vary across models and per task — a policy helps some tasks and hurts others — so compression policy is a per-model measured variable, not a global default (arXiv 2609.32961).

## Scope

- Apply when choosing or tuning an in-window history compression mechanism for long-running coding agents; the study's harness is a modified mini-swe-agent, closest to that regime.
- "Clear, don't summarize" governs mechanical history pruning. When the goal is instead to carry forward a distilled working state across a context reset, a structured summary written to durable artifacts is the right tool — that is [ctx-frequent-intentional-compaction](ctx-frequent-intentional-compaction.md) and [ctx-structured-notes-across-resets](ctx-structured-notes-across-resets.md), a different operation at a phase boundary, not history compression.
- Design space is three-axis: primitive (what is removed/rewritten), trigger (when), depth (how much). State all three when reporting a compression result; a bare "we compact at 70%" is not a comparable policy spec (arXiv 2609.32961).
- Keep cleared tool results re-fetchable via pointers — see [ctx-filesystem-as-external-memory](ctx-filesystem-as-external-memory.md); a placeholder plus a re-fetch path degrades gracefully where a wrong summary cannot.
- System prompt and initial task instruction stay verbatim under all policies; compressible surface is accumulated assistant messages and tool results (arXiv 2609.32961).

## Source

Beyond Token Savings: A Systematic Study of Context Compression in LLM Agents (https://arxiv.org/abs/2609.32961)

## See Also

- [ctx-compaction-recall-then-precision](ctx-compaction-recall-then-precision.md) - already names tool-result clearing as the safest first lever; this rule adds the head-to-head numbers against LLM summarization
- [ctx-frequent-intentional-compaction](ctx-frequent-intentional-compaction.md) - boundary: phase-boundary compaction into durable artifacts (summary is fine there) vs in-window history compression (prefer clearing)
- [ctx-mask-tools-not-remove](ctx-mask-tools-not-remove.md) - the same placeholder-over-removal principle applied to tool definitions
- [ctx-keep-failures-in-context](ctx-keep-failures-in-context.md) - what compression must not clear: the error evidence the model still needs
- [ctx-filesystem-as-external-memory](ctx-filesystem-as-external-memory.md) - pointers make clearing reversible
