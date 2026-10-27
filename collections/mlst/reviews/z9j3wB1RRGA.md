# Solving Chollet's ARC-AGI with GPT4o

[Original episode](https://www.youtube.com/watch?v=z9j3wB1RRGA) · Source: Machine Learning Street Talk · [All reviews](../README.md) · [Learning path](../learning-path.md)

Published: 2024-07-06 · Decision: **Worthwhile** · Confidence: high for the first technical block; moderate for broader cognitive interpretations

## Central claim

An unusually useful worked example of intelligence as learned hypothesis proposal plus explicit evaluation under a compute budget. Its strongest lesson is how prior quality, ambiguity, execution and search allocation jointly determine generalization; the later discussion is mainly a competing philosophical perspective rather than further experimental evidence.

## Ideas I want to keep

- At 03:11–08:15, GPT-4o proposes Python transformation programs; execution filters them against observed ARC input/output pairs. Candidates are then grouped by their output on the held-out input. This separates syntactically different programs, behaviorally equivalent programs and genuinely different hypotheses that agree only on the demonstrations. Voting in output space matches the decision being scored.

- At 05:56–07:04, Greenblatt explicitly depends on a non-adversarial proposal prior: the model should propose plausible rules rather than hard-code examples. Passing demonstrations is only a consistency constraint, so useful generalization comes substantially from what the model tends to propose. Calling this a guarantee would be too strong; it is a contingent learned bias, and he observes overspecialization.

- At 18:48–30:26, search combines many initial drafts with execution-guided repair of near misses. Failures include wrong abstractions, wrong rule details and correct rules implemented incorrectly. Repair and fresh sampling address different bottlenecks. The breadth/depth tradeoff is shaped by prefix caching and API pricing, not purely by a timeless cognitive principle: available hardware and interfaces influence the observed algorithm.

- At 22:34–24:54, runtime scaling has diminishing returns: a doubling of samples reportedly buys a few extra percentage points in the tested regime. This is both evidence of a useful proposal distribution and evidence that rare solutions are expensive to uncover. A compute-performance curve is more informative than a single score or the claim that brute-force search explains everything.

- At 31:21–42:18 and 50:20–01:07:40, the guest resists mapping neural computation to intuition and symbolic execution to reasoning by definition. Program generation can itself involve sequential reasoning; test execution compensates for several kinds of error. Agency is decomposed into planning, persistence, situational understanding, recovery and cross-context goals, allowing disagreement to become testable instead of resting entirely on labels.

## Mathematical anatomy

**Objects:** A task demonstration set D={(x_i,y_i)}, learned program proposal q(p|D), a consistency predicate V_D(p), held-out input x*, output equivalence classes and a compute-dependent revision kernel.

**Objective:** Select the correct output under a runtime budget, not uniquely recover the original generative program. The empirical voting distribution approximates the proposal mass of consistent programs yielding each candidate output; this is not automatically a calibrated Bayesian posterior.

**Mechanism:** The system samples programs, executes them on all demonstrations, optionally revises candidates using discrepancy feedback, then aggregates surviving outputs. With independent draws and per-draw success probability p, discovery probability is 1−(1−p)^n; actual decoding correlations, task heterogeneity and imperfect selection break a naive one-p model. The search prior determines which parts of the vast program space are accessible at affordable n.

**Assumptions:** Examples constrain the intended task; proposals assign sufficient mass to a correct generalizing rule; execution accurately tests candidates; repair feedback is informative; selection does not disproportionately reward overfitting. Budget accounting must include prompt processing, generation, execution, repair and prior training when comparing different notions of efficiency.

**Limits:** Sample voting counts proposal mass, so duplicate implementations and correlated outputs can create false consensus. Python expressivity does not guarantee correctness on unseen grids or unlimited lengths. A public ARC score does not identify the internal reasoning mechanism, establish absence of contamination, or measure broad autonomous scientific ability.

## Evidence, limitations and corrections

- The episode repeatedly distinguishes the approximately 1,000-sample newer submission from earlier more expensive experiments. The original author blog’s 50% public-test result used around 8,000 programs per problem including revision attempts. These settings and public/private evaluation protocols must not be collapsed into one headline score.

- The guest’s scaling figures are conversational approximations. Ten doublings are 1,024×, not the roughly 2,000× uttered in passing; constant percentage-point returns cannot continue indefinitely. Estimated human scores are not a controlled matched-cost comparison.

- The host’s claims that a Python output program necessarily generalizes to infinitely many cases, that gradient training cannot support inventive reasoning, or that a network is confined to a convex hull do not follow. Conversely, plausible chain-of-thought traces do not prove faithful internal reasoning; the guest himself discusses interventions that reveal more complicated dependence.

- The neuroscience analogies, human-brain FLOP estimates, simulation thought experiments and agency forecasts are explicitly uncertain or argumentative. Neither social embodiment nor internal computation is isolated by the ARC experiment. Disability examples and imagined deprivation experiments provide no empirical proof about the necessary substrate of cognition.

- The long economic feedback and control discussion, especially after 01:28:15, is a conditional scenario. Accelerating research depends on idea production, evaluation, coordination, physical experiments and resource bottlenecks; more copies or shared weights do not establish superlinear progress. The review does not treat the proposed timeline or governance position as a result.

## Relevance to my research

A strong case study for my understanding of how apparent insight emerges from learned priors, explicit computation and a selection procedure. It helps me resist both “just brute force” and “proof of general intelligence” interpretations. The first half-hour has the highest density of concrete understanding; I would use the debate selectively to challenge categorical assumptions.

## My viewing plan

**Mode:** chapters

**Ranges:** - **Start:** 00:03:11
  
  **End:** 00:30:26
  
  **Why:** Complete method, program/behavior ambiguity, refinement and compute allocation.

- **Start:** 00:31:21
  
  **End:** 00:42:18
  
  **Why:** I want to test the system-one/system-two and neurosymbolic labels against actual operations.

- **Start:** 00:50:20
  
  **End:** 01:07:40
  
  **Why:** Optional competing model: agency as learned abilities and training-regime dependence.

- **Start:** 02:14:22
  
  **End:** 02:17:45
  
  **Why:** Optional closing distinction between preserving hypotheses and seeking better cognitive strategies.

**Edition note:** Observed timestamps in the local-ASR edition ending 02:17:57. Most of 01:14–02:06 is speculative agency, economics and governance discussion; it is optional for my mathematical learning goal.

**Intention:** I plan to watch the method block and selected conceptual debate; the later agency and governance discussion is optional.

## Objections and open questions

ARC-specific priors and cheap verification make this unusually favorable to repeated sampling. In science, generating a hypothesis is cheap relative to acquiring disambiguating evidence, and an incorrect theory can match many observations. The approach nevertheless makes those dependencies visible and supplies a useful baseline against claims that a more elaborate architecture is essential.

## An experiment I could try

On a held-out set of small grid tasks, I would retain every proposed program, observed-example error, runtime and predicted test output, then compare fresh sampling with one-step repair at equal total compute. Separate plots of oracle discovery, selected-output accuracy and false-consensus rate would expose different bottlenecks. I would add deliberately underdetermined demonstrations and adversarial memorizing programs to test why perfect consistency and strong vote agreement do not imply identification of the intended rule.

## Connections in my notes

- Chaudhuri: proposal/verification is shared, but finite ARC examples are weaker than a proof checker’s specification.

- ARC2024 panel and Berman: this concrete method can replace some high-level benchmark commentary; ARC-AGI-3 remains distinct because interaction changes information acquisition.

- Nanda and Ilyas: behavioral success alone does not determine mechanism or training-data dependence.

- Schmidhuber: program prior and runtime allocation are concrete counterparts to resource-bounded search; cheap verification remains a crucial condition.

## Primary sources checked

- **Title:** Getting 50% (SoTA) on ARC-AGI with GPT-4o
  
  **Url:** https://www.redwoodresearch.org/blog/getting-50-sota-on-arc-agi-with-gpt
  
  **Use:** Author’s original method and evaluation setting; historical public-test result is not interchangeable with later submission settings.

- **Title:** ARC Prize 2024 Technical Report
  
  **Url:** https://arcprize.org/media/arc-prize-2024-technical-report.pdf
  
  **Use:** Organizer account separately describes the leaderboard result and neural program-synthesis approach.

## Source and coverage

**Status:** complete_available_text

**Start:** 00:00:00

**End:** 02:17:57

**Caveats:** - Read all 31,501 words of the local-ASR text, not audio. No speaker diarization; several model names and quantities are corrupted or loosely recalled. The episode discusses a historical 2024 method, followed by an extended speculative agency/risk debate.

Source type: Local asr. Reviewed text: 29,440 words.

Transcript file: `z9j3wB1RRGA.local-asr.txt` (not distributed).

SHA-256: `5ba6d10fffb0c8299e316cb84396ddfcd9c1d207a7ee6ae4458a619becb1f7ff`.

[Structured review](z9j3wB1RRGA.json) · [Source ledger](../sources.json)
