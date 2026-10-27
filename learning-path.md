# My learning path

I’ll begin with how intelligence is recognized and measured, then work through the structures that support learning, abstraction, reasoning and action. From there, I want to understand how systems improve themselves, discover new problems and organize intelligence across multiple agents.

The anchor episodes are my starting points. The deeper branches give me worked examples and alternative explanations when I want to pursue a question further. I plan to use the exercises to check what I actually understand, and the overlap notes to decide whether another interview adds enough to be worth my time.

I’ll begin with generalization, information acquisition and geometric structure, then follow the questions below. The deeper branches are optional; this is a conceptual sequence rather than a strict prerequisite chain.

## Orientation

1. [The Real Reason Huge AI Models Actually Work \[Prof. Andrew Wilson\]](collections/mlst/reviews/M-jTeBCEGHc.md) — Machine Learning Street Talk · Podcast
2. [The Math Behind Every Recommendation You've Ever Seen - Wouter Koolen](collections/mlst/reviews/h-dYzjF8eFA.md) — Machine Learning Street Talk · Podcast
3. [The Geometric Deep Learning Blueprint — Michael Bronstein](collections/mlst/reviews/bIZB1hIJ4u8.md) — Machine Learning Street Talk · Podcast

## 1 · What would count as understanding intelligence?

What distinguishes acquired skill, learning efficiency, decodable information and an actual computational mechanism?

Before interpreting a score or an explanation, I need to specify the system boundary and what is being estimated. The same behavior can fit different beliefs, preferences or policies; interventions should separate these explanations.

### Starting episodes

- [#51 FRANCOIS CHOLLET - Intelligence and Generalisation](collections/mlst/reviews/J0p_thJJnoo.md) — Machine Learning Street Talk · Podcast
- [039 - Lena Voita - NLP](collections/mlst/reviews/Q0kN_ZHHDQY.md) — Machine Learning Street Talk · Podcast
- [NEURAL NETWORKS ARE WEIRD! - Neel Nanda (DeepMind)](collections/mlst/reviews/YpFaPKOeNME.md) — Machine Learning Street Talk · Podcast

### Deeper branches

- [AI BENCHMARKS ARE BROKEN! \[Prof. MELANIE MITCHELL\]](collections/mlst/reviews/29gkDpR2orc.md) — Machine Learning Street Talk · Podcast
- [#107 - Dr. RAPHAËL MILLIÈRE - Linguistics, Theory of Mind, Grounding](collections/mlst/reviews/fhn6ZtD6XeE.md) — Machine Learning Street Talk · Podcast
- [Strange Geometric Shapes Found Inside AIs — Tom McGrath](collections/mlst/reviews/_egu7OFem-k.md) — Machine Learning Street Talk · Podcast
- [#040 - Adversarial Examples (Dr. Nicholas Carlini, Dr. Wieland Brendel, Florian Tramèr)](collections/mlst/reviews/2PenK06tvE4.md) — Machine Learning Street Talk · Podcast
- [#047 Interpretable Machine Learning - Christoph Molnar](collections/mlst/reviews/0LIACHcxpHU.md) — Machine Learning Street Talk · Podcast
- [The Gap Between Humans and Machines Is ___ \[Dr. Max Bartolo\]](collections/mlst/reviews/DL7qwmWWk88.md) — Machine Learning Street Talk · Podcast
- [Is ChatGPT an N-gram model on steroids?](collections/mlst/reviews/W485bz0_TdI.md) — Machine Learning Street Talk · Podcast
- [How Researchers Test AI for Hidden Goals — Apollo Research](collections/mlst/reviews/n1Qk8xbqF-M.md) — Machine Learning Street Talk · Podcast

### An experiment I could try

I want to take one apparent reasoning capability and design separate tests of task elicitation, novel composition, internal causal use and robustness. For each successful test, I’ll record what it still leaves unidentified.

## 2 · Which prior structure makes learning possible?

How can a huge hypothesis class generalize, and when should structure be built in?

Capacity, preference over functions, optimization and invariance are different objects.

### Starting episodes

- [The Real Reason Huge AI Models Actually Work \[Prof. Andrew Wilson\]](collections/mlst/reviews/M-jTeBCEGHc.md) — Machine Learning Street Talk · Podcast
- [#036 - Max Welling: Quantum, Manifolds & Symmetries in ML](collections/mlst/reviews/mmDw5glry9w.md) — Machine Learning Street Talk · Podcast
- [The Geometric Deep Learning Blueprint — Michael Bronstein](collections/mlst/reviews/bIZB1hIJ4u8.md) — Machine Learning Street Talk · Podcast

### Deeper branches

- [The Lottery Ticket Hypothesis with Jonathan Frankle](collections/mlst/reviews/SfjJoevBbjU.md) — Machine Learning Street Talk · Podcast
- [Why More Data Cannot Replace Prior Structure - Alexander Mattick](collections/mlst/reviews/1S1B4XkFCD8.md) — Machine Learning Street Talk · Podcast
- [Sara Hooker - The Hardware Lottery, Sparsity and Fairness](collections/mlst/reviews/sQFxbQ7ade0.md) — Machine Learning Street Talk · Podcast
- [#71 - ZAK JOST (Graph Neural Networks + Geometric DL) \[UNPLUGGED\]](collections/mlst/reviews/jAGIuobLp60.md) — Machine Learning Street Talk · Podcast

### An experiment I could try

I could specify a task transformation group and compare invariance, equivariance and augmentation. Then I’d change the task so the assumed symmetry becomes wrong and measure the cost of that prior.

## 3 · How do useful abstractions emerge?

What information should a representation retain, discard or make easy to use?

Learning objectives, data structure and downstream use jointly determine what counts as a useful abstraction.

### Starting episodes

- [#032- Simon Kornblith / GoogleAI - SimCLR and Paper Haul!](collections/mlst/reviews/1EqJyMy0LnE.md) — Machine Learning Street Talk · Podcast
- [AI Is Learning at the Wrong Level of Abstraction — Matthieu Wyart](collections/mlst/reviews/revreN8LZ_M.md) — Machine Learning Street Talk · Podcast
- [The Mathematical Foundations of Intelligence \[Professor Yi Ma\]](collections/mlst/reviews/QWidx8cYVRs.md) — Machine Learning Street Talk · Podcast

### Deeper branches

- [#55 Dr. ISHAN MISRA - Self-Supervised Vision Models](collections/mlst/reviews/EXJmodhu4_4.md) — Machine Learning Street Talk · Podcast
- [SWaV: Unsupervised Learning of Visual Features by Contrasting Cluster Assignments (Mathilde Caron)](collections/mlst/reviews/uqJ2hbDGHjY.md) — Machine Learning Street Talk · Podcast
- [Neural Networks Are Elastic Origami! \[Prof. Randall Balestriero\]](collections/mlst/reviews/l3O2J3LMxqI.md) — Machine Learning Street Talk · Podcast
- [#97 SREEJAN KUMAR - Human Inductive Biases in Machines from Language](collections/mlst/reviews/VvXfK-Qle-Y.md) — Machine Learning Street Talk · Podcast
- [ML Robustness & Engineering - Andrew Ilyas (MIT)](collections/mlst/reviews/9BC9BsZRCKQ.md) — Machine Learning Street Talk · Podcast
- [AI Interpretability, Safety, and Meaning - Nora Belrose](collections/mlst/reviews/VgPrjHxIS0I.md) — Machine Learning Street Talk · Podcast
- [#87 - ADELE MYERS - Regression-Based Elastic Metric Learning on Shape Spaces of Cell Curves #NEURIPS](collections/mlst/reviews/24u6CTV4t1k.md) — Machine Learning Street Talk · Podcast

### An experiment I could try

A useful experiment would start with hierarchical data generated from two independent latent factors. I’d vary the prediction target or positive-pair construction and check which factor becomes accessible, transferable and causally used.

## 4 · How does structure become executable reasoning?

What separates representing a solution, discovering it and executing it reliably?

Typed composition, proposal priors, search and verification can play different roles in one intelligent system. Learning abstractions changes which hypotheses are computationally accessible, even when expressivity is unchanged.

### Starting episodes

- [Why Program Synthesis Is Next (Kevin Ellis and Zenna Tavares)](collections/mlst/reviews/oYTm0p3DCzg.md) — Machine Learning Street Talk · Podcast
- [What is “reasoning” in modern AI?](collections/mlst/reviews/XFMk0snybAc.md) — Machine Learning Street Talk · Podcast
- [#85 Dr. Petar Veličković (Deepmind) - Categories, Graphs, Reasoning \[NEURIPS22 UNPLUGGED\]](collections/mlst/reviews/1lkdWduuN14.md) — Machine Learning Street Talk · Podcast
- [Decompiling Dreams: A New Approach to ARC?](collections/mlst/reviews/3ZTNps2PraM.md) — Machine Learning Street Talk · Podcast

### Deeper branches

- [Can Latent Program Networks Solve Abstract Reasoning? \[Clement Bonnet\]](collections/mlst/reviews/PHBItVuudbU.md) — Machine Learning Street Talk · Podcast
- [The "Final Boss" of Deep Learning](collections/mlst/reviews/AWqvBdqCAAE.md) — Machine Learning Street Talk · Podcast
- [#50 Dr. CHRISTIAN SZEGEDY - Formal Reasoning, Program Synthesis](collections/mlst/reviews/ehNGGYFO6ms.md) — Machine Learning Street Talk · Podcast
- [#62 Dr. GUY EMERSON + Walid Saba \[Unplugged\]](collections/mlst/reviews/dhM0_EKLg9k.md) — Machine Learning Street Talk · Podcast
- [#53 Prof. BOB COECKE - Quantum Natural Language Processing](collections/mlst/reviews/X9uSV1YcOy4.md) — Machine Learning Street Talk · Podcast
- [Transformers Need Glasses! \[Federico Barbero\]](collections/mlst/reviews/FAspMnu4Rt0.md) — Machine Learning Street Talk · Podcast
- [WE MUST ADD STRUCTURE TO DEEP LEARNING BECAUSE...](collections/mlst/reviews/rie-9AEhYdY.md) — Machine Learning Street Talk · Podcast
- [Solving Chollet's ARC-AGI with GPT4o](collections/mlst/reviews/z9j3wB1RRGA.md) — Machine Learning Street Talk · Podcast

### An experiment I could try

I want to solve the same small task family with a direct network, a learned program proposal plus an exact interpreter, and latent search. I’d track proposal coverage, search cost and execution errors separately.

## 5 · Which evidence is worth acquiring?

How should a finite learner spend observations, memory and adaptation compute?

Information is valuable relative to a decision and existing knowledge; similarity and confidence alone are insufficient acquisition rules.

### Starting episodes

- [The Math Behind Every Recommendation You've Ever Seen - Wouter Koolen](collections/mlst/reviews/h-dYzjF8eFA.md) — Machine Learning Street Talk · Podcast
- [Test-Time Adaptation: A New Frontier in AI \[Dr. Jonas Hübotter\]](collections/mlst/reviews/C6sSs6NgANo.md) — Machine Learning Street Talk · Podcast
- [The AI That Replaces Hours of Model Tuning - Frank Hutter](collections/mlst/reviews/72Im-Mm5JKs.md) — Machine Learning Street Talk · Podcast

### Deeper branches

- [Learning at test time in LLMs \[Jonas Hübotter\]](collections/mlst/reviews/vei7uf9wOxI.md) — Machine Learning Street Talk · Podcast
- [#92 - SARA HOOKER - Fairness, Interpretability, Language Models](collections/mlst/reviews/7oJui4eSCoY.md) — Machine Learning Street Talk · Podcast
- [#063 - Prof. YOSHUA BENGIO - GFlowNets, Consciousness & Causality](collections/mlst/reviews/M49TMqK5uCE.md) — Machine Learning Street Talk · Podcast
- [Test-Time Adaptation: the key to reasoning with DL](collections/mlst/reviews/3p0O28W1ZHg.md) — Machine Learning Street Talk · Podcast
- [The ARC Prize 2024 Winning Algorithm \[Daniel Franzen and Jan Disselhoff\]](collections/mlst/reviews/mTX_sAq--zY.md) — Machine Learning Street Talk · Podcast

### An experiment I could try

I could build a redundant candidate pool and compare nearest-neighbor retrieval with conditional uncertainty reduction. Deliberately misspecifying the representation and task prior should help me locate the limits of each approach.

## 6 · When is a world model good enough to act?

How do inference, active sensing and planning interact when the model is wrong?

Prediction accuracy, decision adequacy and closed-loop stability are distinct requirements. Optimizers can exploit their own models' errors.

### Starting episodes

- [Harri Valpola: System 2 AI and Planning in Model-Based Reinforcement Learning](collections/mlst/reviews/HnZDmxYnpg4.md) — Machine Learning Street Talk · Podcast
- [Dr. THOMAS PARR - Active Inference](collections/mlst/reviews/bk_xCikDUDQ.md) — Machine Learning Street Talk · Podcast
- [Building a GENERAL AI agent with reinforcement learning](collections/mlst/reviews/s3C0sEwixkQ.md) — Machine Learning Street Talk · Podcast

### Deeper branches

- [This man builds intelligent machines](collections/mlst/reviews/2wnJ6E6rQsU.md) — Machine Learning Street Talk · Podcast
- [Why LeCun Thinks Deep Learning Isn't Enough — Yann LeCun](collections/mlst/reviews/86ib0sfdFtw.md) — Machine Learning Street Talk · Podcast
- [AIs can now imagine video games in real-time](collections/mlst/reviews/kbt0ZFoI2Hc.md) — Machine Learning Street Talk · Podcast
- [AutoGrad Changed Everything (Not Transformers) \[Dr. Jeff Beck\]](collections/mlst/reviews/9suqiofCiwM.md) — Machine Learning Street Talk · Podcast
- [Mapping GPT revealed something strange...](collections/mlst/reviews/Bpgloy1dDn0.md) — Machine Learning Street Talk · Podcast
- [#033 Karl Friston - The Free Energy Principle](collections/mlst/reviews/KkR24ieh5Ow.md) — Machine Learning Street Talk · Podcast
- [#67 Prof. KARL FRISTON 2.0 \[Unplugged\]](collections/mlst/reviews/xKQ-F2-o8uM.md) — Machine Learning Street Talk · Podcast

### An experiment I could try

I want to construct a partially observed control task with a misspecified learned model. I’d compare prediction loss with achieved return, look for cases where more planning worsens the policy, and then add an action chosen for information.

## 7 · What can change in a learning system?

Can the learning rule, task generator, search archive or experimental policy itself adapt?

I need to specify the inner and outer variables, timescales and held-out objectives. Improving an artifact does not automatically improve the process that produced it.

### Starting episodes

- [#49 - Meta-Gradients in RL - Dr. Tom Zahavy (DeepMind)](collections/mlst/reviews/hfaZwgk_iS0.md) — Machine Learning Street Talk · Podcast
- [Can AI Improve Itself? \[Chris Lu, Robert Lange, Cong Lu\]](collections/mlst/reviews/1kwbp8hRRfs.md) — Machine Learning Street Talk · Podcast
- [When AI Discovers the Next Transformer — Robert Lange](collections/mlst/reviews/EInEmGaMRLc.md) — Machine Learning Street Talk · Podcast

### Deeper branches

- [ImageNet Moment for Reinforcement Learning? \[Prof. Jakob Foerster\]](collections/mlst/reviews/Jr_nGkCG3og.md) — Machine Learning Street Talk · Podcast
- [Can Rewriting an AI Agent Bend the Intelligence Curve? - Zhengyao Jiang](collections/mlst/reviews/yB6_iFGTq9k.md) — Machine Learning Street Talk · Podcast
- [Wild breakthrough on Math after 56 years... \[Exclusive\]](collections/mlst/reviews/vC9nAosXrJw.md) — Machine Learning Street Talk · Podcast
- [He won a Nobel here for AlphaFold. Then he left. - John Jumper](collections/mlst/reviews/e3gBwLWAerw.md) — Machine Learning Street Talk · Podcast
- [What Building an AI Scientist Actually Requires Beyond Intelligence — Edward Hughes](collections/mlst/reviews/P4bYjTJvD28.md) — Machine Learning Street Talk · Podcast
- [The Man Who Invented Modern AI (Before Everyone Else) — Jürgen Schmidhuber](collections/mlst/reviews/DP454c1K_vQ.md) — Machine Learning Street Talk · Podcast

### An experiment I could try

A small search loop with an archive, proposer and verifier would let me freeze each component in turn and test transfer to unseen task families. I’d also check whether the search can exploit the evaluator.

## 8 · Where do new problems and possibilities come from?

What maintains discovery when distance to a fixed target is misleading?

Diversity, representation neighborhoods, curricula and observers shape open-ended search. Novelty alone is not intelligence. Sampling a reward-weighted distribution differs from optimizing its maximum; a sampler alone does not supply an exploration objective.

### Starting episodes

- [Why Greatness Cannot Be Planned — Kenneth Stanley](collections/mlst/reviews/lhYGXYeMq_E.md) — Machine Learning Street Talk · Podcast
- [AI Isn't Creative \[Prof. Kenneth Stanley\]](collections/mlst/reviews/KKUKikuV58o.md) — Machine Learning Street Talk · Podcast
- [The AI Paradigm That Nobody Talks About — Tim Rocktäschel](collections/mlst/reviews/6DrCq8Ry2cw.md) — Machine Learning Street Talk · Podcast

### Deeper branches

- [Don't invent faster horses - Prof. Jeff Clune](collections/mlst/reviews/mw5WIDGRLnA.md) — Machine Learning Street Talk · Podcast
- [What Most People Get Wrong About Evolution | Akarsh Kumar](collections/mlst/reviews/615B5nyMFPk.md) — Machine Learning Street Talk · Podcast
- [Google Researcher Shows Life "Emerges From Code" \[Blaise Agüera y Arcas\]](collections/mlst/reviews/rMSEqJ_4EBk.md) — Machine Learning Street Talk · Podcast
- [What If Intelligence Didn't Evolve? It "Was There" From the Start! - Blaise Agüera y Arcas](collections/mlst/reviews/M2iX6HQOoLg.md) — Machine Learning Street Talk · Podcast
- [#81  JULIAN TOGELIUS, Prof. KEN STANLEY - AGI, Games, Diversity & Creativity \[UNPLUGGED\]](collections/mlst/reviews/iqkkkA9dtY0.md) — Machine Learning Street Talk · Podcast
- [Exploring Open-Ended Algorithms: POET](collections/mlst/reviews/sIv-JoFf-Ww.md) — Machine Learning Street Talk · Podcast
- [#063 - Prof. YOSHUA BENGIO - GFlowNets, Consciousness & Causality](collections/mlst/reviews/M49TMqK5uCE.md) — Machine Learning Street Talk · Podcast

### An experiment I could try

I could compare objective search, novelty search and quality diversity in a deceptive environment, then change the behavior descriptor and record which stepping stones disappear. I’d measure collective coverage separately from the competence of one deployable generalist.

## 9 · Which parts of intelligence extend beyond one model or brain?

How do feedback, reference frames, communication and incentives organize competence across scales?

Biological and collective accounts suggest different mechanisms; similar behavior does not uniquely identify the same implementation. Shared beliefs and compatible representations do not guarantee aligned incentives.

### Starting episodes

- [Michael Levin - Why Intelligence Isn't Limited To Brains.](collections/mlst/reviews/6w5xr8BYV8M.md) — Machine Learning Street Talk · Podcast
- [#59 JEFF HAWKINS - Thousand Brains Theory](collections/mlst/reviews/6VQILbDqaI4.md) — Machine Learning Street Talk · Podcast
- [Intelligence is collective, not artificial — Prof. Michael I. Jordan (UC Berkeley / Inria)](collections/mlst/reviews/AREWYbVtX64.md) — Machine Learning Street Talk · Podcast

### Deeper branches

- [Your Brain Doesn't Command Your Body. It Predicts It. \[Max Bennett\]](collections/mlst/reviews/RvYSsi6rd4g.md) — Machine Learning Street Talk · Podcast
- [The Hidden Math Behind All Living Systems](collections/mlst/reviews/hf18w6CuY8o.md) — Machine Learning Street Talk · Podcast
- [Rethinking the Mind - Prof. Mark Solms](collections/mlst/reviews/meUtWtY00H8.md) — Machine Learning Street Talk · Podcast
- [Biologically-inspired AI and Mortal Computation](collections/mlst/reviews/ZTE-JVd_QkA.md) — Machine Learning Street Talk · Podcast
- [#041 Dr. SIMON STRINGER - Biologically Plausible Neural Networks](collections/mlst/reviews/aisgNLypUKs.md) — Machine Learning Street Talk · Podcast
- [This is what happens when you let AIs debate](collections/mlst/reviews/WlWAhjPfROU.md) — Machine Learning Street Talk · Podcast
- ["We need AIs with PHYSICAL experience" (Jeff Beck)](collections/mlst/reviews/zv6qzWecj5c.md) — Machine Learning Street Talk · Podcast
- [KARL FRISTON - INTELLIGENCE 3.0](collections/mlst/reviews/V_VXOdf1NMw.md) — Machine Learning Street Talk · Podcast

### An experiment I could try

I want to choose a proposed agent boundary and identify its state, observations, actions, memory, preferences and evidence of adaptation. The next step would be an intervention that distinguishes feedback regulation from model-based planning.

## Working conclusions

**Claim:** Prior structure is unavoidable; its location is a design choice.

**Explanation:** Priors can enter through architectures, task generators, objectives, language targets, programs and search procedures. The useful question is which prior supports which transfer, and at what total cost.

- [The Real Reason Huge AI Models Actually Work \[Prof. Andrew Wilson\]](collections/mlst/reviews/M-jTeBCEGHc.md) — Machine Learning Street Talk · Podcast
- [The Geometric Deep Learning Blueprint — Michael Bronstein](collections/mlst/reviews/bIZB1hIJ4u8.md) — Machine Learning Street Talk · Podcast
- [The AI That Replaces Hours of Model Tuning - Frank Hutter](collections/mlst/reviews/72Im-Mm5JKs.md) — Machine Learning Street Talk · Podcast
- [#97 SREEJAN KUMAR - Human Inductive Biases in Machines from Language](collections/mlst/reviews/VvXfK-Qle-Y.md) — Machine Learning Street Talk · Podcast

**Claim:** Statistical learning and compositional structure are not mutually exclusive categories.

**Explanation:** Wyart supplies a tractable statistical route to hierarchy, while Ellis, Chaudhuri and Petar show how executable structure changes search and generalization. None proves that one recipe covers all intelligence. Claims that neural systems only interpolate require a specified definition and counterexample-sensitive scope.

- [AI Is Learning at the Wrong Level of Abstraction — Matthieu Wyart](collections/mlst/reviews/revreN8LZ_M.md) — Machine Learning Street Talk · Podcast
- [Why Program Synthesis Is Next (Kevin Ellis and Zenna Tavares)](collections/mlst/reviews/oYTm0p3DCzg.md) — Machine Learning Street Talk · Podcast
- [#85 Dr. Petar Veličković (Deepmind) - Categories, Graphs, Reasoning \[NEURIPS22 UNPLUGGED\]](collections/mlst/reviews/1lkdWduuN14.md) — Machine Learning Street Talk · Podcast
- [Why LeCun Thinks Deep Learning Isn't Enough — Yann LeCun](collections/mlst/reviews/86ib0sfdFtw.md) — Machine Learning Street Talk · Podcast

**Claim:** A representation is useful relative to an operation or decision.

**Explanation:** Information can be present but hard to decode, easy to decode but unused, or predictive without supporting intervention. I need to keep accessibility, causal use and control adequacy separate.

- [039 - Lena Voita - NLP](collections/mlst/reviews/Q0kN_ZHHDQY.md) — Machine Learning Street Talk · Podcast
- [#032- Simon Kornblith / GoogleAI - SimCLR and Paper Haul!](collections/mlst/reviews/1EqJyMy0LnE.md) — Machine Learning Street Talk · Podcast
- [Harri Valpola: System 2 AI and Planning in Model-Based Reinforcement Learning](collections/mlst/reviews/HnZDmxYnpg4.md) — Machine Learning Street Talk · Podcast
- [Strange Geometric Shapes Found Inside AIs — Tom McGrath](collections/mlst/reviews/_egu7OFem-k.md) — Machine Learning Street Talk · Podcast

**Claim:** Search success, correctness and discovery are different achievements.

**Explanation:** Candidate generators, search policies, archives and verifiers contribute separately. A sound formal verifier certifies a specified property under assumptions; an interpreter or empirical test establishes only the tested behavior. Neither certifies that a task specification captures intent or that a discovery is scientifically important.

- [#50 Dr. CHRISTIAN SZEGEDY - Formal Reasoning, Program Synthesis](collections/mlst/reviews/ehNGGYFO6ms.md) — Machine Learning Street Talk · Podcast
- [What is “reasoning” in modern AI?](collections/mlst/reviews/XFMk0snybAc.md) — Machine Learning Street Talk · Podcast
- [Wild breakthrough on Math after 56 years... \[Exclusive\]](collections/mlst/reviews/vC9nAosXrJw.md) — Machine Learning Street Talk · Podcast
- [When AI Discovers the Next Transformer — Robert Lange](collections/mlst/reviews/EInEmGaMRLc.md) — Machine Learning Street Talk · Podcast

**Claim:** Free-energy and biological accounts are research frameworks with explicit commitments.

**Explanation:** My interest is in the inference–action mechanisms and the generative model, boundary, preferences and physical assumptions they require. A variational identity does not by itself establish a universal theory of intelligence or consciousness.

- [Dr. THOMAS PARR - Active Inference](collections/mlst/reviews/bk_xCikDUDQ.md) — Machine Learning Street Talk · Podcast
- [#67 Prof. KARL FRISTON 2.0 \[Unplugged\]](collections/mlst/reviews/xKQ-F2-o8uM.md) — Machine Learning Street Talk · Podcast
- [How can we add knowledge to AI agents?](collections/mlst/reviews/qxEfcrmTWO4.md) — Machine Learning Street Talk · Podcast
- [Michael Levin - Why Intelligence Isn't Limited To Brains.](collections/mlst/reviews/6w5xr8BYV8M.md) — Machine Learning Street Talk · Podcast

**Claim:** Open-endedness changes the object of study, but does not remove evaluation assumptions.

**Explanation:** Task generation, novelty measures, learned judges and population memory shape which discoveries become available. Preserving stepping stones is a concrete mechanism; inevitable unlimited creativity is a stronger claim.

- [Why Greatness Cannot Be Planned — Kenneth Stanley](collections/mlst/reviews/lhYGXYeMq_E.md) — Machine Learning Street Talk · Podcast
- [AI Isn't Creative \[Prof. Kenneth Stanley\]](collections/mlst/reviews/KKUKikuV58o.md) — Machine Learning Street Talk · Podcast
- [The AI Paradigm That Nobody Talks About — Tim Rocktäschel](collections/mlst/reviews/6DrCq8Ry2cw.md) — Machine Learning Street Talk · Podcast
- [Don't invent faster horses - Prof. Jeff Clune](collections/mlst/reviews/mw5WIDGRLnA.md) — Machine Learning Street Talk · Podcast

## Overlap between episodes

**Note:** The two Hübotter interviews share conditional information acquisition and test-time specialization. I’ll start with the earlier foundation and return to the later episode for its updated application and representation caveats.

- [Test-Time Adaptation: A New Frontier in AI \[Dr. Jonas Hübotter\]](collections/mlst/reviews/C6sSs6NgANo.md) — Machine Learning Street Talk · Podcast
- [Learning at test time in LLMs \[Jonas Hübotter\]](collections/mlst/reviews/vei7uf9wOxI.md) — Machine Learning Street Talk · Podcast

**Note:** The main Chollet interview is my starting point for skill-acquisition efficiency. The later talk, update and panel add critiques and historical context; I don’t need to finish all of them before moving on to constructive mechanisms.

- [#51 FRANCOIS CHOLLET - Intelligence and Generalisation](collections/mlst/reviews/J0p_thJJnoo.md) — Machine Learning Street Talk · Podcast
- [It's Not About Scale, It's About Abstraction](collections/mlst/reviews/s7_NlkBwdj8.md) — Machine Learning Street Talk · Podcast
- [François Chollet on OpenAI o-models and ARC](collections/mlst/reviews/w9WE1aOPjHc.md) — Machine Learning Street Talk · Podcast
- [Francois Chollet - On the Measure Of Intelligence](collections/mlst/reviews/mEVnu-KZjq4.md) — Machine Learning Street Talk · Podcast

**Note:** Bronstein supplies the geometric foundation, Jost an accessible GNN bridge, Petar concrete algorithmic and topology examples, and Dudzik a broader compositional framework. That gives me a useful progression through their overlapping material.

- [The Geometric Deep Learning Blueprint — Michael Bronstein](collections/mlst/reviews/bIZB1hIJ4u8.md) — Machine Learning Street Talk · Podcast
- [#71 - ZAK JOST (Graph Neural Networks + Geometric DL) \[UNPLUGGED\]](collections/mlst/reviews/jAGIuobLp60.md) — Machine Learning Street Talk · Podcast
- [#85 Dr. Petar Veličković (Deepmind) - Categories, Graphs, Reasoning \[NEURIPS22 UNPLUGGED\]](collections/mlst/reviews/1lkdWduuN14.md) — Machine Learning Street Talk · Podcast
- [The "Final Boss" of Deep Learning](collections/mlst/reviews/AWqvBdqCAAE.md) — Machine Learning Street Talk · Podcast

**Note:** I’ll start with Kornblith. Misra is a follow-up for broader assumptions, while SWaV offers a worked anti-collapse mechanism. The short LeCun/Balestriero episode consolidates the spectral viewpoint.

- [#032- Simon Kornblith / GoogleAI - SimCLR and Paper Haul!](collections/mlst/reviews/1EqJyMy0LnE.md) — Machine Learning Street Talk · Podcast
- [#55 Dr. ISHAN MISRA - Self-Supervised Vision Models](collections/mlst/reviews/EXJmodhu4_4.md) — Machine Learning Street Talk · Podcast
- [SWaV: Unsupervised Learning of Visual Features by Contrasting Cluster Assignments (Mathilde Caron)](collections/mlst/reviews/uqJ2hbDGHjY.md) — Machine Learning Street Talk · Podcast
- [#86 - Prof. YANN LECUN and Dr. RANDALL BALESTRIERO - SSL, Data Augmentation \[NEURIPS2022\]](collections/mlst/reviews/9dLd6n9yT8U.md) — Machine Learning Street Talk · Podcast

**Note:** Nanda’s newer interview is my broad methodological starting point. The older episode and McGrath add particular techniques and geometric structures. The distinction to preserve is between reading a probe and identifying a mechanism.

- [NEURAL NETWORKS ARE WEIRD! - Neel Nanda (DeepMind)](collections/mlst/reviews/YpFaPKOeNME.md) — Machine Learning Street Talk · Podcast
- [Mechanistic Interpretability - NEEL NANDA (DeepMind)](collections/mlst/reviews/_Ygf0GnlwmY.md) — Machine Learning Street Talk · Podcast
- [Strange Geometric Shapes Found Inside AIs — Tom McGrath](collections/mlst/reviews/_egu7OFem-k.md) — Machine Learning Street Talk · Podcast

**Note:** Parr gives me the clearest starting point for inference and action. The longer Friston/Ramstead discussions are opportunities to compare formulations and examine their assumptions; I shouldn’t count them as six independent confirmations of one universal claim.

- [Dr. THOMAS PARR - Active Inference](collections/mlst/reviews/bk_xCikDUDQ.md) — Machine Learning Street Talk · Podcast
- [#033 Karl Friston - The Free Energy Principle](collections/mlst/reviews/KkR24ieh5Ow.md) — Machine Learning Street Talk · Podcast
- [#67 Prof. KARL FRISTON 2.0 \[Unplugged\]](collections/mlst/reviews/xKQ-F2-o8uM.md) — Machine Learning Street Talk · Podcast
- [KARL FRISTON - INTELLIGENCE 3.0](collections/mlst/reviews/V_VXOdf1NMw.md) — Machine Learning Street Talk · Podcast
- [The Physics of AI](collections/mlst/reviews/8qb28P7ksyE.md) — Machine Learning Street Talk · Podcast
- [Autopoietic Enactivism and the Free Energy Principle - Prof. Friston, Prof Buckley, Dr. Ramstead](collections/mlst/reviews/bL00-jtRrMA.md) — Machine Learning Street Talk · Podcast

**Note:** I’ll use the earlier Kambhampati interview for composable validators, domain-model acquisition and partial testing guarantees, then add passages from the later planning discussion. Neither supports a general theorem that autoregressive models cannot reason.

- [Do you think that ChatGPT can reason? \[Prof. Subbarao Kambhampati\]](collections/mlst/reviews/y1WnHpedi2A.md) — Machine Learning Street Talk · Podcast
- [The Professor Who Proved ChatGPT Can't Think — Subbarao Kambhampati](collections/mlst/reviews/2xFTNXK6AzQ.md) — Machine Learning Street Talk · Podcast

**Note:** The later MindsAI interview is my starting point for the more developed algorithmic account. The early panel adds task-dependent objecthood, the optimizer as part of the agent, and the difference between generating examples and generating new concepts.

- [Chollet's ARC Challenge + Current Winners](collections/mlst/reviews/jSAT_RuJ_Cg.md) — Machine Learning Street Talk · Podcast
- [Test-Time Adaptation: the key to reasoning with DL](collections/mlst/reviews/3p0O28W1ZHg.md) — Machine Learning Street Talk · Podcast

**Note:** I’m keeping these together because they address different questions: probe complexity measures accessibility; erasure tests what survives a specified intervention; circuit analysis reconstructs computation; data attribution studies dependence on training examples. None alone establishes all four.

- [039 - Lena Voita - NLP](collections/mlst/reviews/Q0kN_ZHHDQY.md) — Machine Learning Street Talk · Podcast
- [AI Interpretability, Safety, and Meaning - Nora Belrose](collections/mlst/reviews/VgPrjHxIS0I.md) — Machine Learning Street Talk · Podcast
- [NEURAL NETWORKS ARE WEIRD! - Neel Nanda (DeepMind)](collections/mlst/reviews/YpFaPKOeNME.md) — Machine Learning Street Talk · Podcast
- [ML Robustness & Engineering - Andrew Ilyas (MIT)](collections/mlst/reviews/9BC9BsZRCKQ.md) — Machine Learning Street Talk · Podcast

**Note:** The BFF talks substantially overlap. I only need one technical account before turning to the linked July 2026 corrective paper. I want to keep initial replicator discovery separate from later population takeover when evaluating the merger explanation.

- [What If Intelligence Didn't Evolve? It "Was There" From the Start! - Blaise Agüera y Arcas](collections/mlst/reviews/M2iX6HQOoLg.md) — Machine Learning Street Talk · Podcast
- [Google Researcher Shows Life "Emerges From Code" \[Blaise Agüera y Arcas\]](collections/mlst/reviews/rMSEqJ_4EBk.md) — Machine Learning Street Talk · Podcast

[Report](index.html) · [Methodology](README.md#methodology)
