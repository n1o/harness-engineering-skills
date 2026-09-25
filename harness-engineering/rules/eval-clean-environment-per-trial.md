# eval-clean-environment-per-trial

> Each trial starts from a clean, isolated environment; shared state causes correlated failures, flaky results, and unfair advantages.

## Why It Matters

- Leftover files, caches, or resource exhaustion cause correlated failures from infrastructure flakiness rather than agent performance; if multiple trials fail on the same environmental limitation, results are unreliable.

- Shared state can also inflate scores: Anthropic observed Claude gaining unfair advantage on some tasks by reading git history from previous trials.

- Stateful deep agents need environments that reset per test (temp directory per test case, or containerized runs as in Harbor/Inspect's `sandbox="docker"`), otherwise evals become flaky and irreproducible.

- Mock or record-and-replay external API requests (vcr.py, fetch proxying) when the agent depends on live services — faster, cheaper, easier to debug.

- The agent in the eval must function roughly the same as the production agent, so the environment itself introduces no additional noise.

## Scope

- Apply whenever trials share anything mutable — filesystem, git state, caches, live services; per-trial temp directories or containerized sandboxes are the strong form.

- Use record-and-replay/mocking for external services when the service's live behavior isn't itself under test; skip isolation only for fully read-only, deterministic tasks.

- Don't isolate so hard that the eval agent no longer functions roughly like the production agent — the environment itself must introduce no additional noise.

## Source

Anthropic 'Demystifying Evals for AI Agents' (https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents); LangChain 'Evaluating Deep Agents' (https://blog.langchain.com/evaluating-deep-agents-our-learnings/); Inspect AI (https://inspect.aisi.org.uk/)

## See Also

- [obs-runtime-config-first-class-variable](obs-runtime-config-first-class-variable.md) - environment control as a validity requirement here vs resource config as a measured noise variable there
- [eval-pass-at-k-vs-pass-cubed-k](eval-pass-at-k-vs-pass-cubed-k.md) - correlated failures from shared state break the independent-trials assumption behind pass@k/pass^k
- [eval-no-skill-baseline](eval-no-skill-baseline.md) - baseline and skill runs must differ only by the skill, which per-trial isolation guarantees
- [struct-harness-as-declared-config](struct-harness-as-declared-config.md) - environment templates (Dockerfile, instruction, tests) as declared, reproducible config
