# The schools

Twenty-seven schools of thought about learning and intelligence. Each entry gives the school's founding claim, the texts it starts from, the [core](README.md) lenses its claim cannot be stated without, and the phenomena it was built to explain or is obliged to answer.

The core was chosen with this list: a lens counted for more when many schools rest on it. The list is kept here so that each school can also be read in its own texts and judged on its own terms.

**How it was made.** The claims and root texts were gathered by AI agents on 2026-11-22 from field sources, during the research for the core. Two independent AI raters then tied each school to the core; only ties both raters made are listed. Four citations (Hopfield 1982, Rao 1945, and both parts of Grossberg 1976) were re-checked against Crossref on 2026-11-23. The other citations have not been checked line by line, so confirm a reference before citing it.

`schools.json` holds the same records in machine-readable form.

## Learning and generalization

<a id="s1"></a>
### S1 · Statistical learning theory

Learning from finite samples is possible exactly when the hypothesis class has controlled capacity (finite VC dimension), which makes empirical frequencies converge to true risks uniformly over the class.

- **Root texts:** Vapnik & Chervonenkis 1971, "On the uniform convergence of relative frequencies of events to their probabilities", *Theory Probab. Appl.* 16(2):264–280; Valiant 1984 "A theory of the learnable"; Vapnik 1995 *The Nature of Statistical Learning Theory*
- **Rests on:** [Learnability & inductive bias](README.md#l6) (first tier); [Concentration of measure](README.md#l22)
- **Must answer to:** [Interpolating networks still generalize](README.md#p1) (first tier)

<a id="s2"></a>
### S2 · Statistical physics of learning

Learning in large systems can be studied as the typical-case thermodynamics of a disordered system: the volume of weight space that is consistent with the data gives capacity, learning curves and phase transitions.

- **Root texts:** Gardner 1988, "The space of interactions in neural network models", *J. Phys. A* 21(1):257–270; Seung, Sompolinsky & Tishby 1992, "Statistical mechanics of learning from examples", *Phys. Rev. A* 45:6056–6091; Hopfield 1982, "Neural networks and physical systems with emergent collective computational abilities", *PNAS* 79(8):2554–2558
- **Rests on:** [Superposition & content-addressable memory](README.md#l14); [Statistical mechanics & typical-case analysis](README.md#l16) (first tier); [Order parameters & phase transitions](README.md#l17) (first tier); [Rugged landscapes](README.md#l19) (first tier)
- **Must answer to:** [Interpolating networks still generalize](README.md#p1) (first tier); [Sharp thresholds and computational gaps](README.md#p5)

<a id="s3"></a>
### S3 · Deep learning theory

Deep networks generalise and learn features for reasons that classical capacity theory does not capture. These include implicit bias of the optimiser, infinite-width/kernel limits, and effective theories in depth/width.

- **Root texts:** Zhang, Bengio, Hardt, Recht & Vinyals 2017, "Understanding deep learning requires rethinking generalization", ICLR (arXiv:1611.03530), which states the problem; Jacot, Gabriel & Hongler 2018, "Neural tangent kernel", NeurIPS 31; Roberts & Yaida (with Hanin) 2022, *The Principles of Deep Learning Theory*, CUP
- **Rests on:** [Learnability & inductive bias](README.md#l6) (first tier); [Statistical mechanics & typical-case analysis](README.md#l16) (first tier); [Scaling & renormalization](README.md#l18) (first tier)
- **Must answer to:** [Interpolating networks still generalize](README.md#p1) (first tier); [Smooth power-law learning curves](README.md#p2) (first tier); [Adversarial and shortcut vulnerability](README.md#p3)

<a id="s24"></a>
### S24 · Kernel methods

Nonlinear learning becomes linear in a reproducing-kernel Hilbert space: similarity is an inner product in feature space, and regularised solutions lie in the span of the data (representer theorem).

- **Root texts:** Aronszajn 1950, "Theory of reproducing kernels", *Trans. AMS* 68:337–404; Boser, Guyon & Vapnik 1992, "A training algorithm for optimal margin classifiers", COLT '92 pp. 144–152; Kimeldorf & Wahba 1971
- **Rests on:** [Learnability & inductive bias](README.md#l6) (first tier); [Representational geometry](README.md#l15) (first tier); [Concentration of measure](README.md#l22)

<a id="s15"></a>
### S15 · Geometric deep learning and symmetry

Successful architectures are derived from the symmetry group of the data domain (grids, groups, graphs, geodesics, gauges). Equivariance is the inductive bias that defeats the curse of dimensionality.

- **Root texts:** Bronstein, Bruna, Cohen & Veličković 2021, "Geometric deep learning: grids, groups, graphs, geodesics, and gauges", arXiv:2104.13478; Klein 1872; Cohen & Welling 2016 G-CNNs
- **Rests on:** [Learnability & inductive bias](README.md#l6) (first tier); [Concentration of measure](README.md#l22); [Symmetry & invariance](README.md#l31) (first tier)

<a id="s20"></a>
### S20 · Information geometry

A family of probability distributions is a Riemannian manifold with the Fisher metric, which is unique under sufficient-statistic invariance. Learning and estimation are geometric, and the natural gradient is Fisher-efficient.

- **Root texts:** Rao 1945, "Information and the accuracy attainable in the estimation of statistical parameters", *Bull. Calcutta Math. Soc.* 37:81; Amari 1985 *Differential-Geometrical Methods in Statistics*; Amari 1998, "Natural gradient works efficiently in learning", *Neural Computation* 10:251–276
- **Rests on:** [Likelihood & Fisher information](README.md#l4) (first tier); [Symmetry & invariance](README.md#l31) (first tier)

## Inference and information

<a id="s4"></a>
### S4 · Bayesian and probabilistic modelling

All uncertainty is represented by probability, and learning is conditioning a joint model (prior × likelihood) on data. Model comparison by marginal likelihood builds in Occam's razor.

- **Root texts:** Cox 1946 / Jaynes 2003; Pearl 1988, *Probabilistic Reasoning in Intelligent Systems*; MacKay 1992, "Bayesian interpolation", *Neural Computation* 4:415–447
- **Rests on:** [Bayesian updating & exchangeability](README.md#l3) (first tier); [Likelihood & Fisher information](README.md#l4) (first tier); [Causality](README.md#l25)

<a id="s6"></a>
### S6 · Algorithmic information and universal induction

The best prediction weights every computable hypothesis by 2^−(program length). Regularity is compressibility, and universal (uncomputable) induction is optimal up to a constant.

- **Root texts:** Solomonoff 1964, "A formal theory of inductive inference, Part I", *Information and Control* 7(1):1–22, Part II 7(2):224–254; Kolmogorov 1965, "Three approaches to the quantitative definition of information", *Probl. Peredachi Inf.* 1(1):3–11 (English 1968); Hutter 2005, *Universal Artificial Intelligence*
- **Rests on:** [Bayesian updating & exchangeability](README.md#l3) (first tier); [Description length & algorithmic information](README.md#l5) (first tier); [Computation, universality & its limits](README.md#l10) (first tier)

<a id="s7"></a>
### S7 · Information-theoretic: efficient coding, infomax, the information bottleneck

Sensory systems and learners should transmit or keep the most relevant information under capacity limits. Redundancy reduction and relevance-compression trade-offs predict neural codes and representations.

- **Root texts:** Barlow 1961, "Possible principles underlying the transformations of sensory messages", in Rosenblith (ed.) *Sensory Communication*, MIT Press, pp. 217–234; Laughlin 1981, "A simple coding procedure enhances a neuron's information capacity", *Z. Naturforsch. C* 36:910–912; Tishby, Pereira & Bialek, "The information bottleneck method", Allerton 1999 / arXiv physics/0004057 (2000)
- **Rests on:** [Information & coding limits](README.md#l1) (first tier); [Description length & algorithmic information](README.md#l5) (first tier)
- **Must answer to:** [Weber's law and adaptation](README.md#p11); [Receptive fields matched to natural statistics](README.md#p19) (first tier); [Heavy-tailed, scale-invariant natural data](README.md#p30)

<a id="s14"></a>
### S14 · Causality

Causal knowledge is knowledge of what happens under intervention. It cannot be reduced to correlation, and it can be learned from data plus structural assumptions (graphs, potential outcomes).

- **Root texts:** Pearl 2000; Spirtes, Glymour & Scheines 1993, *Causation, Prediction, and Search*; Rubin 1974, "Estimating causal effects of treatments in randomized and nonrandomized studies", *J. Educ. Psychol.* 66(5):688–701
- **Rests on:** [Causality](README.md#l25)

## Mind and brain

<a id="s17"></a>
### S17 · Symbolic and compositional: symbolic AI, the language of thought

Intelligence consists in manipulating structured symbols by rules. A physical symbol system is necessary and sufficient for general intelligent action, and thought has a combinatorial syntax and semantics.

- **Root texts:** Newell & Simon 1976, "Computer science as empirical inquiry: symbols and search", *CACM* 19(3) (Turing lecture); Fodor 1975 *The Language of Thought*; Fodor & Pylyshyn 1988, "Connectionism and cognitive architecture", *Cognition* 28:3–71
- **Rests on:** [Search, tractability & bounded rationality](README.md#l9) (first tier); [Computation, universality & its limits](README.md#l10) (first tier); [Levels of analysis](README.md#l26) (first tier); [Compositionality](README.md#l28)
- **Must answer to:** [Productive, systematic generalization](README.md#p31) (first tier)

<a id="s21"></a>
### S21 · Connectionism, PDP and adaptive resonance

Cognition comes from distributed patterns of activity across simple units, and learning is gradual adjustment of connection weights by local or error-driven rules. ART adds that stable learning requires top-down expectations matched against bottom-up input (resonance), which addresses the stability–plasticity dilemma.

- **Root texts:** Rumelhart, McClelland & PDP Research Group 1986, *Parallel Distributed Processing*, Vol. 1, MIT Press; Rumelhart, Hinton & Williams 1986 *Nature*; Grossberg 1976, "Adaptive pattern classification and universal recoding", *Biol. Cybern.* 23(3):121–134, and Part II, "Feedback, expectation, olfaction, illusions", 23(4):187–202, where adaptive resonance was introduced
- **Rests on:** [Credit assignment & error-driven learning](README.md#l12); [Superposition & content-addressable memory](README.md#l14); [Representational geometry](README.md#l15) (first tier)
- **Must answer to:** [Catastrophic interference](README.md#p4); [Synaptic plasticity](README.md#p20); [Productive, systematic generalization](README.md#p31) (first tier)

<a id="s5"></a>
### S5 · Bayesian cognition

Human learning and inference approximate rational Bayesian inference over structured (often symbolic or causal) hypothesis spaces, given the structure of the environment. Abstract priors are learned hierarchically, which explains learning that outruns the data.

- **Root texts:** Anderson 1990, *The Adaptive Character of Thought* (rational analysis); Tenenbaum, Kemp, Griffiths & Goodman 2011, "How to grow a mind", *Science* 331:1279–1285; Knill & Pouget 2004, "The Bayesian brain", *TINS* 27:712–719
- **Rests on:** [Bayesian updating & exchangeability](README.md#l3) (first tier); [Learnability & inductive bias](README.md#l6) (first tier); [Shrinkage & partial pooling](README.md#l7); [Levels of analysis](README.md#l26) (first tier)
- **Must answer to:** [Learning to learn](README.md#p7); [Universal law of generalization](README.md#p10); [Forgetting, spacing and testing](README.md#p13); [Heuristics, biases and their successes](README.md#p15); [Reliability-weighted cue combination](README.md#p16)

<a id="s22"></a>
### S22 · Predictive processing

The brain is a hierarchical prediction machine. Top-down predictions are matched against input, and only precision-weighted prediction errors are passed upward and used for learning.

- **Root texts:** Rao & Ballard 1999, "Predictive coding in the visual cortex", *Nat. Neurosci.* 2(1):79–87; Clark 2013, "Whatever next?", *BBS* 36(3):181–204; Helmholtz 1867 / Srinivasan, Laughlin & Dubs 1982
- **Rests on:** [Bayesian updating & exchangeability](README.md#l3) (first tier); [Description length & algorithmic information](README.md#l5) (first tier); [Credit assignment & error-driven learning](README.md#l12); [World models & cognitive maps](README.md#l13); [Hierarchy & near-decomposability](README.md#l27)
- **Must answer to:** [Receptive fields matched to natural statistics](README.md#p19) (first tier); [Limits of awareness](README.md#p24)

<a id="s16"></a>
### S16 · Free energy and active inference

Any self-organising system that persists minimises variational free energy, a bound on surprise under a generative model. Perception, learning and action are all forms of this minimisation.

- **Root texts:** Friston 2010, "The free-energy principle: a unified brain theory?", *Nat. Rev. Neurosci.* 11:127–138; Friston, Kilner & Harrison 2006; Parr, Pezzulo & Friston 2022 *Active Inference*
- **Rests on:** [Maximum entropy & variational free energy](README.md#l2) (first tier); [Bayesian updating & exchangeability](README.md#l3) (first tier); [World models & cognitive maps](README.md#l13); [Feedback & regulation](README.md#l32)
- **Must answer to:** [Prediction-error signatures](README.md#p6)

<a id="s8"></a>
### S8 · Normative neuroscience

Neural design is explained by deriving the optimal solution to a stated objective under physical, metabolic and noise constraints, then comparing it with the system. Deviations reveal hidden objectives or constraints.

- **Root texts:** Barlow 1961 (above); Laughlin 1981; Sterling & Laughlin 2015, *Principles of Neural Design*, MIT Press; Bialek 2012, *Biophysics: Searching for Principles*; Marr 1982; for the normative framing as a method, see the review arXiv:2003.13825
- **Rests on:** [Information & coding limits](README.md#l1) (first tier); [Description length & algorithmic information](README.md#l5) (first tier); [Levels of analysis](README.md#l26) (first tier)
- **Must answer to:** [Weber's law and adaptation](README.md#p11); [Reliability-weighted cue combination](README.md#p16); [Receptive fields matched to natural statistics](README.md#p19) (first tier); [Processing near physical limits](README.md#p29)

<a id="s9"></a>
### S9 · Dynamical-systems neuroscience

Neural computation is carried out by the flow of population activity through a low-dimensional state space (attractors, line attractors, rotations), shaped by connectivity and inputs.

- **Root texts:** Hopfield 1982, "Neural networks and physical systems with emergent collective computational abilities", *PNAS* 79(8):2554–2558; Vyas, Golub, Sussillo & Shenoy 2020, "Computation through neural population dynamics", *Annu. Rev. Neurosci.* 43:249–275; Wilson & Cowan 1972; van Gelder 1995 "What might cognition be, if not computation?"
- **Rests on:** [Superposition & content-addressable memory](README.md#l14); [Representational geometry](README.md#l15) (first tier); [Dynamical systems & self-organization](README.md#l21) (first tier)
- **Must answer to:** [Place, grid and attractor codes](README.md#p21); [Low-dimensional structure](README.md#p28) (first tier)

<a id="s27"></a>
### S27 · Generative and usage-based linguistics

Two rival claims about one fact. Generative: children acquire a grammar that their input underdetermines, so part of linguistic structure is innate and specific to language. Usage-based: grammar is built from language use by general learning and social cognition, with no innate grammar.

- **Root texts:** Chomsky 1957 *Syntactic Structures* / 1965 *Aspects*; Hauser, Chomsky & Fitch 2002, *Science* 298:1569–1579; Tomasello 2003, *Constructing a Language*, Harvard UP; Crain & Nakayama 1987, *Language* 63(3):522–543 (poverty-of-stimulus evidence)
- **Rests on:** [Learnability & inductive bias](README.md#l6) (first tier); [Formal languages & the grammar hierarchy](README.md#l11); [Levels of analysis](README.md#l26) (first tier); [Distributional meaning](README.md#l29)
- **Must answer to:** [Innate structure and prepared learning](README.md#p8) (first tier); [Critical periods](README.md#p25) (first tier); [Productive, systematic generalization](README.md#p31) (first tier); [Learners regularize and create structure](README.md#p32)

## Action and embodiment

<a id="s10"></a>
### S10 · Control, reinforcement learning and decision

Intelligent behaviour is choosing actions to maximise long-run value under uncertainty. Learning comes from temporal-difference prediction errors that approximate the Bellman equation.

- **Root texts:** Bellman 1957; Sutton 1988, "Learning to predict by the methods of temporal differences", *Machine Learning* 3:9–44; von Neumann & Morgenstern 1944; Kalman 1960
- **Rests on:** [Decisions under uncertainty](README.md#l8) (first tier); [Credit assignment & error-driven learning](README.md#l12)
- **Must answer to:** [Prediction-error signatures](README.md#p6); [Goal-directed vs habitual control](README.md#p9)

<a id="s18"></a>
### S18 · Cybernetics

Purposeful behaviour in animals and machines is feedback-controlled. A regulator must have requisite variety and, in its simplest optimal form, contain a model of the system it regulates.

- **Root texts:** Rosenblueth, Wiener & Bigelow 1943, "Behavior, purpose and teleology", *Phil. Sci.* 10(1):18–24; Wiener 1948; Ashby 1956; Conant & Ashby 1970, *Int. J. Systems Sci.* 1(2):89–97
- **Rests on:** [Information & coding limits](README.md#l1) (first tier); [Feedback & regulation](README.md#l32)

<a id="s23"></a>
### S23 · Enactivism and embodied cognition

Cognition is not building internal world models. It is the skilled, embodied activity of an autonomous organism coupled to its environment. Perception is mastery of sensorimotor contingencies.

- **Root texts:** Varela, Thompson & Rosch 1991, *The Embodied Mind*; O'Regan & Noë 2001, "A sensorimotor account of vision and visual consciousness", *BBS* 24(5):939–973; Brooks 1991 "Intelligence without representation"
- **Rests on:** [Dynamical systems & self-organization](README.md#l21) (first tier); [Feedback & regulation](README.md#l32)
- **Must answer to:** [Neuropsychological dissociations](README.md#p23); [Limits of awareness](README.md#p24)

## Physics, life and collectives

<a id="s11"></a>
### S11 · Thermodynamics of computation and learning

Information processing has unavoidable thermodynamic costs. Erasure costs kT ln 2, the information a learner acquires is bounded by entropy production, and energy-efficient memory must be predictive.

- **Root texts:** Landauer 1961; Bennett 1982; Still, Sivak, Bell & Crooks 2012, "Thermodynamics of prediction", *PRL* 109:120604; Goldt & Seifert 2017, "Stochastic thermodynamics of learning", *PRL* 118:010601
- **Rests on:** [Information & coding limits](README.md#l1) (first tier); [Noise-driven dynamics](README.md#l20) (first tier); [Thermodynamics of computation](README.md#l30) (first tier)
- **Must answer to:** [Processing near physical limits](README.md#p29)

<a id="s12"></a>
### S12 · Collective and complex systems

Many simple interacting units can produce collective computation and adaptive behaviour that no unit has. This "more is different" emergence is studied with interaction rules, networks and stat-phys methods.

- **Root texts:** Anderson 1972; Simon 1962; Couzin 2009, "Collective cognition in animal groups", *TiCS* 13(1):36–43; Holland 1995 *Hidden Order*
- **Rests on:** [Statistical mechanics & typical-case analysis](README.md#l16) (first tier); [Order parameters & phase transitions](README.md#l17) (first tier); [Dynamical systems & self-organization](README.md#l21) (first tier); [Hierarchy & near-decomposability](README.md#l27)

<a id="s13"></a>
### S13 · Evolution as learning

Natural selection is formally a learning algorithm (Bayesian updating, reinforcement, or PAC-style learning over genotypes). Populations can therefore "learn from experience" and evolve their own evolvability.

- **Root texts:** Watson & Szathmáry 2016, "How can evolution learn?", *TREE* 31(2):147–157; Valiant 2009, "Evolvability", *J. ACM* 56(1), art. 3; Hinton & Nowlan 1987, "How learning can guide evolution", *Complex Systems* 1:495–502
- **Rests on:** [Bayesian updating & exchangeability](README.md#l3) (first tier); [Learnability & inductive bias](README.md#l6) (first tier); [Variation, selection & drift](README.md#l23)

<a id="s19"></a>
### S19 · Basal and diverse intelligence

Cognition is a continuum present in cells, tissues and aneural organisms. Problem-solving competencies scale up through collectives of parts, for example by bioelectric coordination in morphogenesis.

- **Root texts:** Lyon, Keijzer, Arendt & Levin 2021, "Reframing cognition: getting down to biological basics", *Phil. Trans. R. Soc. B* 376:20190750; Levin 2022, "Technological Approach to Mind Everywhere (TAME)", *Front. Syst. Neurosci.* 16:768201
- **Rests on:** [Levels of analysis](README.md#l26) (first tier); [Hierarchy & near-decomposability](README.md#l27); [Feedback & regulation](README.md#l32)

<a id="s25"></a>
### S25 · Physical learning systems

Physical materials (flow and elastic networks, self-assembling molecules, optical media) can learn by local rules driven by their own physics, without a separate computer computing gradients.

- **Root texts:** Stern & Murugan 2023, "Learning without neurons in physical systems", *Annu. Rev. Condens. Matter Phys.* 14:417–441; Scellier & Bengio 2017, "Equilibrium propagation", *Front. Comput. Neurosci.* 11:24; Stern, Hexner, Rocks & Liu 2021 *PRX* (coupled learning)
- **Rests on:** [Credit assignment & error-driven learning](README.md#l12); [Superposition & content-addressable memory](README.md#l14); [Rugged landscapes](README.md#l19) (first tier)

<a id="s26"></a>
### S26 · Open-endedness

Some processes (biological evolution, culture, science) keep producing novel, increasingly complex artefacts without a fixed objective. Pursuing objectives directly is often deceptive, while novelty and stepping stones drive discovery.

- **Root texts:** Lehman & Stanley 2011, "Abandoning objectives: evolution through the search for novelty alone", *Evol. Comput.* 19(2):189–223; Taylor et al. 2016 OEE workshop report, *Artificial Life* 22:408–423; Bedau et al. 2000 "Open problems in artificial life"; Stanley & Lehman 2015 book
- **Rests on:** [Rugged landscapes](README.md#l19) (first tier); [Variation, selection & drift](README.md#l23)
- **Must answer to:** [Cumulative culture](README.md#p35)
