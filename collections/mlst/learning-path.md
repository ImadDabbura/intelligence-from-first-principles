# My learning path

I’ll begin with how intelligence is recognized and measured, then work through the structures that support learning, abstraction, reasoning and action. From there, I want to understand how systems improve themselves, discover new problems and organize intelligence across multiple agents.

The anchor episodes are my starting points. The deeper branches give me worked examples and alternative explanations when I want to pursue a question further. I plan to use the exercises to check what I actually understand, and the overlap notes to decide whether another interview adds enough to be worth my time.

The sequence below is the recommended conceptual order. It is not a strict prerequisite chain or a ranking of speakers.

## Orientation

1. [The Real Reason Huge AI Models Actually Work \[Prof. Andrew Wilson\]](reviews/M-jTeBCEGHc.md)
2. [The Math Behind Every Recommendation You've Ever Seen - Wouter Koolen](reviews/h-dYzjF8eFA.md)
3. [The Geometric Deep Learning Blueprint — Michael Bronstein](reviews/bIZB1hIJ4u8.md)

## 1 · What would count as understanding intelligence?

What distinguishes acquired skill, learning efficiency, decodable information and an actual computational mechanism?

Before interpreting a score or an explanation, I need to specify the system boundary and what is being estimated. The same behavior can fit different beliefs, preferences or policies; interventions should separate these explanations.

### Starting episodes

- [#51 FRANCOIS CHOLLET - Intelligence and Generalisation](reviews/J0p_thJJnoo.md)
- [039 - Lena Voita - NLP](reviews/Q0kN_ZHHDQY.md)
- [NEURAL NETWORKS ARE WEIRD! - Neel Nanda (DeepMind)](reviews/YpFaPKOeNME.md)

### Deeper branches

- [AI BENCHMARKS ARE BROKEN! \[Prof. MELANIE MITCHELL\]](reviews/29gkDpR2orc.md)
- [#107 - Dr. RAPHAËL MILLIÈRE - Linguistics, Theory of Mind, Grounding](reviews/fhn6ZtD6XeE.md)
- [Strange Geometric Shapes Found Inside AIs — Tom McGrath](reviews/_egu7OFem-k.md)
- [#040 - Adversarial Examples (Dr. Nicholas Carlini, Dr. Wieland Brendel, Florian Tramèr)](reviews/2PenK06tvE4.md)
- [#047 Interpretable Machine Learning - Christoph Molnar](reviews/0LIACHcxpHU.md)
- [The Gap Between Humans and Machines Is ___ \[Dr. Max Bartolo\]](reviews/DL7qwmWWk88.md)
- [Is ChatGPT an N-gram model on steroids?](reviews/W485bz0_TdI.md)
- [How Researchers Test AI for Hidden Goals — Apollo Research](reviews/n1Qk8xbqF-M.md)

### An experiment I could try

I want to take one apparent reasoning capability and design separate tests of task elicitation, novel composition, internal causal use and robustness. For each successful test, I’ll record what it still leaves unidentified.

## 2 · Which prior structure makes learning possible?

How can a huge hypothesis class generalize, and when should structure be built in?

Capacity, preference over functions, optimization and invariance are different objects.

### Starting episodes

- [The Real Reason Huge AI Models Actually Work \[Prof. Andrew Wilson\]](reviews/M-jTeBCEGHc.md)
- [#036 - Max Welling: Quantum, Manifolds & Symmetries in ML](reviews/mmDw5glry9w.md)
- [The Geometric Deep Learning Blueprint — Michael Bronstein](reviews/bIZB1hIJ4u8.md)

### Deeper branches

- [The Lottery Ticket Hypothesis with Jonathan Frankle](reviews/SfjJoevBbjU.md)
- [Why More Data Cannot Replace Prior Structure - Alexander Mattick](reviews/1S1B4XkFCD8.md)
- [Sara Hooker - The Hardware Lottery, Sparsity and Fairness](reviews/sQFxbQ7ade0.md)
- [#71 - ZAK JOST (Graph Neural Networks + Geometric DL) \[UNPLUGGED\]](reviews/jAGIuobLp60.md)

### An experiment I could try

I could specify a task transformation group and compare invariance, equivariance and augmentation. Then I’d change the task so the assumed symmetry becomes wrong and measure the cost of that prior.

## 3 · How do useful abstractions emerge?

What information should a representation retain, discard or make easy to use?

Learning objectives, data structure and downstream use jointly determine what counts as a useful abstraction.

### Starting episodes

- [#032- Simon Kornblith / GoogleAI - SimCLR and Paper Haul!](reviews/1EqJyMy0LnE.md)
- [AI Is Learning at the Wrong Level of Abstraction — Matthieu Wyart](reviews/revreN8LZ_M.md)
- [The Mathematical Foundations of Intelligence \[Professor Yi Ma\]](reviews/QWidx8cYVRs.md)

### Deeper branches

- [#55 Dr. ISHAN MISRA - Self-Supervised Vision Models](reviews/EXJmodhu4_4.md)
- [SWaV: Unsupervised Learning of Visual Features by Contrasting Cluster Assignments (Mathilde Caron)](reviews/uqJ2hbDGHjY.md)
- [Neural Networks Are Elastic Origami! \[Prof. Randall Balestriero\]](reviews/l3O2J3LMxqI.md)
- [#97 SREEJAN KUMAR - Human Inductive Biases in Machines from Language](reviews/VvXfK-Qle-Y.md)
- [ML Robustness & Engineering - Andrew Ilyas (MIT)](reviews/9BC9BsZRCKQ.md)
- [AI Interpretability, Safety, and Meaning - Nora Belrose](reviews/VgPrjHxIS0I.md)
- [#87 - ADELE MYERS - Regression-Based Elastic Metric Learning on Shape Spaces of Cell Curves #NEURIPS](reviews/24u6CTV4t1k.md)

### An experiment I could try

A useful experiment would start with hierarchical data generated from two independent latent factors. I’d vary the prediction target or positive-pair construction and check which factor becomes accessible, transferable and causally used.

## 4 · How does structure become executable reasoning?

What separates representing a solution, discovering it and executing it reliably?

Typed composition, proposal priors, search and verification can play different roles in one intelligent system. Learning abstractions changes which hypotheses are computationally accessible, even when expressivity is unchanged.

### Starting episodes

- [Why Program Synthesis Is Next (Kevin Ellis and Zenna Tavares)](reviews/oYTm0p3DCzg.md)
- [What is “reasoning” in modern AI?](reviews/XFMk0snybAc.md)
- [#85 Dr. Petar Veličković (Deepmind) - Categories, Graphs, Reasoning \[NEURIPS22 UNPLUGGED\]](reviews/1lkdWduuN14.md)
- [Decompiling Dreams: A New Approach to ARC?](reviews/3ZTNps2PraM.md)

### Deeper branches

- [Can Latent Program Networks Solve Abstract Reasoning? \[Clement Bonnet\]](reviews/PHBItVuudbU.md)
- [The "Final Boss" of Deep Learning](reviews/AWqvBdqCAAE.md)
- [#50 Dr. CHRISTIAN SZEGEDY - Formal Reasoning, Program Synthesis](reviews/ehNGGYFO6ms.md)
- [#62 Dr. GUY EMERSON + Walid Saba \[Unplugged\]](reviews/dhM0_EKLg9k.md)
- [#53 Prof. BOB COECKE - Quantum Natural Language Processing](reviews/X9uSV1YcOy4.md)
- [Transformers Need Glasses! \[Federico Barbero\]](reviews/FAspMnu4Rt0.md)
- [WE MUST ADD STRUCTURE TO DEEP LEARNING BECAUSE...](reviews/rie-9AEhYdY.md)
- [Solving Chollet's ARC-AGI with GPT4o](reviews/z9j3wB1RRGA.md)

### An experiment I could try

I want to solve the same small task family with a direct network, a learned program proposal plus an exact interpreter, and latent search. I’d track proposal coverage, search cost and execution errors separately.

## 5 · Which evidence is worth acquiring?

How should a finite learner spend observations, memory and adaptation compute?

Information is valuable relative to a decision and existing knowledge; similarity and confidence alone are insufficient acquisition rules.

### Starting episodes

- [The Math Behind Every Recommendation You've Ever Seen - Wouter Koolen](reviews/h-dYzjF8eFA.md)
- [Test-Time Adaptation: A New Frontier in AI \[Dr. Jonas Hübotter\]](reviews/C6sSs6NgANo.md)
- [The AI That Replaces Hours of Model Tuning - Frank Hutter](reviews/72Im-Mm5JKs.md)

### Deeper branches

- [Learning at test time in LLMs \[Jonas Hübotter\]](reviews/vei7uf9wOxI.md)
- [#92 - SARA HOOKER - Fairness, Interpretability, Language Models](reviews/7oJui4eSCoY.md)
- [#063 - Prof. YOSHUA BENGIO - GFlowNets, Consciousness & Causality](reviews/M49TMqK5uCE.md)
- [Test-Time Adaptation: the key to reasoning with DL](reviews/3p0O28W1ZHg.md)
- [The ARC Prize 2024 Winning Algorithm \[Daniel Franzen and Jan Disselhoff\]](reviews/mTX_sAq--zY.md)

### An experiment I could try

I could build a redundant candidate pool and compare nearest-neighbor retrieval with conditional uncertainty reduction. Deliberately misspecifying the representation and task prior should help me locate the limits of each approach.

## 6 · When is a world model good enough to act?

How do inference, active sensing and planning interact when the model is wrong?

Prediction accuracy, decision adequacy and closed-loop stability are distinct requirements. Optimizers can exploit their own models' errors.

### Starting episodes

- [Harri Valpola: System 2 AI and Planning in Model-Based Reinforcement Learning](reviews/HnZDmxYnpg4.md)
- [Dr. THOMAS PARR - Active Inference](reviews/bk_xCikDUDQ.md)
- [Building a GENERAL AI agent with reinforcement learning](reviews/s3C0sEwixkQ.md)

### Deeper branches

- [This man builds intelligent machines](reviews/2wnJ6E6rQsU.md)
- [Why LeCun Thinks Deep Learning Isn't Enough — Yann LeCun](reviews/86ib0sfdFtw.md)
- [AIs can now imagine video games in real-time](reviews/kbt0ZFoI2Hc.md)
- [AutoGrad Changed Everything (Not Transformers) \[Dr. Jeff Beck\]](reviews/9suqiofCiwM.md)
- [Mapping GPT revealed something strange...](reviews/Bpgloy1dDn0.md)
- [#033 Karl Friston - The Free Energy Principle](reviews/KkR24ieh5Ow.md)
- [#67 Prof. KARL FRISTON 2.0 \[Unplugged\]](reviews/xKQ-F2-o8uM.md)

### An experiment I could try

I want to construct a partially observed control task with a misspecified learned model. I’d compare prediction loss with achieved return, look for cases where more planning worsens the policy, and then add an action chosen for information.

## 7 · What can change in a learning system?

Can the learning rule, task generator, search archive or experimental policy itself adapt?

I need to specify the inner and outer variables, timescales and held-out objectives. Improving an artifact does not automatically improve the process that produced it.

### Starting episodes

- [#49 - Meta-Gradients in RL - Dr. Tom Zahavy (DeepMind)](reviews/hfaZwgk_iS0.md)
- [Can AI Improve Itself? \[Chris Lu, Robert Lange, Cong Lu\]](reviews/1kwbp8hRRfs.md)
- [When AI Discovers the Next Transformer — Robert Lange](reviews/EInEmGaMRLc.md)

### Deeper branches

- [ImageNet Moment for Reinforcement Learning? \[Prof. Jakob Foerster\]](reviews/Jr_nGkCG3og.md)
- [Can Rewriting an AI Agent Bend the Intelligence Curve? - Zhengyao Jiang](reviews/yB6_iFGTq9k.md)
- [Wild breakthrough on Math after 56 years... \[Exclusive\]](reviews/vC9nAosXrJw.md)
- [He won a Nobel here for AlphaFold. Then he left. - John Jumper](reviews/e3gBwLWAerw.md)
- [What Building an AI Scientist Actually Requires Beyond Intelligence — Edward Hughes](reviews/P4bYjTJvD28.md)
- [The Man Who Invented Modern AI (Before Everyone Else) — Jürgen Schmidhuber](reviews/DP454c1K_vQ.md)

### An experiment I could try

A small search loop with an archive, proposer and verifier would let me freeze each component in turn and test transfer to unseen task families. I’d also check whether the search can exploit the evaluator.

## 8 · Where do new problems and possibilities come from?

What maintains discovery when distance to a fixed target is misleading?

Diversity, representation neighborhoods, curricula and observers shape open-ended search. Novelty alone is not intelligence. Sampling a reward-weighted distribution differs from optimizing its maximum; a sampler alone does not supply an exploration objective.

### Starting episodes

- [Why Greatness Cannot Be Planned — Kenneth Stanley](reviews/lhYGXYeMq_E.md)
- [AI Isn't Creative \[Prof. Kenneth Stanley\]](reviews/KKUKikuV58o.md)
- [The AI Paradigm That Nobody Talks About — Tim Rocktäschel](reviews/6DrCq8Ry2cw.md)

### Deeper branches

- [Don't invent faster horses - Prof. Jeff Clune](reviews/mw5WIDGRLnA.md)
- [What Most People Get Wrong About Evolution | Akarsh Kumar](reviews/615B5nyMFPk.md)
- [Google Researcher Shows Life "Emerges From Code" \[Blaise Agüera y Arcas\]](reviews/rMSEqJ_4EBk.md)
- [What If Intelligence Didn't Evolve? It "Was There" From the Start! - Blaise Agüera y Arcas](reviews/M2iX6HQOoLg.md)
- [#81  JULIAN TOGELIUS, Prof. KEN STANLEY - AGI, Games, Diversity & Creativity \[UNPLUGGED\]](reviews/iqkkkA9dtY0.md)
- [Exploring Open-Ended Algorithms: POET](reviews/sIv-JoFf-Ww.md)
- [#063 - Prof. YOSHUA BENGIO - GFlowNets, Consciousness & Causality](reviews/M49TMqK5uCE.md)

### An experiment I could try

I could compare objective search, novelty search and quality diversity in a deceptive environment, then change the behavior descriptor and record which stepping stones disappear. I’d measure collective coverage separately from the competence of one deployable generalist.

## 9 · Which parts of intelligence extend beyond one model or brain?

How do feedback, reference frames, communication and incentives organize competence across scales?

Biological and collective accounts suggest different mechanisms; similar behavior does not uniquely identify the same implementation. Shared beliefs and compatible representations do not guarantee aligned incentives.

### Starting episodes

- [Michael Levin - Why Intelligence Isn't Limited To Brains.](reviews/6w5xr8BYV8M.md)
- [#59 JEFF HAWKINS - Thousand Brains Theory](reviews/6VQILbDqaI4.md)
- [Intelligence is collective, not artificial — Prof. Michael I. Jordan (UC Berkeley / Inria)](reviews/AREWYbVtX64.md)

### Deeper branches

- [Your Brain Doesn't Command Your Body. It Predicts It. \[Max Bennett\]](reviews/RvYSsi6rd4g.md)
- [The Hidden Math Behind All Living Systems](reviews/hf18w6CuY8o.md)
- [Rethinking the Mind - Prof. Mark Solms](reviews/meUtWtY00H8.md)
- [Biologically-inspired AI and Mortal Computation](reviews/ZTE-JVd_QkA.md)
- [#041 Dr. SIMON STRINGER - Biologically Plausible Neural Networks](reviews/aisgNLypUKs.md)
- [This is what happens when you let AIs debate](reviews/WlWAhjPfROU.md)
- ["We need AIs with PHYSICAL experience" (Jeff Beck)](reviews/zv6qzWecj5c.md)
- [KARL FRISTON - INTELLIGENCE 3.0](reviews/V_VXOdf1NMw.md)

### An experiment I could try

I want to choose a proposed agent boundary and identify its state, observations, actions, memory, preferences and evidence of adaptation. The next step would be an intervention that distinguishes feedback regulation from model-based planning.

## Working conclusions

**Claim:** Prior structure is unavoidable; its location is a design choice.

**Explanation:** Priors can enter through architectures, task generators, objectives, language targets, programs and search procedures. The useful question is which prior supports which transfer, and at what total cost.

- [The Real Reason Huge AI Models Actually Work \[Prof. Andrew Wilson\]](reviews/M-jTeBCEGHc.md)
- [The Geometric Deep Learning Blueprint — Michael Bronstein](reviews/bIZB1hIJ4u8.md)
- [The AI That Replaces Hours of Model Tuning - Frank Hutter](reviews/72Im-Mm5JKs.md)
- [#97 SREEJAN KUMAR - Human Inductive Biases in Machines from Language](reviews/VvXfK-Qle-Y.md)

**Claim:** Statistical learning and compositional structure are not mutually exclusive categories.

**Explanation:** Wyart supplies a tractable statistical route to hierarchy, while Ellis, Chaudhuri and Petar show how executable structure changes search and generalization. None proves that one recipe covers all intelligence. Claims that neural systems only interpolate require a specified definition and counterexample-sensitive scope.

- [AI Is Learning at the Wrong Level of Abstraction — Matthieu Wyart](reviews/revreN8LZ_M.md)
- [Why Program Synthesis Is Next (Kevin Ellis and Zenna Tavares)](reviews/oYTm0p3DCzg.md)
- [#85 Dr. Petar Veličković (Deepmind) - Categories, Graphs, Reasoning \[NEURIPS22 UNPLUGGED\]](reviews/1lkdWduuN14.md)
- [Why LeCun Thinks Deep Learning Isn't Enough — Yann LeCun](reviews/86ib0sfdFtw.md)

**Claim:** A representation is useful relative to an operation or decision.

**Explanation:** Information can be present but hard to decode, easy to decode but unused, or predictive without supporting intervention. I need to keep accessibility, causal use and control adequacy separate.

- [039 - Lena Voita - NLP](reviews/Q0kN_ZHHDQY.md)
- [#032- Simon Kornblith / GoogleAI - SimCLR and Paper Haul!](reviews/1EqJyMy0LnE.md)
- [Harri Valpola: System 2 AI and Planning in Model-Based Reinforcement Learning](reviews/HnZDmxYnpg4.md)
- [Strange Geometric Shapes Found Inside AIs — Tom McGrath](reviews/_egu7OFem-k.md)

**Claim:** Search success, correctness and discovery are different achievements.

**Explanation:** Candidate generators, search policies, archives and verifiers contribute separately. A sound formal verifier certifies a specified property under assumptions; an interpreter or empirical test establishes only the tested behavior. Neither certifies that a task specification captures intent or that a discovery is scientifically important.

- [#50 Dr. CHRISTIAN SZEGEDY - Formal Reasoning, Program Synthesis](reviews/ehNGGYFO6ms.md)
- [What is “reasoning” in modern AI?](reviews/XFMk0snybAc.md)
- [Wild breakthrough on Math after 56 years... \[Exclusive\]](reviews/vC9nAosXrJw.md)
- [When AI Discovers the Next Transformer — Robert Lange](reviews/EInEmGaMRLc.md)

**Claim:** Free-energy and biological accounts are research frameworks with explicit commitments.

**Explanation:** My interest is in the inference–action mechanisms and the generative model, boundary, preferences and physical assumptions they require. A variational identity does not by itself establish a universal theory of intelligence or consciousness.

- [Dr. THOMAS PARR - Active Inference](reviews/bk_xCikDUDQ.md)
- [#67 Prof. KARL FRISTON 2.0 \[Unplugged\]](reviews/xKQ-F2-o8uM.md)
- [How can we add knowledge to AI agents?](reviews/qxEfcrmTWO4.md)
- [Michael Levin - Why Intelligence Isn't Limited To Brains.](reviews/6w5xr8BYV8M.md)

**Claim:** Open-endedness changes the object of study, but does not remove evaluation assumptions.

**Explanation:** Task generation, novelty measures, learned judges and population memory shape which discoveries become available. Preserving stepping stones is a concrete mechanism; inevitable unlimited creativity is a stronger claim.

- [Why Greatness Cannot Be Planned — Kenneth Stanley](reviews/lhYGXYeMq_E.md)
- [AI Isn't Creative \[Prof. Kenneth Stanley\]](reviews/KKUKikuV58o.md)
- [The AI Paradigm That Nobody Talks About — Tim Rocktäschel](reviews/6DrCq8Ry2cw.md)
- [Don't invent faster horses - Prof. Jeff Clune](reviews/mw5WIDGRLnA.md)

## Overlap between episodes

**Note:** The two Hübotter interviews share conditional information acquisition and test-time specialization. I’ll start with the earlier foundation and return to the later episode for its updated application and representation caveats.

- [Test-Time Adaptation: A New Frontier in AI \[Dr. Jonas Hübotter\]](reviews/C6sSs6NgANo.md)
- [Learning at test time in LLMs \[Jonas Hübotter\]](reviews/vei7uf9wOxI.md)

**Note:** The main Chollet interview is my starting point for skill-acquisition efficiency. The later talk, update and panel add critiques and historical context; I don’t need to finish all of them before moving on to constructive mechanisms.

- [#51 FRANCOIS CHOLLET - Intelligence and Generalisation](reviews/J0p_thJJnoo.md)
- [It's Not About Scale, It's About Abstraction](reviews/s7_NlkBwdj8.md)
- [François Chollet on OpenAI o-models and ARC](reviews/w9WE1aOPjHc.md)
- [Francois Chollet - On the Measure Of Intelligence](reviews/mEVnu-KZjq4.md)

**Note:** Bronstein supplies the geometric foundation, Jost an accessible GNN bridge, Petar concrete algorithmic and topology examples, and Dudzik a broader compositional framework. That gives me a useful progression through their overlapping material.

- [The Geometric Deep Learning Blueprint — Michael Bronstein](reviews/bIZB1hIJ4u8.md)
- [#71 - ZAK JOST (Graph Neural Networks + Geometric DL) \[UNPLUGGED\]](reviews/jAGIuobLp60.md)
- [#85 Dr. Petar Veličković (Deepmind) - Categories, Graphs, Reasoning \[NEURIPS22 UNPLUGGED\]](reviews/1lkdWduuN14.md)
- [The "Final Boss" of Deep Learning](reviews/AWqvBdqCAAE.md)

**Note:** I’ll start with Kornblith. Misra is a follow-up for broader assumptions, while SWaV offers a worked anti-collapse mechanism. The short LeCun/Balestriero episode consolidates the spectral viewpoint.

- [#032- Simon Kornblith / GoogleAI - SimCLR and Paper Haul!](reviews/1EqJyMy0LnE.md)
- [#55 Dr. ISHAN MISRA - Self-Supervised Vision Models](reviews/EXJmodhu4_4.md)
- [SWaV: Unsupervised Learning of Visual Features by Contrasting Cluster Assignments (Mathilde Caron)](reviews/uqJ2hbDGHjY.md)
- [#86 - Prof. YANN LECUN and Dr. RANDALL BALESTRIERO - SSL, Data Augmentation \[NEURIPS2022\]](reviews/9dLd6n9yT8U.md)

**Note:** Nanda’s newer interview is my broad methodological starting point. The older episode and McGrath add particular techniques and geometric structures. The distinction to preserve is between reading a probe and identifying a mechanism.

- [NEURAL NETWORKS ARE WEIRD! - Neel Nanda (DeepMind)](reviews/YpFaPKOeNME.md)
- [Mechanistic Interpretability - NEEL NANDA (DeepMind)](reviews/_Ygf0GnlwmY.md)
- [Strange Geometric Shapes Found Inside AIs — Tom McGrath](reviews/_egu7OFem-k.md)

**Note:** Parr gives me the clearest starting point for inference and action. The longer Friston/Ramstead discussions are opportunities to compare formulations and examine their assumptions; I shouldn’t count them as six independent confirmations of one universal claim.

- [Dr. THOMAS PARR - Active Inference](reviews/bk_xCikDUDQ.md)
- [#033 Karl Friston - The Free Energy Principle](reviews/KkR24ieh5Ow.md)
- [#67 Prof. KARL FRISTON 2.0 \[Unplugged\]](reviews/xKQ-F2-o8uM.md)
- [KARL FRISTON - INTELLIGENCE 3.0](reviews/V_VXOdf1NMw.md)
- [The Physics of AI](reviews/8qb28P7ksyE.md)
- [Autopoietic Enactivism and the Free Energy Principle - Prof. Friston, Prof Buckley, Dr. Ramstead](reviews/bL00-jtRrMA.md)

**Note:** I’ll use the earlier Kambhampati interview for composable validators, domain-model acquisition and partial testing guarantees, then add passages from the later planning discussion. Neither supports a general theorem that autoregressive models cannot reason.

- [Do you think that ChatGPT can reason? \[Prof. Subbarao Kambhampati\]](reviews/y1WnHpedi2A.md)
- [The Professor Who Proved ChatGPT Can't Think — Subbarao Kambhampati](reviews/2xFTNXK6AzQ.md)

**Note:** The later MindsAI interview is my starting point for the more developed algorithmic account. The early panel adds task-dependent objecthood, the optimizer as part of the agent, and the difference between generating examples and generating new concepts.

- [Chollet's ARC Challenge + Current Winners](reviews/jSAT_RuJ_Cg.md)
- [Test-Time Adaptation: the key to reasoning with DL](reviews/3p0O28W1ZHg.md)

**Note:** I’m keeping these together because they address different questions: probe complexity measures accessibility; erasure tests what survives a specified intervention; circuit analysis reconstructs computation; data attribution studies dependence on training examples. None alone establishes all four.

- [039 - Lena Voita - NLP](reviews/Q0kN_ZHHDQY.md)
- [AI Interpretability, Safety, and Meaning - Nora Belrose](reviews/VgPrjHxIS0I.md)
- [NEURAL NETWORKS ARE WEIRD! - Neel Nanda (DeepMind)](reviews/YpFaPKOeNME.md)
- [ML Robustness & Engineering - Andrew Ilyas (MIT)](reviews/9BC9BsZRCKQ.md)

**Note:** The BFF talks substantially overlap. I only need one technical account before turning to the linked July 2026 corrective paper. I want to keep initial replicator discovery separate from later population takeover when evaluating the merger explanation.

- [What If Intelligence Didn't Evolve? It "Was There" From the Start! - Blaise Agüera y Arcas](reviews/M2iX6HQOoLg.md)
- [Google Researcher Shows Life "Emerges From Code" \[Blaise Agüera y Arcas\]](reviews/rMSEqJ_4EBk.md)

[All episode reviews](README.md) · [Methodology](../../METHODOLOGY.md)
