# How can we add knowledge to AI agents?

[Original episode](https://www.youtube.com/watch?v=qxEfcrmTWO4) · [All reviews](../README.md) · [Learning path](../learning-path.md)

Published: 2023-11-05 · Decision: **Worthwhile** · Confidence: high about value and limitations; medium on local ASR detail

## Central claim

The useful research agenda is to combine explicit generative structure, informative priors, and active data acquisition. The interview exposes that a proposed universal principle does not itself solve structure discovery, scalable inference, or interpretability.

## Ideas I want to keep

- At 14–19 minutes Da Costa identifies the missing algorithmic step: discovering a world model, rather than merely inferring states inside a supplied model. Object permanence and agent/object primitives restrict hypothesis space; their benefit is a search and sample-efficiency claim, not a magical consequence of free-energy minimization.

- The contrast at 21–25 minutes between human-like and unconstrained intelligence usefully separates matching human learning trajectories from maximizing task performance. Priors can improve transfer in the intended environment and remove otherwise available hypotheses; the tradeoff depends on distribution and compute, not a scalar quantity called amount of knowledge.

- At 34–42 minutes the host asks what active inference adds beyond agent architectures, then challenges the inference from simple objective to understandable computation. Factor graphs expose conditional dependency structure and message flow; this is a concrete architectural proposal distinct from invoking free energy.

- The late exchange distinguishes descriptive models of human acquisition from engineering intelligence. Da Costa corrects an initially broad Atari comparison: the theory-based learning examples concern simplified Atari-like environments, and the later core-knowledge version improves correspondence. This qualification is central to interpreting sample efficiency.

## Mathematical anatomy

**Objects:** Latent world states z, observations o, candidate model structures M, priors p(M), approximate posterior q(z,M), and action policies that change future evidence. A factor graph expresses p(z,o|M) as a product of factors.

**Assumptions:** The physics story presupposes an appropriate dynamical description and boundary conditions. The engineering story additionally needs a model family, meaningful variables, prior constraints, inference method, and costs. None is supplied just by observing that agents have boundaries.

**Objective:** For a fixed model, F(q)=E_q[log q(z)-log p(o,z)]=KL(q||p(z|o))-log p(o). Equivalently F is complexity minus expected log-likelihood; the spoken accuracy-minus-complexity phrasing at 44 minutes reverses the conventional minimization sign. Structural selection must also account for model prior and approximate evidence.

**Mechanism:** The proposed mechanism restricts model search using core knowledge, infers latent states by factor-graph message passing, selects informative or useful actions, and prunes or revises structures. These are distinguishable modules: a sparse graph can still contain difficult inference or opaque factors.

**Limits:** The KL complexity term does not automatically count graph edges or guarantee semantic interpretability. More restrictive priors do not invariably improve learning, Bayesian model reduction does not guarantee easy recovery after arbitrary distribution shift, and minimizing an approximate objective does not identify the true world model.

## Evidence, limitations and corrections

- The opening assertion that an SDE plus a sensory/active boundary automatically proves universal Bayesian intelligence is substantially stronger than the argument supplied. Even Da Costa and Heins’s technical commentary states sparse dynamical coupling does not generally guarantee a Markov blanket and derives additional conditions. That paper supports demanding explicit hypotheses, not rejecting all active-inference constructions.

- The host provides valuable pushback at 37–40 minutes: simple cellular-automaton rules can produce hard-to-understand behavior, and compositions of readable program primitives can become unintelligible. Replacing neural networks with factors does not remove this objection.

- Claims that an explicit generative model unlocks safety are ambitions, not demonstrated safety guarantees. A perfectly explainable policy may optimize wrong preferences or act on a misspecified environment.

- The episode’s portrayal of the Bitter Lesson as rejecting all symmetries/priors is too sweeping; its human-Elo objection also confuses validity of a particular performance measurement with broad cross-domain inference. The important point is that equal scores do not establish equal capability profiles.

- The late correction at 48–49 minutes narrows the human-learning comparison to simplified games. No complete algorithm, benchmark table, or theorem proof appears in this interview.

## Relevance to my research

Worthwhile because it turns a universal-law ambition into three concrete bottlenecks: hypothesis language, structure search and semantic interpretability. My most productive question is which priors reduce computational search while retaining the right counterfactuals. The episode is less useful as evidence that physics uniquely determines intelligence.

## My viewing plan

**Mode:** chapters

**Segments:** - **Start:** 00:14:03
  
  **End:** 00:25:01
  
  **Purpose:** Structure learning, core knowledge, and the difference between human modeling and engineering goals.

- **Start:** 00:34:04
  
  **End:** 00:49:03
  
  **Purpose:** What active inference contributes, the interpretability objection, factor graphs, and the simplified-game qualification.

**Edition note:** Observed timestamps in locally transcribed publisher podcast; RSS duration differs from listed video by one second. No audio alignment verified.

**Intention:** I would watch the chapters that expose the structure-learning gap and challenge claims about interpretability.

## Objections and open questions

- Hard structural priors can exclude the generative explanation needed after a change of environment; flexible neural representations can sometimes expose scientific structure through experiments despite lacking immediate verbal labels.

- A common probabilistic objective can unify descriptions without selecting a uniquely effective algorithm or proving that all intelligent behavior has the same implementation.

## An experiment I could try

I would create a partially observed object world with occlusion, teleportation in a held-out regime and optional interventions. Bayesian model families with hard permanence, soft permanence and no object identity would be compared on posterior predictive log loss, interaction count, model-search time and recovery after teleportation begins. Representing identical likelihoods as one large factor or many small factors would then test whether graph sparsity improves explanation or merely redraws the same computation.

## Connections in my notes

- DreamCoder/Palmarini: learning reusable primitives addresses part of the structure-search gap.

- Parr and Friston episodes: distinguish an engineering active-inference model from a universal physical characterization.

- Molnar: intelligible representation and faithful causal explanation are separate requirements.

## Primary sources checked

- **Url:** https://arxiv.org/abs/2205.10190
  
  **Claim:** Author commentary explicitly distinguishes sparse coupling from Markov-blanket conditions; abstract checked.

## Source and coverage

**Status:** complete_available_text

**Method:** Read entire saved transcript in contiguous bounded chunks; only repeated timestamp/speaker-label formatting suppressed during reading. Audio and video not checked.

**Last timestamp:** 00:49:52

**Caveats:** - ASR transcription can corrupt names and mathematical terminology; transcript completeness is not an audio audit.

- Source is local Whisper-large-v3-turbo ASR of publisher RSS podcast audio; names, formulas, and speaker assignments can be inaccurate.

- Observed timestamps in locally transcribed publisher podcast; RSS duration differs from listed video by one second. No audio alignment verified.

Source type: Local asr. Reviewed text: 9,160 words.

Transcript file: `qxEfcrmTWO4.local-asr.txt` (not distributed).

SHA-256: `0575e9962b2a65f91742f0d38ea4ec13d03322c9c4bbfacb0a6d716e759f9345`.

[Structured review](qxEfcrmTWO4.json) · [Source ledger](../sources.json)
