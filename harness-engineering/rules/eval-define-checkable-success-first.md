# eval-define-checkable-success-first

> Write down measurable success criteria before building the agent behavior (skill, prompt, or harness change) — split into outcome, process, style, and efficiency goals.

## Why It Matters

- An eval is: prompt → captured run (trace + artifacts) → small set of checks → a score comparable over time; it replaces "does this feel better?" with concrete questions.

- Split checks into categories: outcome goals (did the task complete?), process goals (did the agent follow the intended tools/steps?), style goals (conventions followed?), efficiency goals (no thrashing, bounded token use).

- Keep the must-pass list small; don't encode every preference up front — capture the behaviors you care most about.

- Without clear constraints there is nothing concrete to evaluate — OpenAI's sample skill takes an opinionated stance (exact file structure, exact commands) precisely so success is unambiguous.

- Anthropic: evals force product teams to specify what success means; two engineers reading the same spec can interpret edge cases differently, and an eval suite resolves that ambiguity before code exists.

## Scope

- Apply before building any agent behavior — skill, prompt, or harness change; the outcome/process/style/efficiency split is the vocabulary for the checks.

- Keep the must-pass list small; don't encode every preference up front — capture the behaviors you care most about.

- Skip formal criteria only for exploration whose goal is to learn what to build; once a behavior change ships, write the criteria first.

## Source

OpenAI 'Testing Agent Skills Systematically with Evals' (https://developers.openai.com/blog/eval-skills/); Anthropic 'Demystifying Evals for AI Agents' (https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)

## See Also

- [eval-unambiguous-tasks-reference-solutions](eval-unambiguous-tasks-reference-solutions.md) - success criteria become unambiguous tasks validated by reference solutions
- [eval-no-skill-baseline](eval-no-skill-baseline.md) - defined success is what the no-skill baseline is measured against
- [eval-combine-grader-types](eval-combine-grader-types.md) - each check category maps to a grader type
