# AI Interpretability, Safety, and Meaning - Nora Belrose

[Original episode](https://www.youtube.com/watch?v=VgPrjHxIS0I) · Source: Machine Learning Street Talk · [All reviews](../README.md) · [Learning path](../learning-path.md)

Published: 2024-11-17 · Decision: **Core** · Confidence: high for technical sections; medium for broader philosophical value

## Central claim

A particularly valuable lesson in what it means for a representation to contain a concept, for a decoder to access it, and for a model to use it. LEACE and the failure of stronger erasure attempts turn abstract interpretability questions into precise interventions; the later counting-argument critique supplies a separate lesson about probability measures and inductive bias.

## Ideas I want to keep

- At 00:04:48–00:17:55, concept erasure becomes an operational question relative to a decoder family, a loss and an intervention norm. The whitening/projection/unwhitening picture makes a constrained optimization concrete, and the distinction between ordinary orthogonal projection and a least-distorting transformation is mathematically instructive.

- At 00:16:47–00:25:33, layerwise removal of part-of-speech information tests reliance rather than mere decodability. Prediction degrades but remains better than a unigram baseline. This exposes why an identifiable linguistic feature is not automatically a complete explanation of the computation, and why nonlinear information can survive linear erasure.

- At 00:27:41–00:32:18, the proposed quadratic eraser has an especially instructive failure: choosing a transformation using the class label can leak the label through higher-order statistics. Small classifiers appear defeated while larger ones recover or benefit. An intervention can manufacture the very information channel it is intended to remove.

- At 00:34:23–00:45:43, distributional simplicity bias is probed by editing class means and covariances without making an image look like a different object to a human. Early models follow the edited statistics more strongly than later ones. The relevant complexity ordering is statistical moment order, not automatically Fourier frequency, semantic abstraction or human interpretability.

- At 01:25:17–01:40:30, the critique of counting possible misaligned goals attacks an unspecified probability measure. The number of descriptions consistent with training does not determine how an optimizer samples them. The comparison with generalization is useful because it directs attention to initialization, architecture, data and training dynamics.

## Mathematical anatomy

**Objects:** Representations X, one-hot concept labels Z, their covariance and cross-covariance, affine erasers, restricted decoder classes, and training-time trajectories of feature use. Later, the objects are hypothesis spaces and probability measures over learning outcomes.

**Objective:** Minimize expected representation distortion while removing the specified accessible information. The formal LEACE result concerns affine predictors and losses convex in their predictions; equal class centroids characterize guardedness in that sense. This is not a guarantee of chance 0–1 accuracy for every possible threshold classifier, nor statistical independence X⊥Z.

**Mechanism:** Whiten the representation, project away the relevant concept-correlated directions, then unwhiten. Insert erasers sequentially into a frozen model and measure the resulting prediction loss. For the statistics experiments, transport images toward another class’s first and second moments and track the model’s tendency to predict that target label across training.

**Assumptions:** Concept labels capture the intended concept; estimated moments generalize; the chosen probe family reflects relevant computation; small geometric distortion is an appropriate intervention criterion. A linear information channel is a useful tractable target but is not the entire semantic concept.

**Limits:** Surgicality in squared distance does not guarantee semantic or causal isolation: correlated useful features can change too. Nonlinear transformations can recover information that survives erasure. Label-dependent preprocessing can leak information. A training-induced prior is essential to probabilistic arguments, but knowing that such a prior exists does not establish that it favors benign behavior.

## Evidence, limitations and corrections

- Belrose candidly distinguishes published LEACE experiments from tentative QLEACE results and acknowledges label quality, nonlinear residual information and lack of extensive performance measurements. This makes the technical portion unusually useful for learning how to delimit a claim.

- The spoken shorthand that no linear classifier can do better than chance omits the loss-family qualification. The primary paper’s guardedness definition is the appropriate reference; classification accuracy and optimized convex loss are different criteria.

- The moment-editing results support a tendency in studied networks and datasets, not a universal theorem that all networks learn every moment in order. The discussion itself identifies grokking and regularization as reasons a single monotone simplicity story is inadequate.

- The counting critique undermines an inference from cardinality to probability, not all arguments about deception or harmful optimization. The author also acknowledges disagreement about which version of the argument opponents actually defend.

- Claims around 01:53:06 that imitation-trained systems should not develop autonomous drives are expectations, not proofs. Literal access to weights is not equivalent to understanding them, and economic incentives for controllability do not guarantee the desired outcome.

- The phenomenology, simulation and Buddhist sections are personal philosophical explorations. They introduce useful questions about system boundaries and meaning but supply no tested mathematical theory of intelligence; second-hand descriptions of other philosophers are not treated as definitive scholarship.

## Relevance to my research

Very high for learning to distinguish information present, information accessible, information used, and information removed. These distinctions apply to neuroscience and scientific modeling as well as language models. The failed quadratic intervention is particularly valuable because it shows how a formally successful local criterion can undermine its broader purpose.

## My viewing plan

**Mode:** chapters

**Ranges:** - **Start:** 00:02:55
  
  **End:** 00:45:43
  
  **Why:** Core technical sequence: erasure, mathematical operationalization, intervention failure and distributional simplicity.

- **Start:** 01:25:17
  
  **End:** 01:40:30
  
  **Why:** Probability measures, counting arguments and inductive bias.

- **Start:** 01:03:05
  
  **End:** 01:11:47
  
  **Why:** Optional competing views on embodiment, extended cognition and simulated life.

**Edition note:** Times observed in publisher transcript. Later philosophical discussion is not needed to obtain the episode’s main technical contributions.

## Objections and open questions

Linear probes may still be useful even when higher-order information remains: the downstream network may rely disproportionately on the easiest channel. Conversely, a loss increase after erasure does not uniquely identify the removed concept’s causal contribution. A sound interpretation combines minimal-distortion edits with control interventions, nonlinear probes, distribution-shift tests and measurements of actual downstream behavior.

## An experiment I could try

I want to construct balanced classes where X|Z=0 is uniform on {-1,+1} and X|Z=1 on {-2,+2}. Their equal means permit an optimal constant predictor for logistic cross-entropy, yet a one-sided threshold above 1 achieves 75% classification accuracy. Verifying both results would clarify the loss-family distinction. I would then add a mean-shift feature, apply an affine eraser, and compare linear-loss, threshold-accuracy and quadratic-probe conclusions. A label-dependent moment-matching transform would test whether a larger classifier learns its artifacts. These experiments target distinctions the interview tends to compress.

## Connections in my notes

- Voita: probing complexity and accessible versus used information

- Balestriero: objective-dependent representations and geometric interventions

- Inductive bias and measure selection in generalization

- Agency as a model of behavior versus a persistent internal mechanism

## Primary sources checked

- **Title:** LEACE: Perfect linear concept erasure in closed form
  
  **Url:** https://arxiv.org/html/2306.03819v2
  
  **Use:** Formal guardedness, convex-loss qualification and minimum-distortion affine erasure.

- **Title:** Neural Networks Learn Statistics of Increasing Complexity
  
  **Url:** https://proceedings.mlr.press/v235/belrose24a.html
  
  **Use:** Primary empirical account of distributional simplicity bias.

- **Title:** Counting arguments provide no evidence for AI doom
  
  **Url:** https://optimists.ai/2024/02/27/counting-arguments-provide-no-evidence-for-ai-doom/
  
  **Use:** Authors’ own formulation of the counting critique, not an independent validation of broader optimism.

## Source and coverage

**Status:** complete_available_text

**Start:** 00:00:00

**End:** 02:29:39

**Caveats:** - Read all 30,485 source words of publisher transcript; not audio verified.

- Technical interview occupies first 45 minutes; later sections discuss philosophy, agency, ethics and personal views.

- QLEACE experiments are explicitly unpublished at the time of the interview; they are reviewed as reported results, not independently reproduced.

Source type: Publisher transcript. Reviewed text: 28,289 words.

Transcript file: `VgPrjHxIS0I.publisher.txt` (not distributed).

SHA-256: `ad6f1f75742363fa325b526b5358f02dd900cfe35861cdd0020912e5e45cd3eb`.

[Structured review](VgPrjHxIS0I.json) · [Source ledger](../sources.json)
