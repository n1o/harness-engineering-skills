# eval-negative-controls

> Include cases where the behavior must *not* fire; one-sided evals create one-sided optimization.

## Why It Matters

- In the eval prompt set, mix explicit invocation (names the skill), implicit invocation (describes the scenario), contextual invocation (realistic noisy prompt), and negative controls (`should_trigger=false`).

- OpenAI example: "Add Tailwind styling to my existing React app" should NOT trigger the scaffold-a-new-demo-app skill — negative rows catch false positives where an adjacent request unintentionally matches the description.

- Anthropic learned this building web-search evals: test both queries where the model should search and where it should answer from existing knowledge, or you get an agent that searches for almost everything.

- Balance under-triggering and over-triggering deliberately; it took Anthropic many rounds of prompt+eval refinement to strike.

## Scope

- Apply whenever an eval set exists for a conditional behavior — skill triggering, tool selection, web-search invocation; one-sided evals create one-sided optimization.

- Mix invocation modes deliberately (explicit, implicit, contextual, negative); balancing under- and over-triggering took the source many rounds of prompt+eval refinement.

- Skip negatives only when the behavior is unconditional; otherwise every "must fire" set needs its "must not fire" rows.

## Source

OpenAI 'Testing Agent Skills Systematically with Evals' (https://developers.openai.com/blog/eval-skills/); Anthropic 'Demystifying Evals for AI Agents' (https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)

## See Also

- [eval-define-checkable-success-first](eval-define-checkable-success-first.md) - negative rows belong in the small must-pass list from the start
- [eval-unambiguous-tasks-reference-solutions](eval-unambiguous-tasks-reference-solutions.md) - negative rows need the same unambiguous-by-construction discipline as positive ones
- [eval-no-skill-baseline](eval-no-skill-baseline.md) - the baseline run is where eager over-triggering shows up as regression
