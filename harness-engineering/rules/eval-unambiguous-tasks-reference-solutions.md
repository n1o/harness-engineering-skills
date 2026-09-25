# eval-unambiguous-tasks-reference-solutions

> Every task must be unambiguous, solvable, and validated by a reference solution that passes all graders; low scores often mean broken evals, not a broken agent.

## Why It Matters

- A good task is one where two domain experts would independently reach the same pass/fail verdict, and could pass it themselves; ambiguity in specs becomes noise in metrics.

- Everything the grader checks must be clear from the task description — a Terminal-Bench audit found tasks asking for "a script" while tests assumed a specific filepath, failing agents through no fault of their own.

- With frontier models, 0% pass@100 is most often a broken task, not an incapable agent.

- Create a known-good reference solution per task to prove solvability and verify grader configuration.

- Real failures from grading bugs: Opus 4.5 scored 42% on CORE-Bench until rigid grading (penalizing "96.12" vs "96.124991…"), ambiguous specs, and irreproducible stochastic tasks were fixed → 95%. METR found misconfigured tasks where instructions said to optimize *to* a threshold but grading required *exceeding* it, rewarding models that ignored the stated goal.

- Make graders resistant to bypass: passing must genuinely require solving the problem, not exploiting loopholes.

## Scope

- Apply to every task before trusting scores from it: unambiguous, solvable, and validated by a reference solution that passes all graders — low scores most often mean broken evals, not a broken agent (0% pass@100 with frontier models is a broken task until proven otherwise).

- Two domain experts must independently reach the same verdict, and everything the grader checks must be stated in the task description.

- Skip the reference-solution investment only for throwaway exploratory grading; anything that feeds a comparison or a leaderboard needs it.

## Source

Anthropic 'Demystifying Evals for AI Agents' (https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)

## See Also

- [eval-combine-grader-types](eval-combine-grader-types.md) - graders of every type still need an unambiguous task to grade; reference solutions validate their configuration
- [eval-read-transcripts](eval-read-transcripts.md) - how broken-task and bad-grader failures actually get discovered
- [eval-bespoke-assertions-per-case](eval-bespoke-assertions-per-case.md) - per-case success criteria are the instrument that makes "everything checked is stated" concrete
- [eval-define-checkable-success-first](eval-define-checkable-success-first.md) - defining checkable success up front is how tasks become unambiguous by construction
