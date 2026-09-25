# ctx-layered-instruction-files

> Layer repo-local instruction files hierarchically — root file for project-wide guidance, subdirectory files for subsystem specifics, user-global file for personal preferences — with more-specific files taking precedence, and keep one source of truth across runtimes via a standard format.

## Why It Matters

- agent.md specification: root AGENT.md for general guidance, subdirectory files for subsystem guidance, `~/.config/AGENT.md` for personal preferences; tools merge with specific over general.

- AGENTS.md is "a README for agents": a dedicated, predictable place for dev-environment tips, testing instructions (find the CI plan, exact commands, "fix errors until the whole suite is green"), and PR conventions; wide tool adoption makes it a portable contract rather than per-tool config sprawl (`.cursorrules`, `.clauderules`, …).

- Migrate to one canonical file and symlink legacy names back to it (e.g. `mv CLAUDE.md AGENT.md && ln -s AGENT.md CLAUDE.md`) so every runtime reads the same source of truth.

- Content shape (both specs converge): project structure/organization, build/test/dev commands, code style, testing guidelines, security considerations — "what you'd tell a new team member on their first day."

## Scope

- Apply when guidance outgrows one file or must vary by scope: project-wide at the root, subsystem specifics in subdirectories, personal preferences in `~/.config` — more-specific files take precedence.

- Apply across runtimes: standardize on one canonical format (AGENTS.md) and symlink legacy names back to it so every tool reads the same source of truth.

- Skip the hierarchy when the project fits comfortably in one minimal root file — layers earn their keep only when subdirectory guidance is genuinely distinct.

## Source

agent.md spec (https://github.com/agentmd/agent.md); AGENTS.md format (https://github.com/agentsmd/agents.md); Martin Fowler, "Context Engineering for Coding Agents" (https://martinfowler.com/articles/exploring-gen-ai/context-engineering-coding-agents.html)

## See Also

- [ctx-instruction-file-minimal-universal](ctx-instruction-file-minimal-universal.md) - the family root: keep the always-loaded root file minimal and universal; this rule adds the hierarchy around it.

- [ctx-progressive-disclosure-pointers](ctx-progressive-disclosure-pointers.md) - the family's loading mechanism: pointers and path-scoped rules keep detail out of the root file until relevant.

- [ctx-context-load-ownership](ctx-context-load-ownership.md) - decides which layer loads by which trigger (always-loaded vs path-scoped vs on demand).
