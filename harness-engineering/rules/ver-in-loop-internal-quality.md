# ver-in-loop-internal-quality

> Compiler-passing, functionally-working agent output is not internal quality: agents suppress symptoms at call sites unless quality checks catch it inside the loop, not in after-the-fact review.

## Why It Matters

- Case: the agent declared API-token parameters as non-optional; when a later optional token wouldn't compile, the agent's "fix" was `token ?? ""` at the call site — compiling, kind-of working, but non-idiomatic, not self-documenting, unsupported by the type system, and requiring changes at every call site. The right fix was one `?` in the function declaration.

- Generated code frequently "worked" while degrading the codebase: an unexplained unnecessary cache, logic for a non-existent GitHub-style user/org overlap, duplicated URL-construction logic missing test hooks.

- Agents have a strong tendency to introduce technical debt when unsupervised — making future work harder for both humans and agents; internal quality is what keeps development sustainable over years.

- Consequence for harness design: don't rely on late manual review to catch this class of issue (semantic damage invisible to the type system); put idiomaticity/convention checks and reviewer-in-the-loop signals into the loop itself, and expect an experienced human to direct the agent away from symptom-level fixes.

## Scope

- Apply to any agent doing sustained codebase work: compiling, functionally-working output can still be degrading (symptom-suppressing fixes, unexplained caches, duplicated logic), and this damage is invisible to the type system.

- Don't rely on late manual review — put idiomaticity/convention checks and reviewer-in-the-loop signals into the loop itself; expect an experienced human to steer the agent away from symptom-level fixes.

- Weight the effort by codebase longevity: internal quality is what keeps development sustainable over years; throwaway scripts don't need the in-loop machinery.

- **When to skip**: Applies whenever unsupervised agents modify a codebase; skip when a human reviews every line anyway (though then ask why).

## Source

Martin Fowler / Erik Doernenburg 'Assessing internal quality while coding with an agent' (https://martinfowler.com/articles/exploring-gen-ai/ccmenu-quality.html)

## See Also

- [ver-self-verification-before-exit](ver-self-verification-before-exit.md) - exit-intercepting verification covers "does it work"; this rule covers the orthogonal "is the codebase still good" dimension
- [struct-backpressure-verification-gates](struct-backpressure-verification-gates.md) - tests and type checkers are necessary backpressure but pass while this damage accumulates — add convention checks
- [ver-layered-verification-stack](ver-layered-verification-stack.md) - where a convention/idiomaticity checker fits in the composed verifier stack
