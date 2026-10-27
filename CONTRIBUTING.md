# Suggestions and corrections

This is a personal research collection, but other readers can help make the reasoning better.

## Suggest a podcast or lecture

Open an issue with the original link, speaker, publication date if known, and the question it helps answer. Identify the mechanism, experiment or argument that makes it useful. Publisher notes and relevant timestamps help with the first filter.

Please explain what it adds to the existing collection. A famous guest or an interesting title alone does not establish that contribution. A suggestion enters the metadata screen before it becomes a viewing recommendation.

## Correct a review

Link to the review and the specific statement. Include a timestamp or primary source, explain the correction and say whether it changes the viewing decision. Mention the edition when podcast and video timestamps differ.

Disagreements about the research objective are welcome too; distinguish them from a factual error in the notes.

## Add a collection

1. Create `collections/<collection-name>/` and start with `templates/collection.md`.
2. State the source, snapshot date, publication interval, inclusion rules and exclusions.
3. Record the first-stage decisions before selecting transcripts for the second stage.
4. Use `templates/episode-review.md` for new reviews. Record source coverage and AI assistance accurately.
5. Reconcile overlap and propose a learning order. Record unresolved issues instead of silently filling gaps.
6. Link the collection from the root README when it is ready to read.

The MLST JSON schema preserves the original audit. Future collections can begin as Markdown using these templates; the MLST build script does not automatically ingest a new collection.

## Edit the MLST collection

Edit the structured records, not the generated Markdown or HTML. Episode reviews live in `collections/mlst/reviews/*.json`; metadata, the first-stage screen, source records and learning path live beside that directory. Then run:

```sh
python3 scripts/build_mlst.py
python3 scripts/build_mlst.py --check
```

Keep downloaded transcripts, full publisher notes, audio, credentials and machine-specific paths out of commits. The public records retain source hashes, edition caveats and original links; raw working material belongs in a local ignored directory.
