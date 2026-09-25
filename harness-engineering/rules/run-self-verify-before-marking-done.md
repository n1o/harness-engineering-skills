# run-self-verify-before-marking-done

> Absent explicit prompting, agents mark features complete without proper testing; require end-to-end self-verification as a real user before any feature status flips to passing.

## Why It Matters

- Observed failure mode: the agent makes code changes, even runs unit tests or `curl` against a dev server, yet fails to recognize the feature doesn't work end-to-end.

- Fix in harness: features may only be marked passing after careful testing with browser automation tools, exercising the app the way a human user would.

- Known limit from source: agent vision and browser-tool blind spots leave residual bugs (e.g., Claude can't see browser-native alert modals through the Puppeteer MCP, so modal-dependent features stayed buggier).

## Scope

- Apply whenever an agent can flip a feature or task to "done": the verification method must exercise the changed surface the way its real consumer does — browser automation for UI features, the real CLI invocation for CLI changes, actual API calls for backend work. Unit tests alone are not end-to-end verification.
- Grounded failure mode (from the source's UI-app context): agents marked UI features complete after code changes and even passing unit tests, while the feature didn't work end-to-end; the fix is harness-enforced testing, not trusting the agent's say-so.
- Known limit: browser-tool blind spots (e.g., browser-native alert modals invisible through Puppeteer MCP) leave residual bugs — consumer-path verification reduces but doesn't eliminate this class.

## Source

Anthropic, "Effective harnesses for long-running agents" (https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)

## See Also

- [ver-self-verification-before-exit](ver-self-verification-before-exit.md) - boundary: both about unverified "done", different enforcement points — this rule makes the agent exercise the feature end-to-end as a user before flipping a status flag; that rule intercepts agent exit with a verification checklist against the task spec
- [run-separate-generator-from-skeptical-evaluator](run-separate-generator-from-skeptical-evaluator.md) - second line of defense: self-verification happens in the generator; the skeptical evaluator catches what self-grading can't (agents grading own work skew positive)
- [run-feature-list-expanded-spec-with-pass-state](run-feature-list-expanded-spec-with-pass-state.md) - the status being flipped: `passes: false` entries in the feature list, the mechanical definition of done this rule gates
- [run-make-the-app-legible-and-runnable-init-script](run-make-the-app-legible-and-runnable-init-script.md) - prerequisite machinery: init.sh plus browser automation is what makes "verify as a real user" executable at all

