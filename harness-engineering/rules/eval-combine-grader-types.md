# eval-combine-grader-types

> Combine code-based, model-based, and human graders: deterministic where possible, LLM rubrics where nuance demands them, humans to calibrate — and make model graders emit structured, scoreable output.

## Why It Matters

- Code-based graders (string match, fail-to-pass/pass-to-pass tests, static analysis, state checks, tool-call verification, transcript metrics) are fast, cheap, objective, reproducible — but brittle to valid variation; model-based graders (rubrics, NL assertions, pairwise, multi-judge) capture nuance but are non-deterministic and need calibration; humans are the gold standard for calibration, used sparingly.

- For qualitative checks (component structure, conventions), run a second read-only model pass constrained to a JSON rubric schema (stable fields: per-check id/pass/notes + overall score) so results can be diffed and tracked across runs — free-form grader text is hard to compare.

- Give LLM judges an out ("return Unknown when insufficient info") to avoid hallucinated verdicts; grade each dimension with an isolated judge rather than one judge for all dimensions; validate rubric features against real outcomes before trusting them.

- Frameworks codify this spectrum: Inspect separates dataset/solver/scorer and ships match, pattern, exact, math-equivalence, and model-graded scorers with per-scorer metrics — pick deterministic scorers where the output form permits and model grading for open-ended answers.

## Scope

- Apply when grading has both machine-checkable and nuanced dimensions; pick deterministic scorers wherever the output form permits, model graders only where it doesn't.

- Humans are the calibration gold standard but don't scale — use sparingly, to calibrate the model graders.

- Skip model graders entirely when exact/string/state checks cover the contract; their non-determinism and calibration overhead are real costs.

## Source

Anthropic 'Demystifying Evals for AI Agents' (https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents); OpenAI 'Testing Agent Skills Systematically with Evals' (https://developers.openai.com/blog/eval-skills/); Inspect AI scorers (https://inspect.aisi.org.uk/scorers.html)

## See Also

- [eval-unambiguous-tasks-reference-solutions](eval-unambiguous-tasks-reference-solutions.md) - graders are only as good as the task's unambiguity; reference solutions validate grader configuration
- [eval-read-transcripts](eval-read-transcripts.md) - transcript reading is how you discover a grader is rejecting valid solutions
- [eval-bespoke-assertions-per-case](eval-bespoke-assertions-per-case.md) - per-case mixing of deterministic and LLM-judge assertions in practice
- [eval-grade-outcome-not-path](eval-grade-outcome-not-path.md) - what the graders should be pointed at
