# #040 - Adversarial Examples (Dr. Nicholas Carlini, Dr. Wieland Brendel, Florian Tramèr)

[Original episode](https://www.youtube.com/watch?v=2PenK06tvE4) · [All reviews](../README.md) · [Learning path](../learning-path.md)

Published: 2021-01-31 · Decision: **Core** · Confidence: High for foundational and methodological value; historical claims about which defenses work are confined to the interview date.

## Central claim

Accurate prediction does not uniquely identify the representation or invariances I intended a learner to acquire. Adversarial examples expose that underdetermination, while evaluating defenses exposes a second problem: a weak search for failures can masquerade as evidence of robustness. This is foundational for studying intelligence scientifically, beyond security applications.

## Ideas I want to keep

- Non-robust features can predict held-out labels rather than merely memorize training examples. That distinction explains why ordinary generalization and human-compatible robustness can diverge, and why adversarial examples may transfer between independently trained models sharing predictive features.

- Shortcut learning is a solution-selection problem: many functions agree on the observed train/test distribution but behave differently under interventions or distribution change. Architecture, objective, optimizer, and data jointly bias which solution is found.

- Robustness is relative to a specified perturbation set. Adversarial training penalizes reliance on features unstable under that set; it does not establish invariance to every semantically irrelevant transformation. Randomized smoothing likewise certifies a restricted mathematical neighborhood, not unrestricted semantic correctness.

- Robustness evaluation contains an optimization problem inside the measurement. Failure of a particular attack to find an error is weaker evidence than a certificate that no permitted error exists; preprocessing and awkward gradients can frustrate the attack without improving the classifier.

- Security consequences belong to a deployed system and adversary, not to an isolated misclassified image. The discussion separates a scientific probe of representations from a concrete threat model involving attacker control, objectives, and downstream consequences.

## Mathematical anatomy

**Objects:** A predictor f, data distribution P(x,y), intended semantic label function, allowable perturbation set Delta(x), and an attack algorithm A with finite resources.

**Objective:** Ordinary risk E_P[l(f(x),y)] differs from robust risk E_P[max_delta_in_Delta(x) l(f(x+delta),y)]. The latter assumes the true label remains valid throughout the allowed set; this can fail at genuine semantic boundaries.

**Mechanism:** Adversarial training approximately solves a minimax objective with an inner attack and outer parameter update. Transfer is consistent with common vulnerable features but is not a unique proof of their causal origin. Empirical attack error lower-bounds worst-case error; correspondingly, attack-measured robust accuracy can overestimate true robust accuracy.

**Assumptions:** The threat set, attacker information, attack objective, and stochastic model behavior must be explicit. A successful classifier may use signals humans ignore; whether those signals should be excluded is a task/robustness specification, not an intrinsic property of being small or high-frequency.

**Limits:** Knowing a cause does not logically guarantee an efficient remedy, despite occasional rhetoric in the discussion. Clean/robust accuracy trade-offs depend on the data and threat model and are not a universal law that every robustness improvement must reduce accuracy. Differential privacy bounds sensitivity to individual records; describing it simply as no memorization is an overstatement.

## Evidence, limitations and corrections

- At 00:15:15–00:19:50 the guests explicitly decline a single definitive causal explanation, contrasting sharply with the host’s fatalistic opening recap. Their uncertainty is a strength of the interview.

- At 00:35:00–00:44:47 shortcut learning and human/model error patterns move the question from benchmark score to the function learned. Reported cross-model and human comparisons are interview evidence, not independently reproduced results here.

- At 00:49:25–00:53:14 transfer and perturbation-specific defenses make the scope of a robustness claim precise. Invariance-based attacks are introduced at 00:13:49 but are not developed deeply enough to treat this episode as their full tutorial.

- At 01:06:49–01:16:10 the research-method discussion explains adaptive evaluation, correcting broken claims, and why apparent improvements can vanish. The later negative-result discussion adds how failed hypotheses can still generate scientific knowledge.

- The first eleven minutes contain strong host extrapolations, including that adversarial training is effectively random and nothing can be done. These should not stand in for the more qualified expert discussion. Closing deployment advice is historical and application-specific, not a current blanket recommendation to ignore attacks.

## Relevance to my research

This changes what it means to understand a learner. I need to identify not only successful outputs but the equivalence classes of inputs it treats as the same, which features support predictions, and what evidence could falsify a robustness claim. It also models unusually useful scientific restraint: a compelling explanation is a hypothesis until interventions and appropriately strong tests discriminate it.

## My viewing plan

**Mode:** I plan to watch the main scientific conversation and skip the opening recap and some research-politics discussion.

**Segments:** - **Start:** 00:14:18
  
  **End:** 00:27:01
  
  **Purpose:** Competing explanations, memorization, and semantics beyond human vision.

- **Start:** 00:34:44
  
  **End:** 00:53:14
  
  **Purpose:** Shortcut learning, solution multiplicity, transfer, and scoped defenses.

- **Start:** 00:58:38
  
  **End:** 01:16:10
  
  **Purpose:** Inductive-bias hypotheses and rigorous adaptive evaluation.

- **Start:** 01:22:38
  
  **End:** 01:27:37
  
  **Purpose:** Negative results and tractable settings where progress can be identified.

**Edition:** Saved edition includes an approximately eleven-minute host preface and a postscript at 00:57:43. Ends 01:36:11; no audio verification.

## Objections and open questions

Human vision is not uniformly optimal, and matching human errors is not automatically the right objective. An adversarial failure under an unrealistic perturbation budget may have little practical cost while still exposing a representation property. Conversely, good average performance does not neutralize an adversary who selects inputs. These distinctions prevent both security sensationalism and the opposite mistake of dismissing robustness as irrelevant.

## An experiment I could try

I want to construct a binary dataset with one moderately reliable robust feature and many weakly predictive perturbable features. A standard linear classifier and an adversarially trained one would be compared under clean data, norm-bounded attacks and a different distribution shift. Inserting a non-differentiable preprocessing step would let me test how naive gradient attack accuracy can improve without an actual robustness gain, checking the small example by exhaustive search or a certificate.

## Connections in my notes

- Max Bartolo: human-adversarial data collection selects a new evaluation distribution and requires validity checks.

- Simon Kornblith: contrastive shortcuts and augmentation assumptions determine which representations survive training.

- Sara Hooker: aggregate accuracy can conceal systematic changes in the examples or features that matter.

## Source and coverage

**Read:** Entire available transcript, sequentially; not audio verified.

**Last timestamp:** 01:36:11

**Source caveats:** ASR/publisher transcript may contain wording and mathematical transcription errors; timestamps refer to this saved edition.

Source type: Existing caption or archive. Reviewed text: 17,379 words.

Transcript file: `2PenK06tvE4.hf.txt` (not distributed).

SHA-256: `f9581886838a4274da5b7b8bc48e5d0456a9e18fdc8324060998cea247943425`.

[Structured review](2PenK06tvE4.json) · [Source ledger](../sources.json)
