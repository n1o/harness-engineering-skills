# run-pause-resume-between-selection-and-execution

> Support launching, pausing, and resuming the agent with simple APIs — critically, the ability to interrupt between the moment a tool is selected and the moment it is invoked.

## Why It Matters

- The source calls the inability to review/approve a tool call before it runs the "number one feature request" for agent frameworks.

- Without it you must pick one of: hold the task in memory (losing it on interruption), restrict the agent to low-stakes calls, or "yolo" high-stakes tools and hope.

- Pause points are tool-type-specific in the control loop: benign lookups run inline; human-approval-needed or long-running operations break the loop, persist the thread, and wait for an external trigger (webhook) to resume.

- Pausing/resuming also enables durable multiplayer workflows: many humans, agents, and channels can interact with one thread over time.

## Scope

- Apply whenever an agent can select a tool with stakes worth interrupting: pause between tool selection and invocation — the source calls the inability to review/approve before a call runs the "number one feature request."
- Tool-type-specific pause points: benign lookups run inline; human-approval-needed or long-running operations break the loop, persist the thread, and wait for an external trigger (webhook) to resume.
- Skip pause machinery for low-stakes, well-sandboxed toolsets — without it you're forced into one of: hold the task in memory, restrict to low-stakes calls, or yolo high-stakes tools and hope.

## Source

HumanLayer, "12 Factor Agents" (https://www.humanlayer.dev/blog/12-factor-agents)

## See Also

- [prin-contact-humans-with-tool-calls](prin-contact-humans-with-tool-calls.md) - boundary: pause/resume is the loop machinery; structured human-request tool calls are how the paused thread asks a human something and gets resumed by webhook
- [guard-pre-action-deterministic-authorization](guard-pre-action-deterministic-authorization.md) - boundary: pause-for-approval is judgment the model defers; deterministic pre-call hooks enforce actions that must never run regardless of model intent
- [run-unify-state-own-your-context](run-unify-state-own-your-context.md) - same 12FA source: pausing/resuming is trivial only when all state lives in the serializable thread

