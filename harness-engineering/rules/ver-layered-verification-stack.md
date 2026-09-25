# ver-layered-verification-stack

> Treat verification as a stack of layered verifiers that let coding agents fail fast and produce mergeable changes — trajectory-level critics, patch-level checks, and process guardrails composed together.

## Why It Matters

- OpenHands layer 1: a small, fast (sub-second to ~1s) trajectory-level critic scoring the whole run (conversation, tool calls, actions) — usable interactively to continue/stop/refine. Layer 2 (follow-up): surgical patch-level checks for repo conventions and common footguns.

- Layering composes with cheap process guardrails: loop-detection middleware tracks per-file edit counts via tool-call hooks and injects "…consider reconsidering your approach" after N edits to the same file, breaking doom loops (10+ near-identical retries observed in traces).

- Time-budget warnings nudge agents to stop building and shift to verification — agents are famously bad at time estimation without injected knowledge of constraints.

- Treat these guardrails as explicitly temporary engineering around current model weaknesses — they will likely dissolve as models improve, but today they're what makes autonomous execution reliable.

## Scope

- Apply to coding-agent runs that should fail fast and produce mergeable changes: fast trajectory-level critic (sub-second to ~1s) first, surgical patch-level checks second, cheap process guardrails composed around them.

- Keep each layer cheap enough to stay in the loop — loop-detection middleware and time-budget warnings are lightweight nudges, not heavyweight verification.

- Treat the guardrails as explicitly temporary engineering around current model weaknesses; re-evaluate them as models improve. Skip layers the model has outgrown.

## Source

OpenHands 'Learning to Verify AI-Generated Code' (https://openhands.dev/blog/20260305-learning-to-verify-ai-generated-code); LangChain 'Improving Deep Agents with harness engineering' (https://blog.langchain.com/improving-deep-agents-with-harness-engineering/)

## See Also

- [ver-train-verifiers-on-production-traces](ver-train-verifiers-on-production-traces.md) - how the layer-1 critic gets trained so it scores production outcomes, not benchmark artifacts
- [ver-in-loop-internal-quality](ver-in-loop-internal-quality.md) - the semantic-damage class that patch-level checks must also cover
- [struct-backpressure-verification-gates](struct-backpressure-verification-gates.md) - deterministic backpressure composes with these learned critics
