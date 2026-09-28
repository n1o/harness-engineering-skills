# ver-skill-correctness-as-spec-consistency

> Treat an agent skill as an executable specification, not documentation: the SKILL.md declares the expected behavior, the workflow/scripts encode the factual behavior, and correctness is behavioral consistency between the two — checked by specification reasoning plus sandbox reproduction, never by reading the prose.

## Why It Matters

- Skill ecosystems outgrow review faster than humans can audit: >200,000 skills released within six months and 884,669 listed on skills.sh at data-collection time — automated correctness checking is the only process that scales to the catalog (SkillSpec, arXiv 2609.06052).
- Skills admit semantic faults that type systems and unit tests cannot catch — description drift (SKILL.md no longer matches what the scripts do) and intent conflicts between instructions — because the "program" is natural-language-plus-code (2609.06052).
- The fault rate is not hypothetical: applying Hoare-style specification consistency ({P} C {Q} adapted to prose+code artifacts) found 763 manually confirmed defects across 239 of 515 sampled skills — 46.4% defective — at 61.2% overall precision (55.4% workflow-defect, 67.1% code-defect precision) (2609.06052).
- Script-heavy skills are the worst offenders: 69.4% defective rate for script-carrying skills versus 18.1% for text-only skills — the more executable machinery a skill bundles, the more surface for prose/code divergence (2609.06052).
- Defects are heavily concentrated: 30 skills accounted for 41.7% of all identified defects (long-tail distribution), so targeted auditing of top-usage skills is the high-yield entry point (2609.06052).
- Specification discrepancies are defect hypotheses, not proofs: each candidate must be validated in an isolated sandbox (fresh workspace per run, warm container per skill) with minimal reproduction probes for code defects and synthesized trigger instructions with preconditions for workflow defects (2609.06052).

## Scope

- Apply when authoring or reviewing a skill — write the SKILL.md as a declared spec (per-step preconditions/postconditions) so prose and encoded behavior have a checkable relation.
- Apply when curating third-party skills for a library — run spec-consistency checks and sandbox reproduction before admission.
- Skip for plain deterministic tools or libraries — ordinary unit tests fully determine correctness; there is no prose layer to drift.
- Skip for throwaway one-off prompts with no reuse and no drift surface.

## Source

SkillSpec: Intent-Masked Specification Reasoning for Agent Skill Correctness (https://arxiv.org/abs/2609.06052)

## See Also

- [eval-define-checkable-success-first](eval-define-checkable-success-first.md) - that rule writes checkable criteria before building behavior; this rule extends the discipline to artifacts whose "implementation" includes natural language
- [tool-descriptions-as-prompts](tool-descriptions-as-prompts.md) - that rule makes descriptions unambiguous for invocation; this rule adds the inverse duty — the description must stay consistent with what the skill actually does
- [eval-trace-to-deterministic-checks](eval-trace-to-deterministic-checks.md) - deterministic checks over captured traces; here the checkable object is declared-vs-encoded behavior
- [tool-eval-driven-tool-iteration](tool-eval-driven-tool-iteration.md) - eval-driven iteration for tool behavior; this rule is the correctness gate that should run before those evals
- [ctx-skill-compactness-over-completeness](ctx-skill-compactness-over-completeness.md) - compactness and consistency compose: a compact spec is easier to keep consistent with the scripts
