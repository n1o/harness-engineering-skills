# tool-bounded-token-efficient-responses

> Cap and shape tool responses: pagination, range selection, filtering, and truncation with sensible defaults, plus steering text that teaches the agent cheaper strategies.

## Why It Matters

- Implement some combination of pagination/filtering/truncation for any response that could consume lots of context; Claude Code restricts tool responses to 25,000 tokens by default.

- When truncating, steer agents toward token-efficient strategies ("many small targeted searches instead of one broad search").

- Prompt-engineer error responses to be specific and actionable (with correctly formatted example input), not opaque error codes or tracebacks.

- Diagnose from metrics: lots of redundant calls → resize pagination/limits; lots of invalid-parameter errors → clearer descriptions. Real example: Claude needlessly appended `2025` to web-search queries; the fix was in the tool description, not the model.

## Scope

- Apply to any tool response that could consume lots of context — implement some combination of pagination, range selection, filtering, and truncation with sensible defaults; the source's 25,000-token response cap is Claude Code's default, a measured default from that source, not a universal constant.
- Steering text and prompt-engineered errors are part of the same rule: teach cheaper strategies at the truncation point, and make error responses specific and actionable rather than opaque codes or tracebacks.
- Fix from metrics, not vibes: redundant calls → resize pagination/limits; invalid-parameter errors → clearer descriptions — when diagnostics show a description problem, this rule hands off to description work.

- **When to skip**: Applies to any tool whose output enters model context; skip for tools consumed only by code (not by the model).

## Source

Anthropic, Writing effective tools for agents (https://www.anthropic.com/engineering/writing-tools-for-agents)

## See Also

- [ctx-deterministic-output-backpressure](ctx-deterministic-output-backpressure.md) - boundary: this rule shapes the *tool's* response (pagination, truncation, steering text); that one gates *build/test/lint command output* harness-side — complementary, different layers
- [tool-keep-intermediate-data-out-of-context](tool-keep-intermediate-data-out-of-context.md) - the stronger move when shape alone can't save the tokens: route the data through code, return only what's needed
- [tool-semantic-identifiers-over-uuids](tool-semantic-identifiers-over-uuids.md) - shapes *what* is in the bounded response: interpretable identifiers and a `concise`/`detailed` verbosity enum
- [tool-descriptions-as-prompts](tool-descriptions-as-prompts.md) - the description-side fix when metrics show invalid-parameter errors rather than redundant calls
