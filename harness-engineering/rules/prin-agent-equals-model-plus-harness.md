# prin-agent-equals-model-plus-harness

> Define the harness as everything that isn't the model — and design it by working backwards from the desired agent behavior to a concrete harness feature.

## Why It Matters

- "If you're not the model, you're the harness": system prompts, tools/skills/MCPs and their descriptions, bundled infrastructure (filesystem, sandbox, browser), orchestration logic (subagents, handoffs, routing), and hooks/middleware for deterministic execution.

- Models out of the box cannot maintain durable state, execute code, access realtime knowledge, or set up environments — every one of those is a harness-level feature; convert each desired behavior into an actual harness feature.

- Derivation pattern from source: filesystem → durable storage and offloading of what doesn't fit in context; bash + code exec → general-purpose problem solving without pre-designing every tool; sandbox → safe, scalable, well-defaulted execution environments.

- The harness choice moves benchmark scores materially: the same model can rank far differently across harnesses (source: Top 30 → Top 5 on Terminal Bench 2.0 by only changing the harness) — so the best harness for a task isn't necessarily the one the model was post-trained with.

## Scope

- Apply when designing or debugging any agent system: every desired capability the model lacks out of the box — durable state, code execution, realtime knowledge, environment setup — is a harness feature to build, not a prompt to write.
- Work backwards from a desired agent behavior to a concrete harness feature; a feature with no behavior it serves is speculative weight.
- Skip adding harness machinery while the task already performs acceptably with the raw model — increase complexity only when it demonstrably improves outcomes (see prin-simplest-solution-that-works).

## Source

LangChain, "The Anatomy of an Agent Harness" (https://blog.langchain.com/the-anatomy-of-an-agent-harness/)

## See Also

- [prin-simplest-solution-that-works](prin-simplest-solution-that-works.md) - counterweight: start with direct calls and composed workflows; this rule says the complexity you do add belongs in the harness, not the prompt
- [struct-harness-as-declared-config](struct-harness-as-declared-config.md) - once a harness feature is identified, express it as versioned, inspectable config so the choice is diffable across runs
- [ver-harness-deltas-measured-by-evals](ver-harness-deltas-measured-by-evals.md) - how to prove a harness feature's worth: the same model ranked far differently across harnesses, so measure harness deltas with the model fixed
- [tool-descriptions-as-prompts](tool-descriptions-as-prompts.md) - tool and description design is part of the harness surface this rule tells you to own
