# tool-namespacing-for-selection

> Group related tools under common prefixes (by service, then by resource) so agents pick the right tool among hundreds.

## Why It Matters

- Agents with dozens of MCP servers get confused when tools overlap or have vague purpose; namespacing delineates boundaries (e.g., `asana_projects_search` vs `asana_users_search`, `asana_search` vs `jira_search`).

- Naming scheme choice (prefix- vs suffix-based) had non-trivial, LLM-dependent effects on tool-use evaluations — pick it with your own evals, not by convention.

- Names that reflect natural subdivisions of tasks reduce both the tool descriptions loaded into context and the agent's risk of calling the wrong tool with the wrong parameters.

## Scope

- Apply once an agent faces dozens of MCP servers or hundreds of tools where overlap and vague purpose cause wrong-tool calls: group by service, then by resource (`asana_projects_search` vs `asana_users_search`) so boundaries are visible in the name itself.
- Prefix vs suffix is an empirical choice: the source measured non-trivial, LLM-dependent effects on tool-use evaluations — pick it with your own evals, not by convention.
- For a small, clearly distinct tool set the payoff shrinks — but namespacing still composes with discovery and masking, so a consistent prefix scheme is cheap to adopt early and expensive to retrofit.

- **When to skip**: Applies once the tool count makes selection ambiguous (rule of thumb from the source: dozens+); a 5-tool agent can stay flat.

## Source

Anthropic, Writing effective tools for agents (https://www.anthropic.com/engineering/writing-tools-for-agents)

## See Also

- [tool-progressive-tool-discovery](tool-progressive-tool-discovery.md) - stable prefixes make both masking and search-based discovery workable: discovery narrows candidates by prefix, masking enforces groups at selection
- [ctx-mask-tools-not-remove](ctx-mask-tools-not-remove.md) - namespacing is what makes whole groups enforceable or excludable at decoding time without stateful logits processors
- [tool-few-purposeful-tools](tool-few-purposeful-tools.md) - do the boundary work first: fewer, clearly purposed tools reduce the collisions namespacing has to disambiguate
- [tool-semantic-identifiers-over-uuids](tool-semantic-identifiers-over-uuids.md) - the same interpretability principle applied inside responses: names the model can reason over, not opaque IDs
