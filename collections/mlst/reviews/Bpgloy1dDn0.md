# Mapping GPT revealed something strange...

[Original episode](https://www.youtube.com/watch?v=Bpgloy1dDn0) · Source: Machine Learning Street Talk · [All reviews](../README.md) · [Learning path](../learning-path.md)

Published: 2024-05-23 · Decision: **Worthwhile** · Confidence: high

## Central claim

A learned predictor becomes a dynamical system when its outputs feed future inputs. Treating prompts as control inputs exposes a useful distinction between what a model usually emits, what can be elicited under a limited intervention budget, and what a particular search algorithm manages to find.

## Ideas I want to keep

- The state is a token history, the input is a controllable portion of that history, and the dynamics are the model’s next-token distribution plus the sampling/update rule. This makes questions about reachability and feedback explicit.

- A shortest-prompt game illustrates an operational control objective: make a target token become the most likely next token while minimizing the number of controllable tokens. It is deliberately narrower than making the system reason correctly.

- The empirical study tests targets of different baseline likelihoods. A low unprompted probability need not imply that a small intervention cannot make the target dominant.

- A single-attention-layer analysis decomposes output contributions from fixed and controllable inputs. Bounds on input norms and parameter matrices yield an outer bound on reachable representations.

- The interview notices a practical abstraction failure: optimized token IDs can decode and re-encode to a different sequence. Control at the embedding, token and user-visible string interfaces must be distinguished.

## Mathematical anatomy

**Objects:** History x_t, controllable token sequence u, fixed context x_0, next-token probabilities p_theta, a target y and a prompt-length budget k.

**Objective:** Illustrative form: find u with |u|<=k such that argmax_v p_theta(v|u,x_0)=y; likelihood maximization is a search surrogate. For stochastic generation, specify the required success probability and rollout horizon separately.

**Mechanism:** Autoregressive feedback turns one-step perturbations into trajectories. In a single attention head, weighted value contributions from fixed and controllable positions can be bounded geometrically under norm constraints.

**Assumptions:** The interface, tokenization, decoding rule, context limit, target distribution and search budget are fixed. The theoretical result applies to a bounded-input attention component, not automatically to a complete deployed agent.

**Limits:** A proven outer bound excludes targets outside it but need not establish that every point inside is reachable. Empirical search success provides a lower bound on reachability; failed search does not prove impossibility.

## Evidence, limitations and corrections

- The interview reports approximately 97% success for true next tokens, 89% for sampled top-75 candidates and 46% for randomly selected vocabulary tokens under short controls. These are experimental configurations, not universal properties of all LLMs. The current paper abstract gives at least 85% for the top-75 panel; retain the version/configuration distinction.

- The host’s claim that RLHF should remove trajectories conflates suppressing probabilities with excluding outcomes. With finite logits, ordinary softmax assigns positive probability to every vocabulary item; decoding constraints and practical probability thresholds change operational reachability.

- Soft-prompt optimization has a larger, continuous control space than text prompting. Success there does not guarantee that a nearby valid token sequence exists, nor that the perturbation is small under a relevant interface metric.

- The embedding vector space itself is convex. What may be nonconvex is the subset of meaningful or successful representations, or the optimization landscape. The spoken phrase extremely nonconvex embedding space needs that qualification.

- The later collective-intelligence and morphogenesis discussion is a research agenda. Biological distributed computation is not a proof that many small language models connected by text will match a larger model efficiently.

- A single-head singular-value bound is not an established scalar flexibility score for the entire model. Layer interactions, normalization and nonlinearities are explicitly left as further work.

## Relevance to my research

Worthwhile for extending my systems intuition beyond static prediction. The first half and technical appendix provide concrete distinctions between reachability, search and reliability. The biological analogies are less decisive; they should generate experiments rather than carry the argument.

## My viewing plan

**Mode:** I will focus on the main interview sections below.

**Ranges:** - **Start:** 00:04:34
  
  **End:** 00:17:23
  
  **Reason:** Control formulation, minimal prompting and discrete versus continuous interventions.

- **Start:** 00:20:07
  
  **End:** 00:24:23
  
  **Reason:** Autoregressive feedback, tokenization and stability questions.

- **Start:** 00:31:31
  
  **End:** 00:40:57
  
  **Reason:** Reach/avoid formulation, theoretical scope and empirical controllability.

- **Start:** 01:06:00
  
  **End:** 01:09:38
  
  **Reason:** Technical explanation of the attention bound.

- **Start:** 01:12:29
  
  **End:** 01:17:05
  
  **Reason:** Outer reachable-set geometry and limitations of extending a single-head result.

**Edition:** Recovered podcast audio

## Objections and open questions

Knowing how to force a token is not the same as knowing how to elicit a correct solution or preserve reliable behavior over a long trajectory. A useful control theory must specify semantic objectives, costs and observations, not merely relabel prompt search.

## An experiment I could try

With a small open model, I want to compare human prompts, discrete token search and continuous soft prompts at matched evaluation budgets. Target likelihood, greedy reachability and repeated-sampling success would be measured separately, with every proposed string re-encoded before evaluation. On a toy attention head, plotting the empirical reachable set inside a derived norm bound would clarify why the bound is an exclusion certificate rather than a complete characterization.

## Connections in my notes

- Hooker: capability elicitation and uncertainty about prompting

- Nanda: mechanistic versus input–output understanding

- Valpola/de Vries: feedback, models and control

- Levin/Stanley: collective computation as a separate empirical question

## Primary sources checked

- **Url:** https://arxiv.org/abs/2310.04444
  
  **Purpose:** Checked model panel, single-attention scope and published controllability figures.

- **Url:** https://aman-bhargava.com/ai/2023/12/17/towards-a-control-theory-of-LLMs.html
  
  **Purpose:** Author explanation of outer bounds and the open research agenda.

## Source and coverage

**Status:** complete_available_text

**Method:** Read complete local ASR text in bounded sections; not an independent audio verification.

**First timestamp:** 00:00:00

**Last timestamp:** 01:17:05

**Caveats:** - Local Whisper-large-v3-turbo transcription; proper names and technical notation may be inaccurate.

- Timestamps refer to the recovered podcast edition; exact alignment with the current YouTube edit is not certified.

- Recovered podcast includes an explicitly appended technical segment after the main interview, extending to 77 minutes. The selected YouTube metadata is about 69 minutes; appendix timestamps must not be assumed to exist in that edit.

Source type: Local asr. Reviewed text: 15,321 words.

Transcript file: `Bpgloy1dDn0.local-asr.txt` (not distributed).

SHA-256: `63062ed8cd79f759b444e8bb50f7e9bb92b12ab1298afc7c156715acd44d361d`.

[Structured review](Bpgloy1dDn0.json) · [Source ledger](../sources.json)
