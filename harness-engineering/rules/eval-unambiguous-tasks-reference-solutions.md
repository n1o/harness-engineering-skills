# eval-unambiguous-tasks-reference-solutions

> Every task must be unambiguous, solvable, and validated by a reference solution that passes all graders; low scores often mean broken evals, not a broken agent.

## Why It Matters

- A good task is one where two domain experts would independently reach the same pass/fail verdict, and could pass it themselves; ambiguity in specs becomes noise in metrics.

- Everything the grader checks must be clear from the task description — a Terminal-Bench audit found tasks asking for "a script" while tests assumed a specific filepath, failing agents through no fault of their own.

- With frontier models, 0% pass@100 is most often a broken task, not an incapable agent.

- And validate tasks by *repairing* them against a solver, not just by authoring review: AutoGym (arXiv 2609.22592) found iterative task repair shifts a synthetic suite from 57.0% hard to 39.0% hard (280 of 350 retained) — nearly a fifth of apparent task difficulty was defects in the task, not capability being measured; single-pass synthesis difficulty is largely cosmetic, with models of comparable capability solving convoluted phrasings anyway.

- Real failures from grading bugs: Opus 4.5 scored 42% on CORE-Bench until rigid grading (penalizing "96.12" vs "96.124991…"), ambiguous specs, and irreproducible stochastic tasks were fixed → 95%. METR found misconfigured tasks where instructions said to optimize *to* a threshold but grading required *exceeding* it, rewarding models that ignored the stated goal.

- Write the verification criteria before materializing the task environment (blueprint-first): solvability and verifiability become design constraints rather than post-hoc LLM-judged afterthoughts — the source of the position/verbosity bias that makes post-hoc LLM adjudication unreliable (AutoGym, arXiv 2609.22592).

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
