# WE MUST ADD STRUCTURE TO DEEP LEARNING BECAUSE...

[Original episode](https://www.youtube.com/watch?v=rie-9AEhYdY) · Source: Machine Learning Street Talk · [All reviews](../README.md) · [Learning path](../learning-path.md)

Published: 2024-04-01 · Decision: **Worthwhile** · Confidence: High on conceptual relevance; moderate on claims about practical architecture benefits.

## Central claim

A valuable attempt to turn architectural assumptions into compositional mathematical structure. The enduring contribution is the move from symmetry alone to typed composition, algebraic laws and parameterized computation; the interview does not establish that this program solves reasoning or makes scaling obsolete.

## Ideas I want to keep

- The progression from groups to monoids to categories separates invertible transformations from general operations and from operations whose composition is type restricted. This widens architecture design beyond geometric symmetry without abandoning the question of what structure a learned map should preserve.

- Syntax and semantics are separated: a language specifies allowable expressions, while an interpretation maps them into concrete computations. That suggests designing a domain language whose compositional constraints survive its neural implementation, rather than expecting every relation to emerge from examples.

- The list-monad examples make abstraction tangible. Singleton insertion and flattening define the construction, while a compatible fold selects an algebra such as addition or multiplication. The same data construction admits distinct valid computational meanings.

- The discussion eventually separates computational expressivity from training. Recursion, expandable memory and a stopping rule are architectural mechanisms; demonstrating that a system can implement them is different from demonstrating that optimization learns the desired algorithm.

- Parameterized maps and maps between parameterizations supply another level of structure. A mathematical description can relate implementations without treating a particular tensor layout as the fundamental object. This is an organizing framework, not a replacement gradient algorithm.

## Mathematical anatomy

**Objects:** Typed objects, composable morphisms, functors, natural transformations, monads and their algebras; neural computations interpreted as parameterized maps. Objects need not all represent one homogeneous kind of data.

**Objective:** Structural relations constrain an architecture; learning determines the remaining degrees of freedom. The episode supplies no universal statistical objective that makes the chosen structure correct.

**Mechanism:** For the list monad T, the unit inserts a singleton and multiplication flattens nested lists. An algebra a:T(X)→X obeys compatibility laws. A natural transformation has components that commute with mapped morphisms; that commuting requirement, rather than diagram appearance, expresses preservation.

**Assumptions:** A useful task structure has been identified and can be expressed in the selected formalism. The intended constraints must be compatible with the target function and concrete implementation.

**Limits:** These laws do not themselves give sample-complexity, optimization or out-of-distribution guarantees. A monad is not merely arbitrary function repetition, and free constructions require existence conditions. Finite parameter count does not imply an algorithm cannot execute on arbitrarily long finite inputs.

## Evidence, limitations and corrections

- The complete untimed publisher transcript was read. References to other speakers and material earlier in the video suggest an interview component within an edited presentation; correspondence with the entire YouTube edition is not established. No playback timestamps are inferred.

- The published position-paper abstract confirms the proposed bridge using universal algebra of monads and a 2-category of parameterized maps. That verifies the research framing, not the interview’s projected empirical advantages.

- Several pedagogical shortcuts require correction: addition and multiplication can be different algebras for the same list monad; a Lawvere theory requires more than being any small finite-product category; functors preserve identities as well as composition.

- The passage describing infinite iteration as automatically idempotent should not be used as a proof of free-monad construction. The distinction between structural recursion and a fixed unrolling is also blurred before the participants acknowledge that no blanket neural impossibility follows.

- Funding, compiler aspirations, proprietary demonstrations and contemporary model judgments are not comparative evidence. The training-data-as-program analogy does not establish the interview’s copyright conclusions.

## Relevance to my research

I want to follow geometric deep learning with this interview: it asks how the algebra of a problem can determine permissible computations. Its value for me depends on translating every abstraction into a small executable example. Categorical language can expose assumptions without certifying an intelligence theory.

## My viewing plan

**Mode:** I would watch the conceptual interview, paying particular attention to the algebra examples and skimming company and model-brand discussion.

**Segments:** 

**Text anchors:** - Opening progression from groups and monoids to categories and typed composition

- Middle discussion of recursion, finite resources, syntax and semantics

- Final category primer, natural transformations, list monads and algebras

**Edition:** Publisher source is untimed. These are textual navigation anchors, not verified YouTube chapters; no exact time ranges are available.

**Intention:** I plan to watch the conceptual interview, concentrating on the algebra examples and skimming company and model-brand discussion.

## Objections and open questions

Hand-built structure can be wrong, costly to discover or unnecessary at the relevant data scale. A common language may unify descriptions without producing a better model. Conversely, those limitations do not erase the usefulness of exact compositional constraints when the task genuinely has them. The useful comparison is matched training and extrapolation, not structure versus statistics as mutually exclusive options.

## An experiment I could try

I would implement list reduction with an unconstrained learned binary operator and with an associative construction possessing an identity. Training on short lists and testing longer lists, alternative parenthesizations and empty input would expose the structural differences. I also want to check h(fold_A(xs))=fold_B(map(h,xs)) for a chosen monoid homomorphism. Subtraction as a deliberately nonassociative target would expose the cost of a wrong prior; algebraic guarantees, floating-point error and predictive accuracy would be assessed separately.

## Connections in my notes

- Bronstein: extends the question of preserved symmetry toward typed computation and algebraic composition, while inheriting the need to justify priors.

- Neural algorithmic reasoning: distinguishes representing an iterative algorithm from learning its execution and stopping behavior.

## Primary sources checked

- **Url:** https://proceedings.mlr.press/v235/gavranovic24a.html
  
  **Purpose:** Primary publication abstract confirms framework and position-paper scope; not independent empirical validation.

## Source and coverage

**Read:** Entire available selected transcript read sequentially; audio not verified.

**Last timestamp:** 

**Source caveats:** Publisher transcript edition; wording, speaker labeling and mathematical transcription may contain errors. Timings refer only to this source.

Source type: Publisher transcript. Reviewed text: 20,274 words.

Transcript file: `rie-9AEhYdY.publisher.txt` (not distributed).

SHA-256: `29d39dcf1f1a82c79f6ff99f4865e43f8d8770ad2a7fe42a8e671a801d734c76`.

[Structured review](rie-9AEhYdY.json) · [Source ledger](../sources.json)
