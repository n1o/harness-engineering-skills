# eval-start-small-grow-from-real-failures

> Start with 20–50 tasks (or 10–20 prompts for a single skill) drawn from real failures and manual checks; every failure you fix becomes a new eval case.

## Why It Matters

- Early in development each change has a large, noticeable effect, so small samples suffice; mature agents detecting smaller effects need bigger, harder suites — take the 80/20 approach first.

- Source tasks from what you already test manually, your bug tracker, and support queue; converting user-reported failures into test cases makes the suite reflect actual usage.

- A small CSV of prompts becomes a living record of scenarios the skill must keep getting right — add a row for every triggering miss, eager false-positive, or drift discovered during manual runs.

- Every manual fix during exploratory runs (missing `npm install`, wrong config order, vague trigger description) is a candidate eval — lock the intended behavior in before scaling evaluation.

## Scope

- Apply at eval-program start: 20–50 tasks (10–20 prompts for a single skill) drawn from manual checks, bug tracker, and support queue — every failure you fix becomes a new case.

- Grow only as the suite saturates: early changes have large, noticeable effects so small samples suffice; mature agents detecting smaller effects need bigger, harder suites.

- Skip big-bang suite building up front — take the 80/20 approach first and lock intended behavior in before scaling evaluation.

## Source

Anthropic 'Demystifying Evals for AI Agents' (https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents); OpenAI 'Testing Agent Skills Systematically with Evals' (https://developers.openai.com/blog/eval-skills/)

## See Also

- [eval-capability-vs-regression-suites](eval-capability-vs-regression-suites.md) - the mature-suite split this grows into: capability hill vs regression guard
- [eval-negative-controls](eval-negative-controls.md) - every triggering miss or eager false-positive found during manual runs becomes a row, including "should not fire"
- [eval-read-transcripts](eval-read-transcripts.md) - manual runs are the source of both new cases and the judgment that graders are fair
