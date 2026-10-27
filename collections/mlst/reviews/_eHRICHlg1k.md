# #52 - Dr. HADI SALMAN - Adversarial Examples Beyond Security [MIT]

[Original episode](https://www.youtube.com/watch?v=_eHRICHlg1k) · Source: Machine Learning Street Talk · [All reviews](../README.md) · [Learning path](../learning-path.md)

Published: 2021-04-30 · Decision: **Core** · Confidence: High conceptual relevance; empirical results interpreted within the experiments described.

## Central claim

Robustness changes which predictive information a learner uses, and can therefore change transfer even when source accuracy decreases. The deeper lesson is that intelligence is a relation among a representation, a task, an admissible transformation set, and sometimes an environment I can redesign.

## Ideas I want to keep

- Non-robust features may be genuinely predictive on fresh IID data. The relabeled adversarial-image experiment separates statistical generalization from the human-visible reason for a label: a dog-looking training image can carry predictive cat information for a model.

- Adversarial training acts as an inductive bias on representation, not only as a defense. The reported transfer experiments decouple source accuracy from downstream usefulness; at a fixed robustness level, greater source accuracy can still help, while changing robustness shifts the relationship.

- The hosts challenge whether the selected downstream tasks already privilege human-recognizable features. This turns a claim of generally better representations into the sharper question: better for which family of tasks and shifts? Salman repeatedly acknowledges that the proposed mechanism was not established.

- Certification requires a different quantifier from attack testing. Layerwise convex relaxations can remain loose even when solved optimally, distinguishing optimization failure from limitations of the chosen mathematical relaxation.

- Unadversarial objects reverse the usual intervention: optimize visible textures or patches for a fixed classifier. Intelligence need not reside entirely in model weights; a jointly designed environment can reduce perceptual difficulty, provided the deployment actually permits controlling the objects.

## Mathematical anatomy

**Objects:** A labeled distribution P(x,y), classifier f_theta, perturbation set Delta(x), representations used for transfer, noise-smoothed classifiers, and controllable object or texture parameters phi.

**Objective:** Adversarial training approximately minimizes E_P max_delta_in_Delta loss(f_theta(x+delta),y). Object design instead minimizes over phi an expected correct-label loss across views and placements, holding theta fixed in the principal experiments. These solve different problems.

**Mechanism:** Robust optimization discourages features whose predictive association can be reversed within the permitted perturbations. A smoothed classifier predicts argmax_c Pr[f(x+Gaussian noise)=c], so its certification concerns that wrapped classifier rather than the unsmoothed base network. Convex verification encloses reachable activations in outer sets; an enclosing set crossing a decision boundary may reflect relaxation slack rather than a real attack.

**Assumptions:** Perturbations must preserve the intended label, the chosen norm must be relevant to deployment, probability estimates used for smoothing require statistical confidence, and downstream tasks must share useful information. Object design additionally assumes knowledge of the object label and physical control over its appearance.

**Limits:** Robust does not mathematically mean human-recognizable, and non-robust does not mean simply high-frequency, low-amplitude, or useless. Robustness is relative to Delta. Local certificates do not prove global correctness, and generalization to unseen corruptions is not adversarial robustness.

## Evidence, limitations and corrections

- At 00:42:09–00:45:28 Salman reports transfer improvements across classification, detection, and segmentation despite reduced ImageNet accuracy. This is experimental evidence for those settings, not a universal ordering of representations.

- At 00:46:41–01:02:45 the transfer-task-selection objection and robust-only versus non-robust-only transfer experiment are discussed. The decisive proposed decomposition experiment had not been performed; it must not be reported as a result.

- At 00:24:16–00:29:04 and 01:14:16–01:23:28 certification is distinguished from empirical attack resistance. The informal description briefly treats network mappings as convex; the correct point is convex outer relaxation of generally nonconvex reachable sets.

- At 01:30:37–01:41:22 the speaker explicitly restricts object design to controlled-object scenarios and distinguishes training transformations from held-out corruptions. A pre-labeled patch is not a solution to recognizing arbitrary unknown objects.

- The long introductory recap equates robust features with human perceptibility too strongly. Several contemporary performance numbers and anticipated patch-defense claims are historical interview statements, not independently verified current facts.

## Relevance to my research

I want to retain this alongside the adversarial-examples panel because it contributes two distinct extensions: robustness as representation selection, and environment design as part of perception. The sustained argument over task-relative transfer is especially useful for resisting the temptation to treat accuracy, robustness, interpretability, and intelligence as one scalar quantity.

## My viewing plan

**Mode:** My priority is the technical chapters; the full conversation remains an option if I want the research-development context.

**Segments:** - **Start:** 00:23:26
  
  **End:** 00:34:26
  
  **Purpose:** Relaxation limits, smoothing, and denoising wrappers.

- **Start:** 00:38:04
  
  **End:** 01:13:52
  
  **Purpose:** Robust representation transfer, task selection, and disputed mechanisms.

- **Start:** 01:14:16
  
  **End:** 01:23:28
  
  **Purpose:** What a certificate does and does not establish.

- **Start:** 01:27:21
  
  **End:** 01:47:21
  
  **Purpose:** Redesigning objects and the perception-environment boundary.

**Edition:** Saved transcript ends 01:48:15 and includes an approximately eleven-minute editorial introduction. Timestamps are that edition, not audio checked.

## Objections and open questions

Much of the apparent improvement may depend on how downstream tasks and perturbations were chosen. Conversely, discarding non-robust information can remove real signal useful for another task. Optimized objects may amount to machine-readable labels and inherit brittleness under unmodeled physical changes. Those are scope conditions, not reasons to ignore the conceptual shift.

## An experiment I could try

My proposed experiment uses a binary dataset with one stable feature and many weak but jointly predictive features. Ordinary and adversarial classifiers would be evaluated IID, under weak-feature reversal and stable-feature reversal, and on a downstream task defined by the weak features. Holding a classifier fixed while optimizing a small input marker under transformations would test environment design. I would report clean accuracy, attack-tested robust accuracy, downstream transfer and marker dependence separately.

## Connections in my notes

- Carlini, Brendel, and Tramèr: empirical attack failure is not certification and non-robust information can generalize.

- Kornblith: source-task accuracy and representation transfer need not move together.

- Misra: the augmentation or invariance family defines which distinctions a representation preserves.

## Source and coverage

**Read:** Entire available transcript, sequentially; not audio verified.

**Last timestamp:** 01:48:15

**Source caveats:** ASR/publisher transcript may contain wording and mathematical transcription errors; timestamps refer to this saved edition.

Source type: Existing caption or archive. Reviewed text: 20,727 words.

Transcript file: `_eHRICHlg1k.hf.txt` (not distributed).

SHA-256: `ba0714693700a46e7e59216ed731758662d1c53851115a66f6998d40a09374a5`.

[Structured review](_eHRICHlg1k.json) · [Source ledger](../sources.json)
