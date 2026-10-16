# Agent evaluation protocol | Draft v0.1

**Status: preregistration-style design draft — not a completed benchmark.**

## Experimental unit

One independently scored attempt by one configured agent system on one task. A task is a version-controlled worktree snapshot plus instructions, allowed tools, resource limits, and hidden validation tests. Each attempt runs in a fresh isolated environment.

## Prespecified comparisons

1. Single agent vs. the same agent with disabled tools, where task class permits.
2. Single agent vs. specialized planner / implementer / reviewer team.
3. Local model configurations with disclosed quantization and memory footprints.

Use identical task sets and comparable budgets; note when this cannot be achieved. Randomize task order; fix seeds where possible and report variance. Avoid interpreting one lucky demo as representative.

## Metrics

| Metric | Definition / reporting rule |
| --- | --- |
| Task success | Passes predefined independent tests without manual patching |
| Pass@1 | Number of successful first attempts / all first attempts |
| Reliability | Success across repeated trials; report N, failures and timeouts |
| Latency | Wall-clock from task start to final validation |
| Cost | API charges or local hardware/runtime resource proxy; define clearly |
| Human intervention | Count and type; intervened tasks cannot be called autonomous success |
| Tool safety | Unauthorized actions, policy breaches, or attempts to access prohibited resources |
| Resource use | Peak RAM/unified-memory where available; tokens; tool calls |

## Anti-gaming rules

- Freeze evaluation tasks/tests before comparing systems.
- No test-set leakage into prompts, agent memory, or reviewer instructions.
- Reject post-hoc removal of failed runs; mark invalid runs with explicit reasons.
- Keep model/tool/version configuration alongside each result.
- Publish negative outcomes and uncertainty; do not cherry-pick.
- Never present synthetic example data as observed model output.

## Security controls

Work in disposable local containers or otherwise isolated directories with least-privilege permissions. No real API keys in tasks, no broad filesystem access, no automatic publishing/deployment, no financial transactions. Require human review for consequential actions. Keep sandbox logs where legally and ethically appropriate.

## Report checklist

A publishable report must include research question, hypothesis, benchmark provenance and license, task manifest, environment specification, comparator configurations, raw outcomes, metrics with denominator, failure taxonomy, limitations, and a link to runnable reproduction instructions.

## Next concrete step

Implement a minimal open evaluation harness and complete a **small pilot on the existing laptop** before seeking hardware sponsorship. Performance figures belong here only after the scripts, logs, and reproduction steps are publicly available.

See [research agenda](RESEARCH_AGENDA.md).
