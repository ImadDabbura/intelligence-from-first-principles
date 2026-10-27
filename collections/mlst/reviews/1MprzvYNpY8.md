# CURL: Contrastive Unsupervised Representations for Reinforcement Learning

[Original episode](https://www.youtube.com/watch?v=1MprzvYNpY8) · [All reviews](../README.md) · [Learning path](../learning-path.md)

Published: 2020-04-17 · Decision: **Worthwhile** · Confidence: high

## Central claim

A representation useful for control need not reconstruct every observed bit. Contrastive auxiliary learning makes that distinction concrete, but its usefulness comes partly from the invariances supplied by positive-pair construction, not from a magically task-independent understanding objective.

## Ideas I want to keep

- At 00:05:41–00:10:17 contrastive representation learning is added to an off-policy RL pipeline to improve learning from limited environment interaction. This separates the cost of collecting experience from the cost of reusing experience computationally.

- At 00:14:02–00:17:34 the participants examine shared-encoder multi-objective optimization: reward/value gradients and auxiliary gradients can agree or interfere. The practical simplicity of a classification-like auxiliary loss is useful, although some mathematical claims about bounded losses are wrong.

- At 00:17:43–00:25:40 reconstruction versus discrimination becomes a question of relevant information. Crops can discourage encoding background details while retaining shared structure, and the interviewer correctly presses that choosing augmentations inserts domain knowledge.

- At 00:30:50–00:35:49 the guest distinguishes frozen-feature linear evaluation, transfer to a different downstream task and fine-tuning on the original labeled task. These are different claims about a learned representation and should not be collapsed into one benchmark score.

- At 00:42:30–00:49:26 pixels versus engineered state reveals the interaction of representation, partial observability and optimizer bias. A pixel-based learner beating one state-based baseline does not mean images contain more information than a sufficient state; it may mean the chosen state encoding is harder to learn from.

- At 00:55:31–01:02:24 the disagreement over pretraining despite full labels is valuable: adding an auxiliary objective changes optimization and inductive bias even when it does not add new raw observations.

## Mathematical anatomy

**Objects:** Observation crops, an encoder, a momentum encoder for keys, a similarity score, positive and negative pairs, and an RL objective sharing representation parameters.

**Objective:** Identify the matching view among candidate keys while learning value/policy functions from the same experience. A standard contrastive loss has the form minus log of exp(score-positive) divided by the sum of exp(scores).

**Mechanism:** Augmentation defines an equivalence relation the representation is encouraged to respect; negative examples discourage collapse. Control gradients can retain distinctions relevant to reward.

**Assumptions:** Positive views must share task-relevant state; negative sampling must not systematically repel observations that should be equivalent; the observation history must contain enough information for control.

**Limits:** Invariance can remove needed information. Finite-frame observations can omit hidden velocity or occluded state. More contrastive information is not automatically more decision-relevant information, and multiple losses can conflict.

## Evidence, limitations and corrections

- The primary CURL paper confirms pixel-based contrastive features, off-policy control and comparisons on DeepMind Control Suite/Atari under limited interaction. This supports that specific sample-efficiency result, not every broad forecast in the interview.

- Cross-entropy is lower-bounded by zero but not generally upper-bounded; classifying a true event with probability approaching zero makes its loss diverge. The interview’s well-bounded-loss argument cannot guarantee benign gradient interaction.

- The transcript conflates Gaussian log likelihood and KL divergence. KL is nonnegative under its standard definition; the different scaling/conditioning of objectives must be analyzed directly.

- The guest candidly identifies environments where the method fails or cannot recover state variables. Predictions that larger temporal architectures will solve them are hypotheses.

- Historical claims that masked image modeling cannot compete, or self-supervised pretraining will always beat reward-only learning, should be read as 2020 research bets, not current universal facts.

- The review checked paper-level scope, not a reproduction of the experiments or all implementation details.

## Relevance to my research

Strong for understanding representation as selective preservation of information under task assumptions. For me, its value is in connecting the derivation of contrastive objectives to the invariances that make them useful for an acting system.

## My viewing plan

**Mode:** I will focus on these substantial sections.

**Ranges:** - **Start:** 00:05:41
  
  **End:** 00:25:40
  
  **Why:** Sample efficiency, auxiliary objectives, relevance and augmentation assumptions; I will keep the loss corrections alongside it.

- **Start:** 00:30:50
  
  **End:** 00:35:49
  
  **Why:** Distinctions between representation-evaluation protocols.

- **Start:** 00:42:30
  
  **End:** 00:49:26
  
  **Why:** Pixels versus state and partial observability.

- **Start:** 00:55:31
  
  **End:** 01:02:24
  
  **Why:** Why pretraining can help despite access to labels.

**Edition note:** HF transcript timings, not independently audio-aligned.

## Objections and open questions

A contrastive objective can learn shortcut instance identifiers or harmful invariances. Reconstruction can be appropriate when downstream tasks are unknown and information preservation matters. Equal environment interactions do not imply equal compute, and successful transfer requires matching the pretraining and deployment information structure.

## An experiment I could try

I want to build a visual control task with independently varying background, object position and velocity, comparing RL-only, reconstruction auxiliary loss and contrastive crops at equal environment samples, with compute reported separately. A crop that sometimes deletes the object would test when apparently stronger invariance destroys control. State-recovery probes would complement the control results, without treating probe success as evidence of causal use.

## Connections in my notes

- Sufficient statistics for control

- Information bottleneck and invariance

- Partial observability

- Auxiliary objectives and gradient interference

## Primary sources checked

- **Url:** https://proceedings.mlr.press/v119/laskin20a.html
  
  **Title:** CURL: Contrastive Unsupervised Representations for Reinforcement Learning
  
  **Use:** Confirmed algorithm family and original benchmark scope.

## Source and coverage

**Status:** complete_available_text

**Start:** 00:00:00

**End:** 01:14:39

**Caveats:** - Complete HF transcript read in two contiguous ranges. Audio not verified; names and loss terminology occasionally mistranscribed.

Source type: Existing caption or archive. Reviewed text: 10,951 words.

Transcript file: `1MprzvYNpY8.hf.txt` (not distributed).

SHA-256: `66e0e7206ac17dac2aa9ad9a66523413cc2b69f1d56718b48d8d5dd2ed8eddf6`.

[Structured review](1MprzvYNpY8.json) · [Source ledger](../sources.json)
