# run-repo-as-system-of-record-map-not-manual

> Treat the repository as the agent's only reality: give it a short map (AGENTS.md as table of contents) pointing into a structured, mechanically validated docs/ system — never a monolithic instruction manual.

## Why It Matters

- The "one big AGENTS.md" failed in predictable ways: context is scarce and a giant file crowds out the task; too much guidance becomes non-guidance (when everything is important, nothing is); it rots instantly into a graveyard of stale rules; and a single blob can't be mechanically checked for coverage, freshness, or cross-links.

- The fix: ~100-line AGENTS.md as entry point; structured `docs/` with indexed design docs, product specs, execution plans (active/completed/tech-debt tracker, versioned and checked in), and reference material — enabling progressive disclosure (start small and stable, teach where to look next).

- From the agent's point of view, anything it can't access in-context doesn't exist: decisions living in Slack threads, Google Docs, or people's heads are illegible; push them into the repo as versioned artifacts.

- Enforce mechanically: dedicated linters and CI jobs validate the knowledge base is up to date, cross-linked, and structured; a recurring doc-gardening agent scans for stale docs and opens fix-up PRs.

## Scope

- Apply to any agent-accessible knowledge base beyond one small file: a short map (AGENTS.md as table of contents) pointing into a structured, mechanically validated docs/ system — never a monolithic manual.
- Skip the full structure for repos where the guidance fits in one small file: a single blob fails only at scale (context crowding, rot, no mechanical checking), and the ~100-line entry point presumes enough content beneath it to need an index.
- Enforce mechanically from the start: linters and CI validate freshness/cross-links, and a recurring doc-gardening agent opens fix-up PRs — anything the agent can't access in-context doesn't exist, so push decisions out of Slack threads and heads and into versioned artifacts.

## Source

OpenAI, "Harness engineering: leveraging Codex in an agent-first world" (https://openai.com/index/harness-engineering/)

## See Also

- [run-entropy-garbage-collection-cadence](run-entropy-garbage-collection-cadence.md) - boundary: this rule keeps the knowledge base (docs, specs) current via linters and recurring gardening agents; that rule keeps code patterns current — same map-not-maintenance-burden mechanism
- [ctx-instruction-file-minimal-universal](ctx-instruction-file-minimal-universal.md) - the always-loaded entry point must stay minimal and universal: instruction-following degrades uniformly as instruction count grows, which is why the map points instead of inlining
- [ctx-progressive-disclosure-pointers](ctx-progressive-disclosure-pointers.md) - the same pointers-not-copies principle: path-scoped and on-demand docs load only when relevant

