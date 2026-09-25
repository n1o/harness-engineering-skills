# guard-scope-based-tool-allowlists

> Define per-agent-role scopes with explicit allowed/blocked tool lists; blocked tools must be undiscoverable, not merely uncallable.

## Why It Matters

- scope.yaml declares, per scope (e.g., `support-agent` read-only vs `developer` broad-with-blocklist), which tools on each upstream server are allowed; `developer` allows `"*"` but blocks `delete_file`, `push_files`, `pg_drop_table`, `pg_truncate`.

- Enforce at the tool-exposure layer: blocked tools are excluded from search results entirely so the model never sees them — this prevents both discovery-time confusion and call-time attempts.

- One proxy serves many upstream servers with per-server auth, so scoping, secrets, and audit live in one inspectable config rather than scattered client settings.

- The scope concept generalizes: an agent's autonomy should be a property of its assigned role, not of the full set of tools that happen to be installed.

## Scope

- Apply when one harness serves multiple agent roles (read-only support vs developer-with-blocklist) or many upstream MCP servers: per-scope allowed/blocked tool lists make autonomy a property of the assigned role, not of what happens to be installed.
- Blocked tools must be undiscoverable, not merely uncallable — excluded from search results entirely, preventing both discovery-time confusion and call-time attempts; a blocklist that still shows the tool fails the rule.
- Worth the proxy layer once scopes, per-server auth, or audit need one place to live; for a single-agent, single-server setup the same effect can often be had from the client's own tool config.

## Source

mcp-guardian (https://github.com/S1LV3RJ1NX/mcp-guardian)

## See Also

- [guard-pre-action-deterministic-authorization](guard-pre-action-deterministic-authorization.md) - the enforcement point: the scope's allow/block decisions must run in a deterministic pre-call hook, not in instructions
- [ctx-mask-tools-not-remove](ctx-mask-tools-not-remove.md) - boundary: static role scoping removes tools from the surface up front; that rule masks selection of already-loaded tools mid-task without cache-breaking churn
- [guard-audit-log-every-decision](guard-audit-log-every-decision.md) - each scoped allow/deny execution is a decision worth logging with its parameters and scope
- [tool-progressive-tool-discovery](tool-progressive-tool-discovery.md) - the compatible complement: scopes filter what can ever be discovered; progressive discovery then loads only what the task needs
