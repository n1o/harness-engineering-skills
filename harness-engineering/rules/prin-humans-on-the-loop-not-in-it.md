# prin-humans-on-the-loop-not-in-it

> The human's highest-leverage position is building and improving the harness (the "how" loop), not inspecting every artifact the agents produce ("in the loop") nor abandoning oversight entirely ("out of the loop").

## Why It Matters

- The visible difference: when an agent's output disappoints, the "in the loop" response fixes the artifact; the "on the loop" response changes the harness that produced it so it produces the right result next time.

- Humans in the innermost loop become the bottleneck — agents generate code faster than humans can inspect it; shift-left applies to agents too: they produce better code when they can gauge its quality themselves.

- Internal quality still matters even if agents "don't care about developer experience": a cleanly structured codebase lets LLMs understand and modify code faster, spiral less, and cost less — internal quality affects external outcomes.

- Take it further with the agentic flywheel: direct agents to review loop results and recommend harness improvements (including upstream workflow changes), prioritize them, and progressively auto-approve low-risk recommendations.

- Fowler's complement: the goal is not eliminating human input but directing it to where it matters most — humans bring implicit harness (conventions, accountability, organizational memory, taste) that the explicit harness only partially externalizes.

## Scope

- Apply to recurring agent workflows: when output disappoints, change the harness that produced it so it produces the right result next time — the payoff is in future runs.
- Skip for genuinely one-off artifacts: with no "next time," fixing the artifact directly is the whole job; the on-the-loop stance amortizes harness work across runs.
- The goal is redirecting human input, not eliminating it: humans bring conventions, accountability, organizational memory, and taste that the explicit harness only partially externalizes.

## Source

Kief Morris/Thoughtworks, "Humans and Agents in Software Engineering Loops" (https://martinfowler.com/articles/exploring-gen-ai/humans-and-agents.html); Birgitta Böckeler/Thoughtworks, "Harness engineering for coding agent users" (https://martinfowler.com/articles/harness-engineering.html)

## See Also

- [prin-feedforward-guides-feedback-sensors](prin-feedforward-guides-feedback-sensors.md) - boundary: that rule defines the guides and sensors; this rule defines who improves them — the human steering loop that reacts to recurring issues
- [run-entropy-garbage-collection-cadence](run-entropy-garbage-collection-cadence.md) - a concrete on-the-loop mechanism: capture human taste once as mechanical rules, then let cadence enforcement carry it
- [ver-in-loop-internal-quality](ver-in-loop-internal-quality.md) - why "out of the loop" isn't safe: agents introduce technical debt when unsupervised, and internal quality affects agent outcomes too
- [ver-harness-deltas-measured-by-evals](ver-harness-deltas-measured-by-evals.md) - harness improvements land as measured eval deltas with the model fixed, not as intuition
