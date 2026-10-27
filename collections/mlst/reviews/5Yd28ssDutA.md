# #84 LAURA RUIS - Large language models are not zero-shot communicators [NEURIPS UNPLUGGED]

[Original episode](https://www.youtube.com/watch?v=5Yd28ssDutA) · Source: Machine Learning Street Talk · [All reviews](../README.md) · [Learning path](../learning-path.md)

Published: 2022-12-06 · Decision: **Worthwhile** · Confidence: high

## Central claim

Communication requires recovering intended meaning from shared context, and aggregate language scores can conceal failures of that inference. The durable lesson is how to operationalize and evaluate pragmatics while separating competence, task elicitation and social learning.

## Ideas I want to keep

- The task distinguishes literal sentence content from an implied yes/no answer, such as inferring inability to attend a party from an explanation about work or illness. Shared world knowledge enters the interpretation.

- The study compares base models, instruction-tuned models and few-shot prompting, emphasizing systematic evaluation across examples and prompt wordings instead of celebrated single demonstrations.

- A taxonomy distinguishes relatively conventional implicatures from more context-dependent examples. Aggregate gains can concentrate on the easier category, leaving the mechanism of interest unresolved.

- Ruis explicitly treats in-context examples as potentially priming an already available capability rather than necessarily teaching a new inference algorithm. She also cautions that passing this benchmark would not settle general pragmatic understanding.

## Mathematical anatomy

**Objects:** Utterance u, intended response m, shared context c, model prediction and a distribution over pragmatic situations.

**Objective:** A useful reconstruction is inference over P(m|u,c), evaluated on both conventional and context-dependent subsets. This is an explanatory formalization; the interview does not derive a probabilistic pragmatic model.

**Mechanism:** Instruction and demonstrations may identify the task or response convention; human feedback may change which intentions the model tries to satisfy. The interview proposes interactive social pressure as an additional training signal, not a completed causal demonstration.

**Assumptions:** The annotated intended meaning is sufficiently shared, prompts elicit comparable tasks, and human/model conditions are meaningfully matched.

**Limits:** A binary label compresses genuine ambiguity. A plausible cautious answer can be scored as wrong even when an unusual context makes it defensible; calibrated probability and context counterfactuals are useful complements.

## Evidence, limitations and corrections

- All reported model rankings and roughly 70–80% figures belong to the 2022 experiment and interview. They are not a claim about current systems.

- A performance association with OpenAI instruction-tuned systems does not isolate RLHF as the cause: pretraining, supervised tuning, data, architecture and prompt sensitivity are possible confounders.

- The early ChatGPT party example is an anecdote; the speaker’s insistence on a systematic test is more informative than that demonstration.

- A few-shot plateau is consistent with task identification but does not prove that no information is learned from examples. Distinguishing mechanisms needs matched interventions.

- The informal phrase about moving into an area of weight space should be read as a metaphor. Ordinary prompting changes activations and conditioning, not necessarily model weights.

- The guest acknowledges uncertainty about embodiment and scaling. The discussion offers research hypotheses rather than a proof that text-only learning cannot acquire relevant knowledge.

## Relevance to my research

A worthwhile compact companion to Kumar and the broader evaluation episodes in my research program. It makes intelligence relational: success depends on the agent, shared assumptions and the communicative task. Its strongest contribution is disciplined measurement of a narrow cognitive ability, rather than a mathematical theory of pragmatics.

## My viewing plan

**Mode:** I will focus on the main interview sections below.

**Ranges:** - **Start:** 00:03:44
  
  **End:** 00:12:09
  
  **Reason:** Task design, comparison groups and competence versus elicitation.

- **Start:** 00:19:40
  
  **End:** 00:26:10
  
  **Reason:** Interactive learning hypotheses, subset analysis and limits of benchmark success.

**Edition:** Recovered podcast audio

## Objections and open questions

An agent optimized for cautious literal truth may reasonably avoid a categorical implicature. Evaluation must specify whether the goal is most likely speaker intent, logical entailment, social coordination or risk-sensitive decision making; these need not have the same optimum.

## An experiment I could try

I want to construct paired dialogues with identical utterances but different shared contexts, including work that ends before the party and work that overlaps it. Elicited probabilities over intended answers would allow comparison of zero-shot and example-primed conditions, with calibration and error reported by implicature type. Whole contextual mechanisms would be held out rather than merely paraphrases.

## Connections in my notes

- Kumar: human inductive biases and auxiliary supervision

- Lampinen/Hattie: elicitation versus acquired algorithms

- Chollet/Mitchell: capability measurement and generalization

## Primary sources checked

- **Url:** https://lauraruis.github.io/2022/09/29/comm.html
  
  **Purpose:** Primary author source identifying the historical benchmark and research scope.

## Source and coverage

**Status:** complete_available_text

**Method:** Read complete local ASR text in bounded sections; not an independent audio verification.

**First timestamp:** 00:00:00

**Last timestamp:** 00:27:45

**Caveats:** - Local Whisper-large-v3-turbo transcription; proper names and technical notation may be inaccurate.

- Timestamps refer to the recovered podcast edition; exact alignment with the current YouTube edit is not certified.

Source type: Local asr. Reviewed text: 4,588 words.

Transcript file: `5Yd28ssDutA.local-asr.txt` (not distributed).

SHA-256: `5e40e881c01bb8defede9853905e39bcb45f12ed94e487666093dfeb712b9e52`.

[Structured review](5Yd28ssDutA.json) · [Source ledger](../sources.json)
