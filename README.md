# harness-engineering — an agent skill for harness engineering

**104 evidence-grounded rules for shaping the environment around AI agents so they work reliably.**

Harness engineering is the practice of building the *harness* — everything that isn't the model: context delivery, tools, guardrails, verification, evals, telemetry, and the loop that binds them. When an agent is unreliable, the problem is usually the harness, not the model. This skill codifies how to fix it.

Every rule is distilled from a named primary source — Anthropic and OpenAI engineering articles, HumanLayer's 12 Factor Agents, Manus's context-engineering lessons, Thoughtworks/Martin Fowler, OpenHands, LangChain, the OpenTelemetry GenAI conventions, and open-source reference harnesses (SWE-agent, Harbor, Ralph, Agent AFK, completely, Citadel) — indexed by [awesome-harness-engineering](https://github.com/walkinglabs/awesome-harness-engineering). Runtime-agnostic: applies to Claude Code, Codex, OpenHands, or your own runtime.

## Layout

```
harness-engineering/
├── SKILL.md          # entry point: symptom→category router + start-here paths
├── INDEX.md          # full index: all 104 rules with one-line summaries
├── rules/            # 104 atomic rule files (10 categories, prefix-coded)
└── checks/
    └── validate.py   # structural linter: sections, links, index parity, attribution
```

## The ten categories

| Priority | Category | Prefix | Rules | What it covers |
|---|---|---|---:|---|
| CRITICAL | Context & Working State | `ctx-` | 21 | Context budget, KV-cache layout, compaction, instruction files, filesystem memory |
| CRITICAL | Verification & Quality Gates | `ver-` | 5 | Self-verification, in-loop quality, harness-change eval deltas |
| HIGH | Long-Running Execution | `run-` | 13 | Initializer agents, handoff artifacts, feature lists, session resets |
| HIGH | Tool Design | `tool-` | 8 | Tool naming, descriptions, response shaping, progressive discovery |
| HIGH | Guardrails & Safe Autonomy | `guard-` | 9 | Sandboxing, authorization hooks, untrusted content, allowlists, audit |
| HIGH | Evaluation Design | `eval-` | 14 | Baselines, negative controls, graders, task quality, pass@k vs pass^k |
| MEDIUM | Harness Structure | `struct-` | 10 | Bounded loops, externalized state, default-fail evaluators, worktrees |
| MEDIUM | Observability & Telemetry | `obs-` | 9 | OTel GenAI conventions, token metrics, cost honesty, trace hierarchies |
| MEDIUM | Operational Autonomy | `ops-` | 8 | Spend rails, ledgers, retry budgets, circuit breakers, idempotency |
| MEDIUM | Operating Principles | `prin-` | 7 | Harness-first thinking, humans on the loop, smallest-workable agents |

## How an agent uses it

1. **Route** — `SKILL.md` maps the symptom ("agent says it's done but the work is broken") to a category and a 4-rule start-here path. Rules load on demand, never all at once.
2. **Scope** — every rule states *when to apply it and when to skip it*, with numeric thresholds labeled as measured defaults from their sources, not universal constants.
3. **Cross-links** — `See Also` sections explain boundaries between related rules (compaction vs. condensation, masking vs. progressive discovery) so overlapping advice can't be read as conflicting.
4. **Attribution** — every rule cites its primary source with URL; read the source before adapting a rule to unusual constraints.

## Example rule

```markdown
# guard-sandbox-beats-permission-prompts

> Replace per-action approval prompts with pre-defined sandbox boundaries
> the agent can work freely inside; escalate to a human only for
> boundary violations.

## Why It Matters
- Per-action permission prompts cause approval fatigue — users stop paying
  attention to what they approve, making the system less safe...
- Anthropic measured 84% fewer permission prompts with sandboxing.
...
## Source
Anthropic, Beyond permission prompts: Claude Code sandboxing (https://...)
```

## Checks

```bash
python3 harness-engineering/checks/validate.py
# OK: 104 rules, SKILL.md and INDEX.md in sync, all sections present (0 attribution warning(s))
```

The validator enforces: rule-file structure (`# id` / `> summary` / Why It Matters / Scope / Source / See Also, in order), known category prefixes, valid See Also and INDEX links, SKILL.md category counts matching the directory, and publisher-label↔domain attribution sanity warnings.

## Provenance

Rules were distilled from the primary sources behind [awesome-harness-engineering](https://github.com/walkinglabs/awesome-harness-engineering), then reviewed by an independent reviewer (Codex/gpt-6-sol), which caught mis-attributions and over-absolute prescriptions; all verified findings were fixed. See `## Source` in each rule for its citation.

## License

CC0-1.0. Referenced upstream materials remain under their own licenses.
