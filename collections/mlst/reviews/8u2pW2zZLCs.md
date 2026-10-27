# LSTM: The Comeback Story? [Prof. Sepp Hochreiter]

[Original episode](https://www.youtube.com/watch?v=8u2pW2zZLCs) · [All reviews](../README.md) · [Learning path](../learning-path.md)

Published: 2025-02-11 · Decision: **Worthwhile** · Confidence: high

## Central claim

The lasting contribution is an account of intelligence as selective, revisable state: what to retain, when to overwrite it, and how to preserve the learning signal that teaches those decisions. The xLSTM discussion makes a useful architectural counterpoint to attention. Claims that language models categorically cannot invent concepts are much less defensible than the memory mechanisms.

## Ideas I want to keep

- At 00:15:24–00:20:38, Hochreiter connects the vanishing-gradient problem to the concrete need to remember an early observation until a delayed target arrives. Gated memory separates persistence from incoming computation, turning long-term credit assignment into an architectural design problem rather than merely a larger-data problem.

- At 00:24:57–00:34:10, exponential gating is motivated by revising an earlier storage decision when a much better candidate arrives. The clothes-selection example exposes the difference between representing information and retaining the ability to change its relative importance. Normalization and stabilization are indispensable parts of that proposal.

- At 00:29:51–00:30:49, matrix memory stores key–value associations through outer products. This connects recurrence, associative retrieval and fast weights: a model can update a compact internal data structure on every observation without changing its slow trained parameters.

- At 00:20:54–00:24:47 and 00:37:15–00:42:25, computational complexity and hardware efficiency are separated. A recurrent fixed-size state has attractive sequence-length scaling, yet a parallel quadratic method can win on real accelerators. Architectural theories need both an information-storage account and an execution model.

- At 00:55:00–01:00:25, useful abstractions need not match human vocabulary. An invertible change of coordinates can preserve represented information while changing the apparent concepts, cautioning against identifying intelligence with human-readable individual features.

## Mathematical anatomy

**Objects:** Input sequence, persistent scalar or matrix state, learned input/forget gates, keys, values and queries; slow parameters versus rapidly updated memory.

**Objective:** Predict or act from history while retaining information relevant to later targets under a bounded state and computational budget.

**Mechanism:** A schematic scalar update c_t=f_t c_(t−1)+i_t z_t illustrates the protected memory path; its direct gradient contains products of forget gates. Matrix memory instead accumulates gated v_t k_t^T terms and retrieves through a query, with normalization. These are explanatory schematics, not a complete implementation specification.

**Assumptions:** Relevant history can be compressed into the chosen state; gates can learn relevance before supervision arrives; normalization makes exponential weighting numerically tractable.

**Limits:** Fixed memory creates interference and irreversible information loss. Preserving one gradient path does not eliminate all optimization problems. Attention scores are pairwise, but stacked attention networks can represent higher-order interactions. Compression alone does not prove formation of useful abstractions.

## Evidence, limitations and corrections

- The original xLSTM paper abstract confirms exponential gates, scalar-memory sLSTM and parallelizable matrix-memory mLSTM. Its reported comparisons support a concrete research program, not universal superiority over all Transformers or state-space models.

- The opening assertion that LLMs cannot create new concepts is neither operationally defined nor demonstrated. The interview itself concedes extensive compositional novelty and productive search; architectural limitations must be distinguished from categorical impossibility.

- The transcript’s exponential/softplus/sigmoid equivalence near 00:36 is unsafe to reproduce literally: signs and arguments matter. Likewise, the hypothesized benefit of gradient peaks is presented as an explanation under investigation.

- Anonymous deployment stories, future scaling expectations and the simulation company’s dramatic speedup numbers are claims in the interview, not independently verified comparisons. Classical scientific computing already uses coarse-graining; learned aggregation is a possible improvement, not its invention.

## Relevance to my research

Substantial for my thinking about intelligence as controlled information persistence and transformation. It puts memory capacity, revision, numerical stability, credit assignment and hardware costs in one causal picture. The scientific value is strongest when the mechanism is separated from the guest’s broad philosophical and commercial claims.

## My viewing plan

**Mode:** I will focus on these chapters.

**Ranges:** - **Start:** 00:15:24
  
  **End:** 00:34:10
  
  **Why:** Vanishing gradients, gated state, matrix memory and revisable storage; the central technical argument.

- **Start:** 00:37:15
  
  **End:** 00:42:25
  
  **Why:** Hardware and deployment tradeoffs, while treating performance anecdotes cautiously.

- **Start:** 00:53:08
  
  **End:** 01:00:25
  
  **Why:** Continuum of deliberation and the coordinate-dependence of human-readable concepts.

**Edition note:** Timestamps are observed in the saved publisher transcript; alignment with the YouTube edition remains to be checked. Full viewing remains reasonable for historical context but the opening and ending contain substantial overstatement.

## Objections and open questions

A large context window can preserve details that a fixed state discards; task-dependent retrieval can be more useful than premature compression. Conversely, recurrence may force a useful sufficient statistic. Neither outcome follows from memory size alone, and a hybrid may be preferable. Formal tools can improve correctness without establishing that neural systems are intrinsically incapable of reasoning.

## An experiment I could try

I want to implement gated scalar memory and gated outer-product associative memory on delayed key–value recall with distractors and a later correction to an earlier value. State bits, numerical precision and training compute would be held approximately fixed while sequence length and revision frequency vary. Recall, overwrite errors, gradient norms and throughput would be compared with a context-buffer attention baseline. My question is which failures reflect insufficient capacity, interference or failed credit assignment.

## Connections in my notes

- Barbero’s finite-precision discussion: compact state is an information bottleneck whose behavior depends on architecture and precision.

- Hübotter’s test-time learning: distinguish updating fast memory from updating trained model parameters.

- Formal reasoning discussion here motivates hybrid search and verification but does not provide a complete formal reasoning architecture.

## Primary sources checked

- **Title:** xLSTM: Extended Long Short-Term Memory
  
  **Url:** https://arxiv.org/abs/2405.04517
  
  **Use:** Checked the abstract for gate and memory variants; did not independently reproduce speed or scaling results.

## Source and coverage

**Status:** complete_available_text

**Start:** 00:00:00

**End:** 01:06:55

**Caveats:** - Read the complete publisher transcript, including introduction, historical discussion and commercial ending. Audio and equations on screen were not independently checked. Automatic transcription occasionally garbles technical expressions.

Source type: Publisher transcript. Reviewed text: 12,181 words.

Transcript file: `8u2pW2zZLCs.publisher.txt` (not distributed).

SHA-256: `10d63b374d040de167fa152a7d7eb8107291f814fd467e8db0075b89603ad197`.

[Structured review](8u2pW2zZLCs.json) · [Source ledger](../sources.json)
