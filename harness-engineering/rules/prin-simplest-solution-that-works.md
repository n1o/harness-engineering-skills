# prin-simplest-solution-that-works

> Find the simplest solution possible and only increase complexity when it demonstrably improves outcomes — start with direct LLM API calls and composable patterns, not frameworks and autonomous agents.

## Why It Matters

- Distinguish workflows (LLMs orchestrated through predefined code paths — predictable for well-defined tasks) from agents (LLMs dynamically directing their own processes — for flexibility at scale); often a single optimized LLM call with retrieval is enough.

- Agentic systems trade latency and cost for task performance; decide explicitly when that trade makes sense.

- Frameworks add abstraction layers that obscure prompts and responses and make debugging harder; if used, understand the underlying code — incorrect assumptions about what's under the hood are a common source of failure.

- Known workflow patterns from source: prompt chaining (with programmatic gates), routing, parallelization (sectioning/voting), orchestrator-workers, evaluator-optimizer — compose them rather than reaching for a monolithic agent when a workflow suffices.

- When implementing agents, ground each step in "ground truth" from the environment (tool results, code execution) and include stopping conditions (e.g., max iterations) to maintain control.

- The awesome list's 'Operating Principles & Human Oversight' also contains '12-Factor AgentOps', 'Anchoring AI to a reference application', and Claude Code best-practices docs — outside my assigned slice per the task's explicit source list.

## Scope

- Apply at design time for any LLM task: default to the simplest solution — a workflow with predefined code paths, or a single well-prompted call with retrieval — and escalate to autonomous agents only when flexibility is worth the latency and cost trade.
- Skip agent machinery when the task is well-defined and predictable; reach for it when tasks demand dynamic process direction at scale.
- If a framework is used, understand the code under it — abstraction layers that obscure prompts and responses make debugging harder, and wrong assumptions about the hood are a common source of failure.

## Source

Anthropic, "Building effective agents" (https://www.anthropic.com/engineering/building-effective-agents)

## See Also

- [run-harness-component-attrition-on-model-upgrade](run-harness-component-attrition-on-model-upgrade.md) - boundary: this rule is simplicity-first at design time; that rule removes components whose load-bearing assumption died when the model improved — the useful-combination space moves, it doesn't shrink
- [prin-agent-equals-model-plus-harness](prin-agent-equals-model-plus-harness.md) - counterweight: what simplicity concedes (durable state, execution, realtime knowledge) must be supplied by harness features, not prompt wishes
- [prin-feedforward-guides-feedback-sensors](prin-feedforward-guides-feedback-sensors.md) - known named workflow patterns (chaining with gates, routing, evaluator-optimizer) are the composable middle ground between raw calls and monolithic agents
