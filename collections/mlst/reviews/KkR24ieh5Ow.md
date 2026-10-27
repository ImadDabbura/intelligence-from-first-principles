# #033 Karl Friston - The Free Energy Principle

[Original episode](https://www.youtube.com/watch?v=KkR24ieh5Ow) · Source: Machine Learning Street Talk · [All reviews](../README.md) · [Learning path](../learning-path.md)

Published: 2020-12-13 · Decision: **Worthwhile** · Confidence: high

## Central claim

The productive idea is to treat perception, learning and action selection as inference at different timescales, including the value of information. The episode is valuable as a conceptual research program, but several transitions from variational identities to universal claims about physics, control and intelligence are overstated.

## Ideas I want to keep

- Prediction has distinct meanings: explaining current sensory inputs, filtering changing hidden states, and evaluating action-conditioned future trajectories. Planning adds actions and future observations to the inference problem rather than merely extending a next-frame predictor.

- Epistemic value can concern either hidden states or model parameters. Looking again at an ambiguous object reduces state uncertainty; seeking novel experiences can improve knowledge of transition or likelihood parameters.

- Variational evidence decomposes into fit and complexity relative to a prior. This connects perceptual inference to compression and model selection without making likelihood alone the whole objective.

- Fast deliberative inference can train an amortized response mapping. The proposed cortex/cerebellum account illustrates how a system can retain a sophisticated learning history while executing cheap habitual actions.

- The conversation explicitly separates state inference, parameter learning, hyperparameter or precision learning, structural learning and evolutionary change. These distinctions are more informative than the slogan that everything minimizes one quantity.

- Friston admits that the presented framework presupposes a suitable steady-state system and does not explain abiogenesis. He also identifies changing system boundaries as an unresolved mathematical issue.

## Mathematical anatomy

**Objects:** A generative model p(o,s), approximate beliefs q(s), action policies pi, expected future observations, prior preferences, and a partition into internal, blanket and external variables.

**Assumptions:** The Bayesian identities require normalized distributions and a specified generative model. A Markov blanket is a conditional-independence property, not merely a spatial boundary or absence of direct coupling. The physical interpretation adds dynamical and steady-state assumptions beyond the identity.

**Objective:** For observed o, F[q]=E_q[log q(s)-log p(o,s)]=KL(q||p(s|o))-log p(o). Equivalently F=KL(q||p(s))-E_q log p(o|s). Expected free energy for policies is a further construction involving predicted outcomes and preferences.

**Mechanism:** Belief updates reduce a variational bound; policy evaluation can trade preferred outcomes against expected information gain. Repeated inference may be compiled into faster mappings, while structural hypotheses can be compared using evidence approximations.

**Limits:** The entropy term does not mean more uncertainty is always better: the energy and prior terms constrain it. Approximation error can affect model comparison. No equation here proves that a biological system explicitly represents a Bayesian posterior or that its physical trajectory implements the proposed inference algorithm.

## Evidence, limitations and corrections

- The saved edition contains a long edited summary before the main interview begins around 36:01; the full source was read, but watching both duplicates substantial material.

- At 58:00–64:04 and 75:04–76:01, contrasts with Bellman optimality are too strong. Standard dynamic programming can operate on belief states in a partially observed model, and beliefs about other agents can be included in state. The kidnapping example does not invalidate Bellman reasoning.

- At 65:02–74:02 exact versus changing blankets is presented as an open problem. The physical derivation is asserted conversationally, not demonstrated; the conditional independence alone does not establish all downstream claims.

- At 01:21:01–01:23:02 the assertion of an exact one-to-one mapping from posterior/prior KL to joules used by a computer is stronger than warranted. Actual dissipation depends on physical implementation and protocol; two implementations of the same inference can consume different energy. An information-theoretic quantity is not a hardware electricity meter.

- The opening quantum path-integral analogy conflates summing complex amplitudes with ordinary probabilistic marginalization. It does not show that a surviving system must explicitly model quantum alternatives.

- At 01:47:02–01:49:05 Friston explicitly limits the account: origins of the steady-state systems are outside the stated formulation. The alpha discussion at 01:23:02–01:28:03 also acknowledges unresolved choices in generalizing the objective.

## Relevance to my research

Worth studying for my research as a unifying lens, particularly for active sensing, inference at multiple timescales and amortization. My central question is which parts are mathematical identities, which are engineering design choices, and which are empirical or physical hypotheses. That separation is essential before using the framework as a theory of intelligence.

## My viewing plan

**Mode:** chapters

**Segments:** - **Start:** 00:40:05
  
  **End:** 00:57:00
  
  **Purpose:** Prediction, action-conditioned inference and epistemic value.

- **Start:** 01:05:02
  
  **End:** 01:14:02
  
  **Purpose:** Assumptions and unresolved system-boundary questions.

- **Start:** 01:29:02
  
  **End:** 01:44:06
  
  **Purpose:** Inference, learning, structural adaptation and amortization.

- **Start:** 01:47:02
  
  **End:** 01:49:05
  
  **Purpose:** Explicit scope limit concerning the origin of life.

**Edition note:** Timestamps belong to the saved long edition with approximately 34 minutes of recap before the interview. Several positions in the prose are minute:second anchors, and no audio alignment is claimed.

## Objections and open questions

- A general principle that can retrospectively accommodate many systems may impose few discriminating predictions without a specified model, approximation and experimental test.

- Preference distributions encode what is desirable; expressing reward and information in nats does not eliminate the substantive choice of preferences, scales, planning horizon or computational budget.

## An experiment I could try

My proposed test is a two-location hidden-target POMDP with a costly observation action, solved using both exact belief-state dynamic programming and a declared expected-free-energy policy objective. Varying observation cost, preference precision and horizon would reveal when the policies agree and when intrinsic information value leads to different behavior. A separate derivation and numerical check of the variational identity would clarify why increasing q entropy without respecting the likelihood can increase rather than decrease F.

## Connections in my notes

- Friston Part 2 is useful for further examination of exact blankets, multiple timescales and the unresolved generation of new hypotheses.

- Connects to Schmidhuber’s compression-progress curiosity but uses different objectives and assumptions.

- Connects to DreamCoder through amortizing expensive inference and to Molnar through separating model-level descriptions from claims about the world.

## Source and coverage

**Status:** complete_available_text

**Method:** Read entire saved transcript; any truncated tool section reread in bounded chunks. Audio not checked.

**Last timestamp:** 01:51:20

**Caveats:** - ASR transcription can corrupt names and mathematical terminology; transcript completeness is not an audio audit.

Source type: Existing caption or archive. Reviewed text: 17,482 words.

Transcript file: `KkR24ieh5Ow.hf.txt` (not distributed).

SHA-256: `6a787a4c3cb1e7e5ffd46c527601442ff261fd174199a264b775eb834f684fca`.

[Structured review](KkR24ieh5Ow.json) · [Source ledger](../sources.json)
