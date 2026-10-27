# Adding a source to the shared report

The report reads all entries in the root `collections.json`. Register a podcast, lecture series or course there; there is no per-source HTML template.

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

`episodes.json` is an array of **completed transcript-review entries**. Each has a stable `id`, `title`, original `url`, ISO `published_at` date, `duration_seconds` and optional `publisher_resources` containing objects with `url` and `category`. Omit an unknown date or set it to null; do not invent one. IDs may contain letters, numbers, underscores and hyphens.

`screening.json` contains an `episodes` array for the first-stage inventory. Every entry has an `id`, original title, URL and publication date when known, plus a `screening` object recording its decision, priority, rationale and unresolved transcript question. The inventory includes deferred and rejected items as well as those reviewed in depth. Supplementary or alternate editions can be recorded separately, as in MLST; they do not enter the principal inventory count.

`reviews/<episode-id>.json` contains the detailed assessment. Required fields are `id`, `title`, `decision`, `coverage`, `confidence`, `thesis`, `contributions`, `mathematical_anatomy`, `evidence_and_limits`, `first_principles_value`, `watch_guidance`, `counterarguments`, `exercise` and `connections`. Decisions are `core`, `worthwhile`, `selected_passages` or `drop`. Optional `external_sources`, `external_citations` or `citations` record actual primary-source checks. Use the existing MLST JSON records for field shapes and the [review template](episode-review.md) for the intended substance.

`sources.json` is a transcript evidence ledger, distinct from the publisher directory. Each reviewed episode has one record with the same `id`, a `source_type`, `source_notes`, `words_in_selected_file`, a 64-character SHA-256 `sha256`, and the reviewed edition’s filename in `source_file`. Do not commit the transcript itself or an absolute local path.

The episode metadata, review filenames and evidence ledger must have matching IDs. All reviewed IDs must also exist in the first-stage inventory. A pending transcript belongs in the screening queue; it is not counted as a completed review.

## One learning path

The root `learning-path.json` holds the shared sequence, modules, conclusions and overlap notes. References use `<source-id>:<episode-id>`, so two publishers can use the same local episode ID without colliding. Add an episode to the shared sequence when its role is clear; registration alone makes it searchable in the report.

MLST’s own `learning-path.json` preserves its original collection-specific sequence. The root path is the one displayed in the shared report.

## Build and check

```sh
python3 scripts/build_report.py
python3 scripts/build_report.py --check
python3 scripts/test_report.py
node scripts/check_report.cjs
```

The build uses Python 3.10 or newer, with no third-party packages or network access. The final optional command uses Node.js to check report interactions. The outputs are `index.html`, `report.json` and `learning-path.md` at the repository root. The build also maintains MLST’s existing Markdown archive; a new source does not require a second report generator.
