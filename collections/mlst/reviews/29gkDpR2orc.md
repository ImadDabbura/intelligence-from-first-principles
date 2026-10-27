# AI BENCHMARKS ARE BROKEN! [Prof. MELANIE MITCHELL]

[Original episode](https://www.youtube.com/watch?v=29gkDpR2orc) · [All reviews](../README.md) · [Learning path](../learning-path.md)

Published: 2023-09-10 · Decision: **Core** · Confidence: High for the experimental-method contribution; lower for philosophical conclusions or historical claims about particular model capabilities.

## Central claim

An intelligence claim needs a specified construct, a systematic family of interventions, and an account of failures. A high aggregate benchmark score does not reveal whether a system acquired the abstraction that a human uses to solve those items.

## Ideas I want to keep

- Human test validity does not automatically transfer to machines. A task can correlate with broad competence among humans because humans share a developmental history and architecture; a machine can solve that task through a different route. The missing inference is from observed performance to a latent capability, not from low scores to high scores.

- ConceptARC groups tasks by concepts such as inside/outside and varies abstraction and complexity within each group. This makes generalization across realizations testable. Mitchell contrasts this diagnostic purpose with ARC’s attempt to resist developer anticipation of the test-generation process, acknowledging that these are complementary design goals.

- Researcher adaptation can leak knowledge into a system without literal training-test contamination. Architecture selection, prompt repair, and repeated public-benchmark optimization can encode the task family through the human development loop. A valid evaluation must specify the complete adaptive procedure and its access to evidence.

- Counterfactual task variants distinguish familiar surface regularities from an intended operation: decimal versus other-base arithmetic, or structurally related spatial problems. The result should be a graded generalization profile, with appropriate human baselines, rather than a binary declaration that a system understands nothing.

- Instance-level outputs and error analysis preserve evidence that aggregate accuracy destroys. Two systems with equal scores can fail on disjoint concepts, on the same items, or under different perturbations. The scientific questions concern these structures and the mechanisms that predict them.

## Mathematical anatomy

**Objects:** A construct such as containment; a family of task-generating transformations; model outputs per instance; training and adaptation histories; and human comparison conditions. The episode does not present a new learning algorithm.

**Objective:** Identify which latent capacity explains success, and estimate the scope and reliability of that capacity across controlled changes. Accuracy is a statistic about a sampled task distribution, not an intrinsic scalar measure of intelligence.

**Mechanism:** The targeted relation stays constant while nuisance properties, complexity, representation and domain vary. Failures and transfer are compared, adaptive choices frozen before held-out evaluation, and item-level responses retained. This turns evaluation into hypothesis testing rather than demonstration collection.

**Assumptions:** The task family genuinely instantiates the proposed concept; transformations preserve the relevant operation; interfaces do not add unrelated difficulty; and human and machine comparisons account for experience and adaptation.

**Limits:** No finite test battery proves unrestricted understanding. A failed counterfactual may reflect unfamiliar notation, working-memory demands, or a learned prior rather than total absence of abstraction. A successful battery may still be reverse engineered. Those possibilities motivate discriminating controls, not abandonment of testing.

## Evidence, limitations and corrections

- At 00:22:22–00:28:39 Mitchell describes the explicit design tradeoff between systematic concept groups and avoiding reverse engineering. She says ConceptARC complements rather than supplants ARC.

- At 00:40:27 she accepts that a generally successful solution could count regardless of whether it works like a human. This matters because the introductory narration is more categorical about grounding than the interview’s actual position.

- At 00:44:47–00:48:06 she acknowledges that human reasoning also depends heavily on familiar domains. The comparison should therefore investigate transfer and learning, not assume humans exhibit perfect domain independence.

- At 00:49:31–00:55:54 the central concern is reliability and full error reporting. The casual claim that success half the time is not replication needs qualification: a stochastic effect can replicate at a stable probability; the relevant baseline and uncertainty must be reported.

- The opening existential-risk debate montage is not evidence for the benchmark claims. Understanding a human preference does not logically guarantee optimizing it, and resource access cannot simply be assumed to prevent failure. Historical GPT-4 percentages, chess-variant predictions, and contemporary policy claims were not revalidated and should not drive today’s selection.

## Relevance to my research

Core as a methodological anchor for the entire viewing program. It gives me a way to test grand claims about intelligence: define the capacity, expose the transfer relation, account for human and model priors, and look for structured failures. This complements mathematical model-building by clarifying what evidence could distinguish proposed mechanisms.

## My viewing plan

**Mode:** I will focus on the main methodological discussion.

**Segments:** - **Start:** 00:14:56
  
  **End:** 00:28:39
  
  **Purpose:** Meaning of understanding, construct validity, and ConceptARC design.

- **Start:** 00:39:10
  
  **End:** 00:48:06
  
  **Purpose:** General solution criteria, cross-domain transfer, and counterfactual tasks.

- **Start:** 00:48:27
  
  **End:** 00:55:54
  
  **Purpose:** Demonstration versus reliable capability, development leakage, and instance-level reporting.

**Edition:** All 10,123 whitespace-delimited words of the recovered local ASR through 01:01:45 read. First 4.5 minutes include editorial/debate material; timestamps are local ASR anchors, not independently audio-verified chapters.

## Objections and open questions

Benchmarks can still be useful for engineering comparisons and discovery even when they do not identify mechanisms. Requiring limitless transfer risks making understanding unfalsifiable by moving the goalposts. The constructive response is to preregister a bounded claim and its discriminating tests, then revise the claim transparently when new evidence appears.

## An experiment I could try

I want to design 40 containment tasks in four families: enclosed-grid regions, nested lists, physical containers in prose and visual occlusion. The transferable relation would be declared in advance, with controls separating parsing from reasoning and an entire family held out. Fixed prompts would be compared with an adaptive prompt-development procedure using a separate validation set. I would retain per-item answers, repeat-run reliability and the pattern of errors that co-occur across representations.

## Connections in my notes

- ARC and ConceptARC; developer-aware generalization versus concept-specific diagnosis.

- Max Bennett’s distinction between verbal false-belief success and a reusable model of minds; adversarial robustness episodes’ concern with correct answers through unintended features.

## Source and coverage

**Read:** Entire available selected transcript read sequentially; audio not verified.

**Last timestamp:** 01:01:45

**Source caveats:** Local ASR recovered from episode audio; names, equations and speaker attribution may be inaccurate. Timestamps are ASR segment anchors.

Source type: Local asr. Reviewed text: 9,479 words.

Transcript file: `29gkDpR2orc.local-asr.txt` (not distributed).

SHA-256: `33d90904547535da0eaffe5a276a48fbbd5988b7717a11cbdf07ff074874b876`.

[Structured review](29gkDpR2orc.json) · [Source ledger](../sources.json)
