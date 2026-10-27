# Mechanistic Interpretability - NEEL NANDA (DeepMind)

[Original episode](https://www.youtube.com/watch?v=_Ygf0GnlwmY) · [All reviews](../README.md) · [Learning path](../learning-path.md)

Published: 2023-10-28 · Decision: **Core** · Confidence: high for conceptual and methodological value; medium for transfer of small-model findings to frontier systems

## Central claim

A particularly strong lesson in turning intuitions about intelligence into falsifiable mechanisms: identify represented variables, reconstruct their transformations, intervene precisely, and separate a compelling circuit explanation from an attractive behavioral story.

## Ideas I want to keep

- Grokking becomes a three-stage dynamical explanation: memorization, gradual formation of a Fourier circuit, then cleanup of competing memorizing components. A sudden test-accuracy jump can conceal continuous progress. Restricted loss tracks the proposed circuit before aggregate test loss reveals it. For modular addition, sin/cos embeddings, trigonometric composition and output matching explain finite-domain generalization; they do not establish an unbounded arithmetic algorithm.

- Othello exposes the dependence of apparent representational complexity on the chosen ontology. Black/white board labels looked nonlinear; mine/opponent/empty better matched the model and admitted linear decoding and interventions. The lesson is to search for a coordinate system aligned with the computational task, while remembering that a successful probe can compute rather than merely read a property.

- Superposition is distinguished from ordinary distributed coding and polysemantic observations. More sparse features than dimensions may be economical because feature usefulness grows with prevalence while interference depends on coactivation. Correlations, activation ranges and nonlinear cleanup alter this tradeoff. A French-activating neuron or hockey/Canada confusion is evidence of selective responses, not proof of a single exhaustive semantic function.

- Transformer circuits separate attention routing through QK from transported content through OV. Previous-token and induction heads compose a concrete algorithm, [A][B] ... [A] -> [B]. Architecture interventions and head ablations are stronger evidence than simply observing coincident capability and attention patterns. Larger-model behavioral signatures remain weaker evidence than full circuit reconstruction.

- Activation patching contrasts necessity-like corruption and sufficiency-like restoration while controlling competing features. Zeroing an early component can destroy generic computation and misleadingly make it appear task-specific. Logit differences or log probabilities preserve small cumulative effects that accuracy, rank or saturated probabilities can hide. The indirect-object example also raises backup pathways, so absence of an ablation effect need not mean absence of contribution.

## Mathematical anatomy

**Objects:** Learned feature directions, residual-stream states, attention QK/OV maps, finite-group Fourier bases, circuit graphs, clean/corrupted input pairs and intervention-dependent output distributions.

**Objective:** Explain a specific computation and its training trajectory with a hypothesis that predicts intervention outcomes; this differs from maximizing probe accuracy or attaching plausible natural-language labels to activations.

**Mechanism:** For modular addition, output scores can contain sums of cos(ω(a+b−c)), selecting the correct residue. In attention, a source-selection bilinear form and a source-content linear map compose across layers. For sparse coding, many approximately separated directions trade reconstruction benefit against interference; the p versus p² heuristic requires assumptions about joint activation.

**Assumptions:** The chosen toy task exposes a relevant circuit; intervention examples control nuisance properties; patched activations remain meaningful enough for causal interpretation; metrics resolve small effects; discovered features are not artifacts of labels, basis choices or dataset selection.

**Limits:** A complete account of one modular task or Othello model does not show that general language models reason through the same representation. Linear decodability is neither uniqueness nor exclusive causal use. Induction is a concrete form of in-context learning, not a proof that all few-shot reasoning reduces to copying. Weight decay is influential in these grokking experiments, not a necessary condition for all delayed generalization.

## Evidence, limitations and corrections

- The transcript repeatedly distinguishes demonstrated toy mechanisms from hypotheses about large systems; that discipline takes precedence over the hosts’ occasional universal claims. The original induction-head paper explicitly characterizes its large-model hypothesis as preliminary and indirect.

- The Fourier account has circuit removal and restricted-loss evidence, but fixed modulus and a small enumerable domain bound the generalization claim. Learning a trigonometric lookup table is not learning a continuous trigonometric function everywhere.

- Sparse probing and high-activation examples do not enumerate a complete feature dictionary or establish monosemanticity. Nonlinear probes, correlated concepts and out-of-domain activations are explicit failure cases.

- The long closing risk discussion contains useful distinctions between learned objectives, deliberate goal assignment, misuse and coherent long-term agency, but forecasts and gorilla analogies are arguments under uncertainty, not consequences of the demonstrated circuits. The mathematical learning value is concentrated before this segment.

## Relevance to my research

Exceptionally high: it teaches how to know whether an explanation of intelligence is mechanistic, how an appropriate representation changes the problem, and how observable emergence depends on measurement. These principles transfer to neuroscience, dynamical systems and scientific model identification beyond LLMs.

## My viewing plan

**Mode:** chapters

**Ranges:** 

**Edition note:** Untimed publisher alternate: exact timestamps unavailable and must not be invented. My viewing plan follows the contiguous technical sequence from the grokking/modular-addition discussion through Othello, superposition, the mathematical transformer framework, induction heads and activation patching. The essential block ends at “Beautiful” / the DeepMind hiring exchange before “let’s talk about superintelligence now.” The subsequent risk discussion is optional. Correspondence requires locating these anchors in the actual video.

## Objections and open questions

Toy mechanisms can be unusually clean and selected for tractability; a feature dictionary may fail to scale or change across seeds. Nevertheless, the episode treats this as a research problem and provides intervention logic rather than claiming that current interpretation is complete. One can reject its risk forecasts without losing the central scientific method.

## An experiment I could try

I would train a one-layer modular-addition transformer across several seeds and weight-decay values, tracking train/test cross entropy, accuracy, Fourier-restricted loss and weight norms. Ablating identified frequencies versus equal-size random ablations would test the circuit account, with both linear and logarithmic training axes revealing the dynamics. Two patching effects whose individual logit contributions are real but whose individual accuracy changes are zero would then demonstrate how the metric changes the causal story.

## Connections in my notes

- Belrose: linear erasure and higher-order leakage sharpen the distinction between accessible information and causal computation.

- Voita: probe complexity/MDL provides a complementary warning that decoder success is not a transparent account of representation.

- Balestriero and Wyart: learned geometry and hierarchical statistical structure offer alternatives to reading all progress as discrete symbolic emergence.

## Primary sources checked

- **Title:** Progress measures for grokking via mechanistic interpretability
  
  **Url:** https://arxiv.org/abs/2301.05217
  
  **Use:** Primary reference for the Fourier circuit and progress-measure case study.

- **Title:** In-context Learning and Induction Heads
  
  **Url:** https://transformer-circuits.pub/2022/in-context-learning-and-induction-heads/index.html
  
  **Use:** Primary source explicitly bounds causal evidence and large-model extrapolation.

## Source and coverage

**Status:** complete_available_text

**Start:** Opening woods conversation

**End:** Closing thanks; final source character 226666

**Caveats:** - Read all 39,923 words of the publisher text, not the audio. This is an untimed alternate edition; no reliable video timestamps can be recovered from it. Speaker labels and technical terms contain transcription errors. Historical research and forecast claims describe the interview period, not current field coverage.

Source type: Publisher transcript. Reviewed text: 39,923 words.

Transcript file: `_Ygf0GnlwmY.publisher.txt` (not distributed).

SHA-256: `a9c62af6495cfee6fdc695809c889dbed7f8c37c09835035ea47ffe4f6ee2594`.

[Structured review](_Ygf0GnlwmY.json) · [Source ledger](../sources.json)
