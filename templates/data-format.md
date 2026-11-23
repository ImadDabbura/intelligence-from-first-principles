# Adding a source to the Library

The Library reads all entries in the root `collections.json`. Register a podcast, lecture series or course there; there is no per-source HTML template.

## Source registry

Each entry has:

- `id`: a stable lowercase identifier, such as `mlst`; use letters, numbers and hyphens.
- `name`, `short_name`, `url`: the publisher or series name and original public URL.
- `format`: a reader-facing label, such as Podcast, Lecture or Course.
- `path`: its repository-relative data directory, normally `collections/<id>`.
- `snapshot_date`: the inventory date in `YYYY-MM-DD` form.
- `coverage_note`: what was included, excluded or left unresolved.
- `screening_link`, `scope_link`: optional paths to the collection’s first-filter view and detailed scope record.

Snapshot dates belong to individual sources. Publication ranges and counts are computed from their records, then combined for the report header.

## Records in each source directory

`screening.json` contains an `episodes` array for the inventory. Every entry has an `id`, original title, URL and publication date when known, plus a `screening` object recording its decision, priority, rationale (`screening_reason`), the question a closer look should settle (`transcript_question`) and any `caveat`. Omit an unknown date or set it to null; do not invent one. IDs may contain letters, numbers, underscores and hyphens. Entries with `priority: "high"` appear in the Library. Supplementary or alternate editions can be recorded separately, as in MLST; they do not enter the principal inventory count.

`episodes.json` and `sources.json` are empty arrays (`[]`). They are reserved for detailed reviews and their source ledger, which this repository does not currently hold.

## Core ideas

`core/core.json` holds the core ideas. `core/links.json` maps a Library item, written `<source-id>:<item-id>`, to the ideas it serves, each with a relation: `ROOT`, `ORIGINATOR`, `TEACHING` or `EXTENSION`. Two sources can use the same local ID without colliding. The build rejects a link to an item that is not in the Library or to an unknown idea.

## Build and check

```sh
python3 scripts/build_report.py
python3 scripts/build_report.py --check
python3 scripts/test_report.py
node scripts/check_report.cjs
```

The build uses Python 3.10 or newer, with no third-party packages or network access. The final optional command uses Node.js to check the page’s interactions. The outputs are `index.html` and `report.json` at the repository root. The build also maintains MLST’s Markdown views of its first filter.
