# ctx-evolved-knowledge-gated-by-validation

> When an agent accumulates a durable domain-knowledge layer (ontology, semantic layer, playbook), admit new entries only through a measured validation gate and serve it by active query — never free-form accumulation, and never blind injection of the whole layer into context.

## Why It Matters

- Ungated curation admits regressions: removing the acceptance gate from the evolution loop caused the largest ablation drop of any component (−11.2 points, 89.5→78.3 on DDR-Bench) — candidates were kept only when paired validation showed improvement over the incumbent on the same backbone, and otherwise discarded (EvoOntology, arXiv 2609.15779).
- Passively injecting accumulated knowledge into the prompt can be worse than nothing: baseline + static semantic layer dropped −15.0 points on one backbone (72.5→57.5), while the actively-queried, evolved MCP-served ontology averaged +17.8 points across six backbones — the same content helps as a queryable tool and hurts as dumped context (2609.15779).
- Log rejected candidates with their signatures and outcomes to avoid re-proposing the same ineffective update — the loop needs a negative-results memory, not just a success memory (2609.15779).
- Every knowledge entry should carry evidence back to the source: removing evidence-grounding dropped 4-backbone-average accuracy −8.7, and removing term→field mappings caused the largest object-family drop (−13.4) — unevidenced knowledge is indistinguishable from hallucination (2609.15779).
- Evolved knowledge is backbone-specific, not portable: cross-backbone transfer of an evolved store was uniformly worse than same-backbone use, with Jaccard overlap ≤0.62 between stores evolved for different models — a knowledge layer tuned for one model degrades under another (2609.15779).
- Growth converges rather than exploding: terms grew 61→80 over five rounds with <5% per-round growth after round three — a gated loop self-bounds; unbounded accumulation is a symptom of a missing gate (2609.15779).

## Scope

- Apply to agent-maintained domain-knowledge layers (semantic layers, ontologies, curated metric definitions, tool-usage playbooks) that accumulate over many runs; any loop that lets an agent edit its own long-lived knowledge.
- Skip for static, human-authored instruction files — covered by the layered-instruction-file rules.
- Skip for volatile working state per task, and for skill/rule files the agent can never modify autonomously.

## Source

EvoOntology: A Self-Evolving Ontology Layer for Data Agents (https://arxiv.org/abs/2609.15779)

## See Also

- [ver-harness-deltas-measured-by-evals](ver-harness-deltas-measured-by-evals.md) - the same measured-delta discipline applied to harness changes; here the agent itself is the change proposer
- [run-entropy-garbage-collection-cadence](run-entropy-garbage-collection-cadence.md) - recurring cleanup for repo code; this rule is the add/evolve side for knowledge stores, gated the same way
- [eval-no-skill-baseline](eval-no-skill-baseline.md) - the paired baseline is how you detect the negative-delta injection cases this rule warns about
- [ctx-progressive-disclosure-pointers](ctx-progressive-disclosure-pointers.md) - both reach knowledge by pointers; this rule adds that the content must be validated, versioned, and backbone-matched
- [run-harness-optimization-per-model](run-harness-optimization-per-model.md) - evolved knowledge is backbone-specific the same way harnesses are
