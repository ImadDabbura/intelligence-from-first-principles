# #041 Dr. SIMON STRINGER - Biologically Plausible Neural Networks

[Original episode](https://www.youtube.com/watch?v=aisgNLypUKs) · [All reviews](../README.md) · [Learning path](../learning-path.md)

Published: 2021-02-03 · Decision: **Worthwhile** · Confidence: high

## Central claim

A useful competing account of representation: intelligence needs relations between features, not merely a bag of active detectors. Temporal dynamics and locally learned invariance provide concrete candidate mechanisms, but the episode does not establish that spikes are necessary for relational intelligence.

## Ideas I want to keep

- Trace learning exploits temporal continuity: a local synaptic update uses a decaying activity trace so views occurring near one another become associated. Continuous transformation learning instead exploits overlap along a spatially similar sequence. These are different assumptions about how experience identifies invariant factors.

- The three-neuron binding motif distinguishes coactivation from a particular lower-level feature contributing to a higher-level feature. With matched direct and indirect transmission delays, a third neuron can respond to temporally aligned inputs and carry information about that relation.

- Top-down, lateral and bottom-up connections participate during learning, not merely in a later attention stage. Their interaction can change which representations emerge; adding feedback after learning is a different model.

- A concrete coordinate-frame example explains how hand-centered features can emerge from retinal observations: faster eye movements than hand movement produce temporally adjacent retinal views sharing the same hand-object relation.

- Navigation examples distinguish learning environmental transitions without reward from subsequently selecting a goal. Visual inputs combined with self-motion signals produce different spatial representations in the reported simulations.

## Mathematical anatomy

**Objects:** Spiking units, local synapses, distributed transmission delays, activity traces, competing units and recurrent hierarchical connections. The relevant variable is a relation between features, rather than only a category label.

**Assumptions:** Temporal adjacency and image similarity often preserve identity or a useful relation. Relative spike timing influences plasticity. Architecture, delay distributions, competition and sensory statistics are substantial inductive biases even when initial weights are random.

**Objective:** Learn invariant but relationally specific representations through local self-organization, with downstream recognition and flexible behavior as tests. No single global objective is derived for the whole framework.

**Mechanism:** A schematic trace z_t=(1-alpha)z_(t-1)+alpha y_t can replace an instantaneous activity in a Hebbian update. In a binding motif, direct and indirect path delays approximately match, allowing coincidence detection. STDP selects synapses according to pre/post timing; selecting among contacts with different delays changes effective temporal connectivity.

**Limits:** Temporal precedence is not automatically causal participation: common input and accidental coincidences remain possible. The claimed if-and-only-if binding behavior requires assumptions about thresholds, background input and timing. Invariance can erase information needed for binding unless relations are preserved separately.

## Evidence, limitations and corrections

- The 22:00–34:00 discussion describes actual simulated motifs and the role of transmission delays; the exact topology is partly illustrated with hand gestures, and one transcript sentence appears internally inconsistent. The summary preserves the matched-path principle rather than pretending the text fully specifies the circuit.

- At 44:01–45:00, applying the spiking binding model to realistic faces and objects remains future work. At 58:03 the picket-fence example is explicitly acknowledged as an unrun simulation. Robust occlusion handling is therefore a proposal.

- At 57:01 a CNN modified to preserve binding information reportedly improves MNIST black-box robustness in work being submitted. This is preliminary, narrowly evaluated, and also undercuts any claim that only biological spiking substrates can represent binding.

- At 71:00–73:00 Stringer acknowledges how difficult it is to identify overlapping polychronous groups in recordings and simulations. Similar tuning properties do not uniquely identify the brain’s mechanism.

- The opening claims that artificial networks lack recurrent or local processing, population coding, and relational information are overbroad. Such capabilities can be designed in artificial systems. The episode also conflates some kernel interpretations with mere memorization; that conclusion does not follow.

## Relevance to my research

Substantial for separating category recognition, invariant representation, relational binding, and action-relevant coordinate systems. The strongest learning opportunity is the explicit construction of a plausible local mechanism from environmental statistics. I view the biological route as a research hypothesis and source of mechanisms, not a proof that fine-grained biological simulation is required for intelligence.

## My viewing plan

**Mode:** chapters

**Segments:** - **Start:** 00:22:01
  
  **End:** 00:34:00
  
  **Purpose:** Temporal binding mechanism and the role of delayed pathways.

- **Start:** 00:53:03
  
  **End:** 01:00:00
  
  **Purpose:** Specificity, adversarial examples and explicit limits of the evidence.

- **Start:** 01:07:01
  
  **End:** 01:12:04
  
  **Purpose:** Self-motion inputs, spatial representations and identifiability.

- **Start:** 01:16:03
  
  **End:** 01:27:00
  
  **Purpose:** Trace learning, spatial continuity and the hand-centered-frame thought experiment.

**Edition note:** Observed timestamps refer to the saved transcript, read in full through the closing remarks. The visual circuit demonstration is not independently inspected.

## Objections and open questions

- Rate-based recurrent or relational architectures can implement analogous computations; biological realism alone does not establish superior sample efficiency, generalization or necessity.

- Binding and rich sensory representation may support intelligence without explaining planning, abstraction, language or consciousness. These higher-level implications are conjectural in the conversation.

## An experiment I could try

I want to generate videos of a hand and object while independently controlling retinal translation, relative object-hand displacement and movement rates. A local trace-learning model would test whether units preserve relative position while ignoring retinal translation. Violating the assumed time-scale ordering or rapidly switching objects would reveal whether apparent invariance becomes destructive aliasing. A model receiving explicit relative coordinates would provide a comparison.

## Connections in my notes

- Connects to Ororbia on local learning and dynamic representations, but proposes a distinct temporally precise mechanism.

- Connects to SWaV through the question of which transformations should preserve a representation; here the transformations are supplied by temporal experience.

- Provides a concrete alternative to treating generalization as classification accuracy alone.

## Source and coverage

**Status:** complete_available_text

**Method:** Read entire saved transcript; any truncated tool section reread in bounded chunks. Audio not checked.

**Last timestamp:** 01:27:00

**Caveats:** - ASR transcription can corrupt names and mathematical terminology; transcript completeness is not an audio audit.

Source type: Existing caption or archive. Reviewed text: 17,093 words.

Transcript file: `aisgNLypUKs.hf.txt` (not distributed).

SHA-256: `7dd0417113000c8f5f666f64de79a2d92a1e3f70656ad944d7421d055b08e6e7`.

[Structured review](aisgNLypUKs.json) · [Source ledger](../sources.json)
