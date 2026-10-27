# #71 - ZAK JOST (Graph Neural Networks + Geometric DL) [UNPLUGGED]

[Original episode](https://www.youtube.com/watch?v=jAGIuobLp60) · Source: Machine Learning Street Talk · [All reviews](../README.md) · [Learning path](../learning-path.md)

Published: 2022-03-25 · Decision: **Worthwhile** · Confidence: high

## Central claim

Relational inductive biases make learning efficient, but local invariant aggregation introduces identifiable limits; the graph used for computation should be chosen for the information the task requires.

## Ideas I want to keep

- The discussion distinguishes permutation equivariance of node outputs from invariance of a neighborhood aggregation. Sharing one update rule across nodes makes relabeling commute with computation; aggregating a set discards arbitrary neighbor order.

- The spectral-to-spatial derivation explains why polynomial graph filters become local message passing. Multiplying node features by adjacency aggregates neighbors; powers reach progressively longer walks. Locality is a restriction on the hypothesis class, not merely an implementation trick.

- Over-smoothing and over-squashing are separated. Repeated averaging can make node representations indistinguishable, whereas information from many distant nodes may be forced through a narrow fixed-size representation even without convergence to the same value.

- The one-dimensional Weisfeiler–Leman connection makes an expressivity limit concrete. Message-passing models cannot distinguish certain non-isomorphic graphs; non-injective aggregation can lose additional distinctions, such as two red/two blue versus four red/four blue neighbors under a mean.

- Rewiring, subgraph representations and richer primitives distinguish the observed physical graph from the computational communication graph. Treating an aromatic ring as a unit can remove a long-range communication burden at the cost of supplying domain structure.

- Feature propagation and Correct-and-Smooth illustrate that a good statistical assumption—nearby labels or residuals vary smoothly—can matter more on a benchmark than nominally greater graph-isomorphism power.

## Mathematical anatomy

**Objects:** Graph adjacency A, Laplacian L, node-feature matrix H, permutation P and learned shared update/aggregation maps.

**Objective:** Node, link or graph prediction with relabeling symmetry and a suitable local dependence assumption.

**Mechanism:** A representative update is h_i′=φ(h_i, AGG_{j∈N(i)}ψ(h_i,h_j)); equivariance means f(PAPᵀ,PH)=Pf(A,H). Polynomial filters ∑k c_k L^k have bounded-hop support. These formulas make the verbal explanation precise rather than quoting a derivation in the transcript.

**Assumptions:** The task is invariant to arbitrary identifiers and relevant information is accessible through the chosen graph. Smoothness methods additionally need feature/label regularity along edges; that is not universal.

**Limits:** Finite depth limits receptive field; finite-width bottlenecks and topology constrain communication. Standard message passing is bounded by 1-WL under the usual anonymous-node assumptions. Injective multiset encoding can reach that bound under conditions; plain summation of arbitrary real vectors is not automatically injective.

## Evidence, limitations and corrections

- The guest corrects an initially loose statement: equal final 1-WL color histograms do not prove isomorphism; differing histograms certify non-isomorphism. The corrected version is the one retained in these notes.

- Adjacency powers count walks, not necessarily simple paths. The transcript uses “paths” loosely; this matters when interpreting cycles and return walks.

- The spectral discussion is an intuition-level lineage, not a rigorous derivation of every GCN normalization or graph wavelet construction. An arbitrary polynomial filter need not be low-pass.

- The claim that most complex systems reduce to pairwise interactions is presented with an explicit admission of uncertain recollection; it does not supply a theorem justifying all GNNs.

- Benchmark observations and predictions that transformers will win are historical and conditional. More expressive does not necessarily mean more sample-efficient or easier to optimize; smoothing can fail badly on heterophilic graphs.

## Relevance to my research

A substantial bridge from linear algebra to relational learning. The fixed-capacity message bottleneck and distinction between data topology and computational topology fit my intuition-first approach particularly well. This complements the more systematic Bronstein blueprint.

## My viewing plan

**Mode:** full technical discussion

**Segments:** - **Start:** 00:05:01
  
  **End:** 00:10:04
  
  **Purpose:** Equivariance, invariance and hypothesis restriction.

- **Start:** 00:10:52
  
  **End:** 00:46:52
  
  **Purpose:** Local operators, diffusion, communication bottlenecks and graph choice.

- **Start:** 00:47:17
  
  **End:** 00:57:47
  
  **Purpose:** 1-WL, injectivity and the precise role of aggregation.

**Edition:** Saved HF transcript; I would omit course promotion and closing chatter. ASR consistently renders equivariant as equivalent.

**Intention:** I plan to watch the full technical discussion, omitting course promotion and closing chatter.

## Objections and open questions

A graph can encode the wrong causal or predictive relation; locality may remove the signal, and added edges can overwhelm it. Conversely, fully connected attention must learn which connections matter and can lose the efficiency supplied by correct relational structure. Expressivity, statistical efficiency and optimization are separate axes.

## An experiment I could try

I would implement anonymous-node message passing on a six-cycle and two disjoint triangles with identical initial features, then trace why 1-WL-style updates cannot distinguish them. Adding triangle counts or subgraph features would make the extra information explicit. Further comparisons would test mean versus sum aggregation on repeated neighbor labels, and smoothing on homophilic versus heterophilic synthetic graphs.

## Connections in my notes

- Geometric deep learning and symmetry

- Distributed computation and information bottlenecks

- Graph signal processing and diffusion

- Relational abstraction and representation design

## Source and coverage

**Read:** Entire available transcript, sequentially; not audio verified.

**Last timestamp:** 01:02:30

**Source caveats:** ASR/publisher transcript may contain wording and mathematical transcription errors; timestamps refer to this saved edition.

Source type: Existing caption or archive. Reviewed text: 10,318 words.

Transcript file: `jAGIuobLp60.hf.txt` (not distributed).

SHA-256: `949d67e263a7b7727cc8fb693f3ae96944f59a6282668eefa764397508d39d8d`.

[Structured review](jAGIuobLp60.json) · [Source ledger](../sources.json)
