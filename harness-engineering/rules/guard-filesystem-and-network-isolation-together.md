# guard-filesystem-and-network-isolation-together

> Effective sandboxing requires both filesystem isolation and network isolation; either one alone leaves a trivially exploitable gap.

## Why It Matters

- Without network isolation, a compromised agent can exfiltrate sensitive files like SSH keys; without filesystem isolation, it can escape the sandbox and gain network access.

- Filesystem isolation: allow read/write only to the working directory, block modification of anything outside it.

- Network isolation: route all egress through a proxy outside the sandbox that enforces a domain allowlist and handles user confirmation for newly requested domains; allow arbitrary custom rules on outgoing traffic for stricter setups.

- The payoff is that even a successful prompt injection is fully contained: a compromised agent cannot steal credentials or phone home to an attacker's server.

- Anti-example from source: an agent with `curl` alone hits both failure modes — untrusted content in (injection) and a data channel out (exfiltration).

## Scope

- Apply when the agent handles secrets, untrusted content, or consequential writes: filesystem isolation (read/write only the working directory) and network isolation (proxied egress, domain allowlist, confirmation for new domains) ship together — either alone leaves a trivially exploitable gap.
- The bar for "too small to sandbox" is low: an agent with `curl` alone already spans both failure modes — untrusted content in, data channel out (the source's anti-example); skip only for genuinely offline tasks over non-sensitive data.
- The payoff is that even a successful prompt injection is fully contained: no credentials to steal, no attacker server to phone home to.

## Source

Anthropic, Beyond permission prompts: Claude Code sandboxing (https://www.anthropic.com/engineering/claude-code-sandboxing)

## See Also

- [guard-sandbox-beats-permission-prompts](guard-sandbox-beats-permission-prompts.md) - family: pre-defined boundaries replace per-action prompts; this rule supplies the two isolation axes those boundaries are made of
- [guard-untrusted-content-as-data](guard-untrusted-content-as-data.md) - family: isolation bounds what a compromised agent can do; treating content as data lowers the odds of compromise in the first place
- [guard-credentials-outside-the-sandbox](guard-credentials-outside-the-sandbox.md) - the third wall: an isolated sandbox that also holds no secrets leaves a would-be escapee nothing to loot
- [guard-hard-policies-over-model-judgment](guard-hard-policies-over-model-judgment.md) - the egress allowlist and working-directory bounds here are exactly the deterministic policies that constrain a compromised agent
