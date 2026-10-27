# NEURAL NETWORKS ARE WEIRD! - Neel Nanda (DeepMind)

[Original episode](https://www.youtube.com/watch?v=YpFaPKOeNME) · Source: Machine Learning Street Talk · [All reviews](../README.md) · [Learning path](../learning-path.md)

Published: 2024-12-07 · Decision: **Core** · Confidence: High for first-principles value; empirical findings are scoped to the particular models and experiments discussed.

## Central claim

This is a detailed lesson in how to infer computational structure from a learned system without confusing readable correlations, causal influence, and a complete mechanism. Sparse autoencoders are treated as fallible instruments whose own inductive biases must be studied.

## Ideas I want to keep

- The central decomposition is variables versus computation: activations may encode features, while circuits describe how inputs and intermediate variables produce later ones. A dictionary of interpretable latents is not yet an algorithm, and a local explanation need not generalize across all inputs.

- Superposition separates three hypotheses: more represented concepts than activation dimensions, more computed features than neurons, and overlapping circuits in weights. Sparse co-occurrence can make interference tolerable; distributed coding is not automatically evidence of defective or meaningless representation.

- Activation patching turns interpretation into intervention. Matched contrast prompts isolate a particular distinction; replacing a node with its counterpart tests causal contribution relative to that contrast. Noising and denoising ask different necessity-like and sufficiency-like questions, and patching later nodes can bypass earlier causal steps.

- An SAE jointly learns a dictionary and an approximate sparse inference procedure. Reconstruction plus sparsity can reveal meaningful directions without semantic labels, but neither term directly optimizes interpretability. Width, sparsity, sampling, and reconstruction error are part of the measurement instrument.

- The architecture discussion makes optimization bias concrete: L1 shrinks useful activation magnitudes; JumpReLU separates detection threshold from retained magnitude; TopK controls active counts, while batch TopK permits token-dependent counts at a fixed batch average. Better reconstruction need not mean better semantic recovery.

- Feature splitting and meta-SAEs undermine the assumption of one privileged inventory of atomic concepts. A wider dictionary can split a broad feature, while its fine-grained vectors can themselves decompose into broader properties. Causally meaningful descriptions can exist at several levels.

- The Othello example shows why my choice of ontology can hide a simple mechanism: a board representation looks nonlinear in black/white coordinates but becomes linearly decodable in current-player/opponent coordinates. Choosing the right semantic frame is part of scientific discovery.

## Mathematical anatomy

**Objects:** Activation x, sparse coefficients z, learned decoder dictionary D, reconstruction x_hat=Dz+b, error e=x-x_hat, and an output metric m. Interventions are defined at a specified layer, input distribution, and baseline.

**Assumptions:** Useful internal concepts are sufficiently sparse and approximately linearly represented; relevant dictionary directions can be recovered from the activation distribution. These are hypotheses, not universal properties of cognition.

**Objective:** A basic SAE minimizes expected squared reconstruction error plus lambda times L1(z). Alternatives constrain active count or approximate L0. Circuit analysis must additionally test effects on downstream behavior rather than only activation reconstruction.

**Mechanism:** Sparse uniqueness can hold even for an overcomplete dictionary: a sufficient idealized condition is spark(D)>2k for k-sparse codes. This does not guarantee the learned SAE discovers the true dictionary. Attribution patching approximates an intervention effect by gradient dot activation change; exact patching tests the approximation.

**Limits:** Error terms can contain important missing features. Intervening on x_hat alone changes many things; adding e back isolates a latent edit more cleanly but leaves an uninterpreted causal channel. Transcoders replace an MLP input-output map with a sparse surrogate, introducing another approximation. Attention is linear in values only conditional on its attention pattern.

## Evidence, limitations and corrections

- At 00:46–00:49 Nanda explicitly separates full weight-level reverse engineering, distribution-specific causal circuit analysis, and SAE variable discovery. No complete source-code reconstruction of frontier language models is established.

- At 01:17–01:24 the baseline problem is central: zeroing a component can destroy an ordinary embedding contribution rather than isolate the desired mechanism. Patch effects are conditional on the paired inputs and intervention, not unconditional proof of necessity or sufficiency.

- At 01:59–02:05 he advocates testing across activation strengths, checking counterexamples, and measuring when a concept is present but the latent fails to fire. Top-activating examples alone can create an interpretability illusion.

- At 02:38–02:43 reconstruction errors accumulate across layers and can dominate circuit results. A sparse visible graph that omits those errors is not a faithful full model explanation.

- At 02:48–02:54 he rejects confidence in a fixed atomic feature list. At 03:22 he warns that sudden SAE feature appearance can reflect the detector crossing a salience threshold while the underlying model learned gradually.

- Multilingual or multimodal activation and steering are evidence against a literal keyword-only account, but neither proves general reasoning or human-like understanding. A power-seeking concept used to model fictional characters is not evidence that the model itself is pursuing power.

- Fine-tuning as mostly reweighting existing circuits, entity-recognition explanations of hallucination, and the proposed city-X mechanism have different epistemic status here. Nanda marks several as hypotheses or unpublished work; these cannot all be treated as established results.

## Relevance to my research

Core even beyond language models. It teaches identifiability, sparse coding, causal experimentation, multiscale explanation, measurement bias, and the difference between function approximation and mechanism discovery. Its repeated uncertainty is productive: it shows how to build intuition that survives attempts to falsify it.

## My viewing plan

**Mode:** full or substantial chapters

**Segments:** - **Start:** 00:37:00
  
  **End:** 01:15:03
  
  **Purpose:** Variables, circuits, superposition, universality, and knowing versus hallucinating.

- **Start:** 01:17:07
  
  **End:** 01:24:01
  
  **Purpose:** Causal patching and its assumptions.

- **Start:** 01:37:01
  
  **End:** 02:06:03
  
  **Purpose:** Linear representations, sparse recovery, and testing semantic interpretations.

- **Start:** 02:22:05
  
  **End:** 03:04:03
  
  **Purpose:** SAE objectives, feature granularity, errors, transcoders, and attention.

- **Start:** 03:11:00
  
  **End:** 03:23:01
  
  **Purpose:** Useful interventions versus atomic truth and measuring training dynamics.

**Edition note:** Entire saved transcript read through 03:42:08, including outdoor introduction and indoor technical conversation. The early sections partly repeat the longer interview; no audio or visual validation was performed.

## Objections and open questions

- Sparse recovery is not semantic identification: multiple dictionaries can reconstruct similar data, and correlated concepts can split or merge. Causal edits can still be useful without a unique true factorization.

- Model-internal causality is not causality in the external world. A faithful explanation of why a predictor says something does not establish that its claim is true.

- A tiny task with a fully decoded algorithm is a valuable existence proof, not evidence that all large-model computations share that simplicity. Practical safety claims need operational evaluations beyond attractive circuit diagrams.

## An experiment I could try

I would choose a small model and one factual or syntactic contrast, then compare zero ablation, mean ablation, matched activation patching and gradient attribution. Inspecting one relevant SAE at two widths, while preserving reconstruction error during single-latent edits, would probe granularity effects. Held-out paraphrases, negative controls, missed activations and off-target effects would test the explanation. Dictionary reconstruction, behavioral recovery, explanation precision/recall and stability across random seeds would be reported separately.

## Connections in my notes

- Molnar: explanation depends on the precise estimand and intervention distribution.

- Hawkins: sparse codes and hypothesis unions emphasize different representational constraints from SAE factorization.

- Stanley: readable factorization and useful modification must be tested rather than inferred from visually pleasing units.

- Apollo: behavioral deception evidence and mechanism evidence complement each other; a model’s stated rationale is not a causal trace.

## Source and coverage

**Status:** complete_available_text

**Method:** Read entire saved transcript; any truncated tool section reread in bounded chunks. Audio not checked.

**Last timestamp:** 03:42:27

**Caveats:** - ASR transcription can corrupt names and mathematical terminology; transcript completeness is not an audio audit.

Source type: Publisher transcript. Reviewed text: 41,439 words.

Transcript file: `YpFaPKOeNME.publisher.txt` (not distributed).

SHA-256: `af23f9ca9cbf55756fada0760a35c5ae5e3e46433107631d02b5d28b5149359c`.

[Structured review](YpFaPKOeNME.json) · [Source ledger](../sources.json)
