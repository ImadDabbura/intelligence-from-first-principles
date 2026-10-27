# NLP is not NLU and GPT-3 - Walid Saba

[Original episode](https://www.youtube.com/watch?v=b9qwLkJW2ig) · Source: Machine Learning Street Talk · [All reviews](../README.md) · [Learning path](../learning-path.md)

Published: 2020-11-04 · Decision: **Selected passages** · Confidence: high

## Central claim

The worthwhile problem is pragmatic reconstruction: listeners infer an intended situation from an underspecified utterance using shared background and type constraints. Saba offers an explicit type-based rival to unconstrained text prediction. However, the episode repeatedly presents invalid impossibility arguments and an undisclosed ontology as settled evidence, so it should be watched as a hypothesis to formalize and stress-test, not as a reliable account of what learning cannot do.

## Ideas I want to keep

- At 56:05–01:00:36, the discussion makes the hidden variables of communication explicit: utterance, semantic interpretation and shared background knowledge. The corner-table example illustrates metonymy: an entity of one type is mentioned while an associated agent is intended. Recognizing this is a different task from tokenization or matching a familiar phrase.

- At 59:23–01:00:25 and 01:33:05–01:38:22, type constraints provide a proposed mechanism. A predicate’s expected argument type conflicts with the literal referent; the interpreter introduces a relation connecting that referent to an admissible argument. This is a concrete route to structured abduction, provided the relation inventory, selection criterion and exception handling are specified.

- At 01:06:41–01:09:34 and 02:01:27–02:05:22, Saba distinguishes primitive kinds from relationally defined roles and compresses many lexical instances into shared types. Teacher can be analyzed as an agent of teaching, while brands of car share selectional properties. Even if his universal-ontology claim is unproven, the design question is useful: which distinctions should be primitive, derived, contextual or merely instance data?

- At 01:53:00–01:56:57 and 02:11:05–02:13:59, the proposed evaluation becomes more operational. A system should account for implied referents and support coherent consequences; Saba accepts that suitable continuations could count as understanding. The teenager/policeman examples also separate logical possibility from context-dependent plausibility, weakening the earlier suggestion that interpretation has essentially no degrees of freedom.

- At 02:16:45–02:19:50, intensional descriptions and discourse-dependent assumptions enter explicitly. What someone knows, learns or believes depends on how an object is presented, not only on an extensional value. The final concession that interpretation involves degrees of belief and possible discourse worlds gives a more productive statistical-structural research program than the opening anti-learning rhetoric.

## Mathematical anatomy

**Objects:** An utterance u, context c, background model K, candidate meaning m, typed entities and relations. A useful reconstruction is inference over p(m|u,c,K), with logical constraints restricting admissible interpretations and pragmatic assumptions ranking them. This notation organizes the episode; no complete inference algorithm is provided.

**Objective:** Recover an intended interpretation and its warranted consequences while preserving ambiguity when evidence is insufficient. Saba emphasizes recovering omitted structure; a defensible objective must also penalize inventing unsupported details. A type-compatible interpretation need not be the speaker’s intended one.

**Mechanism:** Given want(table,beer), a type mismatch can motivate an existential person p with sits_at(p,table) and want(p,beer). Ordinary type unification alone cannot choose sits_at rather than owns, serves or designed: this requires relational knowledge and salience. Context can broaden or change selectional restrictions, as the sentient-table example acknowledges.

**Assumptions:** The proposed ontology, relation inventory and typing judgments must be available and accurate. Their universality, innateness and claimed size are substantive empirical hypotheses. Typed semantic structure is compatible with numeric implementations; the representation’s operations and inductive biases matter more than whether its storage uses numbers.

**Limits:** Compression during learning and expansion during inference are compatible: a learned decoder can reconstruct latent structure from a short message plus shared knowledge. Missing from one utterance is not the same as absent from all training evidence. Identical observations with different latent meanings do create nonidentifiability, but that limitation applies to symbolic and neural systems alike unless they receive additional assumptions or context.

## Evidence, limitations and corrections

- The compression-versus-expansion argument is not a proof that NLU is unlearnable. Nor does agreement between people prove knowledge is innate: different samples from a shared environment can support convergent learning. These logical failures recur at58:45 and01:50:43 and undermine the strongest claims.

- At01:29:50 Saba says he stopped publishing the internal structure for commercial reasons. The claimed roughly2,000-type universal ontology is therefore not specified or evaluated sufficiently in this interview to establish coverage, efficiency or cognitive plausibility.

- Claims that embeddings can only express one similarity relation, cannot represent multiple types, or lose all structure through tensor composition confuse a particular readout with representational capacity. A symmetric cosine score cannot encode every directional relation, but a different decoder or structured embedding can. Failed experiments with one GloVe setup are not an impossibility theorem.

- The episode generalizes from selected model failures and anecdotes about children and animals to broad computational ceilings. It supplies no controlled developmental evidence or formal lower bound. Finiteness of a game does not make exhaustive solution computationally feasible, and the allegation that AlphaGo’s search was hidden or cheating is not substantiated here.

- Several inferences are defeasible rather than certain: graduate-school attendance does not establish a fixed age, and an educational-looking image cannot certify a person’s actual social role. The final discussion recognizes context and uncertainty, which should constrain the earlier confident examples. Historical GPT-3 demonstrations are evidence about those prompts and systems only.

## Relevance to my research

Useful as a carefully bounded challenge for my research: what latent structure is required for understanding, how does shared knowledge support efficient communication, and how would a typed abductive interpreter perform? Its distinctive contribution is the worked semantic problem, not the claim that a simple algorithm cannot support complex intelligence. The later Emerson/Saba discussion offers a more balanced confrontation between probabilistic and structured semantics.

## My viewing plan

**Mode:** chapters

**Ranges:** - **Start:** 00:56:05
  
  **End:** 01:00:36
  
  **Why:** Explicit utterance/meaning/background decomposition and metonymy mechanism; the accompanying compression impossibility argument is not valid.

- **Start:** 01:53:00
  
  **End:** 01:57:40
  
  **Why:** Operational understanding tests, contextual exceptions and the costs of rigid typing.

- **Start:** 02:16:45
  
  **End:** 02:19:50
  
  **Why:** Intensional interpretation, defeasible background inference and degrees of belief.

**Edition note:** Timestamps refer to the140-minute released edit. The first36 minutes repeat and amplify claims in a host-produced overview. These selected passages are a critical study of an alternative model, not an endorsement of the whole episode.

## Objections and open questions

A neural predictor can learn latent structure from indirect evidence without seeing every combination, while an explicit ontology can relocate rather than solve the knowledge-acquisition problem. Conversely, good continuation statistics alone do not certify that a system maintains coherent entities, scopes or counterfactual commitments. Both camps need transfer tests, uncertainty handling and mechanistic evidence rather than isolated successes or failures.

## An experiment I could try

My proposed test is a tiny typed interpreter for restaurant utterances with literal, metonymic and fictional contexts. It would include competing relations such as sits_at, owns and serves, plus cases where two patrons share a table. Hard type repair and probabilistic abduction would use the same relation inventory, with object names and relation combinations held out. Referent accuracy and calibrated abstention, followed by a sentient-table fiction, would help me distinguish missing facts, wrong ontology, search limitations and genuinely insufficient evidence.

## Connections in my notes

- Emerson/Saba’s later episode directly contrasts probabilistic semantics and typed structure with fewer unsupported universal claims.

- Voita’s probing episode supplies the discipline needed to distinguish behavior, recoverable information and actual semantic use.

- Hutter’s PFN episode demonstrates how a structural prior and learned inference can coexist, contradicting a forced choice between structure and learning.

## Source and coverage

**Status:** complete_available_text

**Start:** 00:00:00

**End:** 02:20:21

**Caveats:** - Read all 24,779 source words. First approximately36 minutes are an edited host introduction with excerpts, commentary and demonstrations; the sustained interview begins36:06. Transcript repeatedly spells intension as intention and corrupts names. No audio verification.

Source type: Existing caption or archive. Reviewed text: 23,007 words.

Transcript file: `b9qwLkJW2ig.hf.txt` (not distributed).

SHA-256: `cb31e6fe4280ee562aff80536699b8d5cb52132fed22e5eddc00008f383d6e06`.

[Structured review](b9qwLkJW2ig.json) · [Source ledger](../sources.json)
