# ctx-recitation-recenter-attention

> Manipulate attention by reciting: repeatedly rewriting the current plan/todo at the end of context pushes global objectives back into the model's recent attention span, countering lost-in-the-middle drift in long loops.

## Why It Matters

- A typical Manus task runs ~50 tool calls; over long loops the agent drifts off-topic and forgets earlier goals.

- Rewriting todo.md step-by-step (checking off completed items) recites objectives into the context tail — natural-language attention biasing with no architectural changes.

- This is a deliberate mechanism, not cosmetic; it reduces goal misalignment and lost-in-the-middle failures.

## Scope

- Apply in long tool-call loops (the source's typical task runs ~50 calls) where the agent drifts off-topic and forgets earlier goals: rewrite the current plan/todo at the context tail to push objectives back into recent attention.

- Skip for short tasks — there's no drift to counter, and recitation is pure overhead.

- The mechanism is natural-language attention biasing with no architectural change: it deliberately rewrites the tail (new content), not the past — keeping the prefix cache discipline intact is on you.

## Source

Manus (https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus)

## See Also

- [ctx-stable-prefix-kv-cache](ctx-stable-prefix-kv-cache.md) - boundary: recite by appending to the tail; the stable prefix must stay untouched or the cache dies.

- [ctx-break-uniformity-fewshot-ruts](ctx-break-uniformity-fewshot-ruts.md) - same drift problem from the other side: vary repetitive action patterns vs recite objectives.

- [ctx-structured-notes-across-resets](ctx-structured-notes-across-resets.md) - when the todo list lives in a file, recitation and reset-survival become the same practice.
