# tool-few-purposeful-tools

> Build a small set of task-shaped tools that consolidate multi-step workflows, instead of wrapping every API endpoint one-for-one.

## Why It Matters

- A common error is tools that merely mirror existing API endpoints; agents have different affordances than traditional software (limited context, so brute-force enumeration is wasteful).

- Prefer `search_contacts` over `list_contacts`; `schedule_event` (finds availability + schedules) over `list_users` + `list_events` + `create_event`; `get_customer_context` over three separate lookup tools.

- Consolidated tools handle multiple discrete operations under the hood, enrich responses with related metadata, and reduce the intermediate outputs that would otherwise burn context.

- Each tool must have a clear, distinct purpose; too many or overlapping tools distract agents from efficient strategies.

- Anti-example from source: a tool returning ALL contacts that the agent must read token-by-token, like searching an address book page by page.

## Scope

- Apply at tool-design time: build a small set of task-shaped tools that consolidate multi-step workflows (search, not list; schedule_event, not three lookups plus a create) — agents have limited context, so brute-force enumeration is wasteful.
- The test is distinct, clear purpose per tool: overlapping or vague tools distract agents from efficient strategies; consolidation that merges genuinely unrelated tasks fails that test as badly as endpoint-mirroring does.
- Weight against the multi-call cost: a consolidated tool hides multiple discrete operations behind one schema, so it earns its place when the workflow it encodes is real and recurring, not to shrink a tool list cosmetically.

- **When to skip**: Applies at tool-surface design time; skip when you must expose an existing fixed API and consolidation isn't yours to decide.

## Source

Anthropic, Writing effective tools for agents (https://www.anthropic.com/engineering/writing-tools-for-agents)

## See Also

- [tool-progressive-tool-discovery](tool-progressive-tool-discovery.md) - the scale question: when hundreds of tools are genuinely needed, discover them progressively instead of forcing consolidation
- [tool-keep-intermediate-data-out-of-context](tool-keep-intermediate-data-out-of-context.md) - consolidated tools also reduce the intermediate outputs that would otherwise burn context
- [tool-descriptions-as-prompts](tool-descriptions-as-prompts.md) - a small purposeful set still needs onboarding-doc descriptions; fewer tools makes keeping them good tractable
- [tool-bounded-token-efficient-responses](tool-bounded-token-efficient-responses.md) - shaping each response matters more the fewer, bigger tools get
