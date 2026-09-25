# struct-default-fail-evaluator

> Put an independent, read-only evaluator in the close path that returns FAIL for every acceptance criterion unless it has direct, reproducible evidence — no evidence = no pass.

## Why It Matters

- "The agent never grades its own homework": the evaluator is a separate process from the worker, and every criterion starts FAIL, flipping only on evidence the grader re-ran itself

- The evaluator checks work four ways it can be fake: **Path-Exercised** (the real runtime path ran, not a mock or `--dry-run`, with a negative control), **User-Perceived** (exercised as a user — run the command, hit the endpoint, screenshot), **Code-Read** (the grader reads the diff and re-derives correctness — off-by-ones, swallowed errors, fail-open defaults — independent of the reviewer), plus a no-stub/no-downscope lint contract and an adversarial claim-vs-refute mode

- A rejected evaluation loops back to implementation, not to closure — the gate sits in the close path of the loop, not after it

- The harness holds itself to the same bar: during its own development the default-FAIL evaluator "caught a real over-graded task — and its loop caught a flagship crash that shipped with a fully green test suite — before they could land"

- Anti-example: Ralph-style loops trust the agent's self-reported exit signal; a self-graded "done" is indistinguishable from an asserted one

## Scope

- Apply to unattended, high-stakes work where a falsely-graded success is expensive to discover later — the harness itself caught an over-graded task and a flagship crash that shipped with a green suite.

- Skip for cheap, reversible, human-reviewed tasks: rerunning every criterion to get direct, reproducible evidence is the expensive part, so pay it where "the agent never grades its own homework" is a real risk.

- The gate sits in the close path of the loop, not after it — a rejected evaluation loops back to implementation.

## Source

completely (https://github.com/23ag1/completely)

## See Also

- [run-separate-generator-from-skeptical-evaluator](run-separate-generator-from-skeptical-evaluator.md) - the boundary: this rule is a deterministic, evidence-only close-path grader (default FAIL, re-ran the evidence itself); that rule tunes a skeptical *evaluator agent* with prompts and tools
- [struct-deterministic-exit-code-gates](struct-deterministic-exit-code-gates.md) - mechanical gates (lint/types on edit, no closure over unresolved findings) that enforce part of this contract
- [ver-self-verification-before-exit](ver-self-verification-before-exit.md) - in-run self-verification complements the independent close-path evaluator; it doesn't replace it
