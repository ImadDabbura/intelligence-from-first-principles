# Don't invent faster horses - Prof. Jeff Clune

[Original episode](https://www.youtube.com/watch?v=mw5WIDGRLnA) · [All reviews](../README.md) · [Learning path](../learning-path.md)

Published: 2025-01-03 · Decision: **Core** · Confidence: High on relevance and algorithmic distinctions; long-run open-endedness remains unproved.

## Central claim

The object of learning can be the process that generates tasks, discoveries, and learning systems, rather than a predictor for a fixed task. Preserving diverse stepping stones and using learned judgments of interestingness creates a concrete research program for studying the origin of intelligence, with unresolved evaluation and search limits.

## Ideas I want to keep

- Open-ended search needs persistent diversity rather than only successive best solutions. Archives preserve inventions whose value becomes apparent only under later recombination, changing the effective search topology and the available curriculum.

- Novelty, learning progress, and interestingness are distinct. Noisy television supplies new observations without useful structure; memorizing successive random digits supplies progress without the kind of innovation sought. These counterexamples reveal which property a proposed intrinsic reward actually measures.

- Foundation models can supply a learned cultural prior over interesting changes. Clune explicitly separates this practical, human-bootstrapped problem from generating open-endedness without importing human knowledge. That distinction matters if the goal is explaining intelligence’s origins.

- Environment generation and agent learning can coevolve. POET and OMNI-EPIC supply a lineage of challenges, while language-model code mutation broadens the space beyond one fixed simulator. The environment is now a learned variable, not merely the background distribution.

- Automated design of agentic systems searches over programs that orchestrate models and tools. This moves the learning boundary outward: reflection, critique, and tool selection can themselves be selected and recombined rather than fixed by a designer.

- Thought cloning adds intermediate planning supervision to action imitation. The toy experiments reportedly improve sample efficiency and out-of-distribution adaptation; the deeper data question is whether demonstrations show expert execution or the exploration by which expertise was acquired.

## Mathematical anatomy

**Objects:** An archive A of environments, policies, research artifacts, or agent programs; a proposal distribution conditioned on selected archive entries; a novelty or interestingness judge; performance measurements; and optional transfer between learners.

**Objective:** Maintain an expanding repertoire of useful or interesting alternatives rather than optimize one predetermined terminal score. Local objectives remain present: solve an environment, improve an agent, or judge whether a proposed artifact adds something distinct.

**Mechanism:** A model generates a candidate from existing artifacts; execution evaluates feasibility and performance; retrieval supplies nearby archive examples for a second novelty check; accepted candidates enrich future proposal context. The transcript describes selecting an environment plus nearby embedding neighbors, then retrieving neighbors of the new candidate to check duplication. Thought cloning factors action choice through supervised intermediate thought tokens as well as observations.

**Assumptions:** Archive entries must preserve transferable information; learned interestingness must remain informative outside its training culture; generated environments must be valid and learnable; and evaluation must distinguish real capability from exploiting the simulator or judge.

**Limits:** Expressive search spaces do not guarantee effective exploration or endless novelty. A finite neural network is not literally capable of representing every computable environment merely because universal approximation exists. Code is computationally general only under idealized resource assumptions; neither program expressivity nor neural simulation establishes Darwin-complete behavior in practice.

## Evidence, limitations and corrections

- At 00:12:34–00:18:10 the noisy-TV and random-digit examples diagnose concrete proxy failures. Replacing a hand-written score with a learned judge changes the proxy; it does not remove Goodhart effects or make interestingness mathematically undefinable.

- At 00:19:57–00:24:05 an AI-scientist grokking proposal and apparent independent human rediscovery motivate optimism. One anecdote cannot establish priority, absence of training contamination, or indefinite scientific creativity.

- At 00:44:27–00:46:56 thought-cloning evidence comes from a small synthetic setting with access to a bot’s planner. Human narration is not direct access to internal reasoning, and behavioral cloning can learn latent state rather than being restricted to reflexes.

- At 01:43:16–01:48:05 the apparent phylogenetic tree is explicitly revealed as a visualization of a more complicated inheritance graph: candidates may have several parents, and the drawn edge picks a close one. The displayed tree alone does not establish causal ancestry or independence.

- The interview repeatedly acknowledges that indefinite open-endedness has not been solved. Continual-learning impossibility language is too broad; it describes dissatisfaction with general frontier systems, not a proof that no online learner can retain knowledge.

- Evolutionary historical anecdotes contain uncertain details, and governance, immortality, and future threat scenarios are opinions or forecasts. They were read but not independently verified and are not the basis of this recommendation.

## Relevance to my research

Core to my broader intelligence agenda because it asks where tasks, representations, exploration incentives and accumulated knowledge come from. It gives executable alternatives to fixed-objective learning and distinguishes explaining intelligence’s original emergence from bootstrapping new intelligence using existing culture.

## My viewing plan

**Mode:** The technical chapters are core to my learning goals; the extended governance discussion is optional.

**Segments:** - **Start:** 00:05:14
  
  **End:** 00:40:31
  
  **Purpose:** Abstraction, interestingness failures, archives, and environment expressivity.

- **Start:** 00:41:13
  
  **End:** 00:49:24
  
  **Purpose:** Thought cloning, exploration data, and emergent communication.

- **Start:** 01:12:03
  
  **End:** 01:35:34
  
  **Purpose:** Agent-system search, continual learning, task lineages, and capability discovery.

- **Start:** 01:35:47
  
  **End:** 01:48:07
  
  **Purpose:** Contingency experiments and the actual multi-parent archive mechanism.

**Edition:** Saved edition ends 02:00:01; includes a long safety/governance digression around 00:49:53–01:12:03. Not audio verified.

**Intention:** The technical chapters are central to my learning goals; I would leave the extended governance discussion optional.

## Objections and open questions

A culturally trained judge may conserve existing tastes and reject precisely the alien discoveries the program seeks. Unbounded archives incur retrieval and evaluation costs, and apparent diversity may be cosmetic. Direct optimization can outperform diversity search when its objective is informative. The right claim is conditional advantage under deceptive or incomplete objectives, not that goals generally prevent progress.

## An experiment I could try

I want to build a small program-generating environment archive and compare greedy performance selection, novelty-only selection, learning-progress selection and a learned interestingness judge under equal compute. A noisy-TV trap and a random-digit memorization task would test the signals. Held-out skill transfer, behavioral diversity, archive reuse and judge gaming would be measured, with actual parent sets retained so the ancestry plot is not mistaken for a tree.

## Connections in my notes

- Stanley: deceptive objectives and stepping-stone preservation are the philosophical and algorithmic foundation.

- Hughes: replication, question selection, and learned evaluation turn open-endedness into an AI-scientist workflow.

- Blaise Agüera y Arcas: bottom-up artificial life addresses a different level from culturally bootstrapped task generation.

- Ruis: linguistic or code supervision can change reasoning behavior without proving that verbal traces expose the full mechanism.

## Source and coverage

**Read:** Entire available transcript, sequentially; not audio verified.

**Last timestamp:** 02:00:01

**Source caveats:** ASR/publisher transcript may contain wording and mathematical transcription errors; timestamps refer to this saved edition.

Source type: Publisher transcript. Reviewed text: 26,384 words.

Transcript file: `mw5WIDGRLnA.publisher.txt` (not distributed).

SHA-256: `0599beb1ccff558c67253fc32ca8d6d6a3f6f27bd5c2554e3f81575c867a0ff4`.

[Structured review](mw5WIDGRLnA.json) · [Source ledger](../sources.json)
