# struct-harness-as-declared-config

> Express the whole harness — prompts, tools, environment, policy — as versioned, inspectable configuration, and prefer the smallest config surface that reproduces the behavior.

## Why It Matters

- SWE-agent is "configurable & fully documented: governed by a single `yaml` file" — the agent-computer interface (tools, prompts, environment) is a reviewable artifact, which is what makes harness choices "directly inspectable" and comparable across runs

- The successor signal: mini-swe-agent "matches the performance of SWE-agent" in ~100 lines — when the config surface shrinks without losing behavior, the essential harness structure becomes visible and hackable

- Harbor makes evaluation declarative end to end: `harbor run --dataset <name>@<version> --agent <agent> --model <model>` against Docker or a cloud sandbox provider; each benchmark adapter ships a template (Dockerfile, instruction, solution, tests) and a `parity_experiment.json` recording how adapter behavior was matched across models — parity is an artifact, not a claim

- deepagents generalizes the layering: minimal harness (`create_agent`) → opinionated harness (deepagents) where every piece (prompts, middleware, sub-agents, backends) can be "extended, overridden, or replaced without forking"; and it pins the security stance: "trust the LLM" — "enforce boundaries at the tool/sandbox level, not by expecting the model to self-police"

- Anti-example: harness behavior defined by scattered code paths and undocumented defaults — impossible to diff two harness versions or reproduce a reported score

- **Harbor README**: thin as prose (mostly install/run commands); its codifiable patterns live in the repo structure — adapter templates and per-adapter parity experiments — which is what the struct-harness-as-declared-config rule uses.

- **deepagents README**: mostly feature marketing; used only for the harness-layering principle and the explicit trust-the-LLM/tool-boundary security stance.

- **AgentOps README**: the decorator-based span hierarchy and the session-root concept are the durable patterns; the rest is integration listings and roadmap tables.

- **SWE-agent README**: the strongest pattern is the single-YAML agent-computer interface plus the mini-swe-agent supersession warning — both folded into struct-harness-as-declared-config.

## Scope

- Apply to any harness you will compare, reproduce, or evolve: prompts, tools, environment, and policy as one versioned, inspectable config — the smallest surface that still reproduces the behavior (mini-swe-agent's ~100 lines made the essential structure visible).

- Prefer extension points over forks; enforce boundaries at the tool/sandbox level ("trust the LLM" only as a security stance paired with that), not by expecting the model to self-police.

- Anti-example is harness behavior defined by scattered code paths and undocumented defaults — if you can't diff two harness versions, you can't reproduce a reported score.

- **When to skip**: Applies to any harness you'll compare, reproduce, or hand to someone else; throwaway one-off scripts may stay as code.

## Source

SWE-agent (https://github.com/SWE-agent/SWE-agent); Harbor (https://github.com/harbor-framework/harbor); deepagents (https://github.com/langchain-ai/deepagents)

## See Also

- [ver-harness-deltas-measured-by-evals](ver-harness-deltas-measured-by-evals.md) - declared config is what makes harness deltas diffable and measurable with the model held fixed
- [obs-runtime-config-first-class-variable](obs-runtime-config-first-class-variable.md) - the runtime resource config that belongs in this declared surface
- [eval-clean-environment-per-trial](eval-clean-environment-per-trial.md) - environment templates as declared, reproducible config artifacts
- [guard-scope-based-tool-allowlists](guard-scope-based-tool-allowlists.md) - policy-as-declared-config on the security side: explicit tool allowlists, not prompt-level pleading
