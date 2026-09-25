# ctx-stable-prefix-kv-cache

> Design context layout around the KV-cache: keep the prompt prefix stable, context append-only, and serialization deterministic — cache hit rate directly drives latency and 10x cost differences.

## Why It Matters

- Agent loops are prefill-dominated (Manus sees ~100:1 input:output token ratio), so prefix caching dominates cost/TTFT; cached vs uncached input was 0.30 vs 3.00 USD/MTok for Sonnet.

- Keep the system-prompt prefix stable; even a one-token difference invalidates the cache from that token onward. Anti-example: a second-precision timestamp at the top of the system prompt kills the cache to let the model tell time.

- Make context append-only: never rewrite previous actions/observations; use deterministic JSON serialization (many libraries don't guarantee key order and silently break the cache).

- Mark explicit cache breakpoints where the provider lacks automatic incremental caching, placing at minimum one at the end of the system prompt; self-hosted setups should enable prefix caching and route sessions consistently (session IDs).

## Scope

- Apply to any prefill-dominated agent loop (the source sees ~100:1 input:output) — cache hit rate directly drives cost and TTFT (0.30 vs 3.00 USD/MTok cached vs uncached for Sonnet, a measured default from Manus's setup).

- The discipline: stable system-prompt prefix (no timestamps, no one-token drift), append-only history, deterministic JSON serialization (many libraries don't guarantee key order), explicit cache breakpoints where the provider lacks incremental caching.

- Skip when sessions are single-shot (nothing to amortize a rebuild across), the provider bills/tokens are trivial, or a self-hosted stack lacks prefix caching — then only the layout hygiene pays.

## Source

Manus, Context Engineering for AI Agents: Lessons from Building Manus (https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus)

## See Also

- [ctx-mask-tools-not-remove](ctx-mask-tools-not-remove.md) - how to change the action space without invalidating this rule's cache: mask selection, never edit definitions mid-task.

- [ctx-condensation-threshold-cache-friendly](ctx-condensation-threshold-cache-friendly.md) - why condensation triggers at a threshold rather than every turn: each summary rebuilds the cache.

- [ctx-recitation-recenter-attention](ctx-recitation-recenter-attention.md) - recite by appending to the tail; rewriting the past would break this rule's append-only discipline.
