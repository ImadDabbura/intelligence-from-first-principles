# Building a GENERAL AI agent with reinforcement learning

[Original episode](https://www.youtube.com/watch?v=s3C0sEwixkQ) · Source: Machine Learning Street Talk · [All reviews](../README.md) · [Learning path](../learning-path.md)

Published: 2024-03-20 · Decision: **Core** · Confidence: High for the mathematical problem formulation and research value; moderate for broad claims about general intelligence.

## Central claim

A concrete bridge between world models, active data acquisition and robust decision-making: learning priorities must be chosen before the eventual reward is known. The central insight is that a general agent needs not only a reusable dynamics model but a curriculum that deliberately repairs its weaknesses across environments.

## Ideas I want to keep

- At 00:03:20–00:05:56, expected return, worst-case return and worst-case regret are distinguished. An unavoidable catastrophe can dominate maximin return and erase incentives elsewhere; regret compares performance to what was achievable in that same environment. This changes which experiences deserve attention.

- At 00:06:01–00:12:17, dynamics learning is separated from the reward attached to a particular task. Transitions supply a dense learning signal, a learned model can be reused when objectives change, and extra computation can support planning at deployment. None of these advantages requires declaring model-free methods incapable of representing dynamics.

- At 00:20:55–00:27:08, the simulation-lemma intuition links decision quality to model error along relevant trajectories. Partial observability requires history-dependent inference, while a latent state compresses history for prediction rather than assuming a single image reveals the physical state.

- At 01:13:41–01:21:20, two acquisition decisions are combined: where to explore inside an environment and which environment to sample next. WAKER targets the second by model-error estimates; an intrinsically motivated explorer supplies experiences in the first. This is more specific than generic curiosity.

- At 01:21:23–01:25:49, the guest corrects the assumption that curricula must monotonically progress from easy to hard. Reward-free model acquisition can need sustained emphasis on difficult environments, with the allocation changing as uncertainty is reduced.

- At 00:51:51–00:53:55 and 01:48:42–01:50:08, capacity limits, forgetting, noisy-TV distraction and synthetic-data saturation reveal how a self-generated training signal can become self-defeating. Information-seeking is relative to a learner, not an automatic measure of useful discovery.

## Mathematical anatomy

**Objects:** A family of partially observed environments, observation/action histories, a learned latent transition model, downstream reward functions and policies planned using that model. The environment family is a design choice, not every possible world.

**Objective:** The conceptual objective minimizes max over environments and allowed rewards of V* minus the return of the policy obtained from the learned model. WAKER uses model-error-related acquisition as a tractable surrogate; it does not calculate true optimal regret in each experimental environment.

**Mechanism:** The agent explores uncertain transitions, updates a dynamics model, and reweights environment sampling toward remaining estimated modeling error. When a reward becomes available, it trains or plans with imagined trajectories. This separates representation acquisition from a particular downstream utility.

**Assumptions:** The theoretical motivation invokes an optimal planner and controlled model-error quantities; practical learning uses approximations. Reward bounds, horizon or discounting, coverage and the allowed task/environment classes matter for interpreting any value-error bound. A useful latent representation must preserve distinctions relevant to future tasks.

**Limits:** An equilibrium characterization is not convergence of neural training. Prediction error, epistemic uncertainty, learning progress and downstream regret are different quantities. If future rewards are literally unrestricted, discarding apparently irrelevant information can destroy future sufficiency. The available simulator also bounds what an automatic curriculum can discover.

## Evidence, limitations and corrections

- Entire local ASR read through 01:57:11. It contains repeated introductory excerpts and imperfect names/technical terms; no audio or figure inspection was performed.

- At 00:18:52–00:20:32 the authors explicitly deny a practical convergence guarantee and explain that true regret is unavailable. This qualification is essential to the surrounding game-theoretic narrative.

- At 01:50:13–01:55:34 the reported evidence is simulated domains, improved worst-environment performance and selected harder out-of-distribution settings. They explicitly say they did not perform the proposed controlled causal-factor evaluation.

- The primary publication abstract confirms reward-free curriculum design and selection using estimated world-model error. This is support for the algorithm’s stated scope, not an independent reproduction of reported gains.

- Statements that intrinsic motivation removes human-designed objectives, that knowing rewards alone yields a computable optimal policy, or that all two-player zero-sum games automatically have the required equilibrium omit important assumptions. Designers still choose the intrinsic signal; dynamics, computation and game regularity still matter.

- The host’s entropy, Occam and model-retrieval analogies are not derivations. Lower-dimensional prediction does not automatically remove nuisance variables, and high uncertainty does not necessarily mean high learnable information.

## Relevance to my research

Core to my research because it turns the question of intelligence into a coupled design problem: what model to retain, what experiment to perform and which future decisions the information should support. It also supplies a concrete alternative to both fixed-dataset learning and unconstrained novelty search.

## My viewing plan

**Mode:** I plan to watch the technical spine closely; broader industry speculation is optional.

**Segments:** - **Start:** 00:01:25
  
  **End:** 00:27:08
  
  **Purpose:** Robustness objectives, dynamics reuse, regret and partial observability.

- **Start:** 00:33:30
  
  **End:** 00:39:35
  
  **Purpose:** Representation sufficiency and curriculum drift outside useful domains.

- **Start:** 00:47:36
  
  **End:** 00:56:46
  
  **Purpose:** Intrinsic motivation, failure cases and reward specification.

- **Start:** 01:13:41
  
  **End:** 01:28:18
  
  **Purpose:** WAKER mechanism and why reward-free curricula need not run easy to hard.

- **Start:** 01:48:42
  
  **End:** 01:55:34
  
  **Purpose:** Synthetic-data limits and what the experiments establish.

**Edition:** All ranges use observed anchors in the full recovered local ASR; alignment to YouTube playback is not independently checked.

**Intention:** I plan to watch the technical spine closely; broader industry speculation is optional.

## Objections and open questions

A worst-case criterion can spend scarce computation on irrelevant environments. A well-chosen prior over likely tasks can outperform uniform robustness for a real user, while a poor uncertainty estimator can repeatedly request unhelpful samples. Conversely, a fixed average objective can neglect rare but consequential failures. The substantive choice is the task family and acquisition criterion, not a universal preference for either approach.

## An experiment I could try

I want to build three small MDPs: a simple deterministic map, a complex learnable map and a map with irreducible random observations. Uniform environment sampling, raw prediction-error sampling and epistemic-disagreement or learning-progress sampling would be compared at equal interaction budgets, with multiple rewards revealed only afterward. I would measure mean return, worst return and exact regret using dynamic programming, then add a reward depending on a previously discarded feature to test the latent representation’s sufficiency.

## Connections in my notes

- Stanley and Clune: supplies a concrete uncertainty-driven curriculum alongside novelty archives and environment/solver coevolution. These are competing acquisition signals, not interchangeable versions of one objective.

- Bennett: operationalizes the questions of what to simulate and when learning additional dynamics is useful.

- Mitchell: the authors’ missing causal-factor evaluation is precisely where construct-validity discipline should enter.

## Primary sources checked

- **Url:** https://proceedings.iclr.cc/paper_files/paper/2024/hash/0a2b3e9107efed3d361b29f300a903ff-Abstract-Conference.html
  
  **Purpose:** Primary abstract checked for algorithm scope and estimated-error curriculum mechanism.

## Source and coverage

**Read:** Entire available selected transcript read sequentially; audio not verified.

**Last timestamp:** 01:57:11

**Source caveats:** Local ASR recovered from episode audio; names, equations and speaker attribution may be inaccurate. Timestamps are ASR segment anchors.

Source type: Local asr. Reviewed text: 24,506 words.

Transcript file: `s3C0sEwixkQ.local-asr.txt` (not distributed).

SHA-256: `295b20386f6264f367dfa7127356274a15038597f530ce0b240f5ac31d865a78`.

[Structured review](s3C0sEwixkQ.json) · [Source ledger](../sources.json)
