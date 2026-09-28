# harness-engineering — an agent skill for harness engineering

**120 evidence-grounded rules for shaping the environment around AI agents so they work reliably.**

Harness engineering is the practice of building the *harness* — everything that isn't the model: context delivery, tools, guardrails, verification, evals, telemetry, and the loop that binds them. When an agent is unreliable, the problem is usually the harness, not the model. This skill codifies how to fix it.

Every rule is distilled from a named primary source — Anthropic and OpenAI engineering articles, HumanLayer's 12 Factor Agents, Manus's context-engineering lessons, Thoughtworks/Martin Fowler, OpenHands, LangChain, the OpenTelemetry GenAI conventions, and open-source reference harnesses (SWE-agent, Harbor, Ralph, Agent AFK, completely, Citadel) — indexed by [awesome-harness-engineering](https://github.com/walkinglabs/awesome-harness-engineering). Runtime-agnostic: applies to Claude Code, Codex, OpenHands, or your own runtime.

## Layout

```
harness-engineering/
├── SKILL.md          # entry point: symptom→category router + start-here paths
├── INDEX.md          # full index: all 120 rules with one-line summaries
├── PAPERS.md         # provenance: research papers → distilled rules (2026 agent research layer)
├── rules/            # 120 atomic rule files (10 categories, prefix-coded)
└── checks/
    └── validate.py   # structural linter: sections, links, index parity, attribution
```

## The ten categories

| Priority | Category | Prefix | Rules | What it covers |
|---|---|---|---:|---|
| CRITICAL | Context & Working State | `ctx-` | 26 | Context budget, KV-cache layout, compaction, instruction files, filesystem memory, agent memory substrates |
| CRITICAL | Verification & Quality Gates | `ver-` | 7 | Self-verification, in-loop quality, harness-change eval deltas, self-edit gates |
| HIGH | Long-Running Execution | `run-` | 15 | Initializer agents, handoff artifacts, feature lists, session resets, dead-end ledgers |
| HIGH | Tool Design | `tool-` | 8 | Tool naming, descriptions, response shaping, progressive discovery |
| HIGH | Guardrails & Safe Autonomy | `guard-` | 10 | Sandboxing, authorization hooks, untrusted content, allowlists, audit, collusion rotation |
| HIGH | Evaluation Design | `eval-` | 16 | Baselines, negative controls, graders, task quality, pass@k vs pass^k, harness pinning, oversight canaries |
| MEDIUM | Harness Structure | `struct-` | 12 | Bounded loops, externalized state, default-fail evaluators, worktrees, adaptive harness retrieval, bounded generative UI |
| MEDIUM | Observability & Telemetry | `obs-` | 9 | OTel GenAI conventions, token metrics, cost honesty, trace hierarchies |
| MEDIUM | Operational Autonomy | `ops-` | 8 | Spend rails, ledgers, retry budgets, circuit breakers, idempotency |
| MEDIUM | Operating Principles | `prin-` | 9 | Harness-first thinking, humans on the loop, smallest-workable agents, control flow in code, internalization |

Sixteen rules are distilled from 2026 peer-reviewed agent research (self-evolving harnesses, agent memory, skills benchmarks, multi-agent collusion) via their Dissecting AI lecture summaries — see [harness-engineering/PAPERS.md](harness-engineering/PAPERS.md) for the paper→rule provenance map. The papers:

### Research papers cited

**Self-improving harnesses**

- Zhang, H., Zhang, S., Li, K., et al. (2026). *Self-Harness: Harnesses That Improve Themselves.* arXiv:2606.09498. https://arxiv.org/abs/2606.09498 → [ver-self-edit-non-regression-gate](harness-engineering/rules/ver-self-edit-non-regression-gate.md), [run-harness-optimization-per-model](harness-engineering/rules/run-harness-optimization-per-model.md), [run-dead-end-ledger-scar-tissue](harness-engineering/rules/run-dead-end-ledger-scar-tissue.md)
- Huang, L., Yang, C., Zhou, H., et al. (2026). *Evo-Bench: Can Language Models Improve Agent Harness?* arXiv:2608.09096. https://arxiv.org/abs/2608.09096 → [ver-self-edit-non-regression-gate](harness-engineering/rules/ver-self-edit-non-regression-gate.md)
- Zhang, J., Hu, S., Lu, C., Lange, R., & Clune, J. (2025). *Darwin Gödel Machine: Open-Ended Evolution of Self-Improving Agents.* arXiv:2505.22954. https://arxiv.org/abs/2505.22954 → [ver-self-edit-non-regression-gate](harness-engineering/rules/ver-self-edit-non-regression-gate.md), [run-dead-end-ledger-scar-tissue](harness-engineering/rules/run-dead-end-ledger-scar-tissue.md)
- Park, S., Kim, W., Tan, R., et al. (2026). *AutoSaddler: Automatic Harness Optimization with Durable Updates from Agent Execution Traces.* arXiv:2608.23041. https://arxiv.org/abs/2608.23041 → [ver-self-edit-non-regression-gate](harness-engineering/rules/ver-self-edit-non-regression-gate.md)
- Huang, Y., Wang, W., Bao, H., et al. (2026). *MemoHarness: Agent Harnesses That Learn from Experience.* arXiv:2607.14159. https://arxiv.org/abs/2607.14159 → [struct-adaptive-harness-per-task-retrieval](harness-engineering/rules/struct-adaptive-harness-per-task-retrieval.md), [run-harness-optimization-per-model](harness-engineering/rules/run-harness-optimization-per-model.md), [run-dead-end-ledger-scar-tissue](harness-engineering/rules/run-dead-end-ledger-scar-tissue.md), [prin-internalize-harness-into-model](harness-engineering/rules/prin-internalize-harness-into-model.md)
- Liu, H., Ye, T., Gao, S., et al. (2026). *SoL-Pi: Recursively Scaling Auto-Research Loops for Efficient Agent Harness.* arXiv:2609.20519. https://arxiv.org/abs/2609.20519 → [run-harness-optimization-per-model](harness-engineering/rules/run-harness-optimization-per-model.md)
- Ye, H., Lu, Y., Dong, H., Su, Z., & Song, G. (2026). *Harness-Zero: Harness Distillation via Agent-as-Harness.* arXiv:2609.24974. https://arxiv.org/abs/2609.24974 → [prin-internalize-harness-into-model](harness-engineering/rules/prin-internalize-harness-into-model.md)
- Zhang, G., Lu, L., Xie, F., et al. (2026). *JIT-Agent: Scaling Harness Intelligence via Just-in-Time Harness Evolution.* arXiv:2608.25593. https://arxiv.org/abs/2608.25593 → [struct-adaptive-harness-per-task-retrieval](harness-engineering/rules/struct-adaptive-harness-per-task-retrieval.md)
- Li, M., Li, D., Ning, X., et al. (2026). *Auto-RecSys: Harnessing Autonomous Research Agents for Industry-Scale Recommender System.* arXiv:2609.10922. https://arxiv.org/abs/2609.10922 → [run-dead-end-ledger-scar-tissue](harness-engineering/rules/run-dead-end-ledger-scar-tissue.md)
- Wu, Y., Zhang, J., Shi, J., et al. (2026). *HarnessDev: Can LLMs Create and Evolve Their Own Agent Harness?* arXiv:2609.01437. https://arxiv.org/abs/2609.01437 → [run-harness-optimization-per-model](harness-engineering/rules/run-harness-optimization-per-model.md)

**Agent memory**

- Huang, W.-C., Zhang, W., Wu, Y., et al. (2026). *Harness the Memory: A Holistic Evaluation of Memory Substrates in Memory Agents.* arXiv:2608.15008. https://arxiv.org/abs/2608.15008 → [ctx-memory-substrate-routing](harness-engineering/rules/ctx-memory-substrate-routing.md), [ctx-memory-curation-scored-forgetting](harness-engineering/rules/ctx-memory-curation-scored-forgetting.md)
- Wu, R., Fu, D., Wen, L., et al. (2026). *MemHarness: Memory Is Reconstructed, Not Replayed.* arXiv:2607.28272. https://arxiv.org/abs/2607.28272 → [ctx-memory-reconstruct-not-replay](harness-engineering/rules/ctx-memory-reconstruct-not-replay.md), [ctx-memory-curation-scored-forgetting](harness-engineering/rules/ctx-memory-curation-scored-forgetting.md)
- Rusu, T., Khanzadeh, S., & Alalfi, M. (2026). *Selective Forgetting: A Graph-Based Memory Framework for Long-Term LLM Agents.* arXiv:2608.28978. https://arxiv.org/abs/2608.28978 → [ctx-memory-curation-scored-forgetting](harness-engineering/rules/ctx-memory-curation-scored-forgetting.md), [ctx-memory-substrate-routing](harness-engineering/rules/ctx-memory-substrate-routing.md)
- Jiang, D., Li, Y., & Li, B. (2026). *Jev-Mem: System-One-Controlled Agentic Memory for Efficient AI Agents.* arXiv:2609.23986. https://arxiv.org/abs/2609.23986 → [ctx-memory-curation-scored-forgetting](harness-engineering/rules/ctx-memory-curation-scored-forgetting.md)
- Chong, M., Zhang, S., Fan, J., & Du, X. (2026). *EvoOntology: A Self-Evolving Ontology Layer for Data Agents.* arXiv:2609.15779. https://arxiv.org/abs/2609.15779 → [ctx-evolved-knowledge-gated-by-validation](harness-engineering/rules/ctx-evolved-knowledge-gated-by-validation.md)

**Skills, scaffolds, and harness formalization**

- Vats, N., & Golev, O. (2026). *The Scaffold Effect in Coding Agents: Harness Choice as a Hidden Variable in Coding-Agent Evaluation.* arXiv:2607.22585. https://arxiv.org/abs/2607.22585 → [eval-pin-harness-with-model](harness-engineering/rules/eval-pin-harness-with-model.md)
- Li, X., Liu, Y., Chen, W., et al. (2026). *SkillsBench: Benchmarking How Well Agent Skills Work Across Diverse Tasks.* arXiv:2602.12670. https://arxiv.org/abs/2602.12670 → [eval-pin-harness-with-model](harness-engineering/rules/eval-pin-harness-with-model.md), [ctx-skill-compactness-over-completeness](harness-engineering/rules/ctx-skill-compactness-over-completeness.md)
- Zhang, Y., Kang, B., Yang, Y., Duan, Z., Ye, Z., & Yang, S. (2026). *SkillSpec: Intent-Masked Specification Reasoning for Agent Skill Correctness.* arXiv:2609.06052. https://arxiv.org/abs/2609.06052 → [ver-skill-correctness-as-spec-consistency](harness-engineering/rules/ver-skill-correctness-as-spec-consistency.md)
- Qi, J., Fu, Z., Gao, J., Zhang, W., Yan, H., Wu, X., & Zhao, X. (2026). *LLM-as-Code: Agentic Programming for Agent Harness.* arXiv:2606.15874. https://arxiv.org/abs/2606.15874 → [prin-control-flow-in-code-not-model](harness-engineering/rules/prin-control-flow-in-code-not-model.md)

**Multi-agent interaction, oversight, and human-facing surfaces**

- Shi, X., Zhang, Y., & Yang, D. (2026). *Emergent Collusion in Long-Horizon LLM Agent Interaction.* arXiv:2609.24967. https://arxiv.org/abs/2609.24967 → [guard-rotate-peer-verifiers-against-collusion](harness-engineering/rules/guard-rotate-peer-verifiers-against-collusion.md)
- Mitchell, M., Ghosh, A., & Passi, S. (2026). *AI Agents Push Humans Out of the Loop.* arXiv:2608.23642. https://arxiv.org/abs/2608.23642 → [eval-canary-injections-verify-human-oversight](harness-engineering/rules/eval-canary-injections-verify-human-oversight.md)
- Li, X., Jiang, N., & Selvaraj, J. (2025). *Portal UX Agent — A Plug-and-Play Engine for Rendering UIs from Natural Language Specifications.* arXiv:2511.00843. https://arxiv.org/abs/2511.00843 → [struct-generative-ui-schema-bounded](harness-engineering/rules/struct-generative-ui-schema-bounded.md)
- Kong, F., Zheng, C., Zhuang, M., et al. (2026). *Macaron-A2UI: A Model for Generative UI in Personal Agents.* arXiv:2605.24830. https://arxiv.org/abs/2605.24830 → [struct-generative-ui-schema-bounded](harness-engineering/rules/struct-generative-ui-schema-bounded.md)

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
# OK: 120 rules, SKILL.md and INDEX.md in sync, all sections present (0 attribution warning(s))
```

The validator enforces: rule-file structure (`# id` / `> summary` / Why It Matters / Scope / Source / See Also, in order), known category prefixes, valid See Also and INDEX links, SKILL.md category counts matching the directory, and publisher-label↔domain attribution sanity warnings.

## Provenance

Rules were distilled from the primary sources behind [awesome-harness-engineering](https://github.com/walkinglabs/awesome-harness-engineering), then reviewed by an independent reviewer (Codex/gpt-6-sol), which caught mis-attributions and over-absolute prescriptions; all verified findings were fixed. See `## Source` in each rule for its citation.

## License

CC0-1.0. Referenced upstream materials remain under their own licenses.
