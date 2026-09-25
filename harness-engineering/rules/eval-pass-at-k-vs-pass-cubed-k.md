# eval-pass-at-k-vs-pass-cubed-k

> Agent non-determinism demands reporting both "at least one success in k trials" and "all k trials succeed" — they diverge sharply and answer different product questions.

## Why It Matters

- Each task has its own success rate; a task that passed last run may fail this run, so measure the proportion of trials that succeed.

- pass@k = probability of ≥1 success in k attempts (rises with k); pass^k = probability all k trials succeed (falls with k — 0.75 per-trial ⇒ ~42% pass^3).

- At k=10 they tell opposite stories: pass@k approaches 100% while pass^k approaches 0%.

- Use pass@k when one success is enough (search/proposal tools); use pass^k for customer-facing agents where consistent reliability is the requirement.

## Scope

- Apply whenever trials are non-deterministic and you report per-task success; a task that passed last run may fail this run, so report the proportion of trials that succeed.

- The simple p^k math (0.75 per-trial ⇒ ~42% pass^3) assumes a stable, independent per-trial success probability — correlated failures or a drifting agent break it, so treat the numbers as estimates.

- Choose by product shape: pass@k for search/proposal tools where one success suffices; pass^k for customer-facing agents where consistent reliability is the requirement.

## Source

Anthropic 'Demystifying Evals for AI Agents' (https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)

## See Also

- [eval-clean-environment-per-trial](eval-clean-environment-per-trial.md) - shared state correlates trials, invalidating the independence both metrics assume
- [eval-capability-vs-regression-suites](eval-capability-vs-regression-suites.md) - which metric a saturated regression suite should report
- [eval-read-transcripts](eval-read-transcripts.md) - per-trial transcripts are how you tell a genuine failure from grader noise
