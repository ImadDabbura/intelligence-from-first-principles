# Can AI Improve Itself? [Chris Lu, Robert Lange, Cong Lu]

[Original episode](https://www.youtube.com/watch?v=1kwbp8hRRfs) · Source: Machine Learning Street Talk · [All reviews](../README.md) · [Learning path](../learning-path.md)

Published: 2025-03-01 · Decision: **Core** · Confidence: high

## Central claim

Intelligence can improve through an external loop that proposes structured changes, executes them, retains informative results and reuses discoveries. The episode makes several levels of this loop concrete, while its strongest limitation is that producing credible papers or benchmark improvements is not yet cumulative scientific understanding.

## Ideas I want to keep

- DiscoPOP uses an LLM as a code-level mutation operator for preference-training objectives. It replaces blind parameter perturbation with proposals shaped by prior human knowledge, then feeds empirical performance back into context.

- The search substrate matters: a short executable loss is easier to inspect and recombine than a neural-network parameterization of a loss. Readable code and generated rationale nevertheless do not establish the true reason for improved performance.

- Numerical black-box optimization is represented as sequences of candidate vectors and fitness values, ordered to expose improvement. Tokenization, integer discretization and teacher trajectories are part of the learned optimizer’s effective inductive bias.

- Automated agent design searches the organization of computation: prompts, calls, tools, critics and reusable subagents become code that can be recombined from an archive. This extends search from answer generation to the procedure for obtaining answers.

- Intelligent Go-Explore uses a foundation model to select promising archived states and exploration directions. The prior knowledge that makes exploration effective can also systematically hide valuable regions.

- The researchers distinguish a linear paper-production pipeline from iterative science. They explicitly want failed experiments and revised hypotheses to shape subsequent experiments, rather than merely writing up the first idea’s results.

## Mathematical anatomy

**Objects:** Candidate programs c, evaluator E(c), a history or archive H, a proposal distribution q(c|H), downstream task distributions and optional inner trained models.

**Assumptions:** The evaluator measures a useful outcome, execution is controlled, and the proposal prior has relevant structure. Transferring from small discovery tasks to larger tasks requires shared regularities; it is an empirical claim, not guaranteed by meta-optimization.

**Objective:** At the outer level improve performance of losses, optimizers, agent procedures or experiments; at the inner level train or execute the candidate. Open-ended novelty and multiobjective cost control are discussed mainly as extensions beyond the benchmark-driven implementations.

**Mechanism:** Execute a proposal, append score and artifact to context or archive, and sample a revised or recombined program. Different projects apply this same loop to different objects. Scientific hypothesis revision additionally needs evidence capable of distinguishing rival explanations.

**Limits:** Searching a Turing-complete language does not make the finite proposal process universal in practice. Multiple tests overfit evaluators; model-generated judges can reward style or shared biases. More stochastic entropy alone does not restore missing knowledge or guarantee useful novelty.

## Evidence, limitations and corrections

- At 11:00–12:07 the transcript calls the discovered loss nonconvex and discontinuous and offers noisy-data robustness as a hypothesis. Primary paper Appendix E.6 uses smooth sigmoid/logistic/exponential components: nonconvex does not imply discontinuous. The robustness explanation remains a hypothesis, not a proof.

- At 29:08–34:05 smaller-model and numerical-tokenization observations are limited to the tested systems. The speculation about GPT-4 expert sizes is not evidence about its architecture.

- At 55:00–57:02 agents reportedly transfer across base models and tasks, which is more informative than discovery-set performance alone. Exact effect sizes and all evaluation controls were not independently audited here.

- At 01:12:05–01:13:01 Lu explicitly clarifies that Intelligent Go-Explore has not yet been tested on Montezuma’s Revenge in their work. The earlier Montezuma discussion refers to the original Go-Explore lineage.

- At 01:27:01–01:28:01 the authors acknowledge their initial AI Scientist’s experimentation is comparatively linear. Recursive self-improvement and indefinitely growing scientific competence are aspirations beyond the demonstrated system.

- The repeated fourth-generation-collapse claim is not a universal law. Training mixture, data retention, sampling and evaluation determine behavior; neither failure nor immunity follows solely from introducing random prompts.

## Relevance to my research

Core for my interest in learning mechanisms beyond a single model. It shows how prior knowledge, search, environmental feedback, memory and organization jointly produce capability, and asks where new knowledge enters. The most important insight is to distinguish optimizing artifacts from improving a process of inquiry and eventually improving the learner itself.

## My viewing plan

**Mode:** I plan to watch the full technical conversation.

**Segments:** - **Start:** 00:02:14
  
  **End:** 00:15:12
  
  **Purpose:** Structured objective discovery and interpretability of discovered mechanisms.

- **Start:** 00:25:08
  
  **End:** 00:40:12
  
  **Purpose:** Learned optimization representations and cross-scale transfer.

- **Start:** 00:48:01
  
  **End:** 01:19:01
  
  **Purpose:** Agent-program search, archives and exploration; I will distinguish demonstrated from proposed systems.

- **Start:** 01:24:03
  
  **End:** 01:34:03
  
  **Purpose:** Failures, experimental memory and the difference between papers and scientific learning.

**Edition note:** Entire saved transcript through 01:37:02 read. I plan to watch the full technical conversation and skip introductions, sponsorship and company discussion. Names are often corrupted in ASR.

## Objections and open questions

- This family may exploit existing human knowledge without developing new abstractions or autonomous problem selection; external execution supplies evidence, but does not by itself guarantee explanatory science.

- Benchmark optimization can create elaborate expensive procedures whose apparent gain disappears under matched compute, held-out evaluators or new domains. An archive is useful only if retrieval and evaluation preserve valuable diversity.

## An experiment I could try

I want to create a small loss-function discovery loop on synthetic binary classification with controllable label noise. Discovery and final tasks would remain separate, with LLM proposals compared against random combinations of the same primitive losses under matched evaluation budgets and negative results retained. The system would propose rival explanations for a winning loss; I would then choose experiments that distinguish them. The outcome would include both predictive gain and whether the explanation survives intervention.

## Connections in my notes

- DreamCoder supplies a more explicit example of accumulating reusable program abstractions; AlphaEvolve emphasizes execution-grounded search and representation choices.

- POET and Stanley provide alternatives to a fixed performance objective and motivate preserving stepping stones.

- Molnar’s cautions apply to treating generated rationales as mechanistic explanations.

## Primary sources checked

- **Title:** Discovering Preference Optimization Algorithms — NeurIPS 2024, Appendix E.6
  
  **Url:** https://proceedings.neurips.cc/paper_files/paper/2024/file/9d88b87b31986f8293bb0067a841579e-Paper-Conference.pdf
  
  **Scope:** Inspected loss formula/code to distinguish nonconvexity from discontinuity; not a full empirical replication.

## Source and coverage

**Status:** complete_available_text

**Method:** Read entire saved transcript; any truncated tool section reread in bounded chunks. Audio not checked.

**Last timestamp:** 01:37:52

**Caveats:** - ASR transcription can corrupt names and mathematical terminology; transcript completeness is not an audio audit.

Source type: Publisher transcript. Reviewed text: 20,461 words.

Transcript file: `1kwbp8hRRfs.publisher.txt` (not distributed).

SHA-256: `0fa2346840e502ccebb01ff3df5fbb559d7fa583340943d18b202f3b1f3ad889`.

[Structured review](1kwbp8hRRfs.json) · [Source ledger](../sources.json)
