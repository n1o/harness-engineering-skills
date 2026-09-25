# guard-credentials-outside-the-sandbox

> Never place real credentials inside the agent's sandbox; route privileged operations through a verifying proxy that holds the secrets.

## Why It Matters

- Claude Code on the web keeps git credentials and signing keys outside the sandbox; the in-sandbox git client authenticates with a scoped custom credential to a proxy that verifies both the credential and the interaction contents (e.g., pushing only to the configured branch) before attaching the real token.

- Pattern generalizes: per-upstream auth held at a proxy layer (mcp-guardian resolves OAuth/bearer tokens from env/dashboard at the proxy, so tools authenticate per-server without exposing secrets to the client), and harness-side tokenization of PII flowing between tools.

- Rationale: if code inside the sandbox is compromised, there is nothing valuable to steal; blast radius ends at the sandbox wall.

## Scope

- Apply whenever code or content inside the sandbox is exposed to anything untrusted: real credentials stay outside, and the in-sandbox client holds only a scoped credential the proxy verifies (credential and interaction contents) before attaching the real secret.
- The proxy must verify the interaction, not merely relay it — push only to the configured branch, resolve per-server auth at the proxy; a relay without verification just relocates the credential.
- Skip when the sandbox is genuinely offline with no privileged upstreams: nothing valuable inside and no secrets to attach means the proxy layer is pure operational cost.

## Source

Anthropic, Beyond permission prompts: Claude Code sandboxing (https://www.anthropic.com/engineering/claude-code-sandboxing); Anthropic, Code execution with MCP (https://www.anthropic.com/engineering/code-execution-with-mcp)

## See Also

- [guard-filesystem-and-network-isolation-together](guard-filesystem-and-network-isolation-together.md) - the sandbox walls this rule assumes: isolation contains the agent, the proxy contains the secrets
- [tool-keep-intermediate-data-out-of-context](tool-keep-intermediate-data-out-of-context.md) - shares the tokenization boundary: PII is tokenized before it reaches the model and resolved at the edge
- [guard-audit-log-every-decision](guard-audit-log-every-decision.md) - the proxy that attaches credentials is also the natural place to audit every privileged operation it performs
