# eval-no-skill-baseline

> Never evaluate a harness/skill addition in isolation — always compare against a no-skill/no-harness baseline on the same bounded task.

## Why It Matters

- Minimum comparison: no-skill (task with no procedural guidance) vs skill-enabled (same task, skill injected). Without the baseline, success tells you almost nothing — the model might have passed anyway, or the skill made it slower.

- A useful skill eval has three ingredients: a bounded task the agent can finish in one run, a deterministic verifier with pass/fail, and the no-skill baseline.

- Pass/fail is the primary metric; runtime, event count, and tool usage are secondary efficiency signals.

- Baselines expose the three archetypes: essential skills (dependency audit: 0% → 100% pass, 266s → 109s), guardrail skills (financial extraction: 90% → 100%), and mixed skills that help some models and regress others (sales pivot: one model passed more often *without* the skill).

- Skills can be actively harmful — SkillsBench found negative deltas for some skills, so "improved skill" is a hypothesis until measured.

- Skill value is task-dependent and model-dependent; evaluating one task overgeneralizes (the three tasks above yield three opposite conclusions). Skills also decay as models improve — periodically delete guidance and add it back only where the model goes off track.

## Scope

- Apply to any harness/skill addition — the minimum comparison is no-skill vs skill-enabled on the same bounded task; without it, success says almost nothing.

- Requires a bounded task the agent can finish in one run plus a deterministic pass/fail verifier; skip the A/B on unbounded tasks where a single run can't complete.

- Re-run baselines per model and periodically (skills decay as models improve; value is task- and model-dependent — one task overgeneralizes).

## Source

OpenHands 'How to Evaluate Agent Skills' (https://openhands.dev/blog/evaluating-agent-skills)

## See Also

- [tool-eval-driven-tool-iteration](tool-eval-driven-tool-iteration.md) - the same baseline-and-measure discipline for tools; this rule is the skill variant
- [eval-clean-environment-per-trial](eval-clean-environment-per-trial.md) - baseline and skill runs must start from identical environments
- [eval-define-checkable-success-first](eval-define-checkable-success-first.md) - the deterministic verifier presupposes checkable success criteria
- [eval-tier-by-scope](eval-tier-by-scope.md) - where the bounded task fits the single-step/full-run tiering
