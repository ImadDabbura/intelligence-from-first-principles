# #97 SREEJAN KUMAR - Human Inductive Biases in Machines from Language

[Original episode](https://www.youtube.com/watch?v=VvXfK-Qle-Y) · Source: Machine Learning Street Talk · [All reviews](../README.md) · [Learning path](../learning-path.md)

Published: 2023-01-28 · Decision: **Core** · Confidence: high

## Central claim

Inductive bias can be transferred through the structure of a learning target, not only hard-coded into an architecture. Human language and learned program libraries provide compressed descriptions that reshape a neural agent's generalization preferences. The scientific value is a controlled comparison of those preferences, including the tasks where human-like bias makes performance worse.

## Ideas I want to keep

- The experiment operationalizes abstraction in a small stimulus space of binary grids. Human-in-the-loop sampling produces grids with familiar structural regularities; a machine-based control distribution makes an explicit contrast instead of treating all test tasks as interchangeable.

- A sequential tile-revelation game turns priors into observable decisions: rewards for discovering target tiles and penalties for irrelevant queries expose what structure the learner expects in unobserved locations.

- A human/machine performance dissociation demonstrates that training on human-looking tasks does not guarantee human-like generalization. The intervention aims to change the pattern of strengths and weaknesses, not simply raise a pooled benchmark score.

- An auxiliary prediction target can carry prior structure. The described neural agent learns its RL task while predicting a representation of a human-written board description; language acts as a representation-shaping training signal.

- Literal tile-by-tile descriptions differ from compressive concepts such as a U shape. Program primitives alone likewise differ from libraries that introduce reusable abstractions. The comparisons help isolate description structure rather than merely the presence of additional supervision.

## Mathematical anatomy

**Objects:** Task distributions D_human and D_control over binary grids, partially observed histories h, an action policy, and embeddings z(d) of descriptions or program representations.

**Objective:** A schematic reconstruction is L_total=L_RL+lambda||g(h)-z(d)||² for the described embedding-prediction intervention; the interview does not derive the exact full optimization system.

**Mechanism:** Co-training changes the internal features useful for action selection. A compact concept ties together many grid configurations and changes which unobserved cells the agent expects to be rewarding.

**Assumptions:** Descriptions reflect transferable task structure; auxiliary targets are accessible during training; test tasks share relevant structure; comparisons control capacity, training data and information supplied.

**Limits:** Human sampling does not literally expose an uncontaminated ground-truth prior: response noise, cultural experience, population heterogeneity and chain convergence matter. The observed preference shift is specific to this task family, not a universal claim about all neural systems.

## Evidence, limitations and corrections

- Crucially, the speaker reports both improved performance on human-easy tasks and degraded performance on human-hard controls. This is stronger evidence of a bias shift than a one-sided accuracy gain, but human-likeness is not identical to optimality.

- The host repeatedly extrapolates from matching cognitive generalization patterns to aligning human values. The experiment does not establish ethical alignment, grounding in arbitrary real-world environments, or general collaboration success.

- Language targets and learned programs differ along multiple dimensions. Compression is a proposed explanatory factor; the interview alone does not prove it is the only causal difference.

- The speaker explicitly resists the host's blanket claim that neural networks do not generalize: different systems have different priors and different success domains. That qualification is essential to the interpretation.

- Symbolic computation can be a useful design choice without implying finite-resource neural systems uniquely fail at infinity. Representational capacity, learnability, computation budget and task distribution must be separated.

## Relevance to my research

A particularly good bridge between statistical learning, cognitive science and symbolic abstraction. It replaces the false choice between learned representations and built-in priors with a concrete mechanism for learning a prior from another representational medium. The controlled double dissociation is a research design worth learning, not just an interesting result.

## My viewing plan

**Mode:** main_interview

**Ranges:** - **Start:** 00:06:17
  
  **End:** 00:24:16
  
  **Reason:** Controlled task construction, human versus machine priors, auxiliary loss, and compressive abstractions. The long opening repeats these ideas with stronger, less justified alignment rhetoric.

**Edition:** Podcast timestamps, duration-matched to video.

## Objections and open questions

A human-compatible prior may sacrifice performance on environments without human-salient structure. That is not necessarily a defect, but the intended objective must be explicit. Better communication with humans, higher expected reward and faithful cognitive modeling are three different goals.

## An experiment I could try

My proposed experiment uses binary-grid tasks with either line/shape structure or matched-density random structure. The same small agent would be trained with no auxiliary target, literal cell descriptions, shape labels and randomly permuted labels, matching representation dimension and training budget. I would report reward separately on both task families and on novel compositions, then test whether any improvement survives withholding familiar shape names while retaining their spatial structure.

## Connections in my notes

- Geometric deep learning: priors through architecture versus supervision

- Ellis/Tavares and DreamCoder: learned libraries as compression

- Kornblith: training objective shapes transferable representations

- Chollet: skill, prior experience and adaptation efficiency

## Primary sources checked

- **Url:** https://proceedings.neurips.cc/paper_files/paper/2022/hash/0113ef4642264adc2e6924a3cbbdf532-Abstract-Conference.html
  
  **Purpose:** Checked primary paper identification and scope of auxiliary representation comparisons.

## Source and coverage

**Status:** complete_available_text

**First timestamp:** 00:00:00

**Last timestamp:** 00:24:57

**Method:** Read every line of locally generated publisher-podcast transcript.

**Caveats:** - Local Whisper-large-v3-turbo ASR; names imperfect and audio not independently corrected.

- Podcast and video both 1,498 seconds, but exact timestamp alignment not certified.

Source type: Local asr. Reviewed text: 4,000 words.

Transcript file: `VvXfK-Qle-Y.local-asr.txt` (not distributed).

SHA-256: `93b8548343e716d1b18f4f3121b169324c007ae0e8ab26bf258e9cdafec0cf6e`.

[Structured review](VvXfK-Qle-Y.json) · [Source ledger](../sources.json)
