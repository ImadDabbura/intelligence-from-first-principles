# SWaV: Unsupervised Learning of Visual Features by Contrasting Cluster Assignments (Mathilde Caron)

[Original episode](https://www.youtube.com/watch?v=uqJ2hbDGHjY) · [All reviews](../README.md) · [Learning path](../learning-path.md)

Published: 2020-09-13 · Decision: **Core** · Confidence: high for mechanism; moderate for speculative explanations of transfer

## Central claim

Useful self-supervised representations arise from explicit assumptions about which views should agree, combined with a constraint that prevents trivial agreement; “unlabeled” does not mean absence of supervision structure.

## Ideas I want to keep

- SWaV predicts a prototype assignment from a different augmented view of the same image. The training signal is agreement across views at the level of soft cluster codes, rather than direct semantic labels or only pairwise instance discrimination.

- The collapse problem is explicit: assigning every input to one prototype makes prediction easy but destroys useful information. Balanced assignment introduces competition for prototype mass and makes the constant solution incompatible with the assignment constraint.

- The assignment step is a constrained optimal-transport problem solved by iterative row/column rescaling. This is a concrete example of importing a mathematical primitive because a modeling constraint demands it, rather than adding a named algorithm as decoration.

- Augmentations determine what the representation is encouraged to ignore. Crops and color changes discourage pixel/location/color shortcuts, but they can also destroy task-relevant information. The method’s semantic bias comes from this pairing scheme and data curation as well as the loss.

- The author distinguishes soft assignments from hard clustering and explains why noisy minibatch assignments should not be overcommitted early. A queue improves the approximation when there are many prototypes relative to current-batch examples.

- The research narrative identifies orthogonal causes of progress: projection heads, augmentation, optimization settings and online assignments. Multi-crop improvements transfer across several methods, so improved scores cannot all be credited to one new loss.

## Mathematical anatomy

**Objects:** Augmented views x1,x2, normalized embeddings z1,z2, prototype matrix C, soft assignment Q, and predicted prototype probabilities p.

**Assumptions:** Views retain common task-relevant semantic content; a balanced prototype allocation is useful; minibatches/queues approximate the broader feature distribution.

**Objective:** Predict q1 from z2 and q2 from z1 with cross-entropy, while computing assignments subject to specified marginal masses.

**Mechanism:** Similarities CᵀZ enter an entropy-regularized assignment problem; Sinkhorn rescales rows/columns toward balanced marginals. Swapping detached codes across views trains the representation/prototypes. For B examples and K equally used prototypes, expected example mass per prototype is B/K (the transcript reverses this once).

**Limits:** Balanced prototype use is not the same as balanced semantic classes. Soft assignment permits overlapping affinities, but does not guarantee discovery of all meaningful factors. Rectangular transport uses appropriate unequal row/column targets; it is not literally a square doubly stochastic matrix with every marginal summing to one.

## Evidence, limitations and corrections

- The discussion is unusually useful because the author says which explanations are empirical interpretations rather than established theory. Slower optimization with soft assignments is a plausible account, not a proven mechanism.

- Removing ImageNet labels leaves a curated, object-centric dataset. The author reports lower absolute performance on uncurated social-media data while retaining comparative gains; no claim of prior-free learning is justified.

- The small TensorFlow reproduction intentionally changes or omits some recipe details and runs on a small flower dataset. It demonstrates implementability and learning, not exact reproduction of the large-scale published benchmark.

- The author does not claim unsupervised learning is universally superior. The practical motivation is label scarcity; transfer depends on downstream dataset size and relevance. Explanations for beating supervised pretraining remain tentative.

- Cropping two disjoint objects need not preserve semantics, so the core positive-pair assumption is approximate. The interview’s initial simplified statements should be read with that failure mode in mind.

## Relevance to my research

A foundation for my understanding of learning without labels: objectives encode invariances, anti-collapse constraints supply information pressure, and batch approximations shape the algorithm. I find this more useful than a retrospective ranking of SSL methods because each design decision can be tied to an explicit degeneracy or assumption.

## My viewing plan

**Mode:** technical sections; full interview if implementing

**Segments:** - **Start:** 00:11:05
  
  **End:** 00:20:00
  
  **Purpose:** Task formulation, prototypes and what is actually learned.

- **Start:** 00:24:11
  
  **End:** 00:46:02
  
  **Purpose:** Transport, collapse, soft assignments, data priors and multi-crop.

- **Start:** 00:57:01
  
  **End:** 01:04:04
  
  **Purpose:** Derivation through failure cases and evaluation discipline.

- **Start:** 01:12:06
  
  **End:** 01:16:13
  
  **Purpose:** Queue and minibatch approximation tradeoffs.

**Edition note:** HF transcript timestamps; audio/current-edit alignment not independently checked. Introductory puzzle, biography and implementation logistics optional.

**Intention:** I plan to watch the technical sections, extending to the full interview if I implement the method.

## Objections and open questions

The same invariances that improve one task can erase another task’s signal. Balanced prototypes may split frequent classes or merge rare ones. A strong downstream linear probe alone does not establish that the representation has discovered natural concepts or supports action, causality or compositional reasoning.

## An experiment I could try

I want to implement balanced assignment on a tiny two-view dataset, first removing balancing to test for collapse and then comparing hard and soft codes at small batch sizes. Adding a rare class and a color-dependent downstream task before applying color augmentation would let me separate failures due to optimization, sampling, balancing assumptions and deliberately discarded information.

## Connections in my notes

- Balestriero’s later interview: pairwise relations and hidden class-balance assumptions.

- Yi Ma: low-dimensional structured representations and explicit objectives.

- DINO/JEPA-style methods: different anti-collapse mechanisms, same need to account for invariance and retained information.

## Source and coverage

**Status:** complete_available_text

**Method:** Read entire saved transcript; any truncated tool section reread in bounded chunks. Audio not checked.

**Last timestamp:** 01:27:27

**Caveats:** - ASR transcription can corrupt names and mathematical terminology; transcript completeness is not an audio audit.

Source type: Existing caption or archive. Reviewed text: 13,139 words.

Transcript file: `uqJ2hbDGHjY.hf.txt` (not distributed).

SHA-256: `3d578fd4c8887f907829683661c67174729f2f2528161e647cf62846feaf49d5`.

[Structured review](uqJ2hbDGHjY.json) · [Source ledger](../sources.json)
