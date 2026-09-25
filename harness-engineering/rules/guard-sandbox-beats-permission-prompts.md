# guard-sandbox-beats-permission-prompts

> Replace per-action approval prompts with pre-defined sandbox boundaries the agent can work freely inside; escalate to a human only for boundary violations.

## Why It Matters

- Per-action permission prompts cause approval fatigue — users stop paying attention to what they approve, making the system less safe, and constant approval slows dev cycles; Anthropic measured 84% fewer permission prompts with sandboxing.

- Sandboxing defines set boundaries within which the agent runs autonomously; attempted access outside the boundary triggers immediate notification with an allow/deny choice.

- OpenHands frames confirmation mode as a stopgap: it limits agent value without adding proportional security. Pre-defined boundaries give both more autonomy and more safety.

- Sandbox boundaries must be enforced at the OS level (e.g., Linux bubblewrap, macOS seatbelt) so they cover scripts, programs, and subprocesses spawned by any command — not just the agent's direct calls.

## Scope

- Apply to any agent that acts with real side effects on a codebase or system: pre-defined sandbox boundaries replace per-action prompts (approval fatigue makes prompts less safe, and they slow dev cycles — the source measured 84% fewer permission prompts with sandboxing).
- The boundary must be enforced at the OS level (bubblewrap, seatbelt) so it covers scripts, programs, and subprocesses spawned by any command; escalation to a human happens only on boundary violations.
- Per-action confirmation still fits narrowly scoped, rarely-run, high-stakes operations — but as a stopgap that limits agent value, not a security layer; don't rebuild it as the general mechanism.

## Source

Anthropic, Beyond permission prompts: Claude Code sandboxing (https://www.anthropic.com/engineering/claude-code-sandboxing); OpenHands, Mitigating Prompt Injection Attacks (https://openhands.dev/blog/mitigating-prompt-injection-attacks-in-software-agents)

## See Also

- [guard-filesystem-and-network-isolation-together](guard-filesystem-and-network-isolation-together.md) - family: the two isolation axes (filesystem, network) that a real sandbox boundary is made of
- [guard-untrusted-content-as-data](guard-untrusted-content-as-data.md) - family: sandboxing contains the compromised agent; content-as-data lowers the odds of compromise — both replace prompt-time vigilance with structure
- [guard-credentials-outside-the-sandbox](guard-credentials-outside-the-sandbox.md) - complements the boundary: secrets stay outside it, so a contained agent also has nothing to steal
- [prin-humans-on-the-loop-not-in-it](prin-humans-on-the-loop-not-in-it.md) - the escalation posture: humans improve the boundary, not inspect every action inside it
