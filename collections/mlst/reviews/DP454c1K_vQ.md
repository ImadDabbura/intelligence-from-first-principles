# The Man Who Invented Modern AI (Before Everyone Else) — Jürgen Schmidhuber

[Original episode](https://www.youtube.com/watch?v=DP454c1K_vQ) · [All reviews](../README.md) · [Learning path](../learning-path.md)

Published: 2024-08-28 · Decision: **Worthwhile** · Confidence: high for useful distinctions; moderate for the episode as a technically reliable standalone source

## Central claim

The durable contribution is a unified research program in resource-bounded program search, learned use of world models, fast memory and curiosity as compression progress. Its value is reduced by sweeping expressivity claims and celebratory historical framing that require explicit correction.

## Ideas I want to keep

- At 06:35–21:40, the debate usefully separates the computational substrate from the training algorithm. A recurrent circuit can implement a state machine; gradient descent may still fail to find the desired circuit. Parity provides an intuitive example of compact temporal state. Equating a neural architecture with SGD obscures alternatives such as random weight search and program-generated weights. Conversely, emulating a finite laptop does not settle efficient learning or unbounded formal-language recognition.

- At 22:24–25:22 and 01:31:40–01:34:28, universal search and OOPS introduce bias through program description and runtime rather than only parameter count. Candidate programs may themselves generate neural weights or invoke learned procedures. This dissolves a simplistic symbolic/neural opposition: the search space, primitive operations, verification procedure and resource allocation are independently chosen design elements.

- At 34:27–46:53, a predictive world model is not automatically an efficient planner. The controller learns which internal representations to query, how to interpret responses and when those queries improve behavior. This is a concrete interface-learning problem, illustrated by transferring throwing knowledge across different bodies. It replaces exhaustive microscopic rollout with a proposed learned abstraction process, while acknowledging that the proposal still needs effective learning.

- At 51:29–01:05:21, curiosity is refined from maximizing prediction error to seeking learnable regularities. Pure surprise rewards irreducible noise; compression improvement can reward experiments at the current learning frontier. The explanation connects prediction, description length, scientific discovery and reusable subprograms, with an explicit reminder that encoding/decoding time also matters.

- At 01:05:42–01:10:40, slow weights learn how to update fast associative memory using key/value outer products and retrieve it with queries. This gives a mechanistic bridge between recurrent memory and linear attention, showing how a trained learning rule can alter working memory at inference time without treating every change as another SGD update.

## Mathematical anatomy

**Objects:** Programs p with a chosen description language and prior, execution/verification times, recurrent controller state, a predictive world model M, query/response channels, fast memory W and a compressor whose quality changes with experience.

**Objective:** The controller maximizes task return subject to practical time/interaction costs; a curiosity variant rewards improvement in compression of comparable data. Universal-search-style scheduling favors candidates according to program probability and runtime, not an oracle for the exact shortest program.

**Mechanism:** A schematic fast-memory update W_t=W_(t−1)+v_t k_t^T with retrieval W_t q_t realizes an associative computation; interference and forgetting constrain capacity. A schematic intrinsic reward L_old(D)−L_new(D), measured on the same appropriate data with model cost accounted for, distinguishes learning progress from raw error. Learned queries access useful latent knowledge without requiring full pixel-level rollouts.

**Assumptions:** Program encoding and primitive costs define simplicity; candidate solutions must be verifiable; reusable world-model knowledge must be relevant and accessible to the controller; apparent compression progress must not be merely overfitting, forgetting or changing the evaluation data.

**Limits:** Universal-search optimality hides potentially enormous constants tied to program probability and does not make hard search cheap. Kolmogorov complexity is not computable in general. A compact description can still be slow, poorly learned or mismatched to the task distribution. The 2015 learning-to-think paper describes an architecture/research proposal, with experiments deferred, not a demonstrated general planner.

## Evidence, limitations and corrections

- The repeated blanket claim that transformers cannot solve parity is false without specifying architecture, precision, normalization, length-generalization criterion and resource scaling. Chiang and Cholak construct a transformer recognizing parity perfectly; their work also distinguishes cross-entropy/confidence limits from classification accuracy. This is a central correction, not a cosmetic exception.

- The NAND-gate analogy supports finite computational emulation, not automatic learnability. Three successful parity examples cannot certify all lengths for an arbitrary sampled recurrent network; a proof of its transition invariant or wider testing is needed.

- The primary fast-weight equivalence concerns linearized attention. Schmidhuber himself acknowledges at 01:11:12 that this differs from the standard quadratic transformer. Shared ideas do not establish that every later architecture or GAN objective is identical to the early system, and the title’s singular-inventor framing is not a scientific conclusion.

- Parameter count alone does not monotonically determine generalization, and universal approximation does not establish trainability. The episode’s physical analogies also overreach: constancy of locally measured light speed is not the whole derivation of general relativity, and planetary orbital analogies are not a faithful theory of quantum electrons. They illustrate compression rhetoric, not verified physics.

- Claims about AGI dates, cosmic expansion of AI and current model rankings are forecasts or historical opinions. They are unnecessary to the useful architecture-level arguments and are not endorsed by this review.

## Relevance to my research

Substantial: I want to ask separately what a system can express, what search discovers, what prior prefers, what memory updates, and what observation is worth acquiring. The learned-controller/world-model interface and compression-progress distinction are particularly relevant to intelligence beyond language modeling. I will pair it with more disciplined empirical episodes and keep these limitations in view.

## My viewing plan

**Mode:** I will focus on these chapters.

**Ranges:** - **Start:** 00:06:35
  
  **End:** 00:25:22
  
  **Why:** Substrate versus learning algorithm; parity example and resource-bounded program search, with expressivity corrections.

- **Start:** 00:34:27
  
  **End:** 00:46:53
  
  **Why:** Learning to query a world model and abstract planning.

- **Start:** 00:51:29
  
  **End:** 01:05:21
  
  **Why:** Curiosity as compression progress rather than surprise.

- **Start:** 01:05:42
  
  **End:** 01:10:40
  
  **Why:** Slow control of fast associative memory.

- **Start:** 01:31:40
  
  **End:** 01:34:28
  
  **Why:** Short programs generating neural weights.

**Edition note:** All timestamps are observed local-ASR timestamps in part one, ending 01:39:22. No claim is made about the rest of the seven-hour recorded conversation.

## Objections and open questions

Compression is a powerful unifying language but can conceal rather than solve the hard problem: how to search efficiently for the right compressor, choose experiments and preserve task-relevant rare details. A broad assertion that everything is compression is less explanatory than an executable mechanism with measured costs. The episode is useful precisely when these missing pieces become explicit research questions.

## An experiment I could try

I want to build an agent choosing among a predictable stream, pure noise and a stream generated by a learnable hidden rule. Raw prediction-error reward, held-out compression-improvement reward and task-return reward would be compared under identical compute budgets. A rare but task-critical exception would test whether generic compression curiosity neglects it. Separately, I would verify a hand-built parity state machine by induction before comparing SGD and random-search discovery.

## Connections in my notes

- Rocktäschel: open-ended learning requires choosing a moving learning frontier, with objective design still unresolved.

- Valpola: predictive modeling and planning have different failure modes; model exploitation is a useful complementary test.

- Hochreiter: xLSTM provides more architecture-specific treatment of recurrent memory.

- Chaudhuri and Szegedy: learned proposals plus explicit verification offer a more concrete route from program-search ideas to reasoning.

## Primary sources checked

- **Title:** On Learning to Think
  
  **Url:** https://arxiv.org/abs/1511.09249
  
  **Use:** Primary proposal and explicit statement that experiments would appear separately.

- **Title:** Linear Transformers Are Secretly Fast Weight Programmers
  
  **Url:** https://arxiv.org/abs/2102.11174
  
  **Use:** Formal equivalence for linearized attention, with finite-memory limits.

- **Title:** Overcoming a Theoretical Limitation of Self-Attention
  
  **Url:** https://arxiv.org/abs/2202.12172
  
  **Use:** Primary parity construction correcting the interview’s unconditional impossibility claim.

- **Title:** Optimal Ordered Problem Solver
  
  **Url:** https://people.idsia.ch/~juergen/oops.html
  
  **Use:** Primary search framework.

## Source and coverage

**Status:** complete_available_text

**Start:** 00:00:00

**End:** 01:39:22

**Caveats:** - Read all local-ASR text, not audio. This is explicitly part one, despite an introduction mentioning a seven-hour conversation; review covers only this approximately 100-minute edition. ASR corrupts names and terms such as OOPS, Levin and Kolmogorov.

Source type: Local asr. Reviewed text: 14,169 words.

Transcript file: `DP454c1K_vQ.local-asr.txt` (not distributed).

SHA-256: `bd88a77a67036a5aa50a1530fbc69853cabe7ccea0b730dd3b0eaf477bc5dc56`.

[Structured review](DP454c1K_vQ.json) · [Source ledger](../sources.json)
