# Intelligence from first principles

How does a system learn from experience, form useful abstractions, reason about unfamiliar situations and decide what to do next?

This is my working collection of research notes on those questions. I’m interested in the mathematical and statistical structures that make intelligence possible, across learning theory, program synthesis, control, neuroscience and evolution. Language models are one part of that picture.

Podcasts and lectures often introduce ideas I would otherwise miss. I want to keep the ones that change how I think: a mechanism I can reconstruct, an assumption I can examine, a counterexample that exposes a gap, or an experiment I could actually try. The notes record why an episode earns a place and where its argument stops being convincing.

## Start with Machine Learning Street Talk

The first collection covers a channel snapshot taken on **26 October 2026**:

- **269 uploads screened**, published between **9 April 2020 and 26 October 2026**.
- **131 high-priority episodes reviewed in depth**, published between **9 April 2020 and 9 October 2026**.
- **53 core contributions, 60 worthwhile additions, 14 selections of specific passages and 4 drops** after transcript review.

[Follow the learning path](collections/mlst/learning-path.md) · [Browse the episode reviews](collections/mlst/README.md) · [See the first filter](collections/mlst/screening.md)

The learning path starts with Wilson, Koolen and Bronstein for orientation, then follows nine questions from evaluation and learning structure through reasoning, action and open-ended discovery. It is a suggested conceptual order; the deeper branches are optional.

There is also an interactive report with search, filters, episode notes and the full methodology. Clone or download this repository and open `collections/mlst/reports/catalogue.html` in a browser. It works offline without installation. GitHub displays HTML as source; the Markdown links above are the easiest way to read online.

## How I select material

I use two filters. First, I examine the publisher’s summary, notes, chapter headings and references to decide whether an episode deserves a transcript review. Then I examine the full available transcript for its actual contribution: the objects and assumptions involved, the proposed mechanism, the evidence, the limits and what it adds to the rest of the collection.

A promising description earns a place in the reading queue. It does not earn a recommendation to watch. The [methodology](METHODOLOGY.md) explains both stages, including how I handle uncertainty and overlap.

## How these notes were made

I set the research objective and selection criteria and used AI agents to review transcripts and reconcile their findings. These are AI-assisted research notes and a study plan. They are not a claim that I personally watched every episode, checked every proof or completed the proposed experiments. Individual reviews record transcription problems, edition differences and the primary sources checked where applicable.

The repository contains the reviews, screening decisions, learning path, source records and publisher links. Downloaded transcripts, audio and complete publisher descriptions stay in my private research archive. [Attribution and source coverage](ATTRIBUTION.md) explains what is included.

## Beyond MLST

I’ll add other podcasts, lectures and courses when they address the same questions. Each collection will have its own scope, dates and review status. There is no target number of recommendations: another interview needs to add an idea, a useful disagreement or a worked example.

[Suggest a resource or correction](CONTRIBUTING.md). A useful suggestion names the question it helps answer and the passage, mechanism or result that makes it worth examining.

## Rebuild the MLST reports

Python 3.10 or newer is sufficient; there are no third-party dependencies or network calls.

```sh
python3 scripts/build_mlst.py
python3 scripts/build_mlst.py --check
```

The JSON files in `collections/mlst/` are the editable records. The script validates them and regenerates the Markdown views and interactive report. Templates for future collections are in `templates/`.
