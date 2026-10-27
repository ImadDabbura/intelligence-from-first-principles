# #037 - Tour De Bayesian with Connor Tann

[Original episode](https://www.youtube.com/watch?v=RQ31MHw84o0) · Source: Machine Learning Street Talk · [All reviews](../README.md) · [Learning path](../learning-path.md)

Published: 2021-01-10 · Decision: **Selected passages** · Confidence: High. The underlying concepts are fundamental, but this introductory conversation contains enough overstatement that I plan to watch selectively.

## Central claim

Intelligent learning combines prior structure, evidence, uncertainty, and decisions about what to observe next. The episode gives tangible examples of that loop, especially partial pooling and coordinate-dependent priors, but its Bayesian-versus-frequentist rhetoric should not be mistaken for a mathematical result.

## Ideas I want to keep

- The eight-schools example turns transfer into a precise hierarchy: individual populations differ, yet share a distribution. Partial pooling lies between declaring all groups identical and estimating each independently, with uncertainty about both within-group sampling and between-group variation.

- The cube-factory example makes a subtle point intuitive: uniform length and uniform volume define different sampling processes. An apparently uninformative prior depends on coordinates, so prior design must expose the measurement/generative assumptions rather than hide them behind the word uniform.

- The fair-coin discussion separates parameter estimation from comparing a point-null model with a continuous alternative. Marginal likelihood integrates over a model’s parameter uncertainty; it is not just the best fitting likelihood or the posterior density at a single parameter value.

- Gaussian-process uncertainty creates an observation-action loop: data constrain an interpolating distribution and a decision criterion chooses the next expensive measurement. The distinction between computational cost per inference and sample cost per experiment is valuable.

- MCMC discussion acknowledges a limitation often omitted in ideal Bayesian accounts: knowing an unnormalized density is not equivalent to exploring it faithfully. A chain can miss distant modes despite apparently reasonable local behavior.

## Mathematical anatomy

**Objects:** Latent parameters theta, a likelihood p(D|theta), a proper or explicitly justified prior, hyperparameters controlling population variation, and a decision loss.

**Objective:** Posterior updating p(theta|D) proportional to p(D|theta)p(theta) is a coherence rule conditional on the model; a Bayes action additionally minimizes posterior expected loss. Model choice requires prior probabilities on models as well as marginal likelihoods.

**Mechanism:** For H heads and T tails, a Beta(a,b) prior yields Beta(a+H,b+T) and predictive head probability (a+H)/(a+b+H+T). A point hypothesis theta=1/2 needs explicit prior mass if it is to have nonzero posterior probability. In a normal hierarchy, shrinkage strength depends on group sample uncertainty relative to between-group variance.

**Assumptions:** Exchangeability and the chosen likelihood justify sharing information. GP covariance assumptions determine which observations inform each other. Bayesian optimization needs an acquisition objective trading improvement against exploration; maximum uncertainty alone is not generally the optimizer.

**Limits:** A posterior summarizes information only relative to its specified model, not every fact known about reality. Improper priors cannot be used naively for Bayes factors because arbitrary normalizing constants do not cancel across models. Weak priors are not universally equivalent to one observation, especially in high dimensions or model selection.

## Evidence, limitations and corrections

- At 00:21:18–00:26:18 the hierarchy and small-school extremes provide the most concrete modeling example. The guest correctly acknowledges that frequentist mixed-effects methods can also address this; the surrounding claim that they are philosophically incoherent is advocacy.

- At 00:33:45–00:43:46 the coin examples are useful but posterior model odds need model prior odds, and a marginal likelihood alone is not the probability of a model. The discussion understates prior sensitivity.

- At 00:55:17–01:02:27 coordinate dependence and numerical tractability expose real choices. A broad normal still has infinite support; it does not literally change the mathematical integration domain into a bounded interval.

- At 01:03:11–01:07:00 sampler exploration is explained candidly, though a Hamiltonian uses negative log target density plus kinetic energy rather than simply being the unnormalized density itself.

- The opening claim that only Bayesian approaches have a firm mathematical basis is false as a general characterization. Frequentist confidence coverage concerns repeated data conditional on a fixed parameter, not universes with different Saturn masses. Historical anecdotes, neutrino details, and Benford fraud claims were not independently verified and should not be learned from this discussion as established evidence.

## Relevance to my research

My interest is in the models and experiments rather than the tribal framing. Given my mathematical background, the marginal value lies in a few sharply visualizable problems: how transfer depends on an exchangeability assumption, why ignorance is coordinate-dependent, and how posterior uncertainty becomes a policy for acquiring evidence. The introductory probability material is unlikely to add much.

## My viewing plan

**Mode:** Selected passages.

**Segments:** - **Start:** 00:21:18
  
  **End:** 00:26:18
  
  **Purpose:** Partial pooling and heterogeneity.

- **Start:** 00:33:45
  
  **End:** 00:43:46
  
  **Purpose:** Optional coin-model comparison; I would supply the missing model prior odds.

- **Start:** 00:55:17
  
  **End:** 01:07:00
  
  **Purpose:** Coordinate dependence, computational priors, and MCMC limits.

- **Start:** 01:18:32
  
  **End:** 01:28:08
  
  **Purpose:** Observation cost versus computation and surrogate-guided search.

**Edition:** Saved transcript ends 01:35:23; no audio verification. Many technical terms are mistranscribed.

## Objections and open questions

Bayesian coherence does not rescue a wrong likelihood, missing hypothesis, weak identification, or failed sampler. Frequentist calibration can be valuable even for Bayesian procedures. Conversely, these limitations do not diminish the usefulness of hierarchical generative modeling or explicitly propagating parameter uncertainty. The inference philosophy and the empirical adequacy of a model should be evaluated separately.

## An experiment I could try

I would derive the Bayes factor for a fair coin against a Beta(a,b) alternative and plot posterior model probability under three choices of prior model odds and three concentration values. A simulation of heterogeneous schools with unequal sample sizes would compare complete pooling, no pooling and partial pooling on new-school prediction. Transforming a uniform cube-side distribution into a volume density using the Jacobian would clarify why a uniform volume prior is a different experiment.

## Connections in my notes

- Michael Jordan: decision contexts and error guarantees should accompany probabilistic predictions.

- Thomas Ahle: tractable sampling is a separate computational problem from specifying a target distribution.

- Max Welling is explicitly referenced for inductive assumptions and probabilistic representations of irregularly sampled observations.

## Source and coverage

**Read:** Entire available transcript, sequentially; not audio verified.

**Last timestamp:** 01:35:23

**Source caveats:** ASR/publisher transcript may contain wording and mathematical transcription errors; timestamps refer to this saved edition.

Source type: Existing caption or archive. Reviewed text: 16,783 words.

Transcript file: `RQ31MHw84o0.hf.txt` (not distributed).

SHA-256: `c0ba6d0f5fb0c1609fd01235aa5b845c5c30daaff979ba3152e0c1f2db6be8bb`.

[Structured review](RQ31MHw84o0.json) · [Source ledger](../sources.json)
