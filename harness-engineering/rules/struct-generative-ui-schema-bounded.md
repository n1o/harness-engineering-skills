# struct-generative-ui-schema-bounded

> When an agent must surface state, results, or approvals to a human, have it emit a schema-validated declarative UI composition that a deterministic renderer instantiates from a vetted component inventory — the LLM plans, the renderer decides; never free-form generated UI code.

## Why It Matters

- Two-stage split (Portal UX Agent, arXiv 2511.00843): the LLM maps a natural-language spec to a typed JSON composition (template + component types + typed props in declared slots) that must validate against a schema; a deterministic renderer loads vetted templates and fills slots from a component inventory. Invalid compositions are rejected or repaired — no arbitrary code generation; every rendered surface is auditable and design-system-compliant.
- Bounded generation beat unconstrained prompting on reliability: fewer malformed DOM instances, inaccessible elements, and design-system violations than a free-form-code baseline (rubric means 4.42/5 overall, compositionality highest at 4.61/5) (2511.00843).
- Accessibility and performance become mechanically checkable: the evaluation includes explicit accessibility (ARIA labels, contrast ratios) and performance (render time, DOM complexity) dimensions — impossible to enforce on ad-hoc generated markup (2511.00843).
- Hard structural gates work: Macaron-A2UI (arXiv 2605.24830) gives malformed JSON and render-critical errors zero reward and uses deterministic validation + retry, achieving 99.2% renderability across 14,245 assistant turns with 189k component instances.
- The schema, not the model, carries protocol correctness: untuned frontier models score 25.5 on A2UI-Bench without schema hints vs 63.8 with full-schema prompts — a bounded surface degrades gracefully with weaker models instead of silently emitting broken UI (2605.24830).
- For harness engineering this is the human-facing counterpart of deterministic tooling: the agent's claim about state is data in typed props; the presentation is governed infrastructure — schema validation, accessibility checks, and slot-structure assertions can run in CI on what the human will actually see, making the surface itself a verification object.

## Scope

- Apply to agent products presenting results, plans, diffs, dashboards, or approval requests to humans; any harness where the human-facing surface is generated per task rather than static.
- Skip when a static hand-built UI already covers the interaction.
- Skip for terminal/CLI-only harnesses, or one-off internal artifacts never shown to a decision-making human.

## Source

Portal UX Agent (https://arxiv.org/abs/2511.00843); Macaron-A2UI (https://arxiv.org/abs/2605.24830)

## See Also

- [prin-contact-humans-with-tool-calls](prin-contact-humans-with-tool-calls.md) - structured tool calls govern agent→human requests; this rule governs the rendered surface those results appear in
- [run-make-the-app-legible-and-runnable-init-script](run-make-the-app-legible-and-runnable-init-script.md) - makes the app legible to the agent; this is the mirror image — a governed, legible surface for the human
- [ctx-deterministic-tools-before-llm](ctx-deterministic-tools-before-llm.md) - same division of labor — LLM plans, deterministic engine executes — applied to the human-facing output surface
- [guard-pre-action-deterministic-authorization](guard-pre-action-deterministic-authorization.md) - deterministic gate on the action path; this rule is the deterministic gate on the presentation path
