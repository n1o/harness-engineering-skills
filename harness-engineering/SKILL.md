---
name: harness-engineering
description: >
  Harness-engineering guidelines with 104 rules across 10 categories for shaping
  the environment around AI agents so they work reliably. Use when building,
  tuning, or reviewing an agent harness: context management, tool design,
  sandboxing and authorization, long-running execution, verification gates,
  evals, telemetry, and operational autonomy. Covers context windows, KV-cache
  layout, instruction files, sandbox boundaries, retry economics, eval design,
  and harness structure. Runtime-agnostic (Claude Code, Codex, OpenHands,
  custom runtimes).
license: CC0-1.0
metadata:
  author: harness-engineering-skills
  version: "0.2.0"
  sources:
    - awesome-harness-engineering (walkinglabs) primary-source index
    - Anthropic engineering articles (harnesses, context, tools, sandboxing, evals)
    - OpenAI harness-engineering field report
    - HumanLayer 12 Factor Agents and context-engineering posts
    - Manus context-engineering lessons
    - Martin Fowler / Thoughtworks harness and context articles
    - OpenHands blog (condensation, skills evals, verification, security)
    - LangChain anatomy / deep-agents eval posts
    - OpenTelemetry GenAI semantic conventions
    - Reference harnesses: SWE-agent, Harbor, Ralph, Agent AFK, completely, Citadel
---

# Harness Engineering

Guidelines for engineering the environment around AI agents — the harness — so agents work reliably on real tasks. 104 rules across 10 categories, each distilled from a named primary source (article, spec, or reference implementation) and runtime-agnostic: applies whether your harness is Claude Code, Codex, OpenHands, or custom.

**The full rule index lives in [INDEX.md](INDEX.md).** Read this page to route to the right category and a handful of rules — do not load all rules at once.

## Routing: diagnose the failure class first

| Symptom / task | Start with | Then, if needed |
|---|---|---|
| Agent lacks project knowledge, drifts, forgets goals, context bloat | `ctx-` (21 rules) | `run-` for cross-session continuity |
| Agent marks work done without really verifying it | `ver-` (5) | `eval-` to build the gate |
| Long-running / multi-session work degrades or loses state | `run-` (13) | `struct-` for the loop architecture |
| Wrong tool called, tool results waste context, tools misused | `tool-` (8) | `ctx-` for response-size budgeting |
| Agent too dangerous, needs sandboxing or permissions | `guard-` (9) | `ops-` for economic limits |
| Building or fixing an eval suite | `eval-` (14) | `ver-` for in-run verification |
| Harness architecture: loops, workers, worktrees, recovery | `struct-` (10) | `run-` for session boundaries |
| Can't see what the agent did; costs unknown | `obs-` (9) | `eval-` to turn traces into checks |
| Retries, budgets, spending authority, fleet failures | `ops-` (8) | `guard-` for authorization |
| Harness feels over-engineered; humans micromanaging artifacts | `prin-` (7) | `run-` (component attrition) |

Category priorities: `ctx-` and `ver-` are CRITICAL; `run-`, `tool-`, `guard-`, `eval-` are HIGH; `struct-`, `obs-`, `ops-`, `prin-` are MEDIUM. Priority is about default attention, not task importance — for a spending agent, `ops-`/`guard-` outrank everything else.

## Start-here paths by failure mode

- **"The agent gets lost / forgets / drifts mid-task"** → [ctx-working-memory-budget](rules/ctx-working-memory-budget.md), [ctx-frequent-intentional-compaction](rules/ctx-frequent-intentional-compaction.md), [ctx-structured-notes-across-resets](rules/ctx-structured-notes-across-resets.md), [ctx-recitation-recenter-attention](rules/ctx-recitation-recenter-attention.md)
- **"The agent says it's done but the work is broken"** → [ver-self-verification-before-exit](rules/ver-self-verification-before-exit.md), [run-self-verify-before-marking-done](rules/run-self-verify-before-marking-done.md), [struct-default-fail-evaluator](rules/struct-default-fail-evaluator.md), [eval-trace-to-deterministic-checks](rules/eval-trace-to-deterministic-checks.md)
- **"Sessions can't resume / long projects fall apart"** → [run-context-reset-handoff-artifacts-across-windows](rules/run-context-reset-handoff-artifacts-across-windows.md), [struct-externalize-loop-state-files](rules/struct-externalize-loop-state-files.md), [struct-bounded-single-task-loop](rules/struct-bounded-single-task-loop.md), [run-feature-list-expanded-spec-with-pass-state](rules/run-feature-list-expanded-spec-with-pass-state.md)
- **"I need to let it run unattended safely"** → [guard-sandbox-beats-permission-prompts](rules/guard-sandbox-beats-permission-prompts.md), [guard-untrusted-content-as-data](rules/guard-untrusted-content-as-data.md), [guard-pre-action-deterministic-authorization](rules/guard-pre-action-deterministic-authorization.md), [struct-explicit-terminal-states](rules/struct-explicit-terminal-states.md)
- **"Tools confuse the agent / burn context"** → [tool-few-purposeful-tools](rules/tool-few-purposeful-tools.md), [tool-descriptions-as-prompts](rules/tool-descriptions-as-prompts.md), [ctx-deterministic-output-backpressure](rules/ctx-deterministic-output-backpressure.md), [tool-progressive-tool-discovery](rules/tool-progressive-tool-discovery.md)
- **"I can't tell if a harness change helped"** → [eval-no-skill-baseline](rules/eval-no-skill-baseline.md), [ver-harness-deltas-measured-by-evals](rules/ver-harness-deltas-measured-by-evals.md), [eval-pass-at-k-vs-pass-cubed-k](rules/eval-pass-at-k-vs-pass-cubed-k.md), [obs-runtime-config-first-class-variable](rules/obs-runtime-config-first-class-variable.md)

## How to Use

1. **Route** with the table above; read only the rules in the start-here path.
2. **Every rule has a Scope section** stating when it applies and when to skip it — read it before treating the rule as universal.
3. **Attribute**: every rule cites its primary source — read the source before adapting the rule to unusual constraints.
4. **Evolve the harness**: as models improve, remove components that are no longer load-bearing ([run-harness-component-attrition-on-model-upgrade](rules/run-harness-component-attrition-on-model-upgrade.md)).

## Sources & Attribution

This skill is an independent synthesis of publicly published engineering articles, specifications, and open-source reference harnesses. It is not affiliated with or endorsed by any source author. Each rule file cites its source; the primary index is [awesome-harness-engineering](https://github.com/walkinglabs/awesome-harness-engineering). Full per-category rule listing: [INDEX.md](INDEX.md).

Licensed CC0-1.0. Referenced upstream materials remain under their own licenses.