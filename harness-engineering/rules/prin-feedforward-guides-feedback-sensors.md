# prin-feedforward-guides-feedback-sensors

> Harness a coding agent with two complementary control types: guides (feedforward, steer before acting) and sensors (feedback, observe after acting and drive self-correction) — you need both.

## Why It Matters

- Feedback-only yields an agent that keeps repeating the same mistakes; feedforward-only yields an agent that encodes rules but never learns whether they worked.

- Split execution types: computational (deterministic, fast, reliable — tests, linters, type checkers, structural tests, codemods) vs inferential (semantic, LLM-as-judge, AI review — richer but slower, costlier, non-deterministic).

- Distribute sensors across the lifecycle by cost/speed: fast checks before commit, expensive ones (mutation testing, broad architectural review) post-integration; add continuous drift and runtime-health sensors outside the change lifecycle.

- The human's job is the steering loop: when an issue recurs, improve the guides and sensors so it becomes less probable — and use coding agents themselves to build more custom controls more cheaply.

- Honest limits from source: neither sensor type reliably catches misdiagnosis, overengineering, or misunderstood instructions; correctness is outside any sensor's remit if the human didn't specify what they wanted.

## Scope

- Apply when building an agent's control system: pair guides (feedforward, steer before acting) with sensors (feedback, observe after acting); feedback-only repeats mistakes, feedforward-only never learns what worked.
- Distribute sensors by cost and speed — fast computational checks before commit, expensive inferential ones post-integration, drift and runtime-health sensors outside the change lifecycle.
- Skip expecting sensors to fix specification: per the source's own limits, neither sensor type reliably catches misdiagnosis, overengineering, or misunderstood instructions — correctness beyond what was specified is outside any sensor's remit.

## Source

Birgitta Böckeler/Thoughtworks, "Harness engineering for coding agent users" (https://martinfowler.com/articles/harness-engineering.html)

## See Also

- [run-mechanical-invariants-linter-messages-as-injections](run-mechanical-invariants-linter-messages-as-injections.md) - concrete guide-plus-sensor pair: enforced invariants are the guides; instruction-bearing lint messages are feedback sensors optimized for LLM consumption
- [ctx-deterministic-tools-before-llm](ctx-deterministic-tools-before-llm.md) - the same split from the cost side: never spend the LLM (slow, inferential) on a linter's job (deterministic, fast)
- [prin-humans-on-the-loop-not-in-it](prin-humans-on-the-loop-not-in-it.md) - boundary: this rule defines the guides and sensors; that rule defines the human steering loop that improves them when an issue recurs
- [ver-in-loop-internal-quality](ver-in-loop-internal-quality.md) - a sensor-category case: semantic damage invisible to the type system needs checks inside the loop, not after-the-fact review
