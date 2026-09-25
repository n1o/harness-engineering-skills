# run-mechanical-invariants-linter-messages-as-injections

> Enforce architectural invariants mechanically (custom linters, structural tests, validated dependency directions) instead of micromanaging implementations — and write the lint error messages to inject remediation instructions into agent context.

## Why It Matters

- OpenAI's model: rigid layered architecture per business domain (Types → Config → Repo → Service → Runtime → UI) with strictly validated dependency directions, cross-cutting concerns entering only through a Providers interface — enforced by custom linters and structural tests, not documentation goodwill.

- The OpenAI team required outcomes (parse data at the boundary) not methods (didn't mandate a specific validation library) — enforce boundaries centrally, allow autonomy locally.

- Rules that feel pedantic in human-first workflows become multipliers with agents: once encoded, they apply everywhere at once.

- Fowler frames the same move as "a positive kind of prompt injection": custom linter messages that include instructions for self-correction are feedback sensors optimized for LLM consumption.

## Scope

- Apply to architectural invariants worth enforcing across a codebase: dependency directions, layering, cross-cutting-concern boundaries — enforced by custom linters and structural tests, not documentation goodwill.
- Write lint error messages as remediation instructions: the message is injected into agent context, so it's a feedback sensor optimized for LLM consumption, not prose for humans.
- Require outcomes, not methods (enforce "parse data at the boundary" centrally; don't mandate a library) — rules that feel pedantic in human-first workflows become multipliers with agents: once encoded, they apply everywhere at once.

## Source

OpenAI, "Harness engineering: leveraging Codex in an agent-first world" (https://openai.com/index/harness-engineering/); Birgitta Böckeler/Thoughtworks, "Harness engineering for coding agent users" (https://martinfowler.com/articles/harness-engineering.html)

## See Also

- [ctx-deterministic-tools-before-llm](ctx-deterministic-tools-before-llm.md) - boundary: that rule says never send the LLM to do a linter's job (style/formatting mechanics); this rule is the architectural-invariant subset worth encoding — with messages written for the agent to self-correct
- [prin-feedforward-guides-feedback-sensors](prin-feedforward-guides-feedback-sensors.md) - framing: enforced invariants are the guides; instruction-bearing lint messages are the feedback sensors
- [run-entropy-garbage-collection-cadence](run-entropy-garbage-collection-cadence.md) - the recurring counterpart: encoding taste as golden principles + scanning agents keeps drift from reintroducing the violations linters catch
- [ver-in-loop-internal-quality](ver-in-loop-internal-quality.md) - why mechanical beats review: semantic damage (non-idiomatic "fixes") is invisible to the type system and must be caught in-loop

