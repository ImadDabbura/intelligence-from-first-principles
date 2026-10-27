#!/usr/bin/env python3
"""Build the public MLST collection from its portable JSON records, offline."""
import argparse
from collections import Counter
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
C = ROOT / 'collections/mlst'
DECISIONS = ('core', 'worthwhile', 'selected_passages', 'drop')


def read(name):
    return json.loads((C / name).read_text(encoding='utf-8'))


def json_text(value):
    return json.dumps(value, ensure_ascii=False, indent=2) + '\n'


def label(value):
    return str(value).replace('_', ' ').capitalize()


def md(value):
    """Render the heterogeneous review fields without losing their contents."""
    if value is None:
        return ''
    if isinstance(value, str):
        return value
    if isinstance(value, list):
        return '\n\n'.join('- ' + md(item).replace('\n', '\n  ') for item in value)
    if isinstance(value, dict):
        return '\n\n'.join(f'**{label(k)}:** {md(v)}' for k, v in value.items())
    return str(value)


def link(e, prefix='reviews/'):
    title = e['title'].replace('[', '\\[').replace(']', '\\]')
    return f"[{title}]({prefix}{e['id']}.md)"


def build():
    metadata = read('episodes.json')
    screening = read('screening.json')
    sources = read('sources.json')
    method = read('scope-and-method.json')
    path = read('learning-path.json')
    reviews = {p.stem: json.loads(p.read_text(encoding='utf-8')) for p in sorted((C / 'reviews').glob('*.json'))}
    ids = {e['id'] for e in metadata}
    source_ids = {s['id'] for s in sources}
    high = {e['id'] for e in screening['episodes'] if e['screening'].get('priority') == 'high' and e['screening']['decision'] == 'read_transcript'}
    assert len(metadata) == len(ids) == 131, 'Unexpected MLST snapshot size'
    assert ids == set(reviews) == source_ids == high, 'Review, source or high-priority membership differs'
    assert len(sources) == len(source_ids), 'Duplicate source records'
    assert len(screening['episodes']) == len({e['id'] for e in screening['episodes']}) == 269
    assert Counter(e['screening']['decision'] for e in screening['episodes']) == screening['statistics']['decisions']
    counts = Counter(r['decision'] for r in reviews.values())
    assert counts == method['stage_two']['decisions'], 'Review totals disagree with scope record'
    required = {'id', 'title', 'coverage', 'decision', 'confidence', 'thesis', 'contributions', 'mathematical_anatomy', 'evidence_and_limits', 'first_principles_value', 'watch_guidance', 'counterarguments', 'exercise', 'connections'}
    for i, r in reviews.items():
        assert required <= r.keys() and r['id'] == i, f'Incomplete review: {i}'
    for s in sources:
        assert re.fullmatch('[0-9a-f]{64}', s['sha256']), s['id']
        assert s['words_in_selected_file'] > 0
    for module in path['modules']:
        assert set(module['anchors'] + module['deepen']) <= ids
    assert set(path['start']) <= ids

    source_by_id = {s['id']: s for s in sources}
    episodes = []
    for e in metadata:
        r = reviews[e['id']]
        episodes.append(dict(e, review=r, decision=r['decision'], source=source_by_id[e['id']]))
    by_id = {e['id']: e for e in episodes}
    summary = {
        'scope': len(ids), 'reviewed': len(reviews), 'transcripts_available': len(sources),
        'reused_transcripts': sum(s['reused'] for s in sources),
        'recovered_transcripts': sum(not s['reused'] for s in sources),
        'local_asr_transcripts': sum(s['source_type'] == 'local_asr' for s in sources),
        'youtube_captions_recovered': sum(s['source_type'] == 'youtube_automatic_captions' for s in sources),
        'words_in_reviewed_sources': sum(s['words_in_selected_file'] for s in sources),
        'decisions': dict(counts),
    }
    assert summary['reused_transcripts'] == method['stage_two']['reused_transcripts']
    assert summary['recovered_transcripts'] == method['stage_two']['recovered_transcripts']
    payload = {
        'review_date': method['transcript_review_completed'],
        'profile': screening['methodology']['profile'],
        'methodology': method, 'summary': summary, 'episodes': episodes, 'roadmap': path,
        'public_edition': 'Raw transcripts and full publisher descriptions are not distributed.',
    }
    outputs = {}
    outputs[C / 'reports/review-catalogue.json'] = json_text(payload)
    template = (ROOT / 'scripts/mlst-report-template.html').read_text(encoding='utf-8')
    assert template.count('__PAYLOAD__') == 1
    outputs[C / 'reports/catalogue.html'] = template.replace('__PAYLOAD__', json.dumps(payload, ensure_ascii=False).replace('</', '<\\/'))

    for e in episodes:
        r, s = e['review'], e['source']
        content = f"# {e['title']}\n\n[Original episode]({e['url']}) · [All reviews](../README.md) · [Learning path](../learning-path.md)\n\n"
        content += f"Published: {str(e['published_at'])[:10]} · Decision: **{label(r['decision'])}** · Confidence: {r['confidence']}\n\n"
        for title, key in [('Central claim','thesis'), ('Ideas I want to keep','contributions'), ('Mathematical anatomy','mathematical_anatomy'), ('Evidence, limitations and corrections','evidence_and_limits'), ('Relevance to my research','first_principles_value'), ('My viewing plan','watch_guidance'), ('Objections and open questions','counterarguments'), ('An experiment I could try','exercise'), ('Connections in my notes','connections')]:
            content += f'## {title}\n\n{md(r[key])}\n\n'
        for key in ['external_sources', 'external_citations', 'citations']:
            if r.get(key):
                content += f'## Primary sources checked\n\n{md(r[key])}\n\n'
        content += f"## Source and coverage\n\n{md(r['coverage'])}\n\n"
        content += f"Source type: {label(s['source_type'])}. Reviewed text: {s['words_in_selected_file']:,} words.\n\n"
        content += f"Transcript file: `{s['source_file']}` (not distributed).\n\nSHA-256: `{s['sha256']}`.\n\n"
        content += '[Structured review](' + e['id'] + '.json) · [Source ledger](../sources.json)\n'
        outputs[C / 'reviews' / f"{e['id']}.md"] = content

    content = '# Machine Learning Street Talk\n\n'
    content += 'Snapshot: **26 October 2026**. The first filter covers **269 uploads published 9 April 2020–26 October 2026**. The detailed review covers **131 selected episodes published 9 April 2020–9 October 2026**.\n\n'
    content += '[Learning path](learning-path.md) · [First filter](screening.md) · [Methodology](../../METHODOLOGY.md) · [Scope record](scope-and-method.json)\n\n'
    content += 'These are my AI-assisted research notes and viewing priorities. The remaining 138 uploads are outside this transcript-review pass. The interactive report is `reports/catalogue.html`; download or clone the repository to open it in a browser.\n\n'
    for decision in DECISIONS:
        content += f'## {label(decision)} ({counts[decision]})\n\n'
        content += '\n'.join('- ' + link(e) for e in sorted(episodes, key=lambda e:e['title'].casefold()) if e['decision'] == decision) + '\n\n'
    outputs[C / 'README.md'] = content

    content = '# My learning path\n\n' + path['premise'] + '\n\n' + path['how_to_use'] + '\n\n'
    content += 'The sequence below is the recommended conceptual order. It is not a strict prerequisite chain or a ranking of speakers.\n\n## Orientation\n\n'
    content += '\n'.join(f'{n}. {link(by_id[i])}' for n, i in enumerate(path['start'], 1)) + '\n\n'
    for module in path['modules']:
        content += f"## {module['title']}\n\n{module['question']}\n\n{module['lesson']}\n\n### Starting episodes\n\n"
        content += '\n'.join('- ' + link(by_id[i]) for i in module['anchors']) + '\n\n### Deeper branches\n\n'
        content += '\n'.join('- ' + link(by_id[i]) for i in module['deepen']) + f"\n\n### An experiment I could try\n\n{module['exercise']}\n\n"
    for title, key in [('Working conclusions', 'reconciled_findings'), ('Overlap between episodes', 'overlap_guidance')]:
        content += f'## {title}\n\n'
        for item in path[key]:
            content += md({k: v for k, v in item.items() if k != 'episodes'}) + '\n\n'
            content += '\n'.join('- ' + link(by_id[i]) for i in item.get('episodes', [])) + '\n\n'
    content += '[All episode reviews](README.md) · [Methodology](../../METHODOLOGY.md)\n'
    outputs[C / 'learning-path.md'] = content

    content = '# First filter\n\n'
    content += 'Snapshot: **26 October 2026**. I screened publisher descriptions, summaries, notes and resources before selecting any new full transcripts for review. High and medium priority are reading decisions, not recommendations to watch.\n\n'
    content += '**269 Videos-tab uploads: 131 high priority, 115 medium priority, 15 skips and 8 with insufficient information.** Only the 131 high-priority uploads advanced to this transcript-review pass.\n\n'
    content += 'Two livestreams and 37 unmatched podcast-feed entries appear separately below. Feed entries may be alternate editions; they are not 37 additional verified videos. Full publisher text stays in the private archive; the structured public record retains resource links.\n\n[Detailed reviews](README.md) · [Structured screen and resource links](screening.json) · [Methodology](../../METHODOLOGY.md)\n\n'
    for title, group in [('Videos-tab uploads','episodes'), ('Separate livestreams','livestreams'), ('Supplementary feed entries','supplementary_feed_entries')]:
        content += f'## {title}\n\n'
        for e in screening[group]:
            s = e['screening']
            content += f"### {e['title']}\n\n[Original source]({e['url']}) · {e.get('published_at', 'Date unavailable')}\n\n"
            content += f"**{label(s['decision'])}**" + (f" · {s['priority']} priority" if s.get('priority') else '') + '\n\n'
            for title, key in [('Publisher promise','publisher_promise'), ('Reason for the decision','screening_reason'), ('Question for a transcript review','transcript_question'), ('Caveat','caveat')]:
                if s.get(key): content += f"**{title}:** {s[key]}\n\n"
            if e['id'] in ids: content += f"[Completed transcript review](reviews/{e['id']}.md)\n\n"
    outputs[C / 'screening.md'] = content

    for filename, text in outputs.items():
        assert not re.search(r'/Users/|/private/(?:tmp|var)/|file://', text), f'Local path in {filename}'
    return outputs, summary


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Validate data and require generated files to be current; write nothing.')
    args = parser.parse_args()
    outputs, summary = build()
    stale = [str(p.relative_to(ROOT)) for p, text in outputs.items() if not p.exists() or p.read_text(encoding='utf-8') != text]
    if args.check and stale:
        raise SystemExit('Generated files need rebuilding:\n' + '\n'.join(stale))
    if not args.check:
        for p, text in outputs.items():
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(text, encoding='utf-8')
    print(f"{'Checked' if args.check else 'Built'} {summary['reviewed']} reviews, 269 screening records and {len(outputs)} generated files.")


if __name__ == '__main__':
    main()
