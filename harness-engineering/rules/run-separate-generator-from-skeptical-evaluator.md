# run-separate-generator-from-skeptical-evaluator

> Separate the agent that does the work from a separately-tuned agent that judges it — and calibrate the evaluator to be explicitly skeptical, since agents grading their own work (or even each other's) skew positive.

## Why It Matters

- Agents asked to evaluate their own work respond by "confidently praising the work" even when quality is obviously mediocre; separation alone doesn't fix leniency, but tuning a standalone evaluator to be skeptical is far more tractable than making a generator critical of itself.

- Turn subjective judgments ("is this design good?") into concrete gradable criteria — e.g., design quality, originality, craft, functionality — with hard thresholds; any criterion below threshold fails the sprint and the generator gets specific, actionable feedback.

- Give the evaluator real interaction tools (Playwright MCP) so it clicks through the running application like a user, testing UI, API endpoints, and database states — not static screenshots.

- Tune the evaluator by reading its logs, finding where its judgment diverged from yours, and updating its prompt; the source found out-of-the-box Claude "identify[s] legitimate issues, then talk[s] itself into deciding they weren't a big deal."

- Negotiate a sprint contract between generator and evaluator (what "done" looks like, and the testable behaviors that verify it) before any code is written — bridging high-level spec to testable implementation without over-specifying. Communicate via files the agents read and write.

- Keep specs high-level on purpose: if the planner specifies granular technical details upfront and gets something wrong, the errors cascade downstream; constrain deliverables and let the agent figure out the path.

## Scope

- Apply to autonomous builds where quality judgments are subjective enough to fool a self-grader: a separately-tuned evaluator judges the generator's work, because agents grading their own work "confidently praise" it, and separation alone doesn't fix leniency.
- Calibration is the real work: turn subjective judgments into concrete gradable criteria with hard thresholds, give the evaluator real interaction tools (Playwright MCP), and tune it by reading its logs where judgment diverged from yours.
- Cost/benefit, not fixed: per the source, the evaluator is worth it when the task sits beyond what the model does reliably solo; as capability moves outward it becomes overhead for in-boundary tasks — keep it for edge-of-capability work (see run-harness-component-attrition-on-model-upgrade).

## Source

Anthropic, "Harness design for long-running application development" (https://www.anthropic.com/engineering/harness-design-long-running-apps); Anthropic, "Building effective agents" (https://www.anthropic.com/engineering/building-effective-agents)

## See Also

- [run-self-verify-before-marking-done](run-self-verify-before-marking-done.md) - boundary: self-verification happens inside the generator before a status flip; the skeptical evaluator is a separate agent judging the finished work — first line and second line against the same unverified-done failure
- [struct-default-fail-evaluator](struct-default-fail-evaluator.md) - boundary: tuned skeptical evaluator agent (prompted, logged, iterated) vs deterministic evidence-only grader in the close path — default-FAIL, no evidence = no pass; pick by whether judgment needs LLM flexibility or only proof
- [run-harness-component-attrition-on-model-upgrade](run-harness-component-attrition-on-model-upgrade.md) - the lifecycle question: the evaluator is a component encoding what the model can't do solo, so re-run the worth-it decision on every model upgrade
- [eval-define-checkable-success-first](eval-define-checkable-success-first.md) - upstream habit that makes evaluator criteria tractable: concrete checkable success split into outcome/process/style/efficiency

