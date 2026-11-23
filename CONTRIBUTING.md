# Suggestions and corrections

This is a personal research collection, but other readers can help make the reasoning better.

## Suggest a podcast, lecture or paper

Open an issue with the original link, speaker, publication date if known, and the question it helps answer. Identify the mechanism, experiment or argument that makes it useful. Publisher notes and relevant timestamps help with the filter.

Please explain what it adds to the existing collection. A famous guest or an interesting title alone does not establish that contribution.

## Correct an entry

Link to the entry or core idea and the specific statement. Include a timestamp or primary source and explain the correction. Disagreements about the research objective are welcome too; distinguish them from a factual error.

## Add a source

1. Create `collections/<source-id>/` and record its scope, dates and known gaps.
2. Add the source to `collections.json` with its name, original URL, format, snapshot date and data directory.
3. Follow the [data format](templates/data-format.md) for the screening record.
4. Tie its items to core ideas in `core/links.json` where they serve one.
5. Run `python3 scripts/build_report.py` and `python3 scripts/build_report.py --check`. The source appears in the Library and its filter.

The [README methodology](README.md#methodology) applies across sources. Each source keeps its own coverage boundaries; a new source does not change the dates of an older snapshot.

## Edit a record

Edit the structured records, not the generated Markdown or HTML, then run:

```sh
python3 scripts/build_report.py
python3 scripts/build_report.py --check
```

Keep downloaded transcripts, full publisher notes, audio, credentials and machine-specific paths out of commits.
