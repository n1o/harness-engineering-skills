# eval-canary-injections-verify-human-oversight

> Continuously test that human oversight actually functions: inject known-defective artifacts into the human review stream at a measured rate and track catch rate; when catch rate decays, cut review volume and move load to deterministic gates — the presence of an overseer does not entail oversight.

## Why It Matters

- Irony of automation (Bainbridge 1983, revived for agents by arXiv 2608.23642): the more capable the automation, the more the human operator's skills and situation awareness degrade — humans are least prepared to intervene exactly when supervision is most needed. Oversight health must be measured, not assumed.
- Oversight degrades the overseer: the essay-writing study cited by the paper (Kosmyna et al., "Your Brain on ChatGPT") found significantly decreased brain connectivity in LLM-assisted writers — leaning on the agent erodes the capacities review requires (2608.23642, position paper).
- Overreliance studies synthesize a consistent finding: users take incorrect shortcuts, treating well-written style or the mere presence of citations as accuracy signals — a passing-looking agent artifact will be approved, so approval events are not evidence of verification (2608.23642).
- Governance mandates ("meaningful human control": EU AI Act Art. 14, NIST RMF) formalize the requirement while giving overseers virtually no mechanism to audit, review, or double-check — the harness must build the mechanism, and the only way to know it works is to test the overseer the way evals test the agent (2608.23642).
- Explanations don't fix this: the paper argues explanations operate on capacities that AI use itself degrades and can increase inappropriate trust; they cannot address approval fatigue. Canary catch rate is the direct measurement (2608.23642).
- The paper concedes users may disprefer systems that reduce overreliance — oversight preservation conflicts with user satisfaction, so it must be enforced by harness design (injection, measurement, load-shedding), not overseer goodwill (2608.23642).

## Scope

- Apply to any harness with a continuous human approval/review/audit step — merge approvals, release sign-offs, escalation queues, sampled artifact inspection.
- Skip when oversight is purely deterministic gates with no human in the accept path.
- Skip when human review is genuinely occasional high-stakes one-offs where fatigue doesn't accumulate.
- Canary rate and catch-rate threshold are fleet design parameters, not constants — the source reports no numbers of its own; set the injection rate so expected canaries per reviewer-week are large enough to measure but small enough not to train blindness.

## Source

AI Agents Push Humans Out of the Loop (https://arxiv.org/abs/2608.23642)

## See Also

- [prin-humans-on-the-loop-not-in-it](prin-humans-on-the-loop-not-in-it.md) - positions the human on the "how" loop; this rule verifies the residual human review actually functions under attention decay
- [eval-negative-controls](eval-negative-controls.md) - negative controls test the agent's behavior; canaries test the overseer — the oversight-side counterpart
- [ctx-illusion-of-control-probabilities](ctx-illusion-of-control-probabilities.md) - same epistemic stance applied to the human surface: an overseer in the loop is a probability-shifter, not a guarantee
- [guard-audit-log-every-decision](guard-audit-log-every-decision.md) - the decision log is where canary catches (and misses) must be recorded
