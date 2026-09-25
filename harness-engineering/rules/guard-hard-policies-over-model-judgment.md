# guard-hard-policies-over-model-judgment

> Enforce the security-critical restrictions with deterministic policy (network policy, eBPF, allowlists), never by relying on the model's trained common sense.

## Why It Matters

- Model refusals of injected instructions are a *soft* block — non-deterministic, model-dependent, and circumventable by some incantation; OpenHands shows the same agent that refuses one malicious URL going further on a more innocuous-looking one.

- Layer defenses: containers/sandboxes contain damage, but the in-sandbox environment still holds secrets and tools; hard policies (domain allowlists, blocking `curl`, blocking pastebin) constrain what even a compromised agent can do.

- Apply the principle of least privilege per task: different tasks get different policies, and agents can escalate permissions via human approval rather than by default.

- Acknowledge the trade-off honestly: hard policies take setup effort; organizations that already built policy tooling for humans can reuse it for agents.

## Scope

- Apply to every security-critical restriction — network policy, eBPF, allowlists, blocking `curl` or pastebin: model refusals are a soft block (non-deterministic, model-dependent, circumventable by some incantation), so deterministic policy is the only thing that bounds a compromised agent.
- Layer rather than substitute: containers contain damage, but the in-sandbox environment still holds secrets and tools — hard policies constrain that residual surface, per task, with escalation by human approval rather than by default.
- The cost trade-off is real: policy tooling takes setup effort (reusable where organizations already built it for humans); for disposable tasks with nothing consequential reachable, a sandbox plus soft blocks may be an acceptable floor.

## Source

OpenHands, Mitigating Prompt Injection Attacks (https://openhands.dev/blog/mitigating-prompt-injection-attacks-in-software-agents)

## See Also

- [guard-untrusted-content-as-data](guard-untrusted-content-as-data.md) - pairs: labeling reduces the probability the model follows injected instructions; this rule bounds the damage when it does
- [guard-filesystem-and-network-isolation-together](guard-filesystem-and-network-isolation-together.md) - the concrete hard policies: egress allowlisting and working-directory filesystem bounds
- [guard-pre-action-deterministic-authorization](guard-pre-action-deterministic-authorization.md) - the same deterministic-over-model principle, enforced per tool call at a pre-action hook instead of at the environment level
