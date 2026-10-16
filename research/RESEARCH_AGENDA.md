# Research agenda | v0.1

**Project:** Independent AI Research Laboratory  
**Lead:** Ambro Zhong  
**Status:** Proposed research program; results not yet published  
**Scope:** 12 months after equipment procurement, contingent on funding and feasibility

## Mission

Make autonomous AI agent behavior measurable, reproducible, and inspectable on accessible local hardware. The research question is not whether agents can produce impressive demos, but **under what conditions they reliably complete well-defined tasks without hidden human correction or unreported compute cost**.

## Four research questions

| ID | Question | Planned method | Success evidence |
| --- | --- | --- | --- |
| RQ1 | Do tool-using agents outperform non-tool baselines? | Matched coding tasks, fixed execution limits, independent tests | Paired task-level outcomes |
| RQ2 | When do specialist multi-agent teams outperform a single agent? | Same model family, tools, tasks and compute-budget ceilings | Higher completion or lower cost at comparable reliability |
| RQ3 | What is the local memory/latency/cost trade-off across model sizes? | Warm/cold start profiling; repeatable prompts; disclosed quantization | Reproducible throughput, peak memory and energy estimates where measurable |
| RQ4 | Can agents propose and validate small software improvements safely? | Sandbox changes, immutable tests, independent evaluator | Accepted changes with passing tests and full execution traces |

## First benchmark track: coding & tool reliability

Target task families: self-contained Python defects, data transformations, small API fixes in permissively licensed projects, and structured file edits. Each task will have an initial repository state, a written specification, a deterministic checker, and a time/budget cap.

Evaluation will record **pass@1**, wall-clock time, model calls, token consumption where available, error recovery attempts, human interventions, and unexpected tool actions. Report the full denominator, including failures and timeouts.

**Comparators:** a no-agent baseline where meaningful; a single agent with identical allowed tools; then specialist multi-agent variants under matched constraints. The goal is to discover useful operating regimes, not to predetermine a winner.

## Twelve-month milestone proposal

| Window | Work package | Public evidence |
| --- | --- | --- |
| Months 1–2 | Environment, threat model, task design, resource baselines | Environment manifest + protocol |
| Months 3–4 | Single-agent baseline and repeated task runs | First benchmark report |
| Months 5–7 | Specialist multi-agent comparisons | Ablation results + failure taxonomy |
| Months 8–10 | Bounded autonomous improvement experiments | Experiment logs + validation results |
| Months 11–12 | Replication, disclosure and synthesis | Final report + reproducibility bundle |

**Targets (not existing achievements):** >=12 documented experiment runs, >=4 benchmark reports, >=1 prototype, quarterly updates, final report.

## Non-goals

- Training a frontier-scale foundation model from scratch on a desktop.
- Running agents with unrestricted internet, shell, payment, or credential access.
- Claiming peer-reviewed scientific results without external review.
- Treating larger models or more agents as inherently better.

## Resources and disclosure

Every report should include model and license, hardware, inference runtime, prompt/template version, dataset/task version, budget limits, sampling parameters, raw results (where safe), exclusions, analysis scripts, and limitations.

See [evaluation protocol](BENCHMARK_PROTOCOL.md) and [evidence register](EVIDENCE_REGISTER.md).
