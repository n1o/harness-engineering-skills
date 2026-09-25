# obs-runtime-config-first-class-variable

> Treat the runtime's resource and environment configuration as a first-class experimental variable — documented and controlled with the same rigor as prompt format or sampling temperature — because infrastructure alone can move agentic benchmark scores by more than leaderboard gaps.

## Why It Matters

- Measured effect: Terminal-Bench 2.0 scores spanned 6 percentage points (p < 0.01) between strict per-task resource enforcement and uncapped, driven by infra error rates falling from 5.8% to 0.5%; SWE-bench showed the same monotonic effect at smaller magnitude (+1.54pp at 5x RAM)

- Specify two resource parameters per task, not one: a guaranteed allocation and a separate hard kill threshold — setting them equal leaves zero headroom, so transient spikes OOM-kill containers that would have succeeded

- Calibrate the band empirically so scores at floor and ceiling fall within noise: 3x headroom cut infra errors by ~two-thirds while the score lift stayed within noise (p = 0.40); beyond that, extra resources start "actively helping the agent solve problems it couldn't solve before" — changing what the eval measures

- Publish the configuration with any reported score, and run public evals at multiple times and on multiple days (pass rates were observed to fluctuate with time of day via API latency)

- Consumer rule of thumb from the source: "leaderboard differences below 3 percentage points deserve skepticism until the eval configuration is documented and matched"

## Scope

- Apply when reporting or comparing agentic benchmark scores: specify guaranteed allocation and a separate hard kill threshold per task, calibrate the band empirically (the source's 3x headroom cut infra errors ~two-thirds with the score lift within noise), and publish the configuration with any score.

- The "below 3 percentage points deserves skepticism" threshold is a rule of thumb from the source's Terminal-Bench context — apply as a default, re-measure for your own eval.

- Resource changes can start "actively helping the agent solve problems it couldn't solve before," so calibrate to the floor/ceiling noise band; skip the rigor for internal smoke tests whose scores no one will compare.

## Source

Anthropic, "Quantifying infrastructure noise in agentic coding evals" (https://www.anthropic.com/engineering/infrastructure-noise)

## See Also

- [eval-clean-environment-per-trial](eval-clean-environment-per-trial.md) - environment control as a validity requirement here; resource config as a measured noise variable there
- [struct-harness-as-declared-config](struct-harness-as-declared-config.md) - the runtime config belongs in the versioned, inspectable harness config
- [ver-harness-deltas-measured-by-evals](ver-harness-deltas-measured-by-evals.md) - infra noise is exactly the confound that harness-delta evals must hold fixed
