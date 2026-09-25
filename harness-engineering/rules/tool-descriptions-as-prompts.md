# tool-descriptions-as-prompts

> Write tool descriptions and parameter schemas like onboarding docs for a new hire: explicit, unambiguous, and enforced by strict data models.

## Why It Matters

- Descriptions are loaded into context and collectively steer tool-calling behavior; make implicit knowledge explicit (query formats, niche terminology, resource relationships).

- Name parameters unambiguously: `user_id`, not `user`; enforce expected inputs/outputs with strict schemas.

- Small description refinements yield dramatic results: precise tool-description edits gave Claude Sonnet 3.5 state-of-the-art SWE-bench Verified performance.

- Measure description changes with evaluations rather than intuition; use MCP tool annotations to disclose open-world access or destructive effects.

## Scope

- Apply to every tool you expect a model to call: descriptions and parameter schemas are loaded into context and collectively steer calling behavior — write them like onboarding docs (explicit, unambiguous, strict data models), with unambiguous parameter names (`user_id`, not `user`).
- Small edits yield disproportionate results (the source's SWE-bench jump came from description refinements), so iterate them with evaluations rather than intuition; use MCP tool annotations to disclose open-world access or destructive effects.
- Not a substitute for tool *design* — when metrics keep showing the same failure, the fix may be consolidation or response shaping rather than more words in the description.

- **When to skip**: Applies to every agent-facing tool; there is no honest skip case — even one tool has a description.

## Source

Anthropic, Writing effective tools for agents (https://www.anthropic.com/engineering/writing-tools-for-agents)

## See Also

- [tool-eval-driven-tool-iteration](tool-eval-driven-tool-iteration.md) - the measurement loop that tells you whether a description edit worked; never tune descriptions by intuition
- [tool-namespacing-for-selection](tool-namespacing-for-selection.md) - names are the shortest descriptions: prefixes steer selection and reduce the description text that must be loaded
- [tool-few-purposeful-tools](tool-few-purposeful-tools.md) - boundary: consolidate the tool before writing more description — a clearer tool beats a longer description for an overlapping one
- [tool-bounded-token-efficient-responses](tool-bounded-token-efficient-responses.md) - the other side of the contract: what the tool says when it answers, not what it advertises before being called
