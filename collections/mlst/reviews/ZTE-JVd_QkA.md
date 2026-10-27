# Biologically-inspired AI and Mortal Computation

[Original episode](https://www.youtube.com/watch?v=ZTE-JVd_QkA) · Source: Machine Learning Street Talk · [All reviews](../README.md) · [Learning path](../learning-path.md)

Published: 2024-10-15 · Decision: **Worthwhile** · Confidence: high on learning mechanisms; moderate on broader framework

## Central claim

Useful for distinguishing credit assignment, inference dynamics and physical implementation. The concrete predictive-coding and local-learning discussion is more valuable than the sweeping suggestion that substrate mortality or biological similarity supplies intelligence, understanding or alignment.

## Ideas I want to keep

- Mortal computation joins the effective program to an individual physical substrate. Device-specific dynamics can perform useful computation without moving all state through a generic memory/processor interface, but this sacrifices effortless copying and hardware-independent execution. The important engineering question is the accuracy-energy-adaptability tradeoff, not whether every physical computer is already mortal in the ordinary sense.

- Mortal inference, learning and selection separate fast activity dynamics, slower synaptic changes and still slower structural adaptation. Learning can amortize inference by changing the dynamics so useful states are reached faster; structural change modifies which inference and learning processes are accessible. This is a productive decomposition even when implemented on ordinary digital hardware.

- Predictive coding is described as local populations predicting other populations, exchanging error messages and relaxing their activities. Synaptic updates then combine presynaptic activity with local error. The account makes clear why the architecture and inference algorithm determine what local learning signals are available, rather than treating learning as a plug-in optimizer unrelated to computation.

- The survey taxonomy asks where teaching signals originate and whether layers coordinate: explicit targets from feedback, implicit contrastive differences between phases, and synergistic versus relatively independent updates. Contrastive Hebbian learning, recirculation and forward-only approaches occupy different points; none eliminates the need for informative learning signals.

- The speaker gives a concrete stability-plasticity example: local predictive coding still forgets, while a learned gating/resource-allocation circuit can protect task-specific activity. He also acknowledges simulation overhead and hardware translation barriers. These admissions prevent biological plausibility from being mistaken for an already demonstrated scaling advantage.

## Mathematical anatomy

**Objects:** Activities z_l, predictions f_l(z_upper;W_l), residuals e_l, precision matrices Pi_l, synaptic weights, connectivity/gates, physical communication costs and multiple update timescales.

**Assumptions:** A chosen energy or generative objective yields stable inference dynamics; local information is sufficient for the intended update; precision and feedback pathways can be learned or specified; hardware realizes the proposed parallelism efficiently.

**Objective:** A schematic Gaussian predictive objective is F=sum_l 0.5 e_l^T Pi_l e_l plus appropriate priors and normalization terms. Fast dynamics follow dz/dt=-dF/dz; slower weight updates use -dF/dW, often giving local activity-error products. Structural adaptation needs a separately specified discrete rule or relaxation.

**Mechanism:** Iterative local prediction-error exchanges settle activities; plasticity changes connections using local signals; gating or structural changes allocate resources; contrastive alternatives compare activity statistics under different conditions.

**Limits:** Locality does not guarantee global objective optimization, convergence or good generalization. Predictive-coding implementations can still require activation derivatives and precise feedback assumptions. Physical energy dissipation and variational free energy are different quantities unless an explicit mapping is established.

## Evidence, limitations and corrections

- The speaker’s neural generative coding model reportedly learns separate feedback pathways, precision and sample generation on datasets such as MNIST, characters and silhouettes. Those bounded demonstrations are not evidence that the proposed full mortal-computing framework achieves general intelligence.

- Claims that backpropagation has no parallelism, that all biological learning avoids derivatives, or that conventional networks have no dynamics are overstated. Backprop has dependency constraints but also extensive within-layer/batch parallelism; recurrent and continuous-time networks exist, and some local schemes also use derivatives.

- The energy comparison between a brain and a city-scale GPT operation mixes unclear system boundaries and workloads. Landauer’s bound concerns logically irreversible operations under specified conditions; it does not establish the episode’s comparative efficiency claims or a guaranteed advantage for any proposed architecture.

- The speaker explicitly reports that current simulations may run slower than standard backprop networks and that neuromorphic access, toolchains and microcode translation impede implementation. Hardware promises should therefore be separated from measured end-to-end advantages.

- Self-preservation, embodiment and the possibility of pain do not entail empathy or aligned behavior. The discussion recognizes negative possibilities, but no evidence establishes the alignment conjecture. Predicting in latent space also does not automatically solve noisy-TV exploration unless nuisance information is actually excluded.

## Relevance to my research

Worthwhile as a source of alternative computational mechanisms and a reminder to count communication, memory and adaptation costs. Most relevant when asking what a learning system must compute locally and how its substrate changes the cost of doing so. The broader metaphysical and alignment rhetoric is not required to benefit from the technical material.

## My viewing plan

**Mode:** chapters

**Segments:** - **Start:** 00:06:05
  
  **End:** 00:16:06
  
  **Purpose:** Substrate dependence and copying/efficiency tradeoffs, with quantitative claims treated cautiously.

- **Start:** 00:24:03
  
  **End:** 00:37:03
  
  **Purpose:** Three timescales and predictive-coding mechanism.

- **Start:** 00:42:00
  
  **End:** 00:58:01
  
  **Purpose:** Credit-assignment taxonomy and contrastive dynamics.

- **Start:** 01:03:03
  
  **End:** 01:12:15
  
  **Purpose:** Forgetting, resource allocation and real hardware bottlenecks.

- **Start:** 01:14:14
  
  **End:** 01:23:09
  
  **Purpose:** Concrete generative model, forward-only learning and remaining negative-sampling problem.

**Edition note:** Full transcript read through the 01:23:09 closing block. ASR corrupts names, Loihi, and neural generative coding; no audio check. Product availability and comparative performance claims are historical interview claims.

## Objections and open questions

- General-purpose digital abstraction provides reproducibility, fault tolerance and shared learned knowledge; energy savings must be large enough to justify reduced portability and calibration costs.

- A biological mechanism can be a useful inspiration without being either necessary or sufficient for intelligence.

- Selecting a stable local energy landscape is already substantial design work; implementing its gradients does not solve representation learning or semantic grounding automatically.

## An experiment I could try

I would implement a small predictive-coding network with explicit activity relaxation and local weight updates alongside a comparable backprop network. Inference iterations, accuracy, update communication and sequential-task forgetting would be measured before adding task-dependent gating to both systems. Asynchronous updates and device noise would provide further tests. My analysis would attribute gains separately to the learning rule, gating, representation and hardware assumptions.

## Connections in my notes

- Friston part2: inference/learning/structural timescales and the assumptions behind physical-to-inference mappings.

- Schmidhuber: fast weights, learned updates and the distinction between surprise and useful information gain.

- SWaV: negative-free representation learning still needs an anti-collapse mechanism.

## Source and coverage

**Status:** complete_available_text

**Method:** Read entire saved transcript; any truncated tool section reread in bounded chunks. Audio not checked.

**Last timestamp:** 01:23:09

**Caveats:** - ASR transcription can corrupt names and mathematical terminology; transcript completeness is not an audio audit.

Source type: Publisher transcript. Reviewed text: 16,674 words.

Transcript file: `ZTE-JVd_QkA.publisher.txt` (not distributed).

SHA-256: `f4a9a62973abe39b829ec57de9384e82fb272eed9b7fb69f4281760dbdd2cd83`.

[Structured review](ZTE-JVd_QkA.json) · [Source ledger](../sources.json)
