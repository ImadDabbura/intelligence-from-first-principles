# Intelligence from first principles

I want to understand learning, modeling, intelligence and statistical structure from first principles deeply enough to discover better ways of building intelligent systems, and to explain those insights clearly to serious people.

I am especially drawn to the **mathematical anatomy of learning systems**: how their representations, objectives, assumptions and learning dynamics fit together. I want to understand which structures make learning possible, why they work, where they fail and what those limits suggest about how to build better systems.

This collection is part of that work. I use podcasts, lectures, courses and papers to find ideas I can reconstruct mathematically, test and explain in my own words.

## One Library

The [core](core/README.md) lists the ideas to master before branching out: 32 lenses and 35 phenomena, each with its root text, a teaching source where needed, and for phenomena a current-status source. 26 of them form the first tier.

Everything else sits in one [Library](index.html): 570 items from 23 sources in a single list, all in the same form. Each entry says why the item is here and what a closer look should settle, and is tied to the core ideas it serves. Pick a core idea to see its root text, where to start, and every item that teaches it or goes deeper, best sources first. Search and the source filter work across the whole list.

Clone or download this repository and open **`index.html`** in a browser. It works offline without installation. GitHub displays HTML as source, so online the easiest way in is the [core page](core/README.md) and each source’s page under `collections/`.

## How I choose material

I examine the publisher’s summary, notes, chapter headings and references to decide whether an item deserves a place. A place in the Library is a reading decision. It is not a recommendation to watch, and it does not validate the speaker’s claims. The [methodology](#methodology) explains the criteria.

## How this was made

I set the research objective and selection criteria and used AI agents to screen sources, map the fields’ foundations and tie items to core ideas. This is not a claim that I have watched every item or checked every claim. Entries are judged from publisher descriptions unless they say otherwise.

Downloaded transcripts, audio and complete publisher descriptions stay in my private research archive. [Attribution and source coverage](ATTRIBUTION.md) explains what is included. Earlier versions of this repository carried AI-assisted transcript reviews of 131 Machine Learning Street Talk episodes and a study path built on them. I removed them on 22 November 2026 in favour of one Library in one form; the git history keeps them.

## Sources

Machine Learning Street Talk was the first source. The others are lecture series, institutes, conferences and the originators’ own writing, each with its own scope and snapshot date, listed under Sources and coverage in the Library. There is no target number of items: another talk needs to add an idea, a useful disagreement or a worked example.

[Suggest a resource or correction](CONTRIBUTING.md). A useful suggestion names the question it helps answer and the passage, mechanism or result that makes it worth examining.

## Rebuild the Library

Python 3.10 or newer is sufficient; there are no third-party dependencies or network calls.

```sh
python3 scripts/build_report.py
python3 scripts/build_report.py --check
```

`collections.json` registers the sources. Each source keeps its screening record under `collections/`. `core/core.json` holds the core ideas and `core/links.json` records which items serve which ideas. The builder combines them into `index.html` and `report.json`.

See [Adding a source](templates/data-format.md) for the data layout. New sources appear in the same Library and filter.

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

### The filter: does it earn a place?

I start with the publisher’s own summary, description, chapter headings, notes and references. I record the publication date, the inventory date and the version being considered. Alternate edits and duplicate uploads are kept distinct from genuinely different contributions.

The decision is one of:

- **High priority:** a concrete mechanism, discriminating experiment or substantial competing explanation directly bears on the research questions. Only these enter the Library.
- **Medium priority:** promising context or a potentially useful application, with a less specific contribution to those questions.
- **Skip:** a clear mismatch or a duplicate whose contribution is already represented.
- **Insufficient information:** the available metadata does not justify a place.

I record what the publisher promises, why that matters and the question a closer look must settle. References are leads to inspect, not evidence that the linked work has been read.

### The core

The [core](core/README.md) was built separately, from each field’s own account of its foundations, the founding claims of 27 schools of thought and 47 open questions from recognised lists. Its page says how the first tier was chosen and what was checked.

### Revising a judgment

I want corrections tied to a passage, equation, experiment or source. New snapshots receive explicit dates and a record of additions; an old snapshot is never presented as current coverage.
