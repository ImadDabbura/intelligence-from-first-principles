# He Co-Invented the Transformer. Now: Continuous Thought Machines [Llion Jones / Luke Darlow]

[Original episode](https://www.youtube.com/watch?v=DtePicx_kFY) · [All reviews](../README.md) · [Learning path](../learning-path.md)

Published: 2025-11-23 · Decision: **Worthwhile** · Confidence: high for adaptive-computation concepts; conditional for superiority claims

## Central claim

A recurrent model can represent computation through temporal relationships among units and allocate different amounts of internal work to different examples, making reasoning a process rather than a single fixed-depth output.

## Ideas I want to keep

- The Continuous Thought Machine separates an internal sequence of computational ticks from the external output sequence. This gives a concrete architectural handle on latent iterative reasoning rather than requiring every extra computation to be expressed as a word.

- Neuron-level models process a finite history of incoming activations, replacing a memoryless scalar activation with a small learned temporal computation. This changes what an individual unit can detect before the system-level representation is formed.

- The proposed representation is pairwise synchronization of activation histories, computed through dot-product-like statistics with different exponential decay rates. Short and long temporal relationships can coexist in one recurrent state description.

- The classification loss supervises both the lowest-loss tick and the most-confident tick. The authors report that easy examples become confidently correct earlier while difficult ones use more ticks, linking an anytime prediction trajectory with adaptive stopping.

- The maze curriculum trains a little beyond the currently correct path prefix. It distinguishes predicting a whole path image from generating a valid sequential route, showing how the task interface changes computational difficulty.

- Observed backtracking and leapfrogging under restricted time motivate a strong experiment: change the compute budget and ask whether the learned algorithm changes, not just whether the final score rises. The later Sudoku discussion adds the separate bottleneck of discovering rare useful reasoning primitives.

## Mathematical anatomy

**Objects:** Recurrent activation histories h_i(1:t), neuron-specific history processors, selected pairs (i,j), decay parameters and per-tick output distributions.

**Objective:** Task loss at selected internal ticks; for classification the described objective averages cross-entropy at best-performing and most-confident ticks. Maze supervision grows with solved prefix length.

**Mechanism:** A conceptual synchronization statistic is S_ij(t)=∑τ≤t exp[-λ_ij(t−τ)]h_i(τ)h_j(τ), with the paper’s normalization/details not derived in the interview. Recurrent updates and attention to inputs use this temporal representation.

**Assumptions:** Useful task structure is captured by pairwise temporal statistics; the training horizon supports the desired computation; confidence is reliable enough to select a stopping point.

**Limits:** All-pairs features scale quadratically in state width, motivating subsampling. A finite unrolled recurrent model with bounded memory is not thereby an unbounded Turing machine. “Continuous” refers here to ongoing internal computation and continuous-valued states, not a demonstrated continuous-time physical system.

## Evidence, limitations and corrections

- The researchers explicitly describe biological inspiration rather than literal biological plausibility. Synchronization is an engineering choice, not evidence that the model shares human thought mechanisms.

- The claim of near-perfect calibration is an empirical report on the tested setup, not a guarantee under distribution shift. Calibration concerns frequencies across predictions, not whether every high-confidence individual decision is justified.

- Backtracking/leapfrogging are interesting observed behaviors. Attention or rollout visualizations alone do not prove a unique internal planning algorithm; causal interventions are needed.

- The architecture’s potential for language modeling, shared cultural memory and ambiguous mazes is repeatedly described as ongoing or untried work. Those possibilities should not be counted as achieved capabilities.

- The spiral example illustrates an inductive-bias preference but does not prove that an aesthetically spiral boundary is always the correct extrapolation. Many continuations fit finite data.

- The long opening argument about research incentives is motivating context; it does not establish that transformers are a dead end or that CTMs dominate at matched resources.

## Relevance to my research

A valuable concrete alternative for my thinking about representation, time and compute. Its relevance is not that it must be the next dominant architecture, but that it exposes design dimensions hidden by a fixed-depth network: state history, temporal statistics, stopping, curriculum and compute-conditioned algorithms.

## My viewing plan

**Mode:** I will focus on the technical interview and benchmark discussion.

**Segments:** - **Start:** 00:28:58
  
  **End:** 00:50:27
  
  **Purpose:** Architecture, temporal representations, loss, adaptive computation and calibration.

- **Start:** 00:56:00
  
  **End:** 01:00:43
  
  **Purpose:** Observed algorithm changes and proposed memory experiments.

- **Start:** 01:00:43
  
  **End:** 01:11:37
  
  **Purpose:** Variant Sudoku, human reasoning traces and rare-discovery limits of RL.

**Edition:** Saved publisher timestamps. Early architecture-research discussion is optional context.

## Objections and open questions

A richer temporal representation may help because it adds capacity, changes optimization or supplies extra compute; each explanation needs a matched baseline. A confidence-based early exit can create selection bias. Flexible recurrence alone does not ensure causal reasoning, systematic extrapolation or a faithful verbal account of its computation.

## An experiment I could try

On small maze families, I want to compare a recurrent state model, the same model with history-based units and one with synchronization features at matched parameters and tick budgets. Training on short paths and testing long paths plus changed topology would expose generalization limits. Per-tick calibration, stopping regret and path validity would be recorded. Perturbing a purportedly planning-related state or synchronization pair would test whether the observed backtracking behavior causally depends on it.

## Connections in my notes

- Adaptive computation and recurrent algorithm learning

- Temporal representations and multi-scale memory

- Calibration and selective prediction

- Curriculum learning and rare reasoning discoveries

## Source and coverage

**Read:** Entire available transcript, sequentially; not audio verified.

**Last timestamp:** 01:12:34

**Source caveats:** ASR/publisher transcript may contain wording and mathematical transcription errors; timestamps refer to this saved edition.

Source type: Publisher transcript. Reviewed text: 12,436 words.

Transcript file: `DtePicx_kFY.publisher.txt` (not distributed).

SHA-256: `eccda42c96f24dbf81ffd2f71dcdd9f705a2da3f31293adb1b13c5a32f487486`.

[Structured review](DtePicx_kFY.json) · [Source ledger](../sources.json)
