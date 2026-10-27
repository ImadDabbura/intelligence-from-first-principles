# The Real Reason Huge AI Models Actually Work [Prof. Andrew Wilson]

[Original episode](https://www.youtube.com/watch?v=M-jTeBCEGHc) · Source: Machine Learning Street Talk · [All reviews](../README.md) · [Learning path](../learning-path.md)

Published: 2025-09-19 · Decision: **Core** · Confidence: Very high relevance; distinguish formal frameworks from the proposed explanation of scale.

## Central claim

Expressiveness and inductive bias are separate axes: an enormous hypothesis space can strongly prefer simple explanations. This is a foundational corrective to parameter-count reasoning, but the episode also leaves open why particular training systems acquire the claimed simplicity bias.

## Ideas I want to keep

- Parameter counting confuses the support of a model with the probability or optimization preference assigned to each function. Gaussian processes supply a concrete counterexample: infinite-dimensional function spaces can have strong smoothness preferences and work with little data.

- Hard constraints and soft biases are different commitments. Residual pathways can combine an equivariant component with unconstrained alternatives, expressing uncertainty about whether the observed system actually satisfies a symmetry or conservation assumption.

- Double descent and benign overfitting motivate analyzing the selected predictor rather than only worst-case richness of its hypothesis class. Compression-based or PAC-Bayesian arguments can remain meaningful where a capacity measure covering all labelings is uninformative.

- Bayesian prediction means averaging plausible explanations, not merely choosing a prior or adding a penalty. Deep ensembles can serve as useful approximate predictive marginalization even when they are not literal posterior samples.

- Marginal likelihood and posterior predictive performance answer different questions. A prior may spread mass broadly yet adapt effectively after data; maximizing evidence is therefore not automatically equivalent to maximizing future predictive accuracy.

- Shared low-level features are not the only explanation of transfer. A more abstract tendency to discover compressible structure could transfer across text, time series, and materials, while task-specific symmetry and representation still matter.

## Mathematical anatomy

**Objects:** Distributions over functions, parameter priors, posterior predictive distributions, equivariant subspaces and complements, compression lengths, loss-surface geometry, and compute-constrained learning procedures.

**Objective:** For Bayesian prediction integrate p(y|x,theta)p(theta|D) over theta. Model evidence integrates p(D|theta)p(theta) instead. A countable-hypothesis bound can charge a predictor according to its code length or negative log prior mass rather than the raw number of available parameters.

**Mechanism:** Residual-pathway priors give different covariance scales to equivariant and complementary directions. Compression bounds associate short descriptions with lower statistical complexity. Marginalization weights regions by likelihood times prior mass; broad low-loss regions may contribute more than sharp optima, provided the measure and prior are specified. Stochastic weight averaging exploits a connected low-loss region by averaging nearby parameter iterates.

**Assumptions:** A prior or code used for a bound must be valid and its data dependence accounted for. Comparisons of flatness require a parameterization or invariant measure. Bayesian guarantees are conditional on the model, likelihood, and inference approximation; posterior spread is not automatically calibrated under misspecification.

**Limits:** A bias-variance decomposition does not entail a universal monotonic tradeoff, but ensembles do not automatically eliminate bias. Fitting identical training labels leaves room for different inductive biases; that alone does not prove the relevant bias is Kolmogorov simplicity. Short executable descriptions are upper bounds on uncomputable Kolmogorov complexity, and compression-based generalization does not establish implementation of Solomonoff induction.

## Evidence, limitations and corrections

- At 00:10:18–00:11:05 and 00:49:55–00:53:40 Wilson explicitly treats the source of scale-induced simplicity as incompletely understood. The r_a^d/r_b^d volume analogy is heuristic: changing dimension can also change geometry, measure, and optimizer accessibility.

- At 00:32:31–00:35:19 soft equivariance is supported by described experiments, with sensitivity to bias strength acknowledged. A finite soft penalty does not generally force an exact constraint; the reported collapse is setting-dependent.

- At 00:58:40–01:05:06 shortcut learning and matrix-operation failure under distribution shift limit the claim that compression alone delivers understanding. Richer training and looping reportedly helped, but do not establish general algorithmic reliability.

- At 01:27:41–01:32:25 the marginal-likelihood critique is unusually valuable. The chain-rule product of sequential predictive probabilities is exact; identifying it with a practical optimizer learning curve requires additional assumptions.

- At 01:34:35–01:45:01 grokking explanations are explicitly speculative. Likewise, a mode-connecting path does not show all solutions are connected, equal training loss need not imply identical predictions, and uniform curve-parameter sampling is not necessarily uniform arc-length sampling.

- At 01:51:26–02:00:03 compute-optimal architectural observations assume ample data and little generalization gap. Changing a power-law exponent changes polynomial scaling in compute, not literally exponential improvement in compute. Papers and historical anecdotes were not independently checked.

## Relevance to my research

One of the strongest fits for my aims. It restructures the central question from how many parameters a model has to which functions it prefers, how uncertainty over explanations is represented, and which simplicity notion predicts useful generalization. The hosts repeatedly demand an actual mechanism, so unresolved questions remain visible rather than being hidden by a slogan.

## My viewing plan

**Mode:** I plan to watch the full episode after the sponsorship and revisit the mathematical chapters.

**Segments:** - **Start:** 00:07:15
  
  **End:** 00:28:15
  
  **Purpose:** Expressiveness, soft bias, parameter counting, and double descent.

- **Start:** 00:32:31
  
  **End:** 00:58:40
  
  **Purpose:** Equivariance priors, compression bounds, and limitations of the scale explanation.

- **Start:** 01:11:12
  
  **End:** 01:32:25
  
  **Purpose:** Predictive marginalization versus evidence and prequential views.

- **Start:** 01:38:59
  
  **End:** 02:03:17
  
  **Purpose:** Loss geometry, actionable research questions, compute regimes, and scientific theory discovery.

**Edition:** Saved transcript runs to 02:03:19; timestamps refer to that edition. Introductory teaser and sponsorship precede the interview; no audio verification.

## Objections and open questions

A broad compression principle can become retrospective if the coding scheme or notion of simplicity is chosen after seeing success. Universality claims need task distributions and finite-compute restrictions. Hard physical constraints may be essential for safety or long-horizon stability even when soft biases give comparable average error. These are substantive tensions with the prescription, not refutations of its useful separation of flexibility and preference.

## An experiment I could try

I want to compare polynomial regression in monomial and orthogonal bases, an RBF Gaussian process, and minimum-norm overparameterized regression on the same noisy function. Parameter count, predictive error, prior samples and sensitivity to coordinate rescaling would separate expressiveness from preference. A second comparison would contrast evidence-selected hyperparameters with held-out predictive log likelihood, using a diffuse-prior model that adapts well but receives poor evidence.

## Connections in my notes

- Bronstein and Welling: hard symmetry versus uncertain or learned symmetry is the central comparison to make.

- Kornblith and Salman: equal source performance need not imply equivalent transferable representations.

- McGrath: reusable algorithms and geometric representations require mechanistic evidence beyond compression or prediction alone.

## Source and coverage

**Read:** Entire available transcript, sequentially; not audio verified.

**Last timestamp:** 02:03:19

**Source caveats:** ASR/publisher transcript may contain wording and mathematical transcription errors; timestamps refer to this saved edition.

Source type: Publisher transcript. Reviewed text: 23,246 words.

Transcript file: `M-jTeBCEGHc.publisher.txt` (not distributed).

SHA-256: `0ebfcc03c889a72511d8cb83ac8a01aa0fbb7bc5961491343b9d139887c8eff2`.

[Structured review](M-jTeBCEGHc.json) · [Source ledger](../sources.json)
