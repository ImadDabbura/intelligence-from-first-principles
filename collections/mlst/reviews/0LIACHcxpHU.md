# #047 Interpretable Machine Learning - Christoph Molnar

[Original episode](https://www.youtube.com/watch?v=0LIACHcxpHU) · [All reviews](../README.md) · [Learning path](../learning-path.md)

Published: 2021-03-14 · Decision: **Worthwhile** · Confidence: high

## Central claim

An explanation is an estimand produced by a particular intervention, averaging rule and information reduction. Understanding intelligence requires asking what that estimand actually identifies, rather than treating a plausible-looking attribution as a mechanism or a causal explanation of the world.

## Ideas I want to keep

- Permutation importance changes two things at once: dependence between a feature and the target, and dependence between that feature and other inputs. A score therefore measures performance under a particular perturbed distribution, not intrinsic importance independent of context.

- Partial dependence and local surrogate methods query synthetic inputs. When features are dependent, these queries can leave the training support, so an apparently precise explanation can mainly describe arbitrary extrapolation.

- Human usefulness and explanatory fidelity are different dimensions. A short contrastive explanation may be persuasive while omitting interacting causes; a complete allocation may be too difficult to use. There is no universal scalar definition of a good explanation.

- The distinction between a feature causing a model output and causing a real-world outcome is explicit. A correct churn predictor does not establish that contacting likely churners will reduce churn; prediction and intervention answer different questions.

- Explanations inherit training-data, initialization, fitting and estimation uncertainty. Reporting a single attribution vector hides these layers; repeated fitting and uncertainty analysis are part of the scientific claim.

- A deployed model changes later data through its decisions. The rent-index example makes a static explanation incomplete when the object being studied is a model-environment feedback loop.

## Mathematical anatomy

**Objects:** Predictor f, observed joint distribution P(X), an intervention or perturbation kernel Q, a summary functional T(f,Q), and a human interpretation of that summary.

**Assumptions:** An interpretation needs a defined question and appropriate support assumptions. Feature independence cannot be inferred from zero Pearson correlation. Causal conclusions need assumptions beyond predictive fit.

**Objective:** Characterize how a model behaves, debug it, or explain a particular prediction while preserving the distinctions between fidelity, sparsity, robustness, usability and world-level causal validity.

**Mechanism:** Partial dependence averages f(x_j,X_-j) under a chosen reference distribution. Permutation importance compares loss before and after a specified resampling. Shapley attribution averages marginal coalition contributions, but its axioms apply only after specifying the coalition value function and treatment of missing features.

**Limits:** Axiomatic fairness of allocation does not prove semantic or causal correctness. Conditional resampling changes the question rather than magically resolving it. Locality depends on the metric and kernel width; a low-error surrogate locally need not identify a global computation.

## Evidence, limitations and corrections

- At 22:00–24:03 Molnar derives the two effects of feature permutation rather than merely labeling the method flawed. This is the strongest methodological passage.

- At 28:02–35:03 saliency-map criticisms include insensitivity to model changes and class changes. These are useful falsification tests, but the conversation does not establish that every saliency method fails every test. The named sanity-check paper is discussed, not independently reproduced here.

- At 55:06–59:02 uncertainty is discussed carefully, and Molnar explicitly acknowledges existing random-forest importance inference. The broader opening claim that uncertainty quantification does not exist is therefore too sweeping.

- At 63:04–68:05 model-level causation, world-level causation and learning the variables themselves are distinguished. Host claims that causal graphs emerge from data alone need qualification: observational equivalence and modeling assumptions constrain identification.

- At 79:05–83:01 the Shapley discussion includes theoretical attraction and duplicate-feature subtleties. The claim that it is the only theoretically valid explanation is a host overstatement; different questions and axioms lead to different valid tools.

- Several host claims that neural networks are only memorization or have no transfer between learned rules are unsupported generalizations. I do not adopt them.

## Relevance to my research

Useful scientific hygiene for every attempt to infer what a learned system knows or how it computes. The key gain is an explicit separation of function behavior, distribution-dependent summaries, internal mechanism and environmental causation. Much of the operational governance discussion is secondary to my research focus, so I will concentrate on the methodological chapters.

## My viewing plan

**Mode:** I will focus on these chapters.

**Segments:** - **Start:** 00:16:01
  
  **End:** 00:39:00
  
  **Purpose:** Explanatory desiderata, perturbations, dependency and saliency falsification.

- **Start:** 00:53:00
  
  **End:** 01:11:03
  
  **Purpose:** Prediction versus intervention, uncertainty and deployed feedback loops.

- **Start:** 01:19:05
  
  **End:** 01:24:04
  
  **Purpose:** Shapley assumptions and the meaning of locality.

**Edition note:** Entire saved transcript, including opening summary and postscript through 01:40:00, was read. These are transcript navigation anchors, not audio-verified chapter boundaries.

## Objections and open questions

- The episode mostly studies input-output explanations rather than circuit-level mechanisms or theories of learning. It is a complement to mathematical anatomy, not a direct theory of intelligence.

- Interpretability need not reproduce every detail to be valuable. A deliberately lossy summary can answer a precise question even when it cannot certify safety or causality.

## An experiment I could try

I want to construct X2=X1+small noise and a model that uses either X1 alone or both features, then compare marginal permutation, conditional permutation, partial dependence and attributions under several background distributions. Adding a duplicate feature and refitting would expose which scores change despite nearly unchanged predictions on the observed support. Each result needs an explicit estimand. Bootstrapping both the data and training procedure would separate attribution-estimation uncertainty from model uncertainty.

## Connections in my notes

- Connects to Apollo’s hidden-goal study through intervention design and alternative explanations.

- Connects to Frankle through using controlled perturbations to distinguish a hypothesis from an appealing story.

- Provides the methodological background for reading causal-representation and mechanistic-interpretability episodes critically.

## Source and coverage

**Status:** complete_available_text

**Method:** Read entire saved transcript; any truncated tool section reread in bounded chunks. Audio not checked.

**Last timestamp:** 01:40:16

**Caveats:** - ASR transcription can corrupt names and mathematical terminology; transcript completeness is not an audio audit.

Source type: Existing caption or archive. Reviewed text: 17,460 words.

Transcript file: `0LIACHcxpHU.hf.txt` (not distributed).

SHA-256: `2027164b7df181631e28372a9e77f409f4fa0ed0cc6509dd9d59060796df91b3`.

[Structured review](0LIACHcxpHU.json) · [Source ledger](../sources.json)
