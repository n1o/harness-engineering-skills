# eval-bespoke-assertions-per-case

> Deep agents break the one-evaluator-per-dataset assumption: each datapoint may need its own success criteria, asserting across trajectory, final message, and state.

## Why It Matters

- Example: "remember to never schedule meetings before 9am" requires asserting (1) the agent called `edit_file` on `memories.md` (trajectory), (2) it confirmed the update in its final message (LLM judge), (3) the file actually contains the constraint (regex or LLM judge on state).

- Write these as ordinary test functions (pytest/vitest) that log inputs, outputs, and per-assertion feedback to an experiment, so failed cases come with traces for debugging and results track over time.

- Mix deterministic assertions (tool name + args) with LLM-as-judge scores for holistic properties like "did the file update capture the right intent".

## Scope

- Apply to deep-agent evals where datapoints differ in what success means — a single dataset-wide grader can't cover tasks whose evidence spans trajectory, final message, and state.

- Skip when one grader genuinely covers every case (uniform output form); per-case test functions are maintenance cost, so pay it only for behaviors you've decided to track over time.

- Keep trajectory assertions loose (tool called at some point) — don't let per-case criteria drift into rigid path-sequence checks.

## Source

LangChain 'Evaluating Deep Agents: Our Learnings' (https://blog.langchain.com/evaluating-deep-agents-our-learnings/)

## See Also

- [eval-tier-by-scope](eval-tier-by-scope.md) - tiering evals by run scope (single-step/full-run/multi-turn) vs per-datapoint success criteria; combine both when cases and scope both vary
- [eval-combine-grader-types](eval-combine-grader-types.md) - which grader to reach for per assertion (deterministic vs LLM judge)
- [eval-unambiguous-tasks-reference-solutions](eval-unambiguous-tasks-reference-solutions.md) - per-case criteria must still be clear from the task description or they become metric noise
- [eval-grade-outcome-not-path](eval-grade-outcome-not-path.md) - guardrail for the trajectory assertions this rule asks you to write
