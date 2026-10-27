# Intelligence from first principles

How does a system learn from experience, form useful abstractions, reason about unfamiliar situations and decide what to do next?

This is my working collection of research notes on those questions. I’m interested in the mathematical and statistical structures that make intelligence possible, across learning theory, program synthesis, control, neuroscience and evolution. Language models are one part of that picture.

Podcasts and lectures often introduce ideas I would otherwise miss. I want to keep the ones that change how I think: a mechanism I can reconstruct, an assumption I can examine, a counterexample that exposes a gap, or an experiment I could actually try. The notes record why an episode earns a place and where its argument stops being convincing.

## One report, across sources

I keep podcasts, lectures and courses in one [shared report](index.html), with a common learning path, search and source filter. Each episode identifies its publisher and format. Source-specific data stays in `collections/`; the report combines it.

MLST is the first collection. Its channel snapshot was taken on **26 October 2026**:

- **269 uploads screened**, published between **9 April 2020 and 26 October 2026**.
- **131 high-priority episodes reviewed in depth**, published between **9 April 2020 and 9 October 2026**.
- **53 core contributions, 60 worthwhile additions, 14 selections of specific passages and 4 drops** after transcript review.

[Follow the learning path](learning-path.md) · [Browse the episode reviews](collections/mlst/README.md) · [See the first filter](collections/mlst/screening.md)

The learning path starts with Wilson, Koolen and Bronstein for orientation, then follows nine questions from evaluation and learning structure through reasoning, action and open-ended discovery. It is a suggested conceptual order; the deeper branches are optional.

Clone or download this repository and open **`index.html`** in a browser. The report works offline without installation. GitHub displays HTML as source; the Markdown links above are the easiest way to read online. The report keeps the notes and source coverage together; the evaluation methodology is below.

## How I select material

I use two filters. First, I examine the publisher’s summary, notes, chapter headings and references to decide whether an episode deserves a transcript review. Then I examine the full available transcript for its actual contribution: the objects and assumptions involved, the proposed mechanism, the evidence, the limits and what it adds to the rest of the collection.

A promising description earns a place in the reading queue. It does not earn a recommendation to watch. The [methodology](#methodology) explains both stages, including how I handle uncertainty and overlap.

## How these notes were made

I set the research objective and selection criteria and used AI agents to review transcripts and reconcile their findings. These are AI-assisted research notes and a study plan. They are not a claim that I personally watched every episode, checked every proof or completed the proposed experiments. Individual reviews record transcription problems, edition differences and the primary sources checked where applicable.

The repository contains the reviews, screening decisions, learning path, source records and publisher links. Downloaded transcripts, audio and complete publisher descriptions stay in my private research archive. [Attribution and source coverage](ATTRIBUTION.md) explains what is included.

## Beyond MLST

I’ll add other podcasts, lectures and courses when they address the same questions. Each collection will have its own scope, dates and review status. There is no target number of recommendations: another interview needs to add an idea, a useful disagreement or a worked example.

[Suggest a resource or correction](CONTRIBUTING.md). A useful suggestion names the question it helps answer and the passage, mechanism or result that makes it worth examining.

## Rebuild the shared report

Python 3.10 or newer is sufficient; there are no third-party dependencies or network calls.

```sh
python3 scripts/build_report.py
python3 scripts/build_report.py --check
```

`collections.json` registers the sources. Each source has its own episode, review, screening and evidence records. The root `learning-path.json` defines the shared study sequence, using IDs such as `mlst:QWidx8cYVRs`. The builder combines every registered collection into `index.html` and `report.json`. It also preserves the MLST archive’s Markdown views.

See [Adding a source](templates/data-format.md) for the data layout. Future sources appear in the same report and filter; they do not need their own report template.

## Methodology

My objective is to understand the nature of intelligence and the mathematical structures that make learning possible. I assume a working knowledge of linear algebra, probability and calculus. I am looking for explanations I can reason through and test, across different approaches to intelligence.

### Questions I return to

- What would count as understanding or intelligence, and what can an experiment actually identify?
- Which prior structure makes learning and generalization possible?
- How do useful representations and abstractions emerge?
- How do learned structures support composition, search and executable reasoning?
- Which observations should a learner acquire, and how should it adapt?
- When is a world model adequate for planning and control?
- How can intelligence develop through evolution, open-ended discovery and interaction among agents?

These guide selection. They are not a requirement that every episode address every question.

### First filter: is a transcript review justified?

I start with the publisher’s own summary, description, chapter headings, notes and references. I record the publication date, the inventory date and the version being considered. Alternate edits and duplicate uploads are kept distinct from genuinely different contributions.

The decision is one of:

- **Read transcript, high priority:** a concrete mechanism, discriminating experiment or substantial competing explanation directly bears on the research questions.
- **Read transcript, medium priority:** promising context or a potentially useful application, with a less specific contribution to those questions.
- **Skip:** a clear mismatch or a duplicate whose contribution is already represented.
- **Insufficient information:** the available metadata does not justify a full read. A targeted passage or better source is needed before advancing it.

I record what the publisher promises, why that matters and the question a transcript review must resolve. References are leads to inspect, not evidence that the linked work has already been read. No new full transcripts are read as part of this filter.

### Second filter: what survives a full reading?

For an episode that advances, I use the full available transcript and record its source, edition, coverage, word count and file hash. A complete reading refers to that saved text. It does not establish that the text contains every spoken word or matches another edition’s timestamps.

The review separates:

- **The claim:** what the episode is actually arguing.
- **The mathematical anatomy:** objects, objectives, mechanisms, assumptions and limits.
- **The evidence:** what is demonstrated, what is inferred and what remains speculative.
- **The contribution:** what this adds to my existing understanding and to the other episodes.
- **The next step:** a passage to watch, an objection to examine or an experiment I could try.

I check primary sources selectively when a central technical claim needs clarification. I record those checks explicitly; a bibliography alone is not a verification record. I distinguish a guest’s statement from the reviewer’s reconstruction or correction.

The resulting viewing decisions are:

- **Core:** a substantial contribution to the central research questions that merits sustained attention.
- **Worthwhile:** a distinct explanation, example or competing account that adds enough to study.
- **Selected passages:** a useful contribution concentrated in particular sections.
- **Drop:** the full reading does not justify further viewing for this objective.

“Core” is a research priority, not a certification that every claim is correct. When the case for watching is still weak after review, I leave it out. I do not fill a quota, and I do not promote an episode merely because its guest is prominent.

### Reconciliation and learning order

I compare the reviews for repeated material, disagreements and prerequisites. Episodes that make the same claim do not count as independent evidence. A later interview earns a place if it adds a derivation, a useful counterexample, a different mechanism or a better worked example.

The learning path follows conceptual dependencies. It begins with what an evaluation can establish, then moves through learning structure, abstraction, reasoning, information acquisition and action, before broader questions about discovery and collective intelligence. This is a flexible study sequence rather than a ranking of speakers.

### What happened in the first MLST collection

The 26 October 2026 snapshot contained 269 Videos-tab uploads. The metadata filter yielded 131 high-priority entries, 115 medium-priority entries, 15 skips and 8 unresolved entries. Only the 131 high-priority entries advanced to this transcript-review pass.

AI reviewers read the available transcripts in batches. A coordinating agent also reviewed a set directly, compared the written assessments and assembled the learning path. This was not two independent full readings of every transcript. The collection reused 100 transcripts and recovered 31: 7 publisher transcripts, 22 local audio transcriptions and 2 YouTube caption tracks. All 131 selected episodes had a transcript and review by 26 October. Editorial revisions followed on 27 October without a fresh channel scan.

The remaining 138 entries are outside this second-stage pass; they are not 138 transcript-based rejections. Two separately listed livestreams and 37 unmatched podcast-feed entries were screened separately. Feed entries may be alternate edits and are not 37 additional verified episodes. Shorts were excluded. Deleted, private and unlisted material is outside the inventory guarantee.

The reviewed sources contain about 2.1 million words. The 131 videos have 193.4 hours of publisher-listed runtime; this is neither time spent reviewing nor a recommended watching budget. Exact counts and dates are in the [scope record](collections/mlst/scope-and-method.json).

### Revising a judgment

I want corrections tied to a passage, equation, experiment or source. If a correction changes the recommendation, I update both the review and its place in the learning path. New collection snapshots receive explicit dates and a record of additions; an old snapshot is never presented as current coverage.
