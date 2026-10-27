# Why LeCun Thinks Deep Learning Isn't Enough — Yann LeCun

[Original episode](https://www.youtube.com/watch?v=86ib0sfdFtw) · [All reviews](../README.md) · [Learning path](../learning-path.md)

Published: 2022-01-04 · Decision: **Core** · Confidence: High for the guests’ methodological distinctions; several introductory conclusions require correction.

## Central claim

The valuable core is a separation of geometry, generalization, and computation: being outside a training convex hull says little about predictive success, piecewise-affine structure gives a useful analytic lens, and learned models can support iterative inference rather than one forward pass.

## Ideas I want to keep

- LeCun rejects the inference that convex-hull extrapolation proves reasoning. The geometric label can change with representation, sample size, and dimension while the task stays the same; an informative generalization measure must connect to prediction and the task distribution.

- Balestriero separates statistical, approximation, and computational curses. Enough data, enough representational capacity, and feasible optimization are distinct requirements; satisfying one does not automatically satisfy the others.

- For affine-plus-ReLU networks, fixing an activation pattern gives f(x)=A_r x+b_r on a polyhedral region. Training simultaneously changes region boundaries and local maps. Parameter sharing links how nearby regions are divided, unlike independently grown decision-tree branches.

- Supervised task fitting, self-supervised representation learning, architecture, and inference procedure are separate choices. LeCun argues for reusable pretraining and joint embeddings that predict relevant representations rather than every uncertain future pixel.

- Reasoning as energy minimization distinguishes learning model parameters from optimizing latent states or actions at inference. A differentiable dynamics model can be rolled out, scored, and searched; a policy can later amortize expensive planning into rapid behavior.

- Tangent propagation makes an invariance prior operational: penalize the directional derivative of the predictor along known nuisance transformations. This exposes how augmentation, architecture, and regularization encode assumptions rather than making generalization assumption-free.

## Mathematical anatomy

**Objects:** Training set D, hull conv(D), representation phi, region-indexed affine maps, an energy E_theta(x,z), and a dynamics model s_next=f_theta(s,a).

**Assumptions:** Convex-hull results require a data/sampling geometry; low intrinsic dimension and low affine-span dimension differ. Piecewise-affine analysis assumes the corresponding operations, not arbitrary neural architectures. Predictive control requires a model accurate enough along candidate trajectories.

**Objective:** Fit parameters theta from experience, then infer z or an action sequence minimizing an energy or cumulative cost. A model can share these components while using discrete search, continuous optimization, or both.

**Mechanism:** For a fixed ReLU mask, products of weight and diagonal activation matrices give A_r. Changing masks changes the map continuously across shared boundaries. In control, backpropagation through a rollout yields action gradients; later policy learning amortizes that optimization.

**Limits:** A differentiable formulation does not guarantee global optimization, correct long-horizon predictions, calibrated uncertainty, or algorithmic length generalization. A compact local affine description does not imply the complete network is globally linear or a mere lookup table.

## Evidence, limitations and corrections

- At 01:03–01:06 LeCun explicitly says extrapolation is not evidence of reasoning and objects to conflating supervised-learning limits with deep-learning limits. At 01:29 he corrects the host claim that he denied neural reasoning.

- At 02:12–02:14 Balestriero explicitly says the convex-hull result does not invalidate the manifold hypothesis. This contradicts the stronger impression created by the hour-long introduction.

- The introduction repeatedly says there is no continuous morphing. ReLU networks are continuous piecewise-affine maps: derivative discontinuities do not make outputs discontinuous. Multiple local affine formulas do not imply unrelated latent coordinate systems.

- The claim that any continuous function produces a manifold is false, and the intermediate-value principle is confused with the mean-value theorem. Non-smooth representation is also not an argument that a network cannot approximate a smooth physical relation.

- Universal high-dimensional impossibility and fixed 16–20 dimension thresholds are overstatements without specifying function class, distributions, accuracy, and sample size. Structured high-dimensional linear or compositional problems can be learnable; the curse applies to particular broad classes.

- The discussion of variable computation rightly separates variable runtime from symbolic representation. Unrolling a recurrent process is possible, but differentiating a fixed executed trace does not solve arbitrary discrete halting or global program search.

- At 02:37–02:44 Balestriero corrects the proposed MNIST-versus-ImageNet hardness inference: identical patch dimensions cover very different fractions of differently sized images. That plot alone does not rank task difficulty.

## Relevance to my research

Core because the guests expose category errors that repeatedly contaminate debates about intelligence. I gain a precise decomposition into inductive assumptions, geometry, approximation, optimization, inference, and amortization. It also provides a constructive counterweight to the strongest interpolation-only claims in the Chollet discussions.

## My viewing plan

**Mode:** I will focus on these chapters.

**Segments:** - **Start:** 00:58:04
  
  **End:** 01:25:04
  
  **Purpose:** Why the dichotomy is weak, task supervision versus architecture, and joint embeddings.

- **Start:** 01:27:01
  
  **End:** 01:49:00
  
  **Purpose:** Tangent propagation, inference-time optimization, model-based control, and amortization.

- **Start:** 02:04:00
  
  **End:** 02:34:02
  
  **Purpose:** What makes learning work, manifold qualification, spline structure, and shared partitions.

- **Start:** 02:36:00
  
  **End:** 02:45:00
  
  **Purpose:** Careful reading of dimensionality experiments.

**Edition note:** Times are observed in the saved transcript, not validated playback timestamps. Publisher/RSS chapter anchors disagree. The introductory interpretation contains errors; I will prioritize the actual guest exchanges.

## Objections and open questions

- Replacing interpolation with extrapolation can become a semantic victory unless linked to a falsifiable capability claim. The speakers largely recognize this.

- Energy minimization is a broad common language, not by itself an explanation of efficient reasoning. The search geometry, constraints, and inductive priors still determine which problems are tractable.

- Predicting compressed representations avoids nuisance detail but can discard information needed for a future task. Non-collapse constraints and relevance must be investigated, not assumed.

## An experiment I could try

I want to sample points on a circle and predict a simple known label, measuring convex-hull membership, nearest-neighbor distance and predictive error separately. An invertible linear map followed by a nonlinear embedding would reveal which metrics change. A small ReLU model would provide a second test: enumerating activation regions along a path should verify continuity despite changing affine maps. Finally, I would optimize an action sequence through learned toy dynamics and compare it with an amortized policy under model error.

## Connections in my notes

- Chollet: test acquisition efficiency directly rather than equating geometric extrapolation with intelligence.

- Bonnet latent programs: inference-time search is distinct from training parameters.

- Stanley: identical outputs can hide different local modification geometry.

- Caron SWaV and Yi Ma: representation objectives impose different invariances and structural assumptions.

## Primary sources checked

- **Url:** https://arxiv.org/abs/2110.09485
  
  **Claim:** Primary abstract defines the convex-hull convention and questions its relation to generalization.

- **Url:** https://proceedings.mlr.press/v80/balestriero18b/balestriero18b.pdf
  
  **Claim:** Primary spline formulation: learned parameters alter the partition as well as per-region affine maps.

## Source and coverage

**Status:** complete_available_text

**Method:** Read all eight contiguous chunks of saved HF transcript, including introduction, both interviews, and debrief. Audio not checked.

**Last timestamp:** 03:19:04

**Caveats:** - ASR names and technical terms can be corrupted.

- Saved transcript anchors differ from current description and RSS chapter lists: LeCun discussion begins around 00:58, Balestriero around 01:50. I’ll use transcript search because the current publisher chapters may not align.

Source type: Existing caption or archive. Reviewed text: 32,972 words.

Transcript file: `86ib0sfdFtw.hf.txt` (not distributed).

SHA-256: `20787c01778da02268cfbf02959a1c9866d34e516486d016b4465da5d4e739fd`.

[Structured review](86ib0sfdFtw.json) · [Source ledger](../sources.json)
