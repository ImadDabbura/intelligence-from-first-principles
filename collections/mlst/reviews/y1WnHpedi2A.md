# Do you think that ChatGPT can reason? [Prof. Subbarao Kambhampati]

[Original episode](https://www.youtube.com/watch?v=y1WnHpedi2A) · [All reviews](../README.md) · [Learning path](../learning-path.md)

Published: 2024-07-29 · Decision: **Worthwhile** · Confidence: high

## Central claim

The durable lesson is to separate proposing a plausible solution, establishing its validity, and learning the problem specification. The strongest contribution is the bidirectional LLM-Modulo architecture and its explicit limits; the universal claim that autoregressive networks cannot reason is not established by the evidence presented.

## Ideas I want to keep

- The planning experiments around 15–18 minutes use semantics-preserving renaming to probe whether a solver relies on familiar surface labels. Length extrapolation later asks whether a procedure transfers beyond demonstration sizes. These are valuable experimental interventions because a correct familiar answer does not identify the computation that produced it.

- At 33–40 minutes creativity is treated as proposing useful shortcuts through a large search space, with verification supplying a different competence. The interaction matters to my account: broad associative knowledge can increase the density of productive hypotheses even without providing a proof for each proposal.

- The 54–59 minute self-critique discussion identifies two error channels: missing a real error and inventing an error in a correct solution. Repeated reflection can therefore degrade performance. An external correctness signal can improve selection even if the generator does not faithfully understand detailed feedback.

- At 80–89 minutes LLM-Modulo becomes richer than translation into one solver. The LLM can propose plans, domain models, and missing problem details; a bank of validators checks distinct constraints; feedback can be binary, diagnostic, or constructive. Domain-model review and formal plan validation sit at different levels.

- The closing agent discussion separates having an actuator or function-call interface from choosing a valid action sequence. Affordances, planning, and execution monitoring are distinct. The explicit admission that passing unit tests is only partial verification is essential to the architecture’s practical meaning.

## Mathematical anatomy

**Objects:** A domain model D with states, action preconditions/effects, initial state s0, goal predicate g, a proposal distribution Q_theta(plan|prompt), and validators V_j(plan,D). Some critics express preferences or style rather than logical correctness.

**Assumptions:** A sound validator proves only the property it checks under D. The model itself must adequately represent the environment; an LLM-proposed domain needs independent scrutiny. Completeness additionally requires sufficient proposal coverage or exhaustive fallback, which is not guaranteed.

**Objective:** Search for a plan pi with all required V_j(pi,D)=1 while minimizing proposal/validation cost and satisfying soft preferences. For independent proposals with valid-plan probability p, success after k trials is 1-(1-p)^k; correlated or adaptive proposals require different analysis.

**Mechanism:** The system generates a candidate, evaluates multiple critics, returns actionable feedback, and generates again until acceptance conditions hold. Accepted examples can improve the proposal distribution. Validators compose conjunctively for independently specified requirements, but inconsistent specifications can make acceptance impossible.

**Limits:** A failed renaming test establishes lack of robust invariance in that evaluation, not uniquely the absence of all reasoning. Reliability is a degree; soundness is a formal property. Learned computation can be fallible and still algorithmic, while a sound symbolic proof can establish a false real-world conclusion if its premises/model are wrong.

## Evidence, limitations and corrections

- The episode repeatedly treats reasoning as requiring guarantees. That is a defensible specification for a formal solver, but excludes ordinary fallible deductive or probabilistic inference by definition. Failure to meet that specification does not establish a theorem that no learned reasoning occurs.

- Calling the network an n-gram model describes conditional prediction but does not establish its internal algorithm. Distribution-level training can learn instance-level rules; lack of a guarantee is not proof of pure retrieval. The guest himself acknowledges compression/generalization and distinguishes architectural expressivity from what training learns.

- The pause-token dismissal around 72 minutes mischaracterizes the cited idea. The primary study trains with learnable pause tokens and delays output to permit additional computation; it is not simply waiting for wall-clock time to induce thought. This does not prove universal reasoning, but it defeats that particular objection.

- ARC program execution checks consistency on the provided demonstrations, not correctness on unknown test outputs. Kambhampati later explicitly concedes the analogous limitation for unit tests at 88–89 minutes; that qualification also limits the earlier stronger guarantee language.

- Historical PlanBench, Caesar-cipher, multiplication, and chain-of-thought results are examples from the recording period, not a current leaderboard audit. The anecdotal numerical claims and proprietary model sizes are not independently verified here.

- A fixed forward pass has bounded depth for a given architecture, but inference cost depends on context and generated length, and multiple generated tokens enable additional computation. Autoregression and reinforcement-learning training are not mutually exclusive categories.

## Relevance to my research

Worthwhile for my research because it provides a disciplined audit of where correctness evidence comes from and a concrete architecture for turning generative intuition into checked knowledge. It substantially overlaps the later Kambhampati interview; I would use this version for the clearest account of composable critics, domain-model acquisition, and the limits of testing.

## My viewing plan

**Mode:** chapters

**Segments:** - **Start:** 00:15:02
  
  **End:** 00:18:00
  
  **Purpose:** Semantics-preserving renaming as a controlled robustness test.

- **Start:** 00:33:06
  
  **End:** 00:40:01
  
  **Purpose:** Proposal generation, creative shortcuts, and deductive checking.

- **Start:** 00:54:00
  
  **End:** 00:59:04
  
  **Purpose:** Why self-critique can worsen answers and external feedback can help.

- **Start:** 01:20:05
  
  **End:** 01:33:00
  
  **Purpose:** LLM-Modulo architecture, composable critics, partial verification, and acting versus planning.

**Edition note:** All local publisher-podcast ASR read through 01:42:02. Matched RSS is one second shorter than listed video; timings not independently aligned.

**Intention:** I plan to watch the selected passages, prioritizing LLM-Modulo and the limits of testing.

## Objections and open questions

- A model can both propose and partially verify, with different reliability on each task. External tools remain useful without requiring a categorical declaration that the learned system does no reasoning.

- Sometimes a mature solver is cheaper and more complete than repeated proposal-and-test. Modular critics improve flexibility but can also provide poor search guidance, leaving a hard joint feasibility problem.

## An experiment I could try

I want to implement a tiny blocks-world generator and exact simulator, then evaluate a learned or heuristic proposal system on familiar names, random renamings, longer plans, and unsatisfiable goals. No revision, self-critique, binary external rejection, and diagnostic feedback would be compared under equal total compute. Deliberately omitting one action precondition from D would test how formally accepted plans can fail in the true simulator.

## Connections in my notes

- Later Kambhampati interview overlaps the anti-retrieval arguments; I would choose this one for architectural detail.

- AlphaEvolve and Ellis/Tavares: proposal, evaluator, and representation form a coupled search system.

- Molnar: a transparent explanation or validator is only as valid as its assumptions and target property.

## Primary sources checked

- **Url:** https://arxiv.org/abs/2402.01817
  
  **Claim:** Primary abstract checked on bidirectional LLM-Modulo integration.

- **Url:** https://arxiv.org/abs/2310.02226
  
  **Claim:** Primary abstract checked: trained pause tokens enable extra computation before output; not mere elapsed waiting.

## Source and coverage

**Status:** complete_available_text

**Method:** Read entire saved transcript in contiguous bounded chunks; only repeated timestamp/speaker-label formatting suppressed during reading. Audio and video not checked.

**Last timestamp:** 01:42:13

**Caveats:** - ASR transcription can corrupt names and mathematical terminology; transcript completeness is not an audio audit.

- Source is local Whisper-large-v3-turbo ASR of publisher RSS podcast audio; names, formulas, and speaker assignments can be inaccurate.

- All local publisher-podcast ASR read through 01:42:02. Matched RSS is one second shorter than listed video; timings not independently aligned.

Source type: Local asr. Reviewed text: 16,179 words.

Transcript file: `y1WnHpedi2A.local-asr.txt` (not distributed).

SHA-256: `98bf2ac5a52da9334cd4241463088768bb7367ebd7c757059e411622e08ec1f1`.

[Structured review](y1WnHpedi2A.json) · [Source ledger](../sources.json)
