# run-make-the-app-legible-and-runnable-init-script

> Make the running application itself legible to the agent: a script to boot it, browser automation to drive it, and logs/metrics/traces it can query — so verification happens against reality, not code review.

## Why It Matters

- Write an `init.sh` that starts the dev server, and have every session run a basic end-to-end test through it before implementing anything — this catches a broken inherited state immediately instead of compounding it.

- Anthropic found Claude mostly verified features end-to-end well once explicitly prompted to use browser automation (Puppeteer MCP) and "do all testing as a human user would"; unit tests and `curl` alone missed non-working features.

- OpenAI wired Chrome DevTools Protocol into the agent runtime with skills for DOM snapshots, screenshots, and navigation so Codex could reproduce bugs, validate fixes, and reason about UI behavior.

- OpenAI also made the app bootable per git worktree and exposed an ephemeral local observability stack (logs/metrics/traces queryable via LogQL/PromQL/TraceQL), turning prompts like "no span in these four critical user journeys exceeds two seconds" into tractable, verifiable tasks.

## Scope

- Apply when the deliverable is a running application an agent builds or modifies: an `init.sh` to boot it, browser automation to drive it, and queryable logs/metrics/traces — so verification happens against reality, not code review.
- Every session runs a basic end-to-end test through init.sh before implementing anything; unit tests and `curl` alone missed non-working features in the source's experience.
- Skip for non-app work (libraries, CLIs, data pipelines) — the rule's value is making UI/feature behavior directly exercisable as a human user would.

## Source

Anthropic, "Effective harnesses for long-running agents" (https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents); OpenAI, "Harness engineering: leveraging Codex in an agent-first world" (https://openai.com/index/harness-engineering/)

## See Also

- [run-self-verify-before-marking-done](run-self-verify-before-marking-done.md) - this rule provides the machinery; that rule is the policy that no feature flips to passing without exercising it through the running app
- [run-initializer-agent-bootstrap-session-zero](run-initializer-agent-bootstrap-session-zero.md) - same source harness: the initializer session is where init.sh and the run-first-then-build habit get created
- [prin-contact-humans-with-tool-calls](prin-contact-humans-with-tool-calls.md) - same principle at the human boundary: structured, durable interactions rather than free-form inspection

