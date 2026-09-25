# run-entropy-garbage-collection-cadence

> Agents replicate whatever patterns already exist in the repo, good or bad; run a recurring cleanup process — "garbage collection" — that encodes taste as mechanical rules and pays down drift continuously in small increments.

## Why It Matters

- The team first tried manual cleanup — every Friday, 20% of the week removing "AI slop" — and it didn't scale.

- Replacement: "golden principles" encoded in the repo (e.g., prefer shared utility packages over hand-rolled helpers; never probe data YOLO-style — validate boundaries or use typed SDKs), plus background agent tasks on a regular cadence that scan for deviations, update quality grades, and open targeted refactoring PRs — most reviewable in under a minute and automerged.

- Technical debt is like a high-interest loan: continuous small paydowns beat painful bursts; human taste is captured once, then enforced continuously on every line of code.

- Catch bad patterns daily rather than letting them spread for weeks — drift compounds because each agent run trains, implicitly, on the current repo state.

## Scope

- Apply to repos under continuous agent modification: agents replicate whatever patterns exist, drift compounds because each run implicitly trains on current repo state, and manual cleanup (the source's 20%-of-the-week Friday attempt) didn't scale.
- Encode taste mechanically — golden principles as rules plus background agents on a cadence scanning for deviations, grading, and opening small reviewable PRs (most under a minute, automerged) — not as review-time vigilance.
- Skip the recurring-cadence machinery below the threshold where drift outpaces manual cleanup; the payback case is continuous small paydowns (high-interest-loan dynamics), not occasional bursts.

## Source

OpenAI, "Harness engineering: leveraging Codex in an agent-first world" (https://openai.com/index/harness-engineering/)

## See Also

- [run-repo-as-system-of-record-map-not-manual](run-repo-as-system-of-record-map-not-manual.md) - boundary: that rule keeps knowledge (docs, specs) current via linters and doc-gardening agents; this rule keeps code patterns current — both encode taste as mechanical enforcement plus recurring agent upkeep
- [run-mechanical-invariants-linter-messages-as-injections](run-mechanical-invariants-linter-messages-as-injections.md) - the enforcement mechanism both rely on: custom linters and structural tests, not documentation goodwill
- [prin-humans-on-the-loop-not-in-it](prin-humans-on-the-loop-not-in-it.md) - the human's role in both: capture taste once, then let the cadence carry it instead of inspecting every artifact

