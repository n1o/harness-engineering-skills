# Research Paper Provenance

Provenance map for the 21 rules distilled from 2026 agent research papers, read via their [Dissecting AI](https://dissecting-ai.dev) lecture summaries (papers imported 2026-09-07 → 2026-10-11; this file covers the original distillation wave plus the second wave of 2026-10-11). The remaining 104 rules trace to engineering articles, specs, and reference harnesses via [awesome-harness-engineering](https://github.com/walkinglabs/awesome-harness-engineering); this file covers only the research-paper layer.

Every listed paper was read and adjudicated: it either feeds at least one rule below (with the specific claims consumed), or is recorded under "No new rule" with the reason. DA = Dissecting AI public lecture summary.

## Rule → Paper map

### Self-evolving harnesses

| Rule | Primary paper(s) | What was consumed |
|---|---|---|
| [ver-self-edit-non-regression-gate](rules/ver-self-edit-non-regression-gate.md) | [Self-Harness](https://arxiv.org/abs/2606.09498); evidence from [Evo-Bench](https://arxiv.org/abs/2608.09096), [Darwin Godel Machine](https://arxiv.org/abs/2505.22954), [AutoSaddler](https://arxiv.org/abs/2608.23041), [RSEA](https://arxiv.org/abs/2606.28374) | The held-in/held-out non-regression acceptance rule and its measured gains; Evo-Bench's early-saturation and cross-task regression findings; DGM's archive-vs-greedy ablation; AutoSaddler's loop beating expert tuning; RSEA's no-gate overfitting (33-point train–test gap) and catastrophic no-gate transfer (WebShop 0.136 vs 0.429) |
| [run-harness-optimization-per-model](rules/run-harness-optimization-per-model.md) | [Self-Harness](https://arxiv.org/abs/2606.09498), [HarnessDev](https://arxiv.org/abs/2609.01437), [MemoHarness](https://arxiv.org/abs/2607.14159), [SoL-Pi](https://arxiv.org/abs/2609.20519), [Harness Updating Is Not Harness Benefit](https://arxiv.org/abs/2605.30621) | Per-model failure signatures and model-specific edits; identical-weights 14.4pp harness gap; transplant variance (+0.038..+0.233); mechanism degradation on unseen backbones; the updater-vs-benefit split (evolver spread ≤3.1pp, benefit non-monotonic in base pass rate) |
| [run-optimization-label-scarce-regime](rules/run-optimization-label-scarce-regime.md) | [RHO / Evolving Agents in the Dark](https://arxiv.org/abs/2606.05922) | Harness optimization with no labeled validation data: LLM-judged difficulty×diversity coreset + self-preference ranking (+0.19 on held-out SWE-Bench Pro over Vanilla Codex, beating experience-based baselines with 103 agent calls); the label-scarce regime the eval-gated rules assume away |
| [run-do-not-stack-redundant-harness-components](rules/run-do-not-stack-redundant-harness-components.md) | [Agentic Harness Engineering (AHE)](https://arxiv.org/abs/2604.25850) | Component non-additivity: single-component gains sum +11.1pp vs +7.3pp combined; memory-only variant beats the full stack on Hard; components pushing the same mitigation spend turns on redundant re-checks within the finite budget |
| [run-dead-end-ledger-scar-tissue](rules/run-dead-end-ledger-scar-tissue.md) | [Auto-RecSys](https://arxiv.org/abs/2609.10922), [MemoHarness](https://arxiv.org/abs/2607.14159), [Self-Harness](https://arxiv.org/abs/2606.09498), [DGM](https://arxiv.org/abs/2505.22954), [ActiveSaddler](https://arxiv.org/abs/2610.00906) | Dead-end playbook rules cutting fix steps 4.0→0.5 (zero-fix 0%→83%); dual-layer success+failure bank; rejected-edit logging; archive of functional-but-worse agents; failure normalization into reusable weakness classes (arms) steering the optimization curriculum |
| [prin-internalize-harness-into-model](rules/prin-internalize-harness-into-model.md) | [Harness-Zero](https://arxiv.org/abs/2609.24974) | Harness distillation into weights (23.3%→44.3%, beating attached-harness 41.7%); reviewed-rollout data quality over yield; per-domain incompleteness caveat |
| [struct-adaptive-harness-per-task-retrieval](rules/struct-adaptive-harness-per-task-retrieval.md) | [MemoHarness](https://arxiv.org/abs/2607.14159), [JIT-Agent](https://arxiv.org/abs/2608.25593) | Per-case config retrieval from a success+failure bank (0.806 vs 0.722 best static); just-in-time per-task harness synthesis (+7.7/+8.8 avg, 18/18 pairs); AOT-assumption failure mode; lexicographic cost control |

### Agent memory

| Rule | Primary paper(s) | What was consumed |
|---|---|---|
| [ctx-memory-substrate-routing](rules/ctx-memory-substrate-routing.md) | [Harness the Memory](https://arxiv.org/abs/2608.15008); negative control from [Selective Forgetting](https://arxiv.org/abs/2608.28978) | No-dominant-substrate result across regimes; retrieval-breadth sign reversal (QA up, embodied down); memory net-negative cases; write-token and latency costs; graph losing to flat RAG |
| [ctx-memory-reconstruct-not-replay](rules/ctx-memory-reconstruct-not-replay.md) | [MemHarness](https://arxiv.org/abs/2607.28272) | Verbatim-replay penalty (85.2%→70.1%); state-conditioned reconstruction; source-state storage; rejection rates 56–72%; OOD advantage (85.9% vs 76.3%) |
| [ctx-memory-curation-scored-forgetting](rules/ctx-memory-curation-scored-forgetting.md) | [Selective Forgetting](https://arxiv.org/abs/2608.28978); [MemHarness](https://arxiv.org/abs/2607.28272); [Harness the Memory](https://arxiv.org/abs/2608.15008); [Jev-Mem](https://arxiv.org/abs/2609.23986) | Quality-neutral scored pruning; the deterministic importance formula; cheap dedup write path; generative memory-control cost trap (2.7k–9k aux LLM calls); non-generative control winning on quality |
| [ctx-evolved-knowledge-gated-by-validation](rules/ctx-evolved-knowledge-gated-by-validation.md) | [EvoOntology](https://arxiv.org/abs/2609.15779) | Acceptance-gate ablation (−11.2pp); injection-vs-query sign flip (−15.0 static dump vs +17.8 active query); evidence-grounding ablations; backbone-specific evolved knowledge; self-bounding growth |

### Skills, harness formalization, scaffold effects

| Rule | Primary paper(s) | What was consumed |
|---|---|---|
| [eval-pin-harness-with-model](rules/eval-pin-harness-with-model.md) | [The Scaffold Effect in Coding Agents](https://arxiv.org/abs/2607.22585); replication from [SkillsBench](https://arxiv.org/abs/2602.12670), [Scaffold Effects on GAIA](https://arxiv.org/abs/2606.08529) | 3×2×50 controlled study: harness effects at model-upgrade scale; 40x token-efficiency spread; per-scaffold failure fingerprints; ~8pp cross-scaffold swings replicated on 18 configurations; GAIA replication with gaps up to 28pp within one model, "frontier models less scaffold-sensitive" rejected |
| [ver-skill-correctness-as-spec-consistency](rules/ver-skill-correctness-as-spec-consistency.md) | [SkillSpec](https://arxiv.org/abs/2609.06052) | Hoare-style spec-consistency for prose+code skills: 46.4% defective sampled skills, 763 confirmed defects; script-heavy 69.4% vs text-only 18.1%; defect concentration (30 skills = 41.7%); sandbox validation of hypotheses |
| [ctx-skill-compactness-over-completeness](rules/ctx-skill-compactness-over-completeness.md) | [SkillsBench](https://arxiv.org/abs/2602.12670) | Length ablation (compact/standard +19–21.5pp vs comprehensive +0.7pp); count ablation (≥4 skills halves gains); negative-delta tasks and their three mechanisms; self-generated skills underperforming no-skill baseline |
| [prin-control-flow-in-code-not-model](rules/prin-control-flow-in-code-not-model.md) | [LLM-as-Code](https://arxiv.org/abs/2606.15874) | Three LLM-orchestrator pathologies; code-controlled flow at 86.8% OSWorld with 15 vs 100 steps; depth-scoped call-DAG context; unit-testable workflow logic; authors' own applicability boundary |

### Harness architecture from shipped systems

| Rule | Primary paper(s) | What was consumed |
|---|---|---|
| [prin-ship-converged-harness-patterns](rules/prin-ship-converged-harness-patterns.md) | [Harness Engineering: Source-Code Study of Eleven Systems](https://arxiv.org/abs/2609.00006) | Empirical convergence across ~4M lines / 11 production coding harnesses: zero general-purpose agent frameworks, zero vector-embedding code retrieval, skills 9/11 vs MCP 8/11; 29 recurring patterns + 13 cross-cutting observations as the deviation baseline |

### Context compression

| Rule | Primary paper(s) | What was consumed |
|---|---|---|
| [ctx-compression-degrade-not-summarize](rules/ctx-compression-degrade-not-summarize.md) | [Beyond Token Savings](https://arxiv.org/abs/2609.32961) | 65 policies (primitive × trigger × depth), ~35k runs: tool-result clearing ≈ full-context accuracy at 0.57× tokens vs LLM summarization −11.0pp; summarization calls costing 28–46% of wall-clock; per-model policy variance |

### Safety of evolved state

| Rule | Primary paper(s) | What was consumed |
|---|---|---|
| [guard-evolved-state-lifecycle-safety](rules/guard-evolved-state-lifecycle-safety.md) | [SAVER survey](https://arxiv.org/abs/2610.00093); persistence-amplification evidence from [Harness Updating Is Not Harness Benefit](https://arxiv.org/abs/2605.30621) | Substrate×operation→violation lifecycle for persistent evolved state; committed-vs-session failure gap (45.0%→71.9%); field weakness at descendant repair, deletion verification, post-evolution evaluation |

### Multi-agent society, human oversight, UI surfaces

| Rule | Primary paper(s) | What was consumed |
|---|---|---|
| [guard-rotate-peer-verifiers-against-collusion](rules/guard-rotate-peer-verifiers-against-collusion.md) | [Emergent Collusion in Long-Horizon LLM Agent Interaction](https://arxiv.org/abs/2609.24967) | 94% trajectory-level collusion with no adversarial instructions; absorbing-state convergence; high task accuracy masking collusion; three onset pathways; the observable relaxation trigger |
| [eval-canary-injections-verify-human-oversight](rules/eval-canary-injections-verify-human-oversight.md) | [AI Agents Push Humans Out of the Loop](https://arxiv.org/abs/2608.23642) | Irony of automation applied to agent oversight; overseer-capacity decay evidence; overreliance short-circuit findings; the no-mechanism gap in governance mandates |
| [struct-generative-ui-schema-bounded](rules/struct-generative-ui-schema-bounded.md) | [Portal UX Agent](https://arxiv.org/abs/2511.00843), [Macaron-A2UI](https://arxiv.org/abs/2605.24830) | Two-stage NL→typed-JSON→deterministic-renderer split; zero-reward malformed-JSON gates reaching 99.2% renderability; schema hints carrying protocol correctness (25.5 vs 63.8) |

## Papers read but yielding no new rule

| Paper | Reason |
|---|---|
| [Evo-Bench](https://arxiv.org/abs/2608.09096) (Can LMs Improve Agent Harness?) | Benchmark contribution; its design practices restate `ver-harness-deltas-measured-by-evals` and `eval-tier-by-scope`. Consumed as evidence in the non-regression gate rule |
| [HarnessDev](https://arxiv.org/abs/2609.01437) (Can LLMs Create and Evolve Their Own Harness?) | Benchmark contribution; its headline stat (identical weights, 14.4pp harness gap) is consumed by `run-harness-optimization-per-model`; "evaluate harness creation as a capability" is covered by the `eval-` family |
| [AutoSaddler](https://arxiv.org/abs/2608.23041) | Same offline mini-batch optimization loop as Self-Harness without a held-out gate; numbers support the non-regression gate; its EvoDAG lesson store is subsumed by the dead-end ledger |
| [Procedural Graphs](https://arxiv.org/abs/2609.09153) (Self-Evolving Execution Structures) | General lesson (structure accumulated experience with entry conditions and pitfalls) covered by `ctx-structured-notes-across-resets` + `struct-externalize-loop-state-files`; the graph formalism is task-family-specific machinery |
| [The AI Scientist-v2](https://arxiv.org/abs/2504.08066) | End-to-end science system; generalizable mechanisms (per-stage node budgets, explicit stopping) restate `struct-bounded-single-task-loop` and `ver-layered-verification-stack`; peer-review result is domain-specific |
| [Darwin Godel Machine](https://arxiv.org/abs/2505.22954) | Foundational, but its distinctive mechanisms (open-ended archive, novelty-biased selection) are search-algorithm internals; ablation evidence consumed by the non-regression gate and dead-end ledger rules |
| [Jev-Mem](https://arxiv.org/abs/2609.23986) | Its transferable claim — memory bookkeeping as deterministic/typed control, not generative calls — is an instance of `ctx-deterministic-tools-before-llm` applied to memory; folded as evidence into `ctx-memory-curation-scored-forgetting` |
| [What makes a harness a harness](https://arxiv.org/abs/2606.10106) | Actionable cores already covered: `prin-agent-equals-model-plus-harness`, `struct-harness-as-declared-config`, `guard-pre-action-deterministic-authorization`; its T1–T4 membership test is delimitation, not engineering guidance; no quantitative results |
| [Harness as a Language](https://arxiv.org/abs/2609.26891) | Minimal-Turing-complete-core design claim subsumed by `prin-simplest-solution-that-works` + `prin-control-flow-in-code-not-model`; framework-fragility findings reinforce `struct-harness-as-declared-config` |
| [Externalization in LLM Agents](https://arxiv.org/abs/2604.08224) (unified review) | Survey; its four pillars (memory, skills, protocols, harness) are individually encoded by existing rules; its novel warnings (28% misaligned skill artifacts, 18% skills with vulnerabilities) fall inside `guard-untrusted-content-as-data` |
| [Et Tu, Brute?](https://arxiv.org/abs/2609.24927) (Economic Misalignment in Personal AI Agents) | Robust finding (8/13 models recommend pricier options to wealthier personas) but the only harness lever — data minimization — is a least-privilege extension of `guard-scope-based-tool-allowlists`; scenario far from coding harnesses |
| [Critical-State RL](https://arxiv.org/abs/2609.24985) (Trainable States for Multi-Turn Tool Use) | RL credit-assignment training method (train only the action-sufficient turn, +14.3pp); belongs to training pipelines, not runtime harness design |
| [AgentSPEX](https://arxiv.org/abs/2604.13346) (second wave: now readable, pipeline completed) | YAML workflow spec + executor with explicit control flow, state, and conversation-history management; its actionable cores (declared config, control flow in code, bounded iteration) restate `struct-harness-as-declared-config` + `prin-control-flow-in-code-not-model`; benchmark wins are framework-specific machinery. Adjudicated: no new rule |
| [Scaffold Effects on GAIA](https://arxiv.org/abs/2606.08529) (second wave) | Replication, not new rule: extends `eval-pin-harness-with-model` beyond coding (28pp scaffold gap within one model on GAIA; rejects "frontier models less scaffold-sensitive"); consumed as evidence there |
| [AutoGym](https://arxiv.org/abs/2609.22592) (second wave) | Blueprint-first task generation and repair; consumed as evidence in `eval-unambiguous-tasks-reference-solutions` (repair shifted 57.0%→39.0% hard); the RL-gym machinery is task-generation internals |
| [ActiveSaddler](https://arxiv.org/abs/2610.00906) (second wave) | Adaptive curriculum (arms = reusable harness weaknesses) over AutoSaddler's loop; consumed as evidence in `run-dead-end-ledger-scar-tissue`; the curriculum bandit is optimization internals |
| [SkillLift](https://arxiv.org/abs/2609.15763) (second wave) | Dense rubric learned from sparse oracle rollouts; consumed as evidence in `ver-train-verifiers-on-production-traces`; the bilevel-optimization formalism is skill-evolution machinery |
| [Agent Plasticity](https://arxiv.org/abs/2610.08902) (second wave) | Evaluation framework for experience-driven improvement (checkpoint curves, cost-normalized saturation plasticity); consumed as evidence in `eval-tier-by-scope`; not harness design guidance itself |
| [Staying on Task / Long-Transduction](https://arxiv.org/abs/2609.38712) (second wave) | Benchmark contribution: sustained read–mutate–output reliability (62.8% relative drop 4K→128K); the implication (don't assume long-context ⇒ transduction) is covered by `ctx-working-memory-budget` + `ctx-illusion-of-control-probabilities` |
| [ROFT / Shockingly Simple Self-retrospection](https://arxiv.org/abs/2609.35741) (second wave) | Training method (retrospection-only fine-tuning beats GRPO on efficiency); belongs to training pipelines, not runtime harness design — same disposition as Critical-State RL |
| [Harness Learning Enables Generalizable Test-Time Adaptation](https://arxiv.org/abs/2609.35738) (second wave) | Trained proposer for harness revisions; training pipelines, not runtime harness design |
| [Harness-Aware Distillation](https://arxiv.org/abs/2610.02858) (second wave) | Distillation objective conditioned on harness state; training pipelines |
| [MASS / Recursive Self-Improvement through Multi-Agent Self-Supervision](https://arxiv.org/abs/2610.12176) (second wave) | Training procedure (workflow optimization + fine-tuning alternation); training pipelines |
| [Dive into Claude Code](https://arxiv.org/abs/2604.14228) (second wave) | Design-space study of Claude-Code-class systems; its design points are covered by `prin-control-flow-in-code-not-model`, `struct-harness-as-declared-config`, `ctx-layered-instruction-files`; overlaps the Eleven-Systems study, which supplied the convergence evidence instead |
| [Self-Improvements in Modern Agentic Systems: A Survey](https://arxiv.org/abs/2607.13104) (second wave) | Survey; its foundation-model + operational-scaffold decomposition restates `prin-agent-equals-model-plus-harness`; no quantitative harness levers |

## Papers not readable at distillation time

| Paper | Pipeline state |
|---|---|
| RRSI: Regularized Recursive Self-Improvement of Agent Harnesses (arXiv 2609.24972) | summarization LLM API error (400) — retried via `dai paper retry` (retry_count 5, 2026-10-11); full text is readable via `get_paper_context`, but no DA summary yet; revisit once the pipeline completes |
| Building Open-Ended Embodied Agent via Language-Policy Bidirectional Adaptation (arXiv 2401.00006) | parsed only; not public |

## Data-integrity correction

An earlier revision of this file claimed the DA library had the arXiv 2609.01437 / 2609.10922 titles swapped. That claim was **wrong**: the pipeline titles were already correct (2609.01437 = HarnessDev, 2609.10922 = Auto-RecSys, matching arXiv exactly). The confusion arose from a misreading during cluster distillation, and this file has been corrected. The rule → paper attributions above were always correct.

For the record, a `fix-title` was briefly applied to Auto-RecSys during the false-swap investigation (adding a plural "Systems") and was immediately reverted to the arXiv-exact title "Auto-RecSys: Harnessing Autonomous Research Agents for Industry-Scale Recommender System".
