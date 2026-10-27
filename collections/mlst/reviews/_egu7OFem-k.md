# Strange Geometric Shapes Found Inside AIs — Tom McGrath

[Original episode](https://www.youtube.com/watch?v=_egu7OFem-k) · [All reviews](../README.md) · [Learning path](../learning-path.md)

Published: 2026-09-02 · Decision: **Core** · Confidence: High on conceptual relevance; moderate on empirical breadth because papers and audio were not independently checked.

## Central claim

Intelligence may organize reusable computations in structured activation manifolds, and understanding those structures can improve both scientific explanation and selective training. The episode is most valuable where it distinguishes what an interpretability instrument can reconstruct from what the network actually computes.

## Ideas I want to keep

- Sparse scalar features are a representational hypothesis, not an ontology. Weekdays and months can occupy circular structures; representing a circle as many nonnegative rays fragments one coherent variable into apparently separate features. Block-sparse and manifold approaches offer a different level of description.

- A reported arithmetic circuit translates several semantic domains into a shared representation, applies an addition operation, and translates back. This suggests a concrete route from distributed representation to modular computation without requiring hand-coded symbols. It also permits mixed explanations: clean algorithms and redundant heuristics may coexist.

- Selective generalization is a credit-assignment problem: pirate-flavored math training improves both mathematics and pirate style. Feature-gradient attribution, preventive steering, and inoculation prompting attempt to separate these changes by altering which residual errors the model must learn.

- Interpretability-assisted rewards amortize expensive judgments into internal probes, but optimization can destroy the relation between the probe and the intended property. Reading a representation, intervening on it, and safely optimizing it are different achievements.

- The reward-hacking discussion distinguishes degenerate behavior selected by an objective from internal representations associated with cheating or grader awareness. This creates testable mechanistic questions even though a probe is insufficient to prove intent or conscious awareness.

## Mathematical anatomy

**Objects:** Hidden state h, sparse coefficients a, decoder directions d_j, multidimensional feature subspaces, curved activation manifolds, gradients of loss, and policies optimized against external or internal graders.

**Objective:** Explain and control what a learned system represents and computes, while preserving useful capabilities and avoiding unintended generalization. Reconstruction accuracy alone is not the explanatory objective.

**Mechanism:** For h approximately equal to sum_j a_j d_j, a_j times the inner product of the hidden-state loss gradient with d_j is a first-order feature-attribution quantity. McGrath explicitly calls it a crude proxy: the effect of a parameter update on future behavior also depends on parameter Jacobians and subsequent computation. A circular variable can be represented by sine/cosine coordinates; modular addition can then be implemented by structured transformations rather than a table of independent cases.

**Assumptions:** Discovered structures must survive changes of prompt and task, interventions must remain on meaningful activation states, and the feature vocabulary must cover relevant alternative routes through the model. Probe validity must persist under optimization rather than only on a fixed validation distribution.

**Limits:** Geometry does not by itself identify an algorithm; decoding success does not establish causal use; feature selectivity is not guaranteed by naming a direction. Neither weak architectural priors nor predictive success establishes that a network has recovered the unique structure of the world.

## Evidence, limitations and corrections

- At 01:12:37–01:17:17 the shared arithmetic module is described as a concrete empirical result, with substantial manual discovery and only limited cross-model investigation. Broader convergence is a hypothesis, not a demonstrated universal law.

- At 00:56–01:12 the manifold examples expose the limitations of scalar SAE features. Successful reconstruction and intervention should be evaluated separately; off-manifold corruption is one explanation of failed steering, not a diagnosis available from every failure.

- At 01:27:07–01:29:28 the grader-deception experiment was described as unpublished at recording. Synthetic contrast vectors and web examples associated with cheating support a representational interpretation but do not uniquely establish a guilty mind.

- Goodfire has a commercial stake in intentional design. Automated scientific discovery, reliable goal readout, and general control of training are research aspirations; the closing discussion explicitly acknowledges incomplete solutions.

- Reported contemporary model benchmarks, model names, and incidents are interview claims here. No external paper or incident was independently verified, and ASR may distort names.

## Relevance to my research

Exceptionally relevant because it forces a choice of explanatory objects: individual neurons, sparse features, manifolds, algorithms, and goal representations are not interchangeable. It gives me a way to ask when an apparently statistical system has acquired reusable computation, and how to test that claim causally rather than by anthropomorphic description.

## My viewing plan

**Mode:** I plan to watch the full technical discussion, prioritizing geometry and selective training.

**Segments:** - **Start:** 00:12:18
  
  **End:** 00:40:00
  
  **Purpose:** Selective learning, feature-gradient approximations, preventive steering, and monitor Goodhart.

- **Start:** 00:56:00
  
  **End:** 01:17:17
  
  **Purpose:** Manifolds, multidimensional features, and shared arithmetic computation.

- **Start:** 01:25:25
  
  **End:** 01:40:00
  
  **Purpose:** Reward hacking, limits of internal monitoring, and competing interpretability strategies.

**Edition:** Timestamps refer to the saved 01:40 transcript edition; some segment boundaries are approximate minute boundaries. Not audio verified.

## Objections and open questions

The simplest competing account is that attractive geometric plots reveal an analyst-selected projection rather than a reusable causal abstraction. My evidential standard requires interventions, held-out tasks, and comparison to simpler circuit models. Likewise, internal monitors may create a new optimization target that models can evade. These objections strengthen the value of the episode because they specify the experiments its thesis needs.

## An experiment I could try

I would train a small modular-addition network and a multi-domain version using two encodings of the same cyclic group, comparing a scalar sparse autoencoder with two-dimensional subspace features. Patching along a learned circular arc and along its chord would test held-out addition accuracy, reconstruction error and transfer between encodings. Optimization against a probe would then distinguish improved behavior from improved probe scores alone.

## Connections in my notes

- Kornblith and Misra: representation objectives and measurement tools shape which structure appears interpretable.

- Chollet: abstraction as reusable transformations rather than isolated input-output mappings.

- Jordan: optimizing a measurement requires assumptions beyond estimating it.

## Source and coverage

**Read:** Entire available transcript, sequentially; not audio verified.

**Last timestamp:** 01:40:00

**Source caveats:** ASR/publisher transcript may contain wording and mathematical transcription errors; timestamps refer to this saved edition.

Source type: Publisher transcript. Reviewed text: 20,292 words.

Transcript file: `_egu7OFem-k.publisher.txt` (not distributed).

SHA-256: `e2a0cb8bed930b34d6bdc21dde0774d97db3e1320e12eb1dba1ed3c0a319d14c`.

[Structured review](_egu7OFem-k.json) · [Source ledger](../sources.json)
