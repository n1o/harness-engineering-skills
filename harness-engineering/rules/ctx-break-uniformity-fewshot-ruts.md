# ctx-break-uniformity-fewshot-ruts

> Contexts full of near-identical action-observation pairs few-shot the model into repeating the pattern even when it's wrong; introduce small structured variation (serialization templates, phrasing, ordering) in repetitive tasks.

## Why It Matters

- LLMs are mimics: reviewing 20 resumes, the agent fell into a rhythm of repeated similar actions purely because that's what filled its context — causing drift, overgeneralization, hallucination.

- Fix with controlled randomness: alternate serialization templates and phrasing, minor noise in order/format — "the more uniform your context, the more brittle your agent."

## Scope

- Apply in repetitive tasks where the window fills with near-identical action-observation pairs (the source's resume-review case): the uniform history few-shots the model into repeating the pattern even when it's wrong.

- Skip when steps are few or naturally heterogeneous — there is no dominant pattern to mimic, and added variation is noise without a drift problem to fix.

- The lever is deliberately small (alternate serialization templates, phrasing, ordering) — no architectural change, so try it when drift, overgeneralization, or hallucination symptoms appear in repetitive loops.

## Source

Manus (https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus)

## See Also

- [ctx-recitation-recenter-attention](ctx-recitation-recenter-attention.md) - counters the same in-loop drift, but by reciting objectives into the context tail rather than varying the action pattern.

- [ctx-stable-prefix-kv-cache](ctx-stable-prefix-kv-cache.md) - boundary: vary the shape of newly appended turns, never rewrite past ones — the cache-friendly append-only discipline still holds.
