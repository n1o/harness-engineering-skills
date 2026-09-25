# ctx-illusion-of-control-probabilities

> Treat instruction files and prompts as probability-shifters, not guarantees: no amount of context "ensures" behavior, so pick the human-oversight level appropriate to the failure cost, and use deterministic enforcement where determinism is required.

## Why It Matters

- "Ensure it does X" / "prevent hallucinations" framing overpromises; execution always depends on how the LLM interprets instructions — think in probabilities.

- Pair probabilistic context with deterministic mechanisms: hooks for must-fire checks, logit masking/prefill for must-not-happen actions, linters for style.

- Beware copied-from-strangers configurations: low awareness of your own context breeds repeated or contradictory instructions — and the agent gets blamed for faithfully following them.

## Scope

- Apply when writing or reviewing instruction content — especially "ensure/prevent/hallucination-proof" framing — and when choosing how much human oversight a given failure cost requires.

- Skip the probabilistic framing where a deterministic mechanism already exists: hooks for must-fire checks, logit masking/prefill for must-not-happen actions, linters for style — determinism first, prose second.

- Treat it as a standing audit for copied-from-strangers configurations: low awareness of your own context breeds repeated or contradictory instructions.

## Source

Martin Fowler, "Context Engineering for Coding Agents" (https://martinfowler.com/articles/exploring-gen-ai/context-engineering-coding-agents.html); Manus, "Context Engineering for AI Agents" (https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus)

## See Also

- [guard-hard-policies-over-model-judgment](guard-hard-policies-over-model-judgment.md) - the security-critical end of the same spectrum: deterministic policy over trained common sense.

- [ctx-deterministic-tools-before-llm](ctx-deterministic-tools-before-llm.md) - the style/mechanical instance: linters and hooks, not instruction-file prose.

- [ctx-context-load-ownership](ctx-context-load-ownership.md) - the trigger-side corollary: match load determinism to criticality instead of trusting the model to load probabilistically.
