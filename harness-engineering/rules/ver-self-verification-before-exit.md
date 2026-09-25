# ver-self-verification-before-exit

> Agents don't naturally verify their own work — they read their own code, say "looks ok," and stop. Engineer a build→verify→fix loop and intercept exit with a verification checklist.

## Why It Matters

- Prompt a four-phase problem-solving cycle: plan & discovery (including how to *verify* the solution), build (with verification in mind; write tests if none exist, happy path + edge cases), verify (run tests, read full output, compare against the task spec — not against your own code), fix (analyze errors, revisit the original spec).

- Deterministic context injection beats prompting alone: a PreCompletionChecklist middleware intercepts the agent before it exits and forces a verification pass against the task spec (cf. the Ralph Wiggum loop pattern of hooking exit).

- Tell agents their work will be measured by programmatic tests (follow file paths exactly, handle edge cases) — this alone avoids "slop buildup" and is a powerful general strategy.

- Self-verification is the agent self-improving *within* a run; testing gives it a signal to hill-climb against, which matters most in autonomous settings with no human in the loop.

## Scope

- The "agents don't naturally verify their own work" claim is the source's observed default (they read their code, say "looks ok," and stop) — engineer the build→verify→fix cycle and a PreCompletionChecklist that intercepts exit rather than assuming the behavior.

- Apply most where no human is in the loop: self-verification is the agent self-improving within a run, and the programmatic-tests framing alone avoids "slop buildup".

- Skip the exit interception for cheap throwaway tasks where a human sees every output anyway — the checklist is friction when verification has no consequence.

## Source

LangChain 'Improving Deep Agents with harness engineering' (https://blog.langchain.com/improving-deep-agents-with-harness-engineering/)

## See Also

- [run-self-verify-before-marking-done](run-self-verify-before-marking-done.md) - the boundary: this rule intercepts *exit* with a verification checklist against the spec; that rule requires end-to-end verification *as a real user* (browser automation) before any feature flips to passing — both answer "unverified done"
- [struct-default-fail-evaluator](struct-default-fail-evaluator.md) - self-verification feeds an independent default-FAIL evaluator; it is not a substitute for one
- [ver-layered-verification-stack](ver-layered-verification-stack.md) - this checklist is one layer; compose it with trajectory critics and patch checks
