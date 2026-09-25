# guard-static-capability-scan-before-deploy

> Run a static capability scan in CI before deployment to surface what the agent can actually touch — including capabilities the manifest never declared.

## Why It Matters

- Scan the repo surfaces that turn an agent into an actor: workflows that can deploy or expose secrets, tool manifests enabling shell execution, `eval`/`exec`/subprocess inside tool functions, direct prompt interpolation of user input, credentials passed into LLM context, unencrypted private keys, MCP endpoints pointing to non-allowlisted hosts.

- Shadow capabilities are a distinct class: the `declared_vs_imported_delta` rule flags tool registrations (Python and TS/JS MCP `registerTool` shapes) that are not declared in the agent manifest — the agent's real capability surface is larger than its config claims.

- Keep the scanner itself trustworthy: local-only, no network calls, no code execution, redacted findings (raw secrets and command bodies never appear in reports).

- Adopt via baseline: save existing findings, then fail CI only on *new* findings, so scanning is adoptable on legacy repos without a big-bang cleanup.

- Aim for a short list of conservative high-severity rules mapped to concrete controls (remove/restrict/redact), not a giant list of theoretical issues.

## Scope

- Apply before deployment on any repo whose surfaces turn an agent into an actor: workflows that deploy or expose secrets, tool manifests enabling shell execution, `eval`/`exec`/subprocess in tool functions, direct prompt interpolation of user input, credentials in LLM context, unencrypted private keys, non-allowlisted MCP endpoints.
- Two non-negotiables of the scanner itself: it must be trustworthy (local-only, no network calls, no code execution, findings redacted so raw secrets and command bodies never appear) and short — a compact list of conservative high-severity rules mapped to concrete controls beats a giant list of theoretical issues.
- Adopt on legacy repos via baseline (save existing findings, fail CI only on new ones); treat the `declared_vs_imported_delta` shadow-capability check as part of the same pre-deploy gate, since the manifest understating the real surface is exactly what the scan exists to catch.

## Source

Lurkr (https://github.com/agentveil-protocol/lurkr)

## See Also

- [guard-pre-action-deterministic-authorization](guard-pre-action-deterministic-authorization.md) - the runtime counterpart: scanning bounds the declared surface before deploy; the hook enforces policy per call at run time
- [guard-scope-based-tool-allowlists](guard-scope-based-tool-allowlists.md) - what to do with scan findings: narrow the offending role's scope rather than trusting the model with a known-dangerous tool
- [ver-harness-deltas-measured-by-evals](ver-harness-deltas-measured-by-evals.md) - the baseline discipline, eval-side: measure deltas against a fixed reference rather than reacting to each finding in isolation
