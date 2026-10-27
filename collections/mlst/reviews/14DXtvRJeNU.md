# How Do AI Models Actually Think? [Dr. Laura Ruis]

[Original episode](https://www.youtube.com/watch?v=14DXtvRJeNU) · [All reviews](../README.md) · [Learning path](../learning-path.md)

Published: 2025-01-19 · Decision: **Worthwhile** · Confidence: high

## Central claim

Worthwhile for its careful empirical attempt to distinguish procedure reuse from fact retrieval, and for separating representational possibility from what a pretrained model actually learned. The influence-function result is narrower and more interesting than the binary debate over whether language models “reason”; the later agency discussion is exploratory rather than a settled account.

## Ideas I want to keep

- Comparing the training-data influence profiles of different questions adds information beyond answer accuracy. Shared influence across arithmetic questions with different numbers suggests a reusable task-level source of competence, unlike the distinct profiles of unrelated factual questions.

- Code can influence natural-language execution of a procedure even when it describes the procedure rather than giving that exact worked example. This motivates testing cross-representational transfer from algorithms to traces, while recognizing that influential code can help or hurt.

- A connectionist implementation can support variable binding and compositional operations; continuous distributed representation and symbolic structure are not mutually exclusive categories. Whether ordinary training discovers such structure is a separate empirical question.

- Capability evaluation depends on elicitation and distribution design. A failed prompt does not prove incapacity, but optimizing prompts on the test set can itself manufacture misleading capability claims.

- Agency is framed operationally as choosing actions to affect future inputs under uncertainty, with sensitivity to changed action consequences. This distinguishes closed-loop adaptation from merely generating text about agents, although the interview leaves its proposed measurement unresolved.

## Mathematical anatomy

**Objects:** Training documents z, empirical-risk minimizer theta, per-document gradients, Hessian H, query completion log likelihood g(theta), influence vectors across documents, and role/filler representations.

**Objective:** Infer which training information supports reusable procedures and distinguish this from exact retrieval; assess systematicity on held-out combinations rather than familiar instance accuracy.

**Mechanism:** Under classical local regularity assumptions, upweighting document z by epsilon gives d theta/d epsilon≈−H^−1 grad loss_z, so dg/d epsilon≈−grad g^T H^−1 grad loss_z. These influence profiles can then be compared across tasks. For binding, a standard illustrative representation T=sum_i r_i tensor f_i permits recovery using dual role vectors when the roles are appropriately independent.

**Assumptions:** The local approximation is informative despite nonconvex training and approximate curvature; compared outputs and tasks are controlled; shared influence is not merely common style or formatting; held-out combinations actually isolate the intended systematicity.

**Limits:** Influence is a local counterfactual approximation, not literal document lookup during inference. Similar profiles do not uniquely identify an internal algorithm. Exact unbinding requires suitable role geometry, and practical capacity depends on dimensions, noise and nesting—not simply the number of variables alone.

## Evidence, limitations and corrections

- 05:37–08:54 explicitly introduces approximate counterfactual retraining and the factual-retrieval control. The strongest result is shared influence for different instances of the same reasoning task, not proof of arbitrary formal reasoning.

- 11:47–14:44 reports code’s positive and negative influence and acknowledges no clear explanation for its cross-task effects. This is a useful open question, not a demonstrated recipe that more code always improves reasoning.

- 26:54–28:28 carefully distinguishes controlled demonstrations of systematicity from the present paper’s narrower evidence on naturally occurring pretraining data.

- 42:03–45:21 discusses tensor-product representations but contains uncertainty and a paper mentioned explicitly as unread. I treat the mechanism as an introduction; the loose dimensional-complexity discussion and unread-title inference are not established results.

- 09:19–09:25 gives a spoken arithmetic example requiring parentheses: (7−4)×8 differs from standard-precedence 7−4×8. This illustrates why transcript wording is not a formal specification.

- More observational data do not generally identify causal structure: 31:23–32:13 offers an intuition about diversity discouraging shortcuts, not an identifiability theorem. Likewise aphasia evidence can separate language ability from some thought without settling every version of a language-of-thought theory.

## Relevance to my research

High for methodology and conceptual precision. The episode helps replace substrate labels with questions about transferable operations, learning signals, representations and tests. It is particularly useful alongside stronger anti-LLM claims elsewhere in the archive: Ruis repeatedly marks what her experiment establishes and what remains intuition. For my broad research focus, the procedure-learning and compositionality sections are more valuable than the extended speculative safety discussion.

## My viewing plan

**Mode:** I will focus on technical chapters plus optional agency discussion.

**Segments:** - **Start:** 00:04:05
  
  **End:** 00:15:39
  
  **Purpose:** Influence functions, procedural knowledge and cross-representational transfer.

- **Start:** 00:21:30
  
  **End:** 00:28:28
  
  **Purpose:** Retrieval/reasoning boundaries, failures and the actual strength of the evidence.

- **Start:** 00:33:30
  
  **End:** 00:45:21
  
  **Purpose:** Systematicity, distributed representations and role/filler binding, with the stated technical caveats.

- **Start:** 00:48:47
  
  **End:** 00:53:51
  
  **Purpose:** Operational agency, policy adaptation and planning under uncertainty.

- **Start:** 01:15:47
  
  **End:** 01:17:49
  
  **Purpose:** Capability elicitation without test-set prompt overfitting.

**Edition:** Complete saved transcript read, including opening teaser and sponsors. Generic speaker labels and many proper-name errors are present; timestamps refer to this edition and audio/current playback alignment was not verified.

## Objections and open questions

Shared task influence might reflect task vocabulary, formatting or shallow templates rather than execution of the intended procedure. Conversely, occasional errors do not rule out a learned algorithm that is imperfectly invoked or executed. I would use controlled interventions and extrapolation tests rather than settle the argument by choosing a broad or narrow definition of reasoning.

## An experiment I could try

I want to train a small model on procedural code descriptions, worked traces and factual statements in separately tracked corpora. Influence estimates for multiple numeric instances would guide actual removal or upweighting of document clusters, followed by retraining across several seeds. The tests would include matched-format controls, novel numeric ranges, new compositions and paraphrases. My questions are whether influence similarity predicts causal performance changes and whether code-to-trace transfer survives removal of near-duplicate solutions.

## Connections in my notes

- ARC-winning algorithm: task-specific adaptation and representation affect apparent reasoning; separate candidate generation from correctness.

- Chollet: systematic novelty must be operationalized rather than inferred from ordinary held-out accuracy.

- Beck: explicit modular world models are one proposal; this episode explores when useful structure can be learned implicitly.

## Source and coverage

**Read:** Entire available transcript, sequentially; not audio verified.

**Last timestamp:** 01:17:51

**Source caveats:** ASR/publisher transcript may contain wording and mathematical transcription errors; timestamps refer to this saved edition.

Source type: Publisher transcript. Reviewed text: 15,068 words.

Transcript file: `14DXtvRJeNU.publisher.txt` (not distributed).

SHA-256: `c08c18a8f1b0b69462d5117a986c9f4a60026fdd3cfa8e21feee85261b85bee2`.

[Structured review](14DXtvRJeNU.json) · [Source ledger](../sources.json)
