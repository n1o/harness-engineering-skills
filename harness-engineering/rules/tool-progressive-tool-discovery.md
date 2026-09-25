# tool-progressive-tool-discovery

> Don't load every tool definition upfront; expose search/get-schema/execute meta-tools or a browsable tool surface so the agent loads only what the current task needs.

## Why It Matters

- Loading all tool definitions upfront means an agent with thousands of tools processes hundreds of thousands of tokens before reading the request.

- Meta-tool variant: `search_tools(query)` with a detail-level parameter (name only / name+description / full schema), `get_schema`, `execute_tool` — mcp-guardian measured 160,143 → 456 tokens (99.7% reduction), break-even at ~39 tools.

- Code variant: present MCP servers as a file tree of typed functions; the agent lists directories and reads only the tool files it needs (source measured 150,000 → 2,000 tokens, 98.7% saving).

- Progressive discovery can be done at the infrastructure layer (proxy) with no client changes, or in the server itself; choose based on whether you control the client, the server, or neither.

## Scope

- Apply once the upfront definitions cost more than discovery: with thousands of tools, hundreds of thousands of tokens load before the request is read; the source measured 160,143 → 456 tokens via meta-tools (99.7% reduction) and 150,000 → 2,000 via a browsable file-tree — treat those break-evens (~39 tools) as measured defaults from those sources, not universal constants.
- Skip when the tool set is small and stable — the fixed cost of meta-tool indirection (`search_tools`/`get_schema`/`execute_tool` round-trips) outweighs the token savings.
- Implementation location is a deployment choice: proxy infrastructure with no client changes, or in the server itself — choose based on whether you control the client, the server, or neither.

## Source

Anthropic, Code execution with MCP (https://www.anthropic.com/engineering/code-execution-with-mcp); mcp-guardian (https://github.com/S1LV3RJ1NX/mcp-guardian)

## See Also

- [ctx-mask-tools-not-remove](ctx-mask-tools-not-remove.md) - boundary: that rule masks selection of already-present tools mid-task to protect the cache; this one loads definitions on demand so they're never in context — they compose (fixed discoverable surface + masking, never mid-task churn)
- [tool-namespacing-for-selection](tool-namespacing-for-selection.md) - stable prefixes make both workable: search-based discovery narrows by prefix, and masking can enforce or exclude whole groups
- [guard-scope-based-tool-allowlists](guard-scope-based-tool-allowlists.md) - scoping decides what can be discovered at all; progressive discovery then loads only what the current task needs
- [ctx-stable-prefix-kv-cache](ctx-stable-prefix-kv-cache.md) - the cache discipline that motivates loading tools *outside* the stable prefix rather than editing definitions mid-task
