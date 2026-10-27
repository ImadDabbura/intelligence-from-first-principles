# #91 - HATTIE ZHOU - Teaching Algorithmic Reasoning via In-context Learning #NeurIPS

[Original episode](https://www.youtube.com/watch?v=80i6D2TJdQ4) · Source: Machine Learning Street Talk · [All reviews](../README.md) · [Learning path](../learning-path.md)

Published: 2022-12-20 · Decision: **Worthwhile** · Confidence: high

## Central claim

Examples of correct answers can leave the generating procedure highly underdetermined. Explicitly specifying intermediate operations reduces that ambiguity and can improve extrapolation, even without updating model weights. This is evidence about eliciting a procedure, not yet about discovering novel algorithms autonomously.

## Ideas I want to keep

- A scratchpad containing values differs from an algorithmic explanation specifying how each value is obtained. Observing a few input-output traces may support many incompatible procedures; more operational detail constrains the intended interpretation.

- Length extrapolation is a useful intervention: evaluate the same rule on harder inputs outside the demonstrated range rather than treating in-distribution arithmetic accuracy as evidence of the intended algorithm.

- Acquiring or eliciting an execution skill is distinct from inventing the skill. The speaker explicitly identifies autonomous algorithm discovery as another frontier, which prevents the headline from doing too much explanatory work.

- A problem-solving template can combine explicit control structure with learned local interpretation. The math-word-problem discussion motivates that hybrid, while candidly lacking a complete benchmark or precise universal procedure.

- The closing discussion distinguishes inexpensive candidate generation from exact checking: a weak conjecture generator can still be useful when a formal checker supplies trustworthy feedback.

## Mathematical anatomy

**Objects:** A pretrained conditional sequence model, a prompt containing algorithmic demonstrations, execution traces, and test inputs with different lengths or compositions.

**Objective:** Correct outputs and valid intermediate states beyond the demonstration distribution; no weight update is required in the illustrated setup.

**Mechanism:** The prompt supplies operational structure that narrows the set of plausible programs consistent with examples. Autoregressive generation provides additional sequential computation, but each step remains fallible.

**Assumptions:** The model can interpret instructions, maintain needed state, apply local operations and fit the trace within its context/computation budget.

**Limits:** Finite successful tests cannot establish unbounded algorithmic correctness. Trace-answer agreement is evidence of consistency, not proof the trace caused the answer. A correct algorithm is correct on its specified domain; merely being an algorithm does not imply distribution-independent correctness.

## Evidence, limitations and corrections

- The addition example offers a testable mechanism: disambiguate carry and digit-update rules, then increase digit length. At one point the transcript says carry when the sum is greater than10; the correct threshold is at least10, including the incoming carry.

- The speaker's suspicion that fine-tuning would mainly overfit is conjecture here, not a demonstrated impossibility or a general superiority theorem for prompting.

- The compression explanation of emergent abilities is a plausible hypothesis, not a mechanism established by these experiments. More parameters do not automatically force memorization or preclude learning regularities.

- The host's neural-net-versus-Turing-machine framing omits resource assumptions. Fixed finite resources constrain ordinary computers too; the relevant distinctions are fixed-depth evaluation, recurrent computation, external memory and asymptotic model families.

- The interview is from 2022. I retain its experimental logic, treating its capability statements as historical rather than as the performance frontier.

## Relevance to my research

Worth my attention because it makes specification ambiguity concrete. The lesson generalizes beyond LLM prompting: learning failures may come from an underidentified procedure, inadequate execution resources, or a missing primitive, and these require different interventions.

## My viewing plan

**Mode:** I will focus on the technical interview.

**Ranges:** - **Start:** 00:01:45
  
  **End:** 00:13:20
  
  **Reason:** Definition, procedure-versus-trace distinction, prompting intervention, extrapolation and limitations.

- **Start:** 00:18:42
  
  **End:** 00:21:11
  
  **Reason:** Candidate generation, formal verification and context for mathematical reasoning.

**Edition:** Podcast-edition timestamps, near-equal duration to YouTube; exact alignment not checked.

## Objections and open questions

A detailed prompt may supply most of the human-designed algorithm. That does not make the result uninteresting, but it changes the attribution of intelligence. I would test whether the model can compose primitives, detect a deliberately erroneous instruction, and remain correct under new surface forms; these are different from copying a supplied trace.

## An experiment I could try

I want to compare answer-only examples, bare scratchpads and fully specified addition traces at equal prompt budgets, varying digit length and carry-chain length independently. Final answers, each transition and sensitivity to a corrupted intermediate step would be scored against an exact program baseline. A derivation of how per-step error compounds with trace length would then be compared with observed failures.

## Connections in my notes

- Wyart: latent algorithms and scale-dependent generalization

- Kambhampati: testing reasoning claims under controlled transformations

- Lessard: explicit compositional structure and execution

- AlphaEvolve: generation need not be reliable if verification is strong

## Primary sources checked

- **Url:** https://arxiv.org/abs/2211.09066
  
  **Purpose:** Checked primary paper identification, four-stage framework and scope of arithmetic experiments.

## Source and coverage

**Status:** complete_available_text

**Method:** Read complete locally generated transcript of publisher RSS audio, including the closing Markus interview.

**First timestamp:** 00:00:00

**Last timestamp:** 00:21:11

**Caveats:** - Local Whisper-large-v3-turbo transcription; not corrected word-by-word against audio.

- RSS duration1274seconds closely matches video1275seconds; timestamps still refer to podcast audio.

- Names and mathematical boundary conditions may be transcribed imperfectly.

Source type: Local asr. Reviewed text: 3,075 words.

Transcript file: `80i6D2TJdQ4.local-asr.txt` (not distributed).

SHA-256: `87045e1cd86e509e8627824d47af060c1f9a9ed1df5b8e99e1fe164bedbef0de`.

[Structured review](80i6D2TJdQ4.json) · [Source ledger](../sources.json)
