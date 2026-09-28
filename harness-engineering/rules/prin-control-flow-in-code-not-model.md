# prin-control-flow-in-code-not-model

> Put loops, branching, and sequencing in program code enforced by the runtime and invoke the LLM only at reasoning/generation points — never sample control flow from the model when the workflow's structure is known.

## Why It Matters

- LLM-as-orchestrator has three measured, structural pathologies in long-horizon tasks (LLM-as-Code, arXiv 2606.15874): token explosion (context grows with steps × average output), control-flow hallucination (invalid step-skipping, premature termination), and unreliable completion.
- Relocating control flow to code delivered 86.8% overall on OSWorld — beating the strongest prior system (80.4%) and general models (72.1%) — while using 15 steps against the baselines' 100 (2606.15874).
- Context becomes a call DAG scoped by depth: a running call sees its full ancestor chain while completed siblings collapse to one-line summaries, bounding input length by depth instead of by total steps (2606.15874).
- The paradigm inherits ordinary software guarantees: workflow logic becomes unit-testable, failures localize to named function calls, and self-improvement is committed as code only after passing deterministic tests — lessons persist as code instead of being re-sampled every run (2606.15874).
- The control point is a design decision, not a model-capability question: the authors frame it as "not what the LLM can do, but who should control execution," with the program as the answer for structured tasks (2606.15874).
- The boundary is stated by the authors themselves: the paradigm suits tasks with known/codifiable structure; fully exploratory work without a stage model may still need LLM-driven orchestration — measured default from this study, not a universal rule (2606.15874).

## Scope

- Apply to structured workflows — build-verify-fix loops, multi-file refactors, batch processing, GUI automation — where stages are known: write the loop in code, mark LLM call sites as typed functions with docstring contracts.
- Apply to long-horizon reliability problems that trace to the agent skipping steps, terminating early, or re-deciding a fixed sequence every turn.
- Skip for genuinely open-ended exploration with no stage model — the LLM's adaptive branching is the feature, not the bug.
- Skip for single shots with no iteration — there is no control flow to relocate.

## Source

LLM-as-Code: Agentic Programming for Agent Harness (https://arxiv.org/abs/2606.15874)

## See Also

- [prin-small-focused-agents](prin-small-focused-agents.md) - caps individual agent size within a mostly deterministic system; this rule is the architectural commitment that makes the system deterministic in the first place
- [prin-simplest-solution-that-works](prin-simplest-solution-that-works.md) - start with direct calls; graduate to a coded workflow only when reliability evidence demands it
- [ctx-subagent-context-isolation](ctx-subagent-context-isolation.md) - the DAG-of-calls with depth-scoped context is a concrete implementation of that isolation
- [struct-bounded-single-task-loop](struct-bounded-single-task-loop.md) - the bounded outer loop is the minimal coded-control-flow case; this rule generalizes it to branches and recursion
- [struct-harness-as-declared-config](struct-harness-as-declared-config.md) - the coded control flow is itself the declared, diffable harness artifact — code, not yaml, can still be the declared config surface
