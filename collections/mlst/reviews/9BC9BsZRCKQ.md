# ML Robustness & Engineering - Andrew Ilyas (MIT)

[Original episode](https://www.youtube.com/watch?v=9BC9BsZRCKQ) · [All reviews](../README.md) · [Learning path](../learning-path.md)

Published: 2024-08-21 · Decision: **Core** · Confidence: high

## Central claim

I want to study a learning system as a data-dependent scientific object: intervening on the dataset, measuring changes after retraining, and distinguishing genuinely predictive but fragile features from both memorization and robust causal structure.

## Ideas I want to keep

- At 06:38–23:53, datamodeling shifts the unit of analysis from a trained network to the learning algorithm. For a fixed test input, a surrogate predicts its output from the binary membership vector of a training subset. The surprising empirical observation is useful near-linearity in data space despite nonlinear training. Coefficients have shared training-example coordinates across architectures, enabling comparisons that arbitrary hidden representations do not naturally allow.

- At 26:24–36:50, TRAK makes the distinction between a useful approximation and an exact mechanism concrete. It linearizes outputs around trained parameters, applies influence-style reasoning, projects huge gradient features, and averages across trained models. Smaller random projections can improve attribution before becoming too small, suggesting a regularization effect rather than merely information loss. This is a valuable example of computational approximation changing statistical behavior.

- At 37:10–40:49, textual entailment and actual training influence come apart. Retrieval can recover documents that state a fact while another attribution method identifies examples whose removal changes the prediction more. The intervention target therefore determines what counts as correct attribution. This does not mean an influential example is the logical source, nor that deletion fully erases a concept.

- At 53:18–01:01:48, adversarially perturbed and relabeled training data can still yield above-chance accuracy on ordinary images. That challenges the belief that small adversarial signals must be useless noise. Predictiveness under the original distribution, stability to small perturbations and human perceptual salience are separate properties. Adversarial training changes which predictive features remain usable.

- At 59:05–01:00:24 and 01:15:35–01:25:40, the discussion separates robustness to test-input perturbations, removal of training data and distribution/causal changes. It then moves upstream to collection: ambiguous ImageNet labels and occupation self-selection illustrate how a model can learn the sampling procedure rather than the intended target structure.

## Mathematical anatomy

**Objects:** A randomized training procedure A, source dataset D, subset indicator z, test point x, prediction statistic m(A(D_z),x), surrogate coefficients w_x, gradient features, and an explicitly chosen perturbation or selection model.

**Objective:** Predict dataset counterfactuals g_x(z)≈E_A[m(A(D_z),x)], rather than assign a uniquely fair share of credit. Robust learning instead minimizes E_(x,y)[max_{δ in Δ} loss(fθ(x+δ),y)]. These are distinct optimization problems, with different intervention domains.

**Mechanism:** Fit a linear datamodel b_x+w_x·z by repeated subset training. TRAK approximates output variation through first-order parameter features and influence-style estimates, with projection and ensembling. The episode uses correct-class margin as an informative real-valued statistic. Removing influential subsets and retraining tests the surrogate’s practical counterfactual predictions.

**Assumptions:** Results depend on subset sampling distribution and size, training procedure, random-seed averaging, output statistic and projection choice. Adversarial robustness is always relative to Δ, a norm/radius or another allowable transformation set. Self-selection recovery assumes a specified structural data-generation model, not arbitrary missing-not-at-random observations.

**Limits:** A linear fit need not capture interactions or extrapolate to very different subset sizes. Correlation measures ranking/co-movement and does not establish numerical calibration. Datamodel coordinates align examples, but do not make causal effects globally invariant to dataset changes. Parameter linearization is local and is not proof that the original network learns no nonlinear features.

## Evidence, limitations and corrections

- The interview reports very high random-subset correlation and weaker but useful deliberately selected-subset performance. These are empirical regularities, not a theorem about all learning algorithms. The proposed width/linearity explanation is explicitly called unverified folklore.

- The cats/dogs 90% example at 56:53 is a simplified narrative, not a universal quantitative result of the original study. The authors’ original poster reports different dataset-specific accuracies; the durable conclusion is that non-robust information can generalize.

- The non-robust-feature explanation establishes an important mechanism, not exclusivity. A primary Distill discussion constructs adversarial vulnerability without such features; overfitting and other sources of brittleness can coexist.

- Dense data support is suggestive of broad abstraction, while sparse support can expose exemplar dependence; neither alone settles reasoning, semantics or causal understanding. Ilyas appropriately refuses to equate these undefined concepts.

- The selection-bias result is explicitly restricted to a well-specified generative model. Applying a wrong strategic-selection model can move estimates in an unknown direction. Human perceptual robustness likewise should not be interpreted as universal immunity to adversarial or perceptual failures.

## Relevance to my research

Very high for my research and distinct from circuit interpretation: it supplies an experimentally grounded way to ask what learning depends on, what a feature buys, and which invariances an objective actually enforces. The pipeline viewpoint prevents attributing every failure to the architecture while ignoring labels, selection and deployment.

## My viewing plan

**Mode:** I plan to watch the full technical conversation.

**Ranges:** - **Start:** 00:06:38
  
  **End:** 00:43:54
  
  **Why:** Datamodels, TRAK and the distinction between entailment and intervention-based attribution.

- **Start:** 00:53:18
  
  **End:** 01:10:46
  
  **Why:** Predictive non-robust features and different robustness definitions.

- **Start:** 01:15:35
  
  **End:** 01:25:40
  
  **Why:** Collection bias and limits of self-selection correction.

**Edition note:** Ranges are observed in the recovered publisher edition ending 01:27:39; opening sponsor and closing career material can be skipped.

## Objections and open questions

Attribution through retraining may be too expensive and coarse to reveal an actual inference-time algorithm. Its strength is complementary: a circuit story without data counterfactuals can miss learning dependence, while a datamodel without circuits cannot uniquely identify computation. Robust features also depend on what invariances I choose to demand.

## An experiment I could try

I want to construct a small classification dataset with one stable causal feature, a strongly predictive but perturbable feature and a rare subgroup supported by few examples. Models trained on random subsets would supply per-test-point margin datamodels. Held-out random subsets and adversarially chosen removals would be evaluated with correlation and calibration plotted separately. Comparing data-removal brittleness, input-perturbation robustness and shifted-test accuracy would expose where these orderings disagree.

## Connections in my notes

- Nanda: interventions and informative metrics, but on training examples instead of activations.

- Belrose: concept accessibility/erasure differs from deletion of influential training evidence.

- Balestriero: training objectives bias selected features; local geometric smoothness is not equivalent to all forms of robustness.

- Koolen: prospective data acquisition must optimize information relevant to an explicit decision.

## Primary sources checked

- **Title:** Datamodels: Predicting Predictions from Training Data
  
  **Url:** https://arxiv.org/abs/2202.00622
  
  **Use:** Primary datamodel formulation.

- **Title:** TRAK: Attributing Model Behavior at Scale
  
  **Url:** https://arxiv.org/abs/2303.14186
  
  **Use:** Primary attribution method.

- **Title:** Adversarial Examples Are Not Bugs, They Are Features
  
  **Url:** https://arxiv.org/abs/1905.02175
  
  **Use:** Primary non-robust feature experiment.

- **Title:** Authors’ adversarial-features poster
  
  **Url:** https://people.csail.mit.edu/tsipras/bugs_poster.pdf
  
  **Use:** Dataset-specific numerical examples differ from the simplified cats/dogs story.

- **Title:** Adversarial Examples are Just Bugs, Too
  
  **Url:** https://distill.pub/2019/advex-bugs-discussion/response-5/
  
  **Use:** Primary counterexample to an exclusive non-robust-feature explanation.

## Source and coverage

**Status:** complete_available_text

**Start:** 00:00:00

**End:** 01:27:39

**Caveats:** - Read the complete recovered publisher transcript; audio not independently checked. Speaker attribution is generic and several names/technical terms are mistranscribed. Numerical examples in the conversation can be illustrative rather than paper-table results.

Source type: Publisher transcript. Reviewed text: 18,363 words.

Transcript file: `9BC9BsZRCKQ.publisher.txt` (not distributed).

SHA-256: `ddc70f248db43e5d4f8847300d08a281f2c693f0d31c10f45aa0082c56996525`.

[Structured review](9BC9BsZRCKQ.json) · [Source ledger](../sources.json)
