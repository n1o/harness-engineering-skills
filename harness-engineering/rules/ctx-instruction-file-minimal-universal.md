# ctx-instruction-file-minimal-universal

> Keep the always-loaded instruction file (CLAUDE.md/AGENTS.md) minimal and universally applicable: instruction-following degrades uniformly as instruction count grows, and non-universal content actively teaches the agent to ignore the file.

## Why It Matters

- Research cited by HumanLayer: frontier thinking models follow ~150–200 instructions with reasonable consistency; smaller models decay exponentially with instruction count; the harness system prompt alone consumes ~50 of that budget.

- As instruction count grows, models ignore all instructions uniformly — not just the later ones; and more non-universal content means more file-level ignoring (harnesses wrap the file in "may or may not be relevant" reminders).

- Content should onboard the agent: WHY (project purpose), WHAT (stack, structure, map of the repo — especially monorepos), HOW (commands, verification: tests/typechecks/builds).

- Consensus size guidance: <300 lines, shorter is better; HumanLayer's own root file is <60 lines. Anti-pattern: appending behavior "hotfixes" after each bad session.

- Craft it deliberately — this file enters every session and every artifact, making it the highest-leverage point of the harness; don't auto-generate it with /init-style tools.

## Scope

- Apply to the always-loaded file (CLAUDE.md/AGENTS.md) specifically — the slot that enters every session — not to path-scoped or on-demand docs.

- Skip the universal-only bar when guidance is genuinely task- or subsystem-specific: move it to separate self-describing files or path-scoped rules instead of appending exceptions to the root file.

- The ~150–200 instruction budget and <300-line (<60 at HumanLayer) sizes are measured defaults from the cited sources for frontier thinking models — smaller models decay faster, so scale down accordingly.

## Source

HumanLayer, Writing a good CLAUDE.md (https://www.humanlayer.dev/blog/writing-a-good-claude-md)

## See Also

- [ctx-progressive-disclosure-pointers](ctx-progressive-disclosure-pointers.md) - the family companion: this rule keeps the root file minimal, that one puts the detail in separate files and teaches the agent to find them.

- [ctx-layered-instruction-files](ctx-layered-instruction-files.md) - completes the three-way structure: hierarchy and precedence (root project-wide → subdirectory subsystem → user-global personal) on top of the minimal root file.

- [ctx-deterministic-tools-before-llm](ctx-deterministic-tools-before-llm.md) - moving mechanical rules out of the file and into linters/hooks is the cheapest way to keep it small.
