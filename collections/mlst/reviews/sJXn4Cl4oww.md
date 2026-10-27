# This is why Deep Learning is really weird.

[Original episode](https://www.youtube.com/watch?v=sJXn4Cl4oww) · [All reviews](../README.md) · [Learning path](../learning-path.md)

Published: 2023-12-26 · Decision: **Worthwhile** · Confidence: high for conceptual organization and research methodology; moderate for some informal explanations

## Central claim

A useful map of what needs explaining in deep learning: representing a function, finding it efficiently, and generalizing are three different achievements. The most valuable material joins geometric intuition to experimental discipline, while several broad claims about interpolation and cognition require resistance.

## Ideas I want to keep

- At 32:20–43:41, the piecewise-affine view makes the model’s degrees of freedom tangible. A ReLU network partitions input space into activation regions, with a different affine map in each. Its many regions are coupled by shared parameters, so this is not a lookup table with independently adjustable buckets. The contrast between immense ambient space, limited observations and successful fitting motivates asking what data, architecture and optimizer each contribute.

- At 45:10–55:32, architecture and augmentation are two ways of supplying transformation knowledge. Invariance and equivariance require different output behavior. Depth can be viewed as composing, folding and replicating functions or constructing more complex basis functions. These are useful partial views, and Prince explicitly rejects the idea that one simple picture fully captures even a small multilayer network.

- At 57:47–59:06, a high-activation exemplar does not characterize an entire unit’s response. A Gabor-like maximizing stimulus cannot establish that the unit exclusively implements that concept, especially after nonlinear composition. This is a compact but important interpretability lesson about mistaking a selected point for a high-dimensional response function.

- At 01:04:00–01:12:43, random-label fitting separates optimization capacity from meaningful statistical learning, while initialization and grokking expose sensitivity to training dynamics. Parameter count versus sample count is also complicated by dependent augmented examples and nonzero language-model training loss. These observations demand a more precise definition of effective capacity than simply counting weights.

- At 01:13:45–01:32:24, MNIST-1D offers a concrete experimental strategy: use small procedurally generated data with controlled transformations and noise to investigate double descent, adversarial examples and lottery tickets. The discussion of SGD and batch normalization reinforces that a method can work while its original explanation is wrong; causal interpretation requires competing mechanisms and matched baselines, beyond a leaderboard improvement.

## Mathematical anatomy

**Objects:** Input-space activation regions, parameter-space loss surfaces, training/test distributions, augmentation transformations, network depth/width, initialization scale and stochastic update trajectories. Input geometry and parameter geometry must remain separate.

**Objective:** Empirical loss minimization explains fitting; population risk and distributional behavior define generalization. Universal approximation concerns existence of approximants, not efficient optimization or sample complexity. A trainable scientific theory would predict all three under explicit assumptions.

**Mechanism:** For a fixed ReLU activation pattern, f(x)=A_r x+b_r. Composition creates new regions and shares structure across them. Equivariance requires f(Tx)=T′f(x); invariance takes T′ as the identity. SGD alters both computational cost and solution bias, while normalization changes optimization dynamics and may couple examples through batch statistics.

**Assumptions:** The exact affine-region description applies to suitable piecewise-linear architectures, not arbitrary softmax-attention or smooth-activation networks. Augmentations must preserve the intended label relationship. Small experimental systems must retain the mechanism under investigation before their findings are extrapolated.

**Limits:** Region counts bound a kind of representational richness; they do not independently measure effective statistical complexity. Low empirical error does not guarantee good interpolation, and smoothness must be defined in the relevant geometry. A compact generative program can describe a high-dimensional distribution, so small model size alone does not prove a low-dimensional natural-image manifold.

## Evidence, limitations and corrections

- The host’s claim that high dimension leaves no statistical information is too strong: sample complexity depends on structure, hypothesis class and target distribution, not on filling ambient volume. A shallow network is not memorization by definition. Standard approximation statements generally concern an appropriate function class/domain and, for each tolerance, a sufficiently large finite network; they do not require one literally infinite network.

- The discussion often moves from small weights to smooth functions and from flat minima to generalization. These are heuristics, not coordinate-invariant explanations: ReLU rescalings can change parameter norms and sharpness without changing the represented function. Dinh and colleagues provide a primary counterexample to naive sharpness reasoning.

- Grokking as entry into a favorable norm range is one account, not the full mechanism or a universal law. Nanda’s modular-addition analysis supplies stronger circuit evidence than the smooth-interpolation story here. The host’s horizontal convergence-time gap is not the usual train/test generalization gap.

- The useful skepticism about batch normalization should not obscure its definition: it normalizes activations, not simply resets gradients, and the original internal-covariate-shift story concerns changing distributions received by layers as earlier parameters change. SGD can influence escape and exploration in some settings even though escaping bad local minima is not a sufficient universal explanation of its success.

- The early claim that there is no deeper understanding beyond an equation is philosophical, not established by the mathematical account. Mechanistic explanations can exist at higher levels of a known computation. Later claims about memory, agency, labor displacement and governance are discussion/opinion rather than evidence for the geometry of learning.

## Relevance to my research

Substantial for my research as an organizing and hypothesis-testing episode, especially the challenge to explain generalization rather than only fit. It is less precise than the strongest dedicated mechanism episodes; I would use it to formulate a research agenda and expose assumptions rather than settle why intelligence emerges.

## My viewing plan

**Mode:** chapters

**Ranges:** - **Start:** 00:31:28
  
  **End:** 00:55:32
  
  **Why:** Expressivity, ambient geometry, priors, augmentation and depth; I would keep the stated caveats beside the intuitive pictures.

- **Start:** 00:57:47
  
  **End:** 00:59:06
  
  **Why:** Why activation exemplars are incomplete explanations.

- **Start:** 01:04:00
  
  **End:** 01:12:43
  
  **Why:** Trainability versus generalization, initialization and a provisional grokking account.

- **Start:** 01:13:45
  
  **End:** 01:32:24
  
  **Why:** High-dimensional intuition, MNIST-1D and experiments that distinguish a successful method from its rationale.

**Edition note:** Ranges are observed in the local-ASR edition ending 02:06:36. The first half-hour and final ethics/agency segment are optional for my mathematical learning objective; book visuals may substantially help the geometry passages.

**Intention:** I plan to watch the mathematical and experimental chapters, using the book visuals where they help.

## Objections and open questions

The recurring “we do not understand” framing can understate genuine but conditional theory; conversely, a local theorem need not explain practical networks. The productive position is to specify what a theory predicts, what assumptions it uses, and where it fails. Small datasets are excellent for controlled mechanisms but cannot establish that all scale-dependent phenomena are captured.

## An experiment I could try

I want to use procedural MNIST-1D to vary translation range, noise, sample count, label corruption, width and initialization scale. An MLP and a convolutional model would be compared with matched parameter/compute budgets, recording training loss, test error and transformation consistency separately. Rescaling a two-layer ReLU network as W1→cW1 and W2→W2/c would leave predictions fixed while changing naive parameter sharpness. This would test explanations that depend only on raw weight size or coordinate-dependent flatness.

## Connections in my notes

- Balestriero: more focused geometric account; Prince supplies an accessible map and methodological critique.

- Nanda: stronger mechanistic grokking explanation and shared caution about selective activation examples.

- Ilyas: explicitly intervening on data complements Prince’s architecture/optimizer/data decomposition.

- Wyart: a particular hierarchical-data model can answer narrower learnability questions more concretely than a general appeal to the manifold hypothesis.

## Primary sources checked

- **Title:** Understanding Deep Learning — author’s book site
  
  **Url:** https://udlbook.github.io/udlbook/
  
  **Use:** Primary resource for the diagrams and conceptual chapters discussed.

- **Title:** Scaling Down Deep Learning with MNIST-1D
  
  **Url:** https://proceedings.mlr.press/v235/greydanus24a.html
  
  **Use:** Primary small-scale experimental testbed.

- **Title:** Sharp Minima Can Generalize For Deep Nets
  
  **Url:** https://arxiv.org/abs/1703.04933
  
  **Use:** Primary correction to parameterization-dependent flatness explanations.

## Source and coverage

**Status:** complete_available_text

**Start:** 00:00:00

**End:** 02:06:36

**Caveats:** - Read all 22,033 words of local-ASR transcript, not audio. Technical visuals from the book are described but not supplied in this transcript. ASR occasionally corrupts names and terms. Opening narration summarizes the book with stronger wording than the later discussion; historical capability and employment claims are not current assessments.

Source type: Local asr. Reviewed text: 20,582 words.

Transcript file: `sJXn4Cl4oww.local-asr.txt` (not distributed).

SHA-256: `88660e8835d8dfd725ed381357baf4910317d7e67040be75e90ab9b1314cba39`.

[Structured review](sJXn4Cl4oww.json) · [Source ledger](../sources.json)
