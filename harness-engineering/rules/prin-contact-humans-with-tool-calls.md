# prin-contact-humans-with-tool-calls

> Model human interaction as structured tool calls (`request_human_input`, `request_approval`) with explicit metadata — not free-form chat — so approval, clarification, and multi-human coordination become durable, auditable parts of the control flow.

## Why It Matters

- Define typed request objects (question, context, urgency, format: free_text/yes_no/multiple_choice, choices) so the model must specify what it needs from a human and the harness can route it to the right channel.

- The request tool call breaks the loop, persists the thread, and notifies; the response arrives later via webhook with the thread ID — enabling Agent→Human initiated workflows (outer-loop agents triggered by cron/events) rather than only Human→Agent chat.

- Structured human events let you coordinate input from different humans and extend the same pattern to Agent→Agent requests.

- Combined with pause/resume, this makes multiplayer workflows durable, reliable, and introspectable — and is what makes it safe to give agents higher-stakes tools (production deploys, external emails) at all.

## Scope

- Apply wherever an agent can reach a decision a human should make — clarification, approval, multi-human coordination: model it as a typed tool call with structured metadata, not free-form chat.
- Highest leverage for outer-loop, agent-initiated workflows: the request call breaks the loop, persists the thread, and the response arrives later via webhook with the thread ID.
- Scale the request machinery to the stakes: the source's rationale is that structured requests are what make it safe to give agents higher-stakes tools at all — low-stakes, well-specified tasks generate few or none.

## Source

HumanLayer, "12 Factor Agents" (https://www.humanlayer.dev/blog/12-factor-agents)

## See Also

- [run-pause-resume-between-selection-and-execution](run-pause-resume-between-selection-and-execution.md) - the loop machinery this rule rides on: pausing persists the thread, and the human's webhook response resumes it
- [guard-pre-action-deterministic-authorization](guard-pre-action-deterministic-authorization.md) - boundary: structured requests handle judgment the model initiates; deterministic pre-call policy handles actions that must never run regardless of model intent
- [prin-humans-on-the-loop-not-in-it](prin-humans-on-the-loop-not-in-it.md) - where the human answering sits: respond to structured requests, but keep improving the harness so fewer approvals are needed over time
