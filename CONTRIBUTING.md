# Suggestions and corrections

This is a personal research collection, but other readers can help make the reasoning better.

## Suggest a podcast or lecture

Open an issue with the original link, speaker, publication date if known, and the question it helps answer. Identify the mechanism, experiment or argument that makes it useful. Publisher notes and relevant timestamps help with the first filter.

Please explain what it adds to the existing collection. A famous guest or an interesting title alone does not establish that contribution. A suggestion enters the metadata screen before it becomes a viewing recommendation.

## Correct a review

Link to the review and the specific statement. Include a timestamp or primary source, explain the correction and say whether it changes the viewing decision. Mention the edition when podcast and video timestamps differ.

Disagreements about the research objective are welcome too; distinguish them from a factual error in the notes.

## Add a source

1. Create `collections/<source-id>/` and record its scope, dates and known gaps.
2. Add the source to `collections.json` with its name, original URL, format, snapshot date and data directory.
3. Follow the [data format](templates/data-format.md) for screening, episode metadata, reviews and evidence records. Keep the first filter separate from completed transcript reviews.
4. Add useful episodes to the root `learning-path.json` using `<source-id>:<episode-id>` references. Compare them with existing entries across sources.
5. Run `python3 scripts/build_report.py` and `python3 scripts/build_report.py --check`. The source appears in the existing report and filter.

The [README methodology](README.md#methodology) applies across sources. Each source keeps its own coverage boundaries and evidence; a new source does not change the dates of an older snapshot.

## Edit the MLST collection

Edit the structured records, not the generated Markdown or HTML. Episode reviews live in `collections/mlst/reviews/*.json`; metadata, the first-stage screen and source records live beside that directory. The cross-source learning path lives at the repository root; the collection’s path preserves its original MLST study sequence. Then run:

```sh
python3 scripts/build_report.py
python3 scripts/build_report.py --check
```

Keep downloaded transcripts, full publisher notes, audio, credentials and machine-specific paths out of commits. The public records retain source hashes, edition caveats and original links; raw working material belongs in a local ignored directory.
