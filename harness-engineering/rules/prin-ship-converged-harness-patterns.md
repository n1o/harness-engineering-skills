# prin-ship-converged-harness-patterns

> Prefer the design points that shipped harnesses converged on — hand-built loops, deterministic retrieval, skills — over adding a general-purpose agent framework or vector-embedding code retrieval; zero production coding agents ship either.

## Why It Matters

- A source-code study of eleven production coding harnesses (~4M lines, pinned July 2026) finds two "twin absences": zero of eleven runtimes build on a general-purpose agent framework, and zero of eleven use vector-embedding retrieval over code. Loops are hand-built and code retrieval is deterministic — ripgrep, glob, tree-sitter (Harness Engineering: Anatomy, Architecture, and Evolution of Coding Agents, arXiv 2609.00006).
- Skills are implemented by nine of eleven systems, MCP by eight of eleven — the field's own convergence data on which extension surfaces earn their complexity (arXiv 2609.00006).
- The study catalogs 29 recurring design patterns and 13 cross-cutting observations across agent loop, LLM integration, tools, memory/context, safety, orchestration, and extensibility subsystems — a source-verified reference for what "normal" looks like before you deviate (arXiv 2609.00006).
- Loop archetypes observed: iterative action–observation, reflection-augmented, and coordinator–worker; implementations span Mini-SWE-Agent's minimal linear loop with one bash tool to OpenHands' event-sourced conversation with parallel action batches — both ends ship, and the minimum end is well-populated (arXiv 2609.00006).
- This is the empirical base for [prin-simplest-solution-that-works](prin-simplest-solution-that-works.md): "no framework" is not the lazy option, it is the majority-industry position measured across the corpus (arXiv 2609.00006).

## Scope

- Apply when choosing greenfield architecture for a coding-agent harness: default to a hand-built loop plus deterministic tools; treat adding an agent framework or embedding-based code retrieval as a deviation requiring evidence.
- Use the study's seven-subsystem decomposition (loop, LLM integration, tools, memory/context, safety, orchestration, extensibility) as a checklist when auditing or comparing harnesses.
- The evidence is source-code reading, not runtime measurement: it establishes how shipped systems are structured, not that these choices are optimal for your workload. A measured win on your evals still overrides convergence (see [ver-harness-deltas-measured-by-evals](ver-harness-deltas-measured-by-evals.md)).
- Findings are pinned to July 2026 snapshots; recheck convergence before citing the counts for a decision made much later.

## Source

Harness Engineering: Anatomy, Architecture, and Evolution of Coding Agents – A Source-Code Study of Eleven Systems (https://arxiv.org/abs/2609.00006)

## See Also

- [prin-simplest-solution-that-works](prin-simplest-solution-that-works.md) - the prescriptive version of this rule; this rule supplies the measured industry-convergence evidence
- [struct-harness-as-declared-config](struct-harness-as-declared-config.md) - hand-built loops still need to be declared, versioned config, not buried code
- [ctx-just-in-time-retrieval](ctx-just-in-time-retrieval.md) - the deterministic-retrieval side: identifiers plus navigation tools, not pre-embedded vectors
- [ver-harness-deltas-measured-by-evals](ver-harness-deltas-measured-by-evals.md) - how to justify departing from the converged default
