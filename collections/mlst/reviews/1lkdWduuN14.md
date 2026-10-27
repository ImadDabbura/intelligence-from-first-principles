# #85 Dr. Petar Veličković (Deepmind) - Categories, Graphs, Reasoning [NEURIPS22 UNPLUGGED]

[Original episode](https://www.youtube.com/watch?v=1lkdWduuN14) · [All reviews](../README.md) · [Learning path](../learning-path.md)

Published: 2022-12-08 · Decision: **Core** · Confidence: high

## Central claim

Architecture is a hypothesis about which computations should remain valid as inputs change. This compact interview connects categorical consistency, algorithmic alignment and communication topology to concrete neural-network design decisions, making it unusually relevant to the mathematical anatomy of intelligence.

## Ideas I want to keep

- Equivariance to invertible transformations is extended toward consistency under noninvertible operations. Coarsening and algorithmic state updates motivate a language richer than symmetry groups.

- An encode–process–decode system should agree with an algorithmic state transition. The resulting commuting-diagram viewpoint gives a concrete way to inspect whether the representation and computation fit the intended algorithm.

- Separating edge-output and node-aggregation message streams relieves conflicting representational demands. The episode connects an abstract modeling constraint to an empirical architectural change.

- Algorithm pretraining is motivated by the bottleneck between noisy observations and clean algorithm inputs. A differentiable latent executor permits learning the interface rather than forcing all raw information through manually selected scalar features.

- The expander-graph segment makes communication topology a computational resource. Alternating local graph layers with sparse global connections addresses bottlenecks without full quadratic connectivity.

## Mathematical anatomy

**Objects:** Graph states x, encoder E, latent processor P, decoder D, target update A, and message-passing connectivity.

**Objective:** Reconstruction: D(P(E(x))) approximately equals A(x), with consistency required along longer trajectories and under graph-size changes. For shortest paths the update has a min-plus structure: d_new(v)=min_u[d(u)+w(u,v)].

**Mechanism:** Putting the difficult structural operation into the architecture gives learned subfunctions simpler extrapolation requirements. A min/max aggregator aligns better with path relaxation than making a generic sum-based module discover the entire operation.

**Assumptions:** The target algorithm is relevant to the downstream task; intermediate states provide useful supervision; the encoding preserves information needed by the executor; global communication is actually desirable.

**Limits:** Exact algebraic compatibility, successful optimization and finite-data generalization are separate claims. A diagram does not prove the trained model commutes everywhere. Fixed-width features still impose information limits even on well-connected graphs.

## Evidence, limitations and corrections

- The phrase that one message used twice is no longer a function is too broad. A function can produce a product-valued output and can be copied in suitable categories. The substantive issue is compatibility with the chosen typed/algebraic formulation and pressure on a shared representation, not a universal prohibition on reuse.

- ReLU networks are eventually affine along a fixed ray under standard finite-network assumptions. This is a useful constraint on extrapolation, not a theorem that all neural networks cannot learn algorithms.

- The speaker carefully distinguishes leaving the convex hull from distributional or algorithm-length generalization. Testing 16-node training graphs against 64-node graphs can also require much longer execution trajectories.

- The Google Maps discussion motivates the raw-data interface. It should not be read as proof that every routing example described was deployed as a neural Dijkstra replacement.

- The expander argument concerns bottleneck reduction under stated graph constructions. Negative curvature alone is not a contradiction: the referenced failure theorem requires a stronger regime. Sparse global mixing can also harm tasks that need local separation.

- Category-theory terminology is a design aid here; the broader claim that a small library of algorithms forms a universal basis of reasoning remains a research hypothesis.

## Relevance to my research

Core for my research goals because it connects mathematical structure to testable generalization, and also shows why topology can limit computation independently of parameter count. I plan to watch it after the geometric deep learning overview and derive a small experiment from it, rather than merely collect categorical vocabulary.

## My viewing plan

**Mode:** I will focus on the main interview sections below.

**Ranges:** - **Start:** 00:02:24
  
  **End:** 00:08:07
  
  **Reason:** Noninvertible transformations, commuting computations and message-stream design.

- **Start:** 00:12:50
  
  **End:** 00:27:40
  
  **Reason:** Weight-sharing assumptions, neural algorithmic reasoning, and the distinction between geometric and algorithmic extrapolation.

- **Start:** 00:29:39
  
  **End:** 00:36:52
  
  **Reason:** Oversquashing, sparse expanders and why a theorem’s precise hypotheses matter.

**Edition:** Recovered podcast audio

## Objections and open questions

If an exact algorithm already solves the complete problem, replacing it with an approximate neural executor can reduce reliability. The strongest case is learning interfaces to noisy observations or transferring useful structure, with exact algorithms retained as baselines and correctness checks.

## An experiment I could try

I want to train equal-budget graph models on small shortest-path problems using sum aggregation, min-plus-aligned aggregation and separate edge/node streams. Larger graphs, longer paths, changed weight ranges and altered topology would be tested independently, alongside an exact solver with a learned input interface. Adding expander layers would then let me measure when communication improves accuracy and when it erases useful locality.

## Connections in my notes

- Geometric deep learning: symmetry as prior

- Dudzik categorical architectures: composition laws

- Hattie: trace supervision versus algorithm identification

- Chaudhuri: search, verification and executable structure

## Primary sources checked

- **Url:** https://research.google/pubs/graph-neural-networks-are-dynamic-programmers/
  
  **Purpose:** Primary publication identification and scope of the categorical algorithm-alignment result.

- **Url:** https://proceedings.mlr.press/v198/deac22a.html
  
  **Purpose:** Checked expander propagation and negative-curvature qualification.

## Source and coverage

**Status:** complete_available_text

**Method:** Read complete local ASR text in bounded sections; not an independent audio verification.

**First timestamp:** 00:00:00

**Last timestamp:** 00:36:52

**Caveats:** - Local Whisper-large-v3-turbo transcription; proper names and technical notation may be inaccurate.

- Timestamps refer to the recovered podcast edition; exact alignment with the current YouTube edit is not certified.

Source type: Local asr. Reviewed text: 7,304 words.

Transcript file: `1lkdWduuN14.local-asr.txt` (not distributed).

SHA-256: `3a229a38614e797d957ed03cb6cd33d49c4e5595587ca7c448f491b7726392dc`.

[Structured review](1lkdWduuN14.json) · [Source ledger](../sources.json)
