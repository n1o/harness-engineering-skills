# tool-keep-intermediate-data-out-of-context

> Route data between tool calls through the execution environment, not the model's context window; only explicitly logged/returned values should reach the model.

## Why It Matters

- With direct tool calls, every intermediate result passes through the model twice (e.g., a 2-hour meeting transcript ≈ 50,000 extra tokens; large documents can exceed the window and break the workflow).

- With code execution, agents filter/transform results before returning them: fetch 10,000 rows, filter in code, log only 5 for review.

- Loops, conditionals, and error handling run as code instead of alternating tool-call/sleep rounds through the agent loop — also cutting time-to-first-token latency.

- This yields a privacy boundary: the harness can tokenize PII (e.g., `[EMAIL_1]`) before it reaches the model and detokenize in the MCP client on the way out, so real data flows between systems without ever entering model context; it also lets you write deterministic rules about where data may flow.

- Caveat from source: code execution requires a sandboxed, resource-limited, monitored execution environment — weigh that operational cost against the savings.

## Scope

- Apply to multi-step workflows whose intermediate results are large relative to the context window: route data between tool calls through the execution environment (fetch 10,000 rows, filter in code, log 5), and let only explicitly logged/returned values reach the model.
- The code-execution variant presupposes its own infrastructure: a sandboxed, resource-limited, monitored execution environment — weigh that operational cost (from the source) against the token savings; simple direct tool calls may cost less overall for small payloads.
- Privacy boundary included: the harness can tokenize PII before it reaches the model and detokenize at the client, enabling deterministic data-flow rules — relevant only when sensitive data is actually in play.

## Source

Anthropic, Code execution with MCP (https://www.anthropic.com/engineering/code-execution-with-mcp)

## See Also

- [ctx-filesystem-as-external-memory](ctx-filesystem-as-external-memory.md) - the durable counterpart: intermediate data lives in files/paths the model can revisit, rather than in the window
- [tool-bounded-token-efficient-responses](tool-bounded-token-efficient-responses.md) - the lighter alternative: when shape suffices, paginate/filter/truncate instead of rerouting through code
- [guard-credentials-outside-the-sandbox](guard-credentials-outside-the-sandbox.md) - the tokenization boundary in its security form: PII and secrets resolved at the edge, never in model context
