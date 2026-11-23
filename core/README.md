# The core

The ideas to master before branching out: **32 lenses** (ways of seeing that transfer across fields) and **35 phenomena** (established facts any theory of learning and intelligence must answer to). Each item lists its root text, a teaching source where the root does not teach well on its own, and for phenomena a current-status source saying what is robust and what is contested.

Built 2026-11-22 from two rounds of sourced checks: nine field canons (statistics, ML/AI, information and computation, physics, neuroscience, cognitive science, evolution, philosophy of mind, linguistics), the founding claims of 27 schools, and 47 open questions from recognised lists; then a blind saturation test and adversarial checks. Root texts were checked against Crossref and arXiv records. Paywalled items link to their DOI.

Items are grouped into threads. The order inside the study plan comes from the dependencies listed under each item; the threads themselves are a starting arrangement, not a fixed curriculum.

**Tiers.** 26 items (19 lenses, 7 phenomena) form the first tier, marked below. They were chosen from an evidence tally: how many of 27 schools rest on an item, how many of 47 open questions need it, how many of nine independent field lists named it, and how many other core items are built on it; the physics lenses are first tier by choice. The Requires links were checked against what each root text uses.

`core.json` holds the same records in machine-readable form.

## Computation and explanation

<a id="l10"></a>
### L10 · Computation, universality & its limits

*Lens, first tier.*

- **Root text** (free): Turing, A. M. (1936). On Computable Numbers, with an Application to the Entscheidungsproblem. Proc. London Math. Soc. s2-42:230-265. (Gödel 1931 is first-listed, but it is in German with no verified free translation; Turing founds computation and universality.) [link](https://www.cs.virginia.edu/~robins/Turing_Paper_1936.pdf)
- **Does the root teach?** No. Fraktur notation, cumbersome machine encodings and known errors make it hard to learn from first.
- **Start with:** Scott Aaronson, *How Much Math Is Knowable?* (66 min) [link](https://www.youtube.com/watch?v=dQC7AIT91_g)
- **Order:** Aaronson lecture first, then Turing 1936 §§1-6 and §§8-9 (machines, universal machine, the halting-style argument).

<a id="l26"></a>
### L26 · Levels of analysis

*Lens, first tier.* Levels of analysis & implementation independence

- **Root text** (free): Marr, D. & Poggio, T. (1976). From understanding computation to understanding neural circuitry. MIT AI Memo 357. Note: Mayr 1961 (first listed; Science 134:1501, doi:10.1126/science.134.3489.1501, paywalled) is about proximate vs ultimate causes, not implementation independence; Marr & Poggio found the computation/algorithm/implementation split. [link](https://dspace.mit.edu/handle/1721.1/5782)
- **Does the root teach?** Yes. It is a short, plain memo that states the levels and why they are independent, though its neuroscience is dated.
- **Start with:** Tomaso Poggio, *The Levels of Understanding framework, revised (Perception 41:1017-23, 2012; MIT-CSAIL-TR-2012-014)* (~7 pp.) [link](http://hdl.handle.net/1721.1/70970)
- **Requires:** [L10 · Computation, universality & its limits](#l10)
- **Order:** Marr & Poggio 1976 memo first, then Poggio 2012 revision (adds learning and the link between levels).

<a id="l27"></a>
### L27 · Hierarchy & near-decomposability

*Lens.* Hierarchy & near-decomposability, incl. temporal abstraction

- **Root text** (free): Simon, H. A. (1962). The architecture of complexity. Proc. American Philosophical Society 106(6):467-482. [link](https://faculty.sites.iastate.edu/tesfatsi/archive/tesfatsi/ArchitectureOfComplexity.HSimon1962.pdf)
- **Does the root teach?** Yes. Simon derives near-decomposability with clear examples and little formalism; temporal abstraction is only implicit, in the fast/slow dynamics section.
- **Order:** Simon 1962 in full, with close attention to the near-decomposable systems section (fast within-subsystem vs slow between-subsystem dynamics).

## Inference and information

<a id="l1"></a>
### L1 · Information & coding limits

*Lens, first tier.* Information & coding limits: source, channel, rate–distortion; communicative efficiency as a transfer case

- **Root text** (free): Shannon, C. E. (1948). A Mathematical Theory of Communication. Bell System Technical Journal 27:379-423, 623-656. [link](https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf)
- **Does the root teach?** Yes. Shannon builds the source and channel theorems from worked examples in plain notation, and Part V already sketches the fidelity-criterion (rate-distortion) idea; rate-distortion itself is only fully developed in Shannon 1959.
- **Order:** Root Parts I-II (source and noiseless coding), then Part IV (continuous channels) and Part V (fidelity rate); for full rate-distortion read Shannon 1959 (IRE Nat. Conv. Rec., no free copy verified).

<a id="l2"></a>
### L2 · Maximum entropy & variational free energy

*Lens, first tier.* Maximum entropy & the free-energy variational principle

- **Root text** (free): Jaynes, E. T. (1957). Information Theory and Statistical Mechanics. Physical Review 106:620-630. (Gibbs 1902 is the stat-mech precursor; Jaynes founds MaxEnt as an inference principle.) [link](https://bayes.wustl.edu/etj/articles/theory.1.pdf)
- **Does the root teach?** Yes. Short, self-contained derivation of the Gibbs distribution from maximum entropy, in modern notation; it does not cover the variational free-energy (Neal & Hinton) side.
- **Start with:** David M. Blei, Alp Kucukelbir, Jon D. McAuliffe, *Variational Inference: A Review for Statisticians* (~41 pp. paper) [link](https://arxiv.org/abs/1601.00670)
- **Requires:** [L1 · Information & coding limits](#l1)
- **Order:** Root (Jaynes 1957) §§1-4, then Blei et al. §§1-2 (ELBO = negative free energy), then Neal & Hinton 1998 (https://www.cs.toronto.edu/~hinton/absps/emk.pdf, verified).

<a id="l3"></a>
### L3 · Bayesian updating & exchangeability

*Lens, first tier.*

- **Root text** (free): Bayes, T. (1763). An Essay towards Solving a Problem in the Doctrine of Chances. Phil. Trans. R. Soc. 53:370-418. doi:10.1098/rstl.1763.0053 [link](https://archive.org/details/philtrans09948070)
- **Does the root teach?** No. 18th-century geometric argument (the billiard table) with Price's long framing; there is no modern notation, and it says nothing about exchangeability, which is de Finetti 1937 (no free copy verified).
- **Start with:** Josh Tenenbaum, *Development of Intelligence: Bayesian Inference (5/31/14)* (96 min) [link](https://www.youtube.com/watch?v=icEdI0AIOlU)
- **Order:** Tenenbaum lecture first, then Bayes's essay (Price's introduction and Proposition 9), then a de Finetti exchangeability exposition (gap: none verified).

<a id="l4"></a>
### L4 · Likelihood & Fisher information

*Lens, first tier.* Likelihood, sufficiency & Fisher information

- **Root text** (free): Fisher, R. A. (1922). On the Mathematical Foundations of Theoretical Statistics. Phil. Trans. R. Soc. A 222:309-368. doi:10.1098/rsta.1922.0009 (Univ. of Adelaide Fisher digital archive, part 1 of 2; part 2 at .../bitstreams/39f1e753-5765-49fd-b1e8-3b79453a5809/content) [link](https://digital.library.adelaide.edu.au/server/api/core/bitstreams/0eed5b2d-5ac1-4e8e-a847-8de2cd574e65/content)
- **Does the root teach?** No. It is long (60 pp.) and uses 1920s notation, and it introduces consistency, efficiency and sufficiency without the geometric view (Rao 1945, Amari) that the item needs.
- **Start with:** Frank Nielsen, *An elementary introduction to information geometry* (~60 pp. paper) [link](https://arxiv.org/abs/1808.08271)
- **Order:** Root §§1-6 (definitions and the criteria of estimation), then Nielsen §§1-3 (Fisher metric, dual connections), then the Amari survey talk (https://www.youtube.com/watch?v=2Uy6xCpvnj0, backlog).

<a id="l5"></a>
### L5 · Description length & algorithmic information

*Lens, first tier.* Description length & algorithmic information; efficient coding as its sensory form

- **Root text** (free): Solomonoff, R. J. (1964). A Formal Theory of Inductive Inference, Part I. Information and Control 7(1):1-22. (Author's archive.) [link](https://raysolomonoff.com/publications/1964pt1.pdf)
- **Does the root teach?** No. The notation and machine models are idiosyncratic, and it predates Kolmogorov complexity, MDL and Barlow's sensory framing, so it cannot carry the whole lens.
- **Start with:** Paul Vitanyi, Ming Li, *Minimum Description Length Induction, Bayesianism, and Kolmogorov Complexity* (~35 pp. paper (IEEE Trans. IT 2000)) [link](https://arxiv.org/abs/cs/9901014)
- **Requires:** [L1 · Information & coding limits](#l1), [L10 · Computation, universality & its limits](#l10)
- **Order:** Vitanyi & Li first (it ties Solomonoff, Kolmogorov, MDL and Bayes), then Solomonoff 1964 §§1-3, then Grunwald & Roos 2019 (arXiv 1908.08484) for modern MDL, then Barlow 1961 (cnbc.cmu.edu copy, verified) for the sensory form.

<a id="l7"></a>
### L7 · Shrinkage & partial pooling

*Lens.*

- **Root text** (free): James, W. and Stein, C. (1961). Estimation with Quadratic Loss. Proc. Fourth Berkeley Symp. Math. Stat. Prob. 1:361-379. (Project Euclid.) [link](https://projecteuclid.org/euclid.bsmsp/1200512173)
- **Does the root teach?** No. Terse decision-theoretic proofs with no empirical-Bayes or partial-pooling intuition.
- **Start with:** Bradley Efron and Trevor Hastie, *Computer Age Statistical Inference, Ch. 7 'James-Stein Estimation and Ridge Regression' (free PDF from the authors' page)* (~20 pp. chapter) [link](https://hastie.su.domains/CASI/)
- **Requires:** [L6 · Learnability & inductive bias](#l6)
- **Order:** Efron & Hastie Ch. 7 first, then James & Stein 1961 §§1-2, then Baxter 2000, 'A Model of Inductive Bias Learning' (arXiv 1106.0245, verified), for the multi-task transfer.

<a id="l25"></a>
### L25 · Causality

*Lens.* Causality: conditional independence → intervention

- **Root text** (free): Wright, S. (1921). Correlation and causation. J. Agricultural Research 20(7):557-585 (USDA, public domain). Note: Wright founds path diagrams, not intervention; the CI-to-intervention step is founded by Pearl 1995, 'Causal diagrams for empirical research', Biometrika 82:669-710, free at https://ftp.cs.ucla.edu/pub/stat_ser/R218-B.pdf (verified). [link](https://archive.org/details/sim_journal-of-agricultural-research_1921-01-03_20_7)
- **Does the root teach?** No. Wright gives path coefficients in 1921 notation with no do-operator or identification theory, so it shows the origin but not the method.
- **Start with:** Judea Pearl, *Causal inference in statistics: An overview (Statistics Surveys 3, 2009)* (51 pp.) [link](https://ftp.cs.ucla.edu/pub/stat_ser/r350.pdf)
- **Order:** Pearl 2009 overview §§1-3 first, then Pearl 1995 Biometrika (the real founding text), then Wright 1921 for the path-diagram origin.

<a id="p10"></a>
### P10 · Universal law of generalization

*Phenomenon.*

- **Root text** (paywalled): Shepard, R. N. (1987). Toward a universal law of generalization for psychological science. Science 237:1317-1323. doi:10.1126/science.3629243. Only course-site copies exist online. [DOI](https://doi.org/10.1126/science.3629243)
- **Does the root teach?** Yes. Self-contained derivation of the exponential gradient from consequential regions. It assumes only basic probability and MDS, though the geometry is terse.
- **Start with:** Joshua B. Tenenbaum & Thomas L. Griffiths, *Generalization, similarity, and Bayesian inference (BBS 24:629-640, 2001)* (12 pp. + commentaries (paywalled)) [link](https://www.cambridge.org/core/journals/behavioral-and-brain-sciences/article/generalization-similarity-and-bayesian-inference/595CAA321C9C56270C624057021DE77A)
- **Current status:** The Universal Law of Generalization Holds for Naturalistic Stimuli (2023) — Finds the exponential law holds across many naturalistic domains once psychological space is estimated. Its origin (Bayesian vs efficient coding, Sims 2018 doi:10.1126/science.aaq1118) remains debated. [link](https://arxiv.org/abs/2306.08564)
- **Requires:** [L15 · Representational geometry](#l15)
- **Order:** Shepard 1987 first, then Tenenbaum & Griffiths 2001 sections 1-3, then Marjieh et al. 2023.

<a id="p11"></a>
### P11 · Weber's law and adaptation

*Phenomenon.* Weber's law, adaptation and normalization to input statistics

- **Root text** (free): Laughlin, S. B. (1981). A simple coding procedure enhances a neuron's information capacity. Z. Naturforsch. C 36:910-912. doi:10.1515/znc-1981-9-1040. Listed first-root Weber 1834 (De Pulsu, Latin) states only the constant-fraction law. Laughlin founds the claim of matching to input statistics. Free copy: the Max Planck ZfN open archive (1946-2001; Edmond dataset doi:10.17617/3.GRUJYR). The URL resolves to that archive, but a bot check blocked the PDF [unverified file]. [link](https://zfn.mpdl.mpg.de/data/Reihe_C/36/ZNC-1981-36c-0910.pdf)
- **Does the root teach?** Yes. Three pages: the fly LMC response curve matches the cumulative contrast distribution (histogram equalization). It is clear with basic information theory.
- **Start with:** Matteo Carandini & David J. Heeger, *Normalization as a canonical neural computation (Nat. Rev. Neurosci. 13:51-62, 2012)* (12 pp.) [link](https://pmc.ncbi.nlm.nih.gov/articles/PMC3273486/)
- **Current status:** Coding principles in adaptation (Annual Review of Vision Science 5:427-449, 2019) — Adaptation to mean and variance (Brenner et al. 2000) is robust. Whether it serves efficient coding, inference or prediction, and Weber's law's deviations at extremes, are open. [DOI](https://doi.org/10.1146/annurev-vision-091718-014818)
- **Order:** Laughlin 1981 first, then Carandini & Heeger 2012, then Weber et al. 2019 (Brenner et al. 2000 as the worked case).

<a id="p15"></a>
### P15 · Heuristics, biases and their successes

*Phenomenon.*

- **Root text** (paywalled): Tversky, A. & Kahneman, D. (1974). Judgment under uncertainty: heuristics and biases. Science 185:1124-1131. doi:10.1126/science.185.4157.1124. Cambridge UP's free publisher excerpt of the 1982 book reprints chapter 1 but stops mid-availability section: https://assets.cambridge.org/97805212/84141/excerpt/9780521284141_excerpt.pdf (verified, partial). [DOI](https://doi.org/10.1126/science.185.4157.1124)
- **Does the root teach?** Yes. Eight plain-language pages with the classic demonstrations. No background needed.
- **Current status:** Heuristic decision making (Annual Review of Psychology 62:451-482, 2011) — Documents when simple heuristics match or beat complex models (ecological rationality), the 'successes' side. Which biases are robust versus artifacts of framing or format is still contested. Meehl 1954's actuarial-beats-clinical result is robust (Grove et al. 2000 meta-analysis). [DOI](https://doi.org/10.1146/annurev-psych-120709-145346)
- **Order:** Tversky & Kahneman 1974 first, then Gigerenzer & Gaissmaier 2011.

<a id="p16"></a>
### P16 · Reliability-weighted cue combination

*Phenomenon.* Reliability-weighted cue combination, near but not at optimum

- **Root text** (paywalled): Ernst, M. O. & Banks, M. S. (2002). Humans integrate visual and haptic information in a statistically optimal fashion. Nature 415:429-433. doi:10.1038/415429a. Only course-site copies exist online. [DOI](https://doi.org/10.1038/415429a)
- **Does the root teach?** Yes. Five pages that derive the inverse-variance MLE rule and test it directly. Needs only Gaussian algebra.
- **Current status:** Suboptimality in perceptual decision making (BBS 41:e223, 2018) — Reliability weighting is qualitatively robust, but cue combination often falls short of the optimal variance reduction. Whether 'optimality' is a useful standard is contested in the commentaries. [link](https://pmc.ncbi.nlm.nih.gov/articles/PMC6110994/)
- **Requires:** [L4 · Likelihood & Fisher information](#l4)
- **Order:** Ernst & Banks 2002 first, then Rahnev & Denison 2018 (cue-combination section, then the commentaries).

<a id="p30"></a>
### P30 · Heavy-tailed, scale-invariant natural data

*Phenomenon.* Natural data are heavy-tailed and scale-invariant, incl. Zipf and the law of abbreviation

- **Root text** (paywalled): Field 1987, Relations between the statistics of natural images and the response properties of cortical cells, JOSA A 4:2379-2394, doi:10.1364/JOSAA.4.002379 [DOI](https://doi.org/10.1364/JOSAA.4.002379)
- **Does the root teach?** Yes. Readable with careful exposition of the 1/f amplitude spectrum and its coding consequences. It covers images only, so the Zipf and abbreviation strand comes from the status source. The free copy is on a UCSD course site, not the publisher.
- **Start with:** Eero Simoncelli & Bruno Olshausen, *Natural Image Statistics and Neural Representation (Annu Rev Neurosci 2001)* (24 pp) [link](https://www.cns.nyu.edu/pub/eero/simoncelli01-reprint.pdf)
- **Current status:** Zipf's word frequency law in natural language: A critical review and future directions — Near-Zipfian word frequencies are robust across languages. The review argues that many proposed explanations are untestable or explain too little. Image 1/f scaling is robust on average, though it varies with scene type. [link](https://pmc.ncbi.nlm.nih.gov/articles/PMC4176592/)
- **Order:** Simoncelli & Olshausen review first, then Field 1987, then Piantadosi 2014

## Generalization

<a id="l6"></a>
### L6 · Learnability & inductive bias

*Lens, first tier.* Learnability, inductive bias & capacity

- **Root text** (free): Valiant, L. G. (1984). A Theory of the Learnable. Communications of the ACM 27(11):1134-1142. (Gold 1967 is earlier, but it is about identification in the limit; Valiant founds the PAC learnability used here.) [link](https://homepages.math.uic.edu/~lreyzin/papers/valiant84.pdf)
- **Does the root teach?** Yes. It is short and readable, but it covers only learnability; capacity (VC), bias-variance and No Free Lunch need other sources.
- **Start with:** Peter Bartlett and Sasha Rakhlin, *Generalization I (Simons Institute Foundations of Machine Learning boot camp)* (77 min) [link](https://www.youtube.com/watch?v=Ntl_WNW8yGc)
- **Requires:** [L9 · Search, tractability & bounded rationality](#l9), [L10 · Computation, universality & its limits](#l10)
- **Order:** Bartlett & Rakhlin lecture first, then Valiant 1984 §§1-3, then Wolpert's 'What is important about the No Free Lunch theorems?' (arXiv 2007.10928, backlog).

<a id="l15"></a>
### L15 · Representational geometry

*Lens, first tier.* Representational geometry: similarity, dimensionality, manifolds

- **Root text** (paywalled): Shepard, R. N. (1987). Toward a universal law of generalization for psychological science. Science 237(4820):1317-1323. doi:10.1126/science.3629243. [A UCSD course page hosts a JSTOR copy (cseweb.ucsd.edu/~gary/PAPER-SUGGESTIONS/shepard-science-87.pdf), but it is not an author or publisher copy.] [DOI](https://doi.org/10.1126/science.3629243)
- **Does the root teach?** Yes. Short and lucid derivation of exponential generalization in a psychological space, but it covers similarity only; dimensionality, manifolds and RSA come later.
- **Start with:** Nikolaus Kriegeskorte & Rogier A. Kievit, *Representational geometry: integrating cognition, computation, and the brain (Trends Cogn Sci 2013)* (review article, about 15 pp) [link](https://pmc.ncbi.nlm.nih.gov/articles/PMC3730178/)
- **Order:** Shepard 1987 in full, then the Kriegeskorte & Kievit review, then Tenenbaum et al. 2000 (Isomap) for manifolds.

<a id="l22"></a>
### L22 · Concentration of measure

*Lens.* Concentration of measure & high-dimensional geometry

- **Root text** (free): Lévy, P. (1922). Leçons d'analyse fonctionnelle. Paris: Gauthier-Villars (archive.org, U. Toronto scan). [Concentration on the sphere is in Part III. Cover 1965, 'Geometrical and statistical properties of systems of linear inequalities', is free on the author's Stanford page: isl.stanford.edu/~cover/papers/paper2.pdf, verified.] [link](https://archive.org/details/leonsdanalysef00lvuoft)
- **Does the root teach?** No. A long French monograph in 1920s notation; the concentration result is a small part, and the modern framing comes from Milman.
- **Start with:** Roman Vershynin, *High-Dimensional Probability: An Introduction with Applications in Data Science, 2nd ed. (free pre-publication PDF)* (341 pp (study Chs. 2-3 and 5)) [link](https://www.math.uci.edu/~rvershyn/papers/HDP-book/HDP-2.pdf)
- **Order:** Vershynin Chs. 2-3 and 5, then Cover 1965 §§1-3, then Lévy Part III as history. The backlog Mallat lecture (90 min) is in French and is a good optional companion.

<a id="l31"></a>
### L31 · Symmetry & invariance

*Lens, first tier.*

- **Root text** (free): Klein, F. (1872). Vergleichende Betrachtungen über neuere geometrische Forschungen (Erlangen Program); English translation by M. W. Haskell (1893), 'A comparative review of recent researches in geometry', arXiv:0807.3161. Noether 1918 (English translation by Tavel: arXiv physics/0503066, verified) is the other founding text. [link](https://arxiv.org/abs/0807.3161)
- **Does the root teach?** No. It is a dense 19th-century programme statement that assumes projective geometry and never works an example in modern group language.
- **Start with:** Michael Bronstein, *Lecture 1: A Brief History of Geometric Deep Learning* (unknown [length not verified]) [link](https://www.youtube.com/watch?v=yuw_LwqHsgM)
- **Order:** Bronstein Lecture 1 first, then Klein (Haskell translation) §§1-5, then Noether (Tavel translation) §§1-2; Bronstein et al. 2021 arXiv:2104.13478 (verified) for the modern synthesis.

<a id="p1"></a>
### P1 · Interpolating networks still generalize

*Phenomenon, first tier.* Interpolating networks still generalize; double descent is setup-dependent

- **Root text** (free): Zhang, C., Bengio, S., Hardt, M., Recht, B. & Vinyals, O. (2017). Understanding deep learning requires rethinking generalization. ICLR. arXiv:1611.03530. [link](https://arxiv.org/abs/1611.03530)
- **Does the root teach?** No. It shows the random-label experiments but gives no theory of why interpolation can generalize (benign overfitting, double descent).
- **Start with:** Mikhail Belkin, *Fit without fear: remarkable mathematical phenomena of deep learning through the prism of interpolation (Acta Numerica 2021)* (~80 pp.) [link](https://arxiv.org/abs/2105.14368)
- **Current status:** A U-turn on Double Descent: Rethinking Parameter Counting in Statistical Learning (NeurIPS 2023) — It argues that non-deep double descent comes from switching mechanisms along the x-axis and goes away with effective-parameter counting. Interpolation that still generalizes is robust; double descent is not a universal law. For the theory consensus on benign overfitting, see Bartlett, Montanari & Rakhlin 2021, arXiv:2103.09177 (verified). [link](https://arxiv.org/abs/2310.18988)
- **Requires:** [L6 · Learnability & inductive bias](#l6)
- **Order:** Zhang et al. 2017 first, then Belkin 2021 §§1-4, then Curth et al. 2023 on what is contested.

<a id="p2"></a>
### P2 · Smooth power-law learning curves

*Phenomenon, first tier.* Smooth, roughly power-law learning curves in machines and human practice; form and exponents setup-dependent and beatable

- **Root text** (free): Kaplan, J. et al. (2020). Scaling laws for neural language models. arXiv:2001.08361. [link](https://arxiv.org/abs/2001.08361)
- **Does the root teach?** Yes. Its empirical fits are stated clearly with figures; it needs little background, but its compute-optimal allocation was later revised (Hoffmann 2022).
- **Current status:** Chinchilla Scaling: A replication attempt — It refits Hoffmann et al.'s data and finds their third method's parametric fit inconsistent with the other two: power-law form is robust, exponents and constants are fragile. Heathcote et al. 2000 (Psychonomic Bull. Rev.) covers the human-practice side, where the exponential beats the power law for individuals. [link](https://arxiv.org/abs/2404.10102)
- **Order:** Kaplan 2020 §§1-3, then Hoffmann 2022, then Besiroglu 2024 replication; then Heathcote 2000 and Sorscher 2022 for the human side and for beating the law.

<a id="p3"></a>
### P3 · Adversarial and shortcut vulnerability

*Phenomenon.*

- **Root text** (free): Szegedy, C. et al. (2014). Intriguing properties of neural networks. ICLR. arXiv:1312.6199. Geirhos et al. 2020 'Shortcut learning in deep neural networks' (arXiv:2004.07780, verified) founds the shortcut half. [link](https://arxiv.org/abs/1312.6199)
- **Does the root teach?** No. It is a short discovery paper; the explanation it offers was later superseded and it gives no threat model or robust training.
- **Start with:** Zico Kolter & Aleksander Madry, *Adversarial Robustness - Theory and Practice (NeurIPS 2018 tutorial notes)* (5 chapters with code) [link](https://adversarial-ml-tutorial.org/)
- **Current status:** Adversarial Examples Are Not Bugs, They Are Features (NeurIPS 2019) — Vulnerability is robust and persists (RobustBench, arXiv:2010.09670, verified, tracks the best defenses). Contested: whether it comes from non-robust predictive features or from geometry and high dimension; the Distill 2019 responses debate this. [link](https://arxiv.org/abs/1905.02175)
- **Order:** Szegedy 2014 first, then Kolter-Madry tutorial Ch. 1-4, then Geirhos 2020, then Ilyas 2019.

<a id="p7"></a>
### P7 · Learning to learn

*Phenomenon.* Learning to learn and the human–machine data-efficiency gap

- **Root text** (paywalled): Harlow, H. F. (1949). The formation of learning sets. Psychological Review 56:51-65. doi:10.1037/h0062474. No legitimate free copy found. [DOI](https://doi.org/10.1037/h0062474)
- **Does the root teach?** Yes. Short, clear presidential-address paper with learning-set curves. It needs no background, but it says nothing about the human-machine gap.
- **Start with:** Lake, Ullman, Tenenbaum & Gershman, *Building Machines That Learn and Think Like People (BBS 2017)* (~58 pp. (arXiv v3)) [link](https://arxiv.org/abs/1604.00289)
- **Current status:** Bridging the data gap between children and large language models (Trends in Cognitive Sciences 27:990-992, 2023) — Quantifies the 4-5 orders-of-magnitude gap in language input. Which factors close it (innate bias, grounding, interaction, evaluation) is open. [link](https://osf.io/preprints/psyarxiv/qzbgx)
- **Order:** Harlow 1949 first, then Lake et al. 2017 sections 1-4, then Frank 2023.

<a id="p17"></a>
### P17 · Typicality effects

*Phenomenon.* Typicality effects, even for well-defined categories

- **Root text** (paywalled): Rosch, E. (1975). Cognitive representations of semantic categories. J Exp Psychol: General 104(3):192-233. doi:10.1037/0096-3445.104.3.192. (Rosch founds typicality. The 'even for well-defined categories' half comes from Armstrong, Gleitman & Gleitman 1983, Cognition 13:263-308, doi:10.1016/0010-0277(83)90012-4, also paywalled) [DOI](https://doi.org/10.1037/0096-3445.104.3.192)
- **Does the root teach?** Yes. A clear empirical paper in plain prose with typicality norms and priming experiments that needs no special background. Armstrong et al. is equally readable and carries the conceptual argument.
- **Current status:** Cognition 129(3):615-636 (2013), doi:10.1016/j.cognition.2013.08.015 — Extends Armstrong et al. and finds typicality effects in parity and triangle judgments even when people can state the rule. What is contested is the interpretation (graded representation vs. identification heuristics over a classical core), not the effect itself. [DOI](https://pubmed.ncbi.nlm.nih.gov/24156803/)
- **Order:** Rosch 1975, then Armstrong, Gleitman & Gleitman 1983 (the well-defined-category twist), then Lupyan 2013 for current status

<a id="p28"></a>
### P28 · Low-dimensional structure

*Phenomenon, first tier.* Low-dimensional structure in natural data and neural population activity

- **Root text** (paywalled): Tenenbaum, J.B., de Silva, V. & Langford, J.C. (2000). A global geometric framework for nonlinear dimensionality reduction. Science 290:2319-2323. doi:10.1126/science.290.5500.2319 [DOI](https://doi.org/10.1126/science.290.5500.2319)
- **Does the root teach?** Yes. Short and self-contained Isomap paper, though terse. Pope et al. 2021 (arXiv:2104.08894, verified) covers the natural-image side, Churchland 2012 (PMC3393826) and Gallego 2017 (PMC6122849) the neural side, all free.
- **Start with:** John Cunningham & Byron Yu, *Dimensionality reduction for large-scale neural recordings* (~10 pp (Nat Neurosci 17:1500-1509, 2014)) [link](https://pmc.ncbi.nlm.nih.gov/articles/PMC4433019/)
- **Current status:** Curr Opin Neurobiol 70:113-120 (2021) — Separates intrinsic from embedding dimensionality. Low dimensionality is task-dependent and contested by high-dimensional power-law findings (Stringer et al. 2019). [link](https://arxiv.org/abs/2107.04084)
- **Requires:** [L15 · Representational geometry](#l15)
- **Order:** Tenenbaum 2000, then Pope 2021, then Cunningham & Yu 2014, then Churchland 2012 and Gallego 2017, then Jazayeri & Ostojic 2021

## Learning mechanisms

<a id="l8"></a>
### L8 · Decisions under uncertainty

*Lens, first tier.* Decisions under uncertainty: tests, signal detection, sequential evidence, value, exploration

- **Root text** (free): Neyman, J. and Pearson, E. S. (1933). On the Problem of the Most Efficient Tests of Statistical Hypotheses. Phil. Trans. R. Soc. A 231:289-337. doi:10.1098/rsta.1933.0009 [link](https://royalsocietypublishing.org/doi/10.1098/rsta.1933.0009)
- **Does the root teach?** No. It is long and covers only the testing corner of a broad lens; signal detection, sequential analysis (Wald), Bellman value and exploration each need their own source.
- **Start with:** Michael I. Jordan, *Bayesian or Frequentist, Which Are You? (Part 1 of 2)* (89 min) [link](https://www.youtube.com/watch?v=HUAE26lNDuE)
- **Requires:** [L3 · Bayesian updating & exchangeability](#l3), [L4 · Likelihood & Fisher information](#l4)
- **Order:** Jordan lecture first (decision-theoretic frame), then N-P 1933 §§I-III, then Szepesvari & Wang on MDPs (https://www.youtube.com/watch?v=XkfV0wv8GUQ) and Lattimore 'Bandit Algorithms - 1' (https://www.youtube.com/watch?v=xN11-epRuSU, verified) for value and exploration.

<a id="l12"></a>
### L12 · Credit assignment & error-driven learning

*Lens.*

- **Root text** (free): Widrow, B. and Hoff, M. E. (1960). Adaptive Switching Circuits. IRE WESCON Convention Record 4:96-104. (Author's Stanford page.) Rumelhart, Hinton & Williams 1986 is the backlog ROOT for backprop (https://www.cs.toronto.edu/~hinton/absps/naturebp.pdf, verified). [link](https://isl.stanford.edu/~widrow/papers/c1960adaptiveswitching.pdf)
- **Does the root teach?** Yes. The LMS/delta rule is derived simply, though in circuit terms; it does not reach multilayer or temporal credit assignment.
- **Start with:** Richard S. Sutton and Andrew G. Barto, *Reinforcement Learning: An Introduction (2nd ed.), Ch. 14 'Psychology' (§14.2 Rescorla-Wagner and the TD model), with Ch. 9 for the delta rule* (~35 pp. chapter) [link](http://incompleteideas.net/book/RLbook2020.pdf)
- **Order:** Widrow & Hoff 1960 first, then Sutton & Barto Ch. 14 (links Rescorla-Wagner to TD), then Rumelhart et al. 1986 (4 pp.).

<a id="l13"></a>
### L13 · World models & cognitive maps

*Lens.* World models & cognitive maps: model-based vs model-free

- **Root text** (free): Tolman, E. C. (1948). Cognitive maps in rats and men. Psychological Review 55(4):189-208. doi:10.1037/h0061626. [Chosen over first-listed Craik 1943: Craik founds the idea of an internal model but it is a book, available only as a borrow-only Internet Archive copy (archive.org/details/natureofexplanat0000crai, 1952 reprint). Tolman is the first empirical case for a map versus stimulus-response learning, and it is free.] [link](http://psychclassics.yorku.ca/Tolman/Maps/maps.htm)
- **Does the root teach?** Yes. Clear, short experimental argument for latent learning and maps, but it has no formal model-based vs model-free account; that comes from Sutton 1990 and Daw, Niv & Dayan 2005 (free course copy: sites.socsci.uci.edu/~lpearl/courses/readings/DawEtAl2005.pdf, verified).
- **Start with:** Peter Dayan, *Peter Dayan: Interactions Between Model-Free and Model-Based Reinforcement Learning* (66 min) [link](https://www.youtube.com/watch?v=01z6agTRvOo)
- **Requires:** [L8 · Decisions under uncertainty](#l8), [L12 · Credit assignment & error-driven learning](#l12)
- **Order:** Tolman 1948 in full, then the Dayan lecture, then Daw, Niv & Dayan 2005 for the arbitration model.

<a id="p6"></a>
### P6 · Prediction-error signatures

*Phenomenon.* Prediction-error signatures: extinction ≠ erasure, RPE-like dopamine, blocking (parameter-sensitive; RPE reading contested by ANCCR)

- **Root text** (free): Kamin, L. J. (1969). Predictability, surprise, attention, and conditioning. In B. A. Campbell & R. M. Church (Eds.), Punishment and Aversive Behavior, pp. 279-296. Appleton-Century-Crofts. The volume is on archive.org as a controlled-digital-lending loan, not open access. For the RPE strand, the free root is Schultz, Dayan & Montague 1997, Science 275:1593, on Dayan's Gatsby page: https://www.gatsby.ucl.ac.uk/~dayan/papers/sdm97.pdf (verified). [link](https://archive.org/details/punishmentaversi0000unse)
- **Does the root teach?** No. Experiment-by-experiment chapter on blocking with no formal model. The unifying error-correction account (Rescorla-Wagner, then TD) and the extinction and dopamine strands come from later work.
- **Start with:** Yael Niv, *Reinforcement learning in the brain (J. Math. Psych. 53:139-154, 2009)* (38 pp. preprint) [link](https://www.princeton.edu/~yael/Publications/Niv2009.pdf)
- **Current status:** Explaining dopamine through prediction errors and beyond (Nature Neuroscience 27:1645-1655, 2024) — Concludes that a generalized prediction error covers most findings. Ramps, sensory and motor responses, and causal accounts such as ANCCR (Jeong et al. 2022, free at https://pmc.ncbi.nlm.nih.gov/articles/PMC9910357/) remain contested. [DOI](https://doi.org/10.1038/s41593-024-01705-4)
- **Requires:** [L12 · Credit assignment & error-driven learning](#l12)
- **Order:** Niv 2009 sections 1-4 first, then Kamin 1969, then Schultz-Dayan-Montague 1997, then Gershman et al. 2024 (with Jeong 2022 as the counter-case).

<a id="p8"></a>
### P8 · Innate structure and prepared learning

*Phenomenon, first tier.*

- **Root text** (paywalled): Garcia, J. & Koelling, R. A. (1966). Relation of cue to consequence in avoidance learning. Psychonomic Science 4:123-124. doi:10.3758/BF03342209. Springer page was bot-blocked, so access was not checked [unverified access]. Tinbergen 1951, The Study of Instinct, is on archive.org as a lending copy: https://archive.org/details/studyofinstinct0000ntin_a1t3 (verified). [DOI](https://doi.org/10.3758/BF03342209)
- **Does the root teach?** Yes. Two-page 2x2 design (taste vs audiovisual cue x illness vs shock). It is fully readable, but it does not supply the 'preparedness' framework.
- **Start with:** Martin E. P. Seligman, *On the generality of the laws of learning (Psychological Review 77:406-418, 1970)* (13 pp. (paywalled)) [link](https://doi.org/10.1037/h0029790)
- **Current status:** Experimental evolution of prepared learning (PNAS 111:11750-11755, 2014) — Shows that preparedness evolves as a function of environmental reliability, which turns 'innate constraint' into a testable trade-off. Whether these are specialised modules or parameter settings of general learning is still debated. [link](https://pmc.ncbi.nlm.nih.gov/articles/PMC4136563/)
- **Order:** Garcia & Koelling 1966 first, then Seligman 1970, then Dunlap & Stephens 2014. Tinbergen 1951 chs. 1-2 is optional background on innate releasing mechanisms.

<a id="p9"></a>
### P9 · Goal-directed vs habitual control

*Phenomenon.* Goal-directed vs habitual control; latent learning

- **Root text** (free): Tolman, E. C. (1948). Cognitive maps in rats and men. Psychological Review 55:189-208. Full text at Classics in the History of Psychology (York U.). [link](https://psychclassics.yorku.ca/Tolman/Maps/maps.htm)
- **Does the root teach?** Yes. Plain-prose address that walks through latent learning and place learning. Its weakness is that it gives no devaluation test of goal-directedness; that comes from Adams & Dickinson 1981.
- **Start with:** Ray J. Dolan & Peter Dayan, *Goals and habits in the brain (Neuron 80:312-325, 2013)* (14 pp.) [link](https://pmc.ncbi.nlm.nih.gov/articles/PMC3807793/)
- **Current status:** Shifting the balance between goals and habits: five failures in experimental habit induction (JEP: General 147:1043-1065, 2018) — Overtraining-induced habits are robust in rats but did not replicate in humans across five experiments. The model-based/model-free mapping is also contested. [link](https://pmc.ncbi.nlm.nih.gov/articles/PMC6033090/)
- **Order:** Tolman 1948 first, then Dolan & Dayan 2013, then de Wit et al. 2018.

<a id="p20"></a>
### P20 · Synaptic plasticity

*Phenomenon.* Synaptic plasticity, Hebbian and homeostatic (STDP's in-vivo role open)

- **Root text** (free): Bliss, T.V.P. & Lømo, T. (1973). Long-lasting potentiation of synaptic transmission in the dentate area of the anaesthetized rabbit following stimulation of the perforant path. J Physiol 232:331-356 [link](https://pmc.ncbi.nlm.nih.gov/articles/PMC1350458/)
- **Does the root teach?** No. Dense electrophysiology methods that show LTP exists but cover neither spike timing nor homeostatic plasticity. Bi & Poo 1998 is free at https://pmc.ncbi.nlm.nih.gov/articles/PMC6793365/ (verified).
- **Start with:** L.F. Abbott & S.B. Nelson, *Synaptic plasticity: taming the beast* (6 pp review (Nat Neurosci 3 Suppl:1178-1183, 2000)) [DOI](https://doi.org/10.1038/81453)
- **Current status:** Neuron 75(4):556-571 (2012) — Shows that STDP depends strongly on firing rate, dendritic location and neuromodulation, and that in-vivo evidence for STDP as the operative learning rule is limited. [link](https://pmc.ncbi.nlm.nih.gov/articles/PMC3431193/)
- **Order:** Abbott & Nelson 2000, then Bliss & Lømo 1973 (results and discussion), then Bi & Poo 1998, then Feldman 2012

## Memory and representation

<a id="l14"></a>
### L14 · Superposition & content-addressable memory

*Lens.*

- **Root text** (free): Hopfield, J. J. (1982). Neural networks and physical systems with emergent collective computational abilities. PNAS 79(8):2554-2558. doi:10.1073/pnas.79.8.2554. [Hebb 1949 is a book and a precursor; Hopfield 1982 founds content-addressable memory as energy minima.] [link](https://pmc.ncbi.nlm.nih.gov/articles/PMC346238/)
- **Does the root teach?** Yes. Five readable pages with the energy function, the Hebbian outer-product storage of superposed memories, and a capacity of about 0.15N, but the capacity argument is only heuristic.
- **Start with:** Dmitry Krotov, Benjamin Hoover, Parikshit Ram, *Modern Methods in Associative Memory (tutorial)* (47 min) [link](https://slideslive.com/39043831)
- **Order:** Hopfield 1982 in full, then the Krotov et al. tutorial for dense associative memory, capacity and the link to attention.

<a id="p4"></a>
### P4 · Catastrophic interference

*Phenomenon.*

- **Root text** (paywalled): McCloskey, M. & Cohen, N. J. (1989). Catastrophic interference in connectionist networks: The sequential learning problem. Psychology of Learning and Motivation 24:109-165. doi:10.1016/S0079-7421(08)60536-8. Ratcliff 1990 Psych. Rev. 97:285 (doi:10.1037/0033-295X.97.2.285) is also paywalled. [DOI](https://doi.org/10.1016/S0079-7421(08)60536-8)
- **Does the root teach?** Yes. Its simulations are clear and the networks small, though it is long (57 pp.) and uses 1980s backprop.
- **Start with:** Robert M. French, *Catastrophic forgetting in connectionist networks (Trends in Cognitive Sciences 3:128-135, 1999)* (8 pp.) [link](https://lead.ube.fr/wp-content/uploads/2023/09/000282-catastrophic-forgetting-in-connectionist-networks.pdf)
- **Current status:** Three types of incremental learning (Nature Machine Intelligence 4:1185-1197, 2022, open access) — It shows how severe forgetting is depends on the scenario (task-, domain- or class-incremental): regularization fixes like EWC fail in class-incremental settings, while replay helps. [link](https://www.nature.com/articles/s42256-022-00568-3)
- **Requires:** [L12 · Credit assignment & error-driven learning](#l12)
- **Order:** French 1999 first, then McCloskey & Cohen 1989 §§1-3 (via library), then van de Ven et al. 2022.

<a id="p12"></a>
### P12 · Working-memory limits

*Phenomenon.* Working memory holds ~3–5 chunks; slots vs resources disputed

- **Root text** (free): Cowan, N. (2001). The magical number 4 in short-term memory: a reconsideration of mental storage capacity. BBS 24:87-185. Free on the author's Missouri lab site. Listed first-root Miller 1956 (free: https://psychclassics.yorku.ca/Miller/, verified) argued 7+/-2 and introduced chunking. The ~3-5 figure comes from Cowan. [link](https://memory.psych.missouri.edu/assets/doc/articles/2001/cowan-bbs-2001.pdf)
- **Does the root teach?** No. The 99-page target article plus commentaries is an evidence compendium, not a first exposition.
- **Start with:** Nelson Cowan, *The magical mystery four: how is working memory capacity limited, and why? (Current Directions in Psych. Sci. 19:51-57, 2010)* (7 pp.) [link](https://pmc.ncbi.nlm.nih.gov/articles/PMC2864034/)
- **Current status:** Changing concepts of working memory (Nature Neuroscience 17:347-356, 2014) — Argues for continuous-resource and variable-precision models over fixed slots (Zhang & Luck 2008). Slots vs resources is still disputed; the ~4 limit itself is robust but measure-dependent. [link](https://pmc.ncbi.nlm.nih.gov/articles/PMC4159388/)
- **Order:** Miller 1956 (short) first, then Cowan 2010, then Cowan 2001 sections 1-3 only, then Ma, Husain & Bays 2014.

<a id="p13"></a>
### P13 · Forgetting, spacing and testing

*Phenomenon.* Retention follows environmental recurrence: forgetting, spacing, testing

- **Root text** (free): Ebbinghaus, H. (1885/1913). Memory: A Contribution to Experimental Psychology (trans. Ruger & Bussenius). Full text at Classics in the History of Psychology. Ch. 7 is the forgetting curve: https://psychclassics.yorku.ca/Ebbinghaus/memory7.htm (verified). [link](https://psychclassics.yorku.ca/Ebbinghaus/index.htm)
- **Does the root teach?** Yes. Clear, self-experimental prose with tables. It gives the curve and the spacing observation but not the environmental-recurrence explanation (Anderson & Schooler 1991, doi:10.1111/j.1467-9280.1991.tb00174.x, paywalled).
- **Start with:** John R. Anderson & Lael J. Schooler, *Reflections of the environment in memory (Psychological Science 2:396-408, 1991)* (13 pp. (paywalled; ACT-R site copy unreachable)) [link](https://doi.org/10.1111/j.1467-9280.1991.tb00174.x)
- **Current status:** Improving students' learning with effective learning techniques (Psych. Sci. in the Public Interest 14:4-58, 2013) — Rates practice testing and distributed practice as high-utility and robust across ages, materials and delays. Optimal lag (Cepeda et al. 2006/2008) and the transfer of benefits are less settled. Murre & Dros 2015 replicated Ebbinghaus's curve: https://pmc.ncbi.nlm.nih.gov/articles/PMC4492928/. [link](https://www.psychologicalscience.org/publications/journals/pspi/learning-techniques.html)
- **Order:** Ebbinghaus chs. 1 and 7 first, then Anderson & Schooler 1991, then Dunlosky et al. 2013 (testing and spacing sections).

<a id="p19"></a>
### P19 · Receptive fields matched to natural statistics

*Phenomenon, first tier.* Hierarchical receptive fields matched to natural statistics

- **Root text** (free): Hubel, D.H. & Wiesel, T.N. (1962). Receptive fields, binocular interaction and functional architecture in the cat's visual cortex. J Physiol 160:106-154 [link](https://pmc.ncbi.nlm.nih.gov/articles/PMC1359523/)
- **Does the root teach?** No. About 50 pages of single-unit physiology that establish the simple/complex hierarchy but say nothing about natural statistics. Olshausen & Field 1996 (Nature 381:607, doi:10.1038/381607a0) is paywalled, and the author-page link is a dead FTP link.
- **Start with:** Bruno Olshausen, *From Natural Scene Statistics to Models of Neural Coding & Representation, Pt. 1 (IPAM)* (61 min) [link](https://www.youtube.com/watch?v=6O-EE2JC-yA)
- **Current status:** Neural Computation 17(8):1665-1699 (2005) — Estimates how much of V1 response variance standard models explain (well under half) and lists the open problems: biased sampling, nonlinearities, context. [link](https://redwood.berkeley.edu/wp-content/uploads/2005/08/olshausen2005close.pdf)
- **Order:** Olshausen lecture first, then Hubel & Wiesel 1962 (Part I and the hierarchy discussion), then Olshausen & Field 1996, then the 2005 status review

<a id="p21"></a>
### P21 · Place, grid and attractor codes

*Phenomenon.*

- **Root text** (paywalled): O'Keefe, J. & Dostrovsky, J. (1971). The hippocampus as a spatial map. Preliminary evidence from unit activity in the freely-moving rat. Brain Res 34:171-175. doi:10.1016/0006-8993(71)90358-1 [DOI](https://doi.org/10.1016/0006-8993(71)90358-1)
- **Does the root teach?** No. A 5-page preliminary report on place units only. It covers neither grid cells (Hafting 2005, doi:10.1038/nature03721, paywalled) nor attractor theory (Kim et al. 2017, doi:10.1126/science.aal4835, paywalled).
- **Start with:** Mikail Khona & Ila Fiete, *Attractor and integrator networks in the brain* (long review (~40 pp)) [link](https://arxiv.org/abs/2112.03978)
- **Current status:** Nature 602:123-128 (2022); also PMC8810387 — The strongest test so far of the continuous-attractor prediction (a torus that persists in sleep). What remains contested is how the attractor is wired, how it is learned, and whether place-cell maps are attractors. [link](https://www.nature.com/articles/s41586-021-04268-7)
- **Requires:** [L21 · Dynamical systems & self-organization](#l21)
- **Order:** Khona & Fiete review (place, grid and ring-attractor sections), then O'Keefe & Dostrovsky 1971, Hafting 2005, Kim 2017, then Gardner 2022

<a id="p22"></a>
### P22 · Consolidation and replay

*Phenomenon.*

- **Root text** (paywalled): Wilson, M.A. & McNaughton, B.L. (1994). Reactivation of hippocampal ensemble memories during sleep. Science 265:676-679. doi:10.1126/science.8036517 [DOI](https://doi.org/10.1126/science.8036517)
- **Does the root teach?** No. A 4-page report of replay. It contains no consolidation theory. Squire & Alvarez 1995 (Curr Opin Neurobiol) is also paywalled.
- **Start with:** James McClelland, Bruce McNaughton & Randall O'Reilly, *Why there are complementary learning systems in the hippocampus and neocortex* (~40 pp (Psychol Rev 102:419-457, 1995)) [link](https://stanford.edu/~jlmcc/papers/McCMcNaughtonOReilly95.pdf)
- **Current status:** Nat Rev Neurosci 19:744-757 (2018) — Causal disruption studies support a role for ripple replay. Still contested: replay for consolidation vs. planning, and standard systems consolidation vs. multiple-trace and transformation accounts. [link](https://pmc.ncbi.nlm.nih.gov/articles/PMC6794196/)
- **Order:** McClelland et al. 1995 (§§1-3), then Wilson & McNaughton 1994, then Squire & Alvarez 1995, then Joo & Frank 2018

<a id="p23"></a>
### P23 · Neuropsychological dissociations

*Phenomenon.* Neuropsychological dissociations: memory systems, blindsight, perception vs action, language vs thought, confabulation

- **Root text** (free): Scoville, W.B. & Milner, B. (1957). Loss of recent memory after bilateral hippocampal lesions. J Neurol Neurosurg Psychiatry 20:11-21 [link](https://pmc.ncbi.nlm.nih.gov/articles/PMC497229/)
- **Does the root teach?** Yes. Readable clinical case series for the memory strand. The other strands (blindsight, DF, aphasia, confabulation) each need their own root.
- **Start with:** Larry Squire & John Wixted, *The cognitive neuroscience of human memory since H.M.* (~25 pp (Annu Rev Neurosci 34:259-288, 2011)) [link](https://pmc.ncbi.nlm.nih.gov/articles/PMC3192650/)
- **Current status:** Ann NY Acad Sci 1369:132-153 (2016) — Covers only the language-vs-thought strand, where the dissociation is currently most contested. No single review covers all five dissociations. [link](https://pmc.ncbi.nlm.nih.gov/articles/PMC4874898/)
- **Order:** Scoville & Milner 1957, then Squire & Wixted 2011, then Fedorenko & Varley 2016; take the other strand roots one at a time

## The physics of learning

<a id="l16"></a>
### L16 · Statistical mechanics & typical-case analysis

*Lens, first tier.* Statistical mechanics: ensembles & typical-case analysis

- **Root text** (free): Boltzmann, L. (1877). Über die Beziehung zwischen dem zweiten Hauptsatze der mechanischen Wärmetheorie und der Wahrscheinlichkeitsrechnung... Wien. Ber. 76:373-435. English translation: Sharp & Matschinsky, Entropy 17(4):1971-2009 (2015), CC-BY. doi:10.3390/e17041971. [Gibbs 1902 is public domain on archive.org. Typical-case analysis is founded separately by Gardner 1988.] [link](https://doi.org/10.3390/e17041971)
- **Does the root teach?** No. Long 1877 combinatorial derivation with dated notation; it founds W-counting but says nothing about the ensemble or replica analysis of learning.
- **Start with:** Bruno Loureiro, *Four lectures on Statistical Physics of Learning (Princeton ML Theory Summer School 2024)* (74 pp) [link](https://brloureiro.github.io/assets/pdf/NotesPrinceton_BL.pdf)
- **Order:** Loureiro Lecture 1 (stat-phys 101), then Boltzmann 1877 §§I-II in translation, then Loureiro Lectures 2-4 (Gardner, teacher-student, replicas).

<a id="l17"></a>
### L17 · Order parameters & phase transitions

*Lens, first tier.* Order parameters, broken symmetry & phase transitions

- **Root text** (free): Landau, L. D. (1937). On the theory of phase transitions. Zh. Eksp. Teor. Fiz. 7:19-32 / Phys. Z. Sowjetunion 11:26, 545. English in Collected Papers of L. D. Landau (ed. ter Haar, 1965), pp. 193-216. [Anderson 1972 'More is different' is the generalising essay.] [link](https://archive.org/details/collectedpaperso0000lddt)
- **Does the root teach?** No. Terse and group-theoretic, and it assumes 1930s crystallography; the only legitimate free route is a borrow-only Internet Archive lending copy (otherwise paywalled).
- **Start with:** David Tong (Cambridge DAMTP), *Statistical Physics lecture notes, Chapter 5: Phase Transitions (Ising, mean field, Landau theory, broken symmetry)* (51 pp) [link](https://www.damtp.cam.ac.uk/user/tong/statphys/five.pdf)
- **Requires:** [L16 · Statistical mechanics & typical-case analysis](#l16), [L31 · Symmetry & invariance](#l31)
- **Order:** Tong Ch. 5 (§§5.2-5.4), then Landau 1937 §§1-3, then Anderson 1972.

<a id="l18"></a>
### L18 · Scaling & renormalization

*Lens, first tier.* Scaling, coarse-graining & renormalization

- **Root text** (free): Kadanoff, L. P. (1966). Scaling laws for Ising models near Tc. Physics Physique Fizika 2:263-272. doi:10.1103/PhysicsPhysiqueFizika.2.263. [Chosen over first-listed Widom 1965 (J. Chem. Phys. 43:3898, paywalled), which founds the scaling hypothesis but not coarse-graining; Kadanoff's block-spin argument founds coarse-graining. Wilson 1971 is paywalled (PRB).] [link](https://journals.aps.org/ppf/abstract/10.1103/PhysicsPhysiqueFizika.2.263)
- **Does the root teach?** Yes. Short, physical block-spin argument that derives the scaling laws; readable with basic Ising background.
- **Start with:** Leo P. Kadanoff, *Relating Theories via Renormalization (arXiv:1102.3705)* (57 pp) [link](https://arxiv.org/abs/1102.3705)
- **Requires:** [L16 · Statistical mechanics & typical-case analysis](#l16), [L17 · Order parameters & phase transitions](#l17)
- **Order:** Kadanoff 1966 in full, then Kadanoff 2011 §§ on scaling, universality and Wilson's RG; optionally Wilson's 1982 Nobel lecture (nobelprize.org/uploads/2018/06/wilson-lecture-2.pdf, verified).

<a id="l19"></a>
### L19 · Rugged landscapes

*Lens, first tier.* Disorder & rugged landscapes: energy, loss, fitness

- **Root text** (free): Wright, S. (1932). The roles of mutation, inbreeding, crossbreeding and selection in evolution. Proc. Sixth Int. Congress of Genetics 1:356-366 (ESP facsimile). [link](http://www.esp.org/books/6th-congress/facsimile/contents/6th-cong-p356-wright.pdf)
- **Does the root teach?** Yes. Eleven non-mathematical pages that introduce the rugged fitness landscape cleanly, but they contain none of the disorder physics (SK, Parisi) the item also covers.
- **Start with:** Giulio Biroli, *The many facets of the rough high-dimensional landscape problem (KITP Blackboard Talk)* (65 min) [link](https://www.youtube.com/watch?v=vYwC1UNuRgU)
- **Requires:** [L16 · Statistical mechanics & typical-case analysis](#l16), [L17 · Order parameters & phase transitions](#l17)
- **Order:** Wright 1932 in full, then the Biroli blackboard talk, then the Parisi lecture (backlog) for replica symmetry breaking.

<a id="l20"></a>
### L20 · Noise-driven dynamics

*Lens, first tier.* Noise-driven dynamics: diffusion, barrier escape, fluctuation–dissipation

- **Root text** (free): Langevin, P. (1908). Sur la théorie du mouvement brownien. C. R. Acad. Sci. Paris 146:530-533 (Gallica ark:/12148/bpt6k3100t). English translation: Lemons & Gythiel, Am. J. Phys. 65:1079 (1997), doi:10.1119/1.18725, paywalled. [link](https://gallica.bnf.fr/ark:/12148/bpt6k3100t)
- **Does the root teach?** Yes. Three pages in French; the translation is very readable and derives diffusion from a stochastic force. It does not cover barrier escape or fluctuation-dissipation. [Gallica blocks automated fetches (403), so the ark ID comes from a BnF guide.]
- **Start with:** Christopher Jarzynski, *Equalities and Inequalities: Irreversibility and the Second Law of Thermodynamics at the Nanoscale (Annu. Rev. Condens. Matter Phys. 2:329, 2011)* (23 pp) [link](https://terpconnect.umd.edu/~cjarzyns/CHEM-CHPH-PHYS_703_Spr_20/resources/Jarzynski_AnnuRevCondMattPhys_2_329_2011.pdf)
- **Requires:** [L16 · Statistical mechanics & typical-case analysis](#l16)
- **Order:** Langevin 1908 (translation), then the Jarzynski 2011 review. Kramers barrier escape needs Hänggi, Talkner & Borkovec 1990 (RMP, paywalled).

<a id="l21"></a>
### L21 · Dynamical systems & self-organization

*Lens, first tier.* Dynamical systems, chaos & self-organization

- **Root text** (free): Poincaré, H. (1890). Sur le problème des trois corps et les équations de la dynamique. Acta Mathematica 13:1-270. [Hosted in parts on the Tsinghua YMSC Acta archive; this link is Part I, Ch. I (§1). Turing 1952 and Lorenz 1963 are separate roots.] [link](https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/4918-11511_2006_Article_BF02392507.pdf)
- **Does the root teach?** No. A 270-page French memoir in 19th-century notation; it founds Poincaré sections and homoclinic chaos, but only experts can study it.
- **Start with:** Steven Strogatz (Cornell), *MAE5790-17 Chaos in the Lorenz equations* (77 min) [link](https://www.youtube.com/watch?v=gscKcPAm-H0)
- **Order:** Strogatz lecture first, then Lorenz 1963, then Poincaré 1890 only as a reference for sections and recurrence. Self-organization (Turing 1952) still needs its own teaching source.

<a id="l30"></a>
### L30 · Thermodynamics of computation

*Lens, first tier.*

- **Root text** (free): Landauer, R. (1961). Irreversibility and heat generation in the computing process. IBM J. Res. Dev. 5(3):183-191. doi:10.1147/rd.53.0183. Szilard 1929 is listed first but is a precursor about measurement and entropy; Landauer founds the erasure bound. [link](https://sites.pitt.edu/~jdnorton/lectures/Rotman_Summer_School_2013/thermo_computing_docs/Landauer_1961.pdf)
- **Does the root teach?** No. It is readable, but the argument is heuristic and comes before the Bennett resolution of Maxwell's demon and modern stochastic thermodynamics, so it can mislead without them.
- **Start with:** Takahiro Sagawa, *[ICTP KIAS School] Sagawa 2 - Thermodynamics of information I* (64 min) [link](https://www.youtube.com/watch?v=YkkbIt8s1no)
- **Requires:** [L1 · Information & coding limits](#l1), [L10 · Computation, universality & its limits](#l10), [L16 · Statistical mechanics & typical-case analysis](#l16)
- **Order:** Sagawa lecture first, then Landauer 1961, then Bennett 2003 'Notes on Landauer's principle' (arXiv physics/0210005, verified) as Bennett's own summary of his 1982 review.

<a id="p5"></a>
### P5 · Sharp thresholds and computational gaps

*Phenomenon.* Sharp thresholds and computational gaps in random problems

- **Root text** (free): Kirkpatrick, S. & Selman, B. (1994). Critical behavior in the satisfiability of random Boolean expressions. Science 264:1297-1301. doi:10.1126/science.264.5163.1297. Free copy is the preprint on Selman's Cornell page (10 pp.). For the computational-gap half, see Mezard & Zecchina 2002, arXiv cond-mat/0207194. For the rigorous threshold, see Ding, Sly & Sun, arXiv 1411.0650. [link](https://www.cs.cornell.edu/selman/papers/pdf/94.science.crit.pdf)
- **Does the root teach?** No. Short empirical paper that reports the threshold and finite-size scaling. It does not explain the clustering or replica-symmetry-breaking picture behind the computational gaps.
- **Start with:** Lenka Zdeborová, *Phase transitions in computational problems, Day 1 (Simons Lectures, MIT, April 2024)* (69 min) [link](https://www.youtube.com/watch?v=94XXGGNDeCc)
- **Current status:** The Overlap Gap Property: a geometric barrier to optimizing over random structures (PNAS 2021) — Sharp thresholds are now theorems (Friedgut; Ding-Sly-Sun for large k). Algorithmic hardness is proved only for restricted algorithm classes (OGP, low-degree, SOS). Gaps for all polynomial algorithms remain conjectural. [link](https://arxiv.org/abs/2109.14409)
- **Requires:** [L9 · Search, tractability & bounded rationality](#l9), [L17 · Order parameters & phase transitions](#l17), [L19 · Rugged landscapes](#l19)
- **Order:** Zdeborová lecture first, then Kirkpatrick & Selman (all), then Mezard-Zecchina 2002 sections 1-3, then Gamarnik for status.

<a id="p26"></a>
### P26 · Degeneracy and sloppiness

*Phenomenon.* Degeneracy and sloppiness: many parameter sets, same function

- **Root text** (paywalled): Prinz, A.A., Bucher, D. & Marder, E. (2004). Similar network activity from disparate circuit parameters. Nat Neurosci 7:1345-1352. doi:10.1038/nn1352 [DOI](https://doi.org/10.1038/nn1352)
- **Does the root teach?** Yes. Short and clear, but it assumes background on the stomatogastric ganglion and conductance models and does not cover sloppiness. Gutenkunst et al. 2007 is free at https://pmc.ncbi.nlm.nih.gov/articles/PMC2000971/ (verified).
- **Start with:** Jim Sethna, *Sloppy Models, Differential Geometry, and Why Science Works (SFI)* (71 min) [link](https://www.youtube.com/watch?v=QfaWnTToDWY)
- **Current status:** Nat Neurosci 14:133-138 (2011) — Experimental support for animal-to-animal conductance variability with conserved output. How general this is beyond small circuits remains open. For the sloppiness side see Transtrum et al. 2015, arXiv:1501.07668 (verified). [link](https://pmc.ncbi.nlm.nih.gov/articles/PMC3686573/)
- **Order:** Sethna lecture, then Prinz et al. 2004, then Gutenkunst et al. 2007, then Edelman & Gally 2001, then Marder & Taylor 2011

<a id="p27"></a>
### P27 · Balanced, irregular spiking

*Phenomenon.* Irregular spiking with balanced excitation and inhibition

- **Root text** (free): Softky, W.R. & Koch, C. (1993). The highly irregular firing of cortical cells is inconsistent with temporal integration of random EPSPs. J Neurosci 13(1):334-350. (This poses the puzzle. The balanced-state resolution is van Vreeswijk & Sompolinsky 1996, Science 274:1724, doi:10.1126/science.274.5293.1724, paywalled) [link](https://pmc.ncbi.nlm.nih.gov/articles/PMC6576320/)
- **Does the root teach?** Yes. Clear statement of the CV puzzle with simple models. Shadlen & Newsome 1998 (free, https://pmc.ncbi.nlm.nih.gov/articles/PMC6793166/, verified) gives the balance answer in readable form.
- **Current status:** Neuron 109:3373-3391 (2021) — Argues that cortex is loosely balanced and inhibition-stabilized rather than in the tight balanced state of van Vreeswijk & Sompolinsky. What remains contested is the degree of balance. [link](https://arxiv.org/abs/1908.10101)
- **Order:** Softky & Koch 1993, then Shadlen & Newsome 1998, then van Vreeswijk & Sompolinsky 1996, then Ahmadian & Miller 2021

<a id="p29"></a>
### P29 · Processing near physical limits

*Phenomenon.* Processing near physical limits: photon and molecule counting, energy per bit, energy paid for accuracy

- **Root text** (free): Hecht, Shlaer & Pirenne 1942, Energy, quanta, and vision, J Gen Physiol 25:819-840, doi:10.1085/jgp.25.6.819 [link](https://pmc.ncbi.nlm.nih.gov/articles/PMC2142545/)
- **Does the root teach?** No. The paper teaches the photon-counting argument well, but it covers only one of the item's four strands. Molecule counting (Berg & Purcell), kinetic proofreading (Hopfield) and the energy cost per bit (Attwell & Laughlin) need a single text that ties them together.
- **Start with:** William Bialek, *Thinking about the brain (Les Houches lectures, 2001)* (long lecture notes, roughly 100 pages [page count unverified]) [link](https://arxiv.org/abs/physics/0205030)
- **Current status:** Direct detection of a single photon by humans — The rod's single-photon response is robust. Whether a person can consciously report a single photon is contested: this study finds a small above-chance effect and has not been widely replicated. It does not address the energy-per-bit strand. [link](https://www.nature.com/articles/ncomms12172)
- **Requires:** [L16 · Statistical mechanics & typical-case analysis](#l16)
- **Order:** Bialek lectures (photon counting, then the Berg-Purcell limit) first, then HSP 1942 in full, then Tinsley 2016

## Agency and the closed loop

<a id="l9"></a>
### L9 · Search, tractability & bounded rationality

*Lens, first tier.*

- **Root text** (paywalled): Simon, H. A. (1955). A Behavioral Model of Rational Choice. Quarterly Journal of Economics 69(1):99-118. doi:10.2307/1884852 [DOI](https://doi.org/10.2307/1884852)
- **Does the root teach?** Yes. Clear prose with light formalism; it covers bounded rationality but not complexity or heuristic search.
- **Start with:** Avi Wigderson, *The P vs. NP Problem* (74 min) [link](https://www.youtube.com/watch?v=ph_PIF-Ry8A)
- **Requires:** [L10 · Computation, universality & its limits](#l10)
- **Order:** Simon 1955 first, then Wigderson lecture, then Newell & Simon 1976 'Computer Science as Empirical Inquiry' (CACM, doi:10.1145/360018.360022) [unverified].

<a id="l24"></a>
### L24 · Strategic interaction & signalling

*Lens.*

- **Root text** (free): von Neumann, J. (1928). Zur Theorie der Gesellschaftsspiele. Mathematische Annalen 100:295-320. doi:10.1007/BF01448847 (GDZ digitization; EuDML 159291). [Nash 1950 is free at PMC1063129, verified.] [link](http://gdz.sub.uni-goettingen.de/dms/resolveppn/?PPN=GDZPPN002272717)
- **Does the root teach?** No. A German minimax proof with 1920s topology; no English translation is freely available.
- **Start with:** Roger B. Myerson, *Nash Equilibrium and the History of Economic Theory (J. Econ. Lit. 1999)* (32 pp) [link](https://home.uchicago.edu/~rmyerson/research/jelnash.pdf)
- **Order:** Myerson 1999, then Nash 1950 (one page), then von Neumann 1928 §1 for minimax. Signalling (Lewis 1969, Maynard Smith & Price 1973) still needs its own teaching source.

<a id="l32"></a>
### L32 · Feedback & regulation

*Lens.*

- **Root text** (free): Rosenblueth, A., Wiener, N. & Bigelow, J. (1943). Behavior, purpose and teleology. Philosophy of Science 10(1):18-24. doi:10.1086/286788 (course-hosted copy). [link](https://home.csulb.edu/~cwallis/382/readings/482/wiener.behavior.purpose.teleology.1943.pdf)
- **Does the root teach?** No. It is a 7-page conceptual taxonomy of behavior with no mathematics of feedback, stability or regulation.
- **Start with:** W. Ross Ashby, *An Introduction to Cybernetics (1956), Parts I-III* (156 pp. (exercises included)) [link](http://pespmc1.vub.ac.be/books/IntroCyb.pdf)
- **Requires:** [L1 · Information & coding limits](#l1)
- **Order:** Rosenblueth/Wiener/Bigelow 1943 first (the frame), then Ashby 1956 Ch. 1-4 and 10-11 (requisite variety, regulation), then Conant & Ashby 1970 (free: http://pespmc1.vub.ac.be/books/Conant_Ashby.pdf, verified).

## Language and symbols

<a id="l11"></a>
### L11 · Formal languages & the grammar hierarchy

*Lens.*

- **Root text** (free): Chomsky, N. (1956). Three Models for the Description of Language. IRE Trans. Information Theory 2(3):113-124. doi:10.1109/TIT.1956.1056813 (free copy on chomsky.info; the IEEE version is paywalled) [link](https://chomsky.info/wp-content/uploads/195609-.pdf)
- **Does the root teach?** Yes. Short and readable: finite-state, phrase-structure and transformational models argued from examples.
- **Start with:** Gerhard Jäger and James Rogers, *Formal language theory: refining the Chomsky hierarchy (Phil. Trans. R. Soc. B 367:1956-1970, open access)* (15 pp. review) [link](https://pmc.ncbi.nlm.nih.gov/articles/PMC3367686/)
- **Requires:** [L10 · Computation, universality & its limits](#l10)
- **Order:** Chomsky 1956 first, then Jäger & Rogers (adds the subregular and mildly context-sensitive classes and cognitive tests).

<a id="l28"></a>
### L28 · Compositionality

*Lens.*

- **Root text** (paywalled): Montague, R. (1970). Universal grammar. Theoria 36(3):373-398. doi:10.1111/j.1755-2567.1970.tb00434.x. Fodor & Pylyshyn 1988 (Cognition 28:3-71) is free at https://ruccs.rutgers.edu/images/personal-zenon-pylyshyn/proseminars/Proseminar13/ConnectionistArchitecture.pdf (verified). [DOI](https://doi.org/10.1111/j.1755-2567.1970.tb00434.x)
- **Does the root teach?** No. It is terse intensional logic and model theory with no motivating exposition, and it assumes logic background.
- **Start with:** Zoltán Gendler Szabó, *Compositionality (Stanford Encyclopedia of Philosophy)* (long entry (~1.5 h)) [link](https://plato.stanford.edu/entries/compositionality/)
- **Order:** SEP Compositionality first, then Fodor & Pylyshyn 1988 §§1-3 (systematicity argument); Montague 1970 only for the homomorphism definition.

<a id="l29"></a>
### L29 · Distributional meaning

*Lens.*

- **Root text** (paywalled): Harris, Z. S. (1954). Distributional structure. Word 10(2-3):146-162. doi:10.1080/00437956.1954.11659520 (publisher copy paywalled; an unofficial scan exists at gwern.net, not used). [DOI](https://doi.org/10.1080/00437956.1954.11659520)
- **Does the root teach?** Yes. It is a short, readable argument, but it is structuralist linguistics with no vectors or computation.
- **Start with:** Dan Jurafsky & James H. Martin, *Speech and Language Processing (3rd ed. draft), Ch. 5 'Embeddings'* (27 pp.) [link](https://web.stanford.edu/~jurafsky/slp3/5.pdf)
- **Order:** Harris 1954 first (the hypothesis), then J&M Ch. 5 (from co-occurrence to PPMI to word2vec).

<a id="p31"></a>
### P31 · Productive, systematic generalization

*Phenomenon, first tier.* Productive, systematic generalization and structure dependence

- **Root text** (free): Berko 1958, The child's learning of English morphology, Word 14:150-177, doi:10.1080/00437956.1958.11659661 [link](https://researchgate.net/profile/Jean-Berko-Gleason/publication/243750735_The_Child's_Learning_of_English_Morphology/links/553ddc310cf29b5ee4bce4de/The-Childs-Learning-of-English-Morphology.pdf)
- **Does the root teach?** Yes. A plain, self-contained account of the wug test. It covers morphological productivity only: structure dependence comes from Crain & Nakayama 1987 and systematicity from Fodor & Pylyshyn 1988. [The author's ResearchGate copy blocks automated fetches, so it is unverified. The publisher DOI is confirmed and paywalled.]
- **Current status:** Human-like systematic generalization through a meta-learning neural network — In its instruction-learning experiments, people generalize systematically but not perfectly and show predictable error biases. The paper argues that neural networks can match this after meta-learning, which reopens Fodor & Pylyshyn's argument. [link](https://www.nature.com/articles/s41586-023-06668-3)
- **Order:** Berko 1958 first, then Fodor & Pylyshyn 1988 section 3, then Lake & Baroni 2023

<a id="p32"></a>
### P32 · Learners regularize and create structure

*Phenomenon.* Learners regularize input and create structure

- **Root text** (free): Senghas, Kita & Ozyurek 2004, Children creating core properties of language: evidence from an emerging sign language in Nicaragua, Science 305:1779-1782, doi:10.1126/science.1100199 [link](https://wrap.warwick.ac.uk/66237/20/WRAP_Senghas_Ms.pdf)
- **Does the root teach?** Yes. A short accepted manuscript (17 pp) that is easy to follow. Note that the controlled demonstration of regularization is Hudson Kam & Newport 2005, so that paper arguably founds the learner-regularizes claim, with Senghas as the field case.
- **Current status:** The cognitive roots of regularization in language — Regularization replicates in the lab. The authors separate a domain-general, load-driven source from a language-specific one. How strong it is depends on age, load and task. [link](https://arxiv.org/abs/1703.03442)
- **Order:** Senghas 2004 first, then Hudson Kam & Newport 2005, then Ferdinand et al. 2019

<a id="p33"></a>
### P33 · Predictability drives comprehension

*Phenomenon.* Predictability drives comprehension cost (log form contested; garden paths)

- **Root text** (paywalled): Kutas, M. & Hillyard, S. A. (1984). Brain potentials during reading reflect word expectancy and semantic association. Nature 307:161-163. doi:10.1038/307161a0 [DOI](https://doi.org/10.1038/307161a0)
- **Does the root teach?** No. A 3-page report on the N400 for anomalous words. It does not test predictability: the link to cloze probability is Kutas & Hillyard 1984, Nature 307:161, doi:10.1038/307161a0 (also paywalled), which is the better root. No free copy of either was found.
- **Start with:** Marta Kutas & Kara Federmeier, *Thirty years and counting: Finding meaning in the N400 component of the ERP (Annu Rev Psychol 2011)* (review, about 30 pp) [link](https://pmc.ncbi.nlm.nih.gov/articles/PMC4052444/)
- **Current status:** Large-scale evidence for logarithmic effects of word predictability on reading time — That predictability affects processing cost is robust. Whether the relation is logarithmic is contested: this reanalysis of six datasets supports a log effect, against the linear result of Brothers & Kuperberg 2021. Garden-path costs are larger than surprisal predicts. [link](https://pmc.ncbi.nlm.nih.gov/articles/PMC10927576/)
- **Order:** Kutas & Federmeier 2011 first, then Kutas & Hillyard 1980 and 1984, then Smith & Levy 2013, then Shain et al. 2024 alongside Brothers & Kuperberg 2021

## Evolution, development and culture

<a id="l23"></a>
### L23 · Variation, selection & drift

*Lens.*

- **Root text** (free): Darwin, C. (1859). On the Origin of Species. London: John Murray (Darwin Online, F373). [link](https://darwin-online.org.uk/converted/pdf/1859_Origin_F373.pdf)
- **Does the root teach?** Yes. Clear prose on variation and selection, but it is book-length and has no math; drift, the Price equation and replicator dynamics come from the later roots.
- **Start with:** Boris Shraiman (Simons Institute), *Statistical Physics Views of Evolution I* (47 min) [link](https://www.youtube.com/watch?v=9Th6qMLtJsU)
- **Order:** Origin Chs. 4-5, then the Shraiman lecture, then Price 1970 and Kimura 1968.

<a id="p25"></a>
### P25 · Critical periods

*Phenomenon, first tier.* Critical periods, perceptual narrowing and age-of-acquisition (sharp L2 cutoff contested)

- **Root text** (free): Wiesel, T.N. & Hubel, D.H. (1963). Single-cell responses in striate cortex of kittens deprived of vision in one eye. J Neurophysiol 26:1003-1017. doi:10.1152/jn.1963.26.6.1003 [link](https://journals.physiology.org/doi/10.1152/jn.1963.26.6.1003)
- **Does the root teach?** Yes. Short and readable physiology on visual deprivation. It does not reach speech or language. [unverified] The APS back archive should be free but returned 403 to automated fetches.
- **Start with:** Janet Werker & Takao Hensch, *Critical periods in speech perception: new directions* (~24 pp (Annu Rev Psychol 66:173-196, 2015)) [DOI](https://doi.org/10.1146/annurev-psych-010814-015104)
- **Current status:** Cognition 177:263-277 (2018) — Estimates a grammar-learning decline at around 17 years. The sharp cutoff and the model's assumptions have been disputed in later reanalyses. [link](https://pmc.ncbi.nlm.nih.gov/articles/PMC6559801/)
- **Order:** Wiesel & Hubel 1963, then Werker & Hensch 2015, then Werker & Tees 1984 / Maye et al. 2002 / Mayberry 1993, then Hartshorne et al. 2018

<a id="p34"></a>
### P34 · Convergence and contingency

*Phenomenon.* Convergent evolution, including of cognition, alongside contingency

- **Root text** (paywalled): Emery & Clayton 2004, The mentality of crows: convergent evolution of intelligence in corvids and apes, Science 306:1903-1907, doi:10.1126/science.1098410 [DOI](https://doi.org/10.1126/science.1098410)
- **Does the root teach?** Yes. A readable review that lays out the convergence argument. The free copy is a reprint on a UCSD course site. For the contingency half, Blount et al. 2008 is free at PMC2430337.
- **Current status:** Contingency and determinism in evolution: Replaying life's tape (Science 362:eaam5979, 2018) — Lab and natural replay experiments show both convergence and contingency. Which one dominates depends on scale and on how similar the starting points are. Note that this review covers evolution in general, not cognition specifically. [link](https://www.blount-lab.org/uploads/2/3/0/3/23037222/blount_et_al_2018_with_supplement_-_contingency_and_determinism_in_evolution.pdf)
- **Requires:** [L23 · Variation, selection & drift](#l23)
- **Order:** Emery & Clayton 2004 first, then Blount et al. 2008, then Blount, Lenski & Losos 2018

<a id="p35"></a>
### P35 · Cumulative culture

*Phenomenon.*

- **Root text** (free): Tomasello, Kruger & Ratner 1993, Cultural learning, Behavioral and Brain Sciences 16:495-552, doi:10.1017/S0140525X0003123X [link](https://access.archive-ouverte.unige.ch/access/metadata/938f161a-2e7f-460f-bbbf-a79381c72568/download)
- **Does the root teach?** Yes. Clear, but long (59 pp with commentaries). It founds high-fidelity cultural learning; the ratchet framing comes later, in Tomasello 1999 and Tennie et al. 2009. The free PDF is filed under a Schneuwly commentary but contains the full target article and commentaries.
- **Start with:** Kenny Smith, *Language Learning, Language Use, and The Evolution of Linguistic Structure (SFI)* (70 min) [link](https://www.youtube.com/watch?v=NjBtagmAi40)
- **Current status:** What is cumulative cultural evolution? (Proc R Soc B 285:20180712, 2018) — Cumulative culture is robust in humans and in lab transmission chains. Whether non-human animals have it is contested, and so are its defining criteria. Open-ended cumulative culture has been shown only in humans. [link](https://pmc.ncbi.nlm.nih.gov/articles/PMC6015846/)
- **Order:** Tomasello 1993 target article (skip commentaries) first, then Tennie et al. 2009, then the Kenny Smith lecture with Kirby et al. 2008, then Mesoudi & Thornton 2018

## Mind and awareness

<a id="p14"></a>
### P14 · The positive manifold (g)

*Phenomenon.* Positive manifold (g); its cause disputed

- **Root text** (free): Spearman, C. (1904). 'General intelligence,' objectively determined and measured. American Journal of Psychology 15:201-293. Full text at Classics in the History of Psychology. [link](https://psychclassics.yorku.ca/Spearman/)
- **Does the root teach?** No. About 90 pages of pre-factor-analysis correlational method (tetrad-style corrections) in dated notation. It is hard to extract the modern model from it.
- **Start with:** van der Maas, Dolan, Grasman, Wicherts, Huizenga & Raijmakers, *A dynamical model of general intelligence: the positive manifold of intelligence by mutualism (Psychological Review 113:842-861, 2006)* (20 pp. (paywalled)) [link](https://doi.org/10.1037/0033-295X.113.4.842)
- **Current status:** Network models for cognitive development and intelligence (Journal of Intelligence 5:16, 2017) — The positive manifold is among psychology's most replicated findings. Its cause (a latent g, sampling/bonds, mutualism, or process overlap) is not settled by the factor-analytic data. [link](https://pmc.ncbi.nlm.nih.gov/articles/PMC6526461/)
- **Order:** van der Maas et al. 2006 sections 1-2 first, then Spearman 1904 Part I skim, then van der Maas et al. 2017.

<a id="p18"></a>
### P18 · The false-belief transition

*Phenomenon.* Explicit false-belief transition around age four

- **Root text** (paywalled): Wimmer, H. & Perner, J. (1983). Beliefs about beliefs: representation and constraining function of wrong beliefs in young children's understanding of deception. Cognition 13(1):103-128. doi:10.1016/0010-0277(83)90004-5 [DOI](https://doi.org/10.1016/0010-0277(83)90004-5)
- **Does the root teach?** Yes. Introduces the Maxi task in plain language. It does not pin the transition at age four; for that you need Wellman, Cross & Watson 2001 (Child Dev 72:655-684, doi:10.1111/1467-8624.00304, paywalled).
- **Current status:** Nature Reviews Psychology 1:223-235 (2022), doi:10.1038/s44159-022-00037-z — The explicit transition at age four is robust. What is contested is the implicit or infant false-belief findings, which have failed to replicate across many labs, and whether the transition reflects a conceptual change or a performance change. [link](https://www.psych.uni-goettingen.de/de/development/pdfs/rakoczy_tom_nature_review_psychology_2022.pdf)
- **Order:** Wimmer & Perner 1983, then the Wellman et al. 2001 meta-analysis, then Rakoczy 2022

<a id="p24"></a>
### P24 · Limits of awareness

*Phenomenon.* Limits of awareness: inattentional and change blindness, bistable perception, partial report

- **Root text** (free): Sperling, G. (1960). The information available in brief visual presentations. Psychological Monographs 74(11, Whole No. 498):1-29. doi:10.1037/h0093759 [link](https://sites.socsci.uci.edu/~whipl/staff/sperling/PDFs/Sperling_PsychMonogr_1960.pdf)
- **Does the root teach?** Yes. A long but lucid monograph whose partial-report logic is fully explained. It covers iconic memory only, not inattentional blindness, change blindness or rivalry.
- **Current status:** Trends Cogn Sci 9(1):16-20 (2005) — The effects are robust. What is contested is the inference from failure to report to failure to represent, which is the same overflow debate partial report feeds. [link](https://www.cs.ubc.ca/~rensink/publications/download/S&R-TICS-05a.pdf)
- **Order:** Sperling 1960 (Exps 1-3), then Simons & Chabris 1999 (free: http://www.chabris.com/Simons1999.pdf, verified), then Logothetis & Schall 1989 (paywalled), then Simons & Rensink 2005
