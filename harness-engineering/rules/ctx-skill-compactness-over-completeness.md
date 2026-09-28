# ctx-skill-compactness-over-completeness

> Author skills compact and attach few per task: measured gains collapse as skill documentation grows comprehensive or skill count rises past 2–3 — more skill material can subtract performance, so never pad a skill into an exhaustive manual.

## Why It Matters

- Length ablation on 87 tasks (SkillsBench, arXiv 2602.12670): compact skills gained +19.0pp and standard-length +21.5pp, while detailed gained +14.5pp and comprehensive gained only +0.7pp — a ~21pp gain collapses to near zero as documentation becomes exhaustive.
- Count ablation: tasks with 1 skill (+18.0pp) or 2–3 skills (+19.0pp) outperformed tasks with ≥4 skills (+10.1pp) — stacking skills roughly halves the benefit (2602.12670).
- Skills actively hurt on 13 of 87 tasks (down to −7.4pp): trajectory audits identified three mechanisms — heavyweight pipelines crowd out simpler solutions, skill activation displaces stronger native strategies, and skills point agents at solvers they cannot debug (2602.12670).
- Invocation is not efficacy: one model invoked the skill on 99.2% of trials without proportionate resolution — failures happen after skill access, so making skills more discoverable or more thorough does not fix them (2602.12670).
- Self-generated skills underperformed even the no-skill baseline by −8.1 to −11.5pp, while curated skills gained +18.2 to +24.8pp — model-authored procedural text does not reproduce curated quality, so compactness must come from curation, not generation volume (2602.12670).
- Aggregate effect for calibration: 33.9% → 50.5% average pass rate across 18 model-harness configurations (+16.6pp) with every configuration improving — the ceiling for what compact curation delivers is real but bounded (2602.12670).

## Scope

- Apply when writing or trimming any SKILL.md — default to compact/standard length; comprehensive prose must justify itself with a measured paired delta.
- Apply when deciding how many skills to load or attach per task — prefer 1–3 and treat ≥4 as a smell requiring evidence.
- Skip when a task genuinely needs a heavyweight domain procedure the model cannot reconstruct from pretraining — the specialized-procedure domains showed the largest measured gains; but verify by paired evaluation rather than assuming.
- The always-loaded instruction file (CLAUDE.md/AGENTS.md) is a different case — governed by `ctx-instruction-file-minimal-universal`.

## Source

SkillsBench: Benchmarking How Well Agent Skills Work Across Diverse Tasks (https://arxiv.org/abs/2602.12670)

## See Also

- [ctx-instruction-file-minimal-universal](ctx-instruction-file-minimal-universal.md) - bounds the always-loaded instruction file; this rule bounds on-demand skills, where the same degradation appears with sharper measured penalties
- [eval-no-skill-baseline](eval-no-skill-baseline.md) - the paired no-skill baseline is how you detect the negative-delta cases this rule warns about
- [ctx-working-memory-budget](ctx-working-memory-budget.md) - skills consume the attention budget; the +0.7pp comprehensive-skill result is what losing that budget to padding looks like
- [ctx-progressive-disclosure-pointers](ctx-progressive-disclosure-pointers.md) - the mechanism that keeps compact skills sufficient: pointers into detail instead of inlined detail
- [ver-skill-correctness-as-spec-consistency](ver-skill-correctness-as-spec-consistency.md) - a compact spec is also easier to keep consistent with the encoded scripts
