#!/usr/bin/env python3
"""Build the MLST collection's Markdown views from its screening record, offline."""
import argparse
from collections import Counter
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
C = ROOT / 'collections/mlst'


def read(name):
    return json.loads((C / name).read_text(encoding='utf-8'))


def label(value):
    return str(value).replace('_', ' ').capitalize()


def title(e):
    return e['title'].replace('[', '\\[').replace(']', '\\]')


def build():
    screening = read('screening.json')
    episodes = screening['episodes']
    assert len(episodes) == len({e['id'] for e in episodes}) == 269, 'Unexpected MLST snapshot size'
    decisions = Counter(e['screening']['decision'] for e in episodes)
    assert decisions == screening['statistics']['decisions'], 'Decision totals disagree with the screening record'
    high = [e for e in episodes if e['screening'].get('priority') == 'high']
    medium = sum(e['screening'].get('priority') == 'medium' for e in episodes)
    assert all(e['screening']['decision'] == 'read_transcript' for e in high)
    counts = (f"**269 Videos-tab uploads: {len(high)} high priority, {medium} medium priority, "
              f"{decisions['skip']} skips and {decisions['insufficient_information']} with insufficient information.**")
    outputs = {}

    content = '# Machine Learning Street Talk\n\n'
    content += 'Snapshot: **26 October 2026**. The first filter covers **269 uploads published 9 April 2020–26 October 2026**.\n\n'
    content += '[First filter](screening.md) · [Methodology](../../README.md#methodology) · [Scope record](scope-and-method.json) · [Library](../../index.html)\n\n'
    content += counts + ' The high-priority uploads are in the Library, in the same form as every other source.\n\n'
    content += f'## In the Library ({len(high)})\n\n'
    content += '\n'.join(f"- [{title(e)}]({e['url']})" for e in sorted(high, key=lambda e: e['title'].casefold())) + '\n'
    outputs[C / 'README.md'] = content

    content = '# First filter\n\n'
    content += 'Snapshot: **26 October 2026**. I screened publisher descriptions, summaries, notes and resources. High and medium priority are reading decisions, not recommendations to watch.\n\n'
    content += counts + ' The high-priority uploads are in the Library.\n\n'
    content += 'Two livestreams and 37 unmatched podcast-feed entries appear separately below. Feed entries may be alternate editions; they are not 37 additional verified videos. Full publisher text stays in the private research archive.\n\n'
    for heading, group in [('Videos-tab uploads', 'episodes'), ('Separate livestreams', 'livestreams'), ('Supplementary feed entries', 'supplementary_feed_entries')]:
        content += f'## {heading}\n\n'
        for e in screening[group]:
            s = e['screening']
            content += f"### {e['title']}\n\n[Original source]({e['url']}) · {e.get('published_at', 'Date unavailable')}\n\n"
            content += f"**{label(s['decision'])}**" + (f" · {s['priority']} priority" if s.get('priority') else '') + '\n\n'
            for name, key in [('Publisher promise', 'publisher_promise'), ('Reason for the decision', 'screening_reason'), ('Question to settle', 'transcript_question'), ('Caveat', 'caveat')]:
                if s.get(key):
                    content += f"**{name}:** {s[key]}\n\n"
    outputs[C / 'screening.md'] = content

    for filename, text in outputs.items():
        assert not re.search(r'/Users/|/private/(?:tmp|var)/|file://', text), f'Local path in {filename}'
    return outputs, {'screened': len(episodes), 'high': len(high)}


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
            p.write_text(text, encoding='utf-8')
    print(f"{'Checked' if args.check else 'Built'} {summary['screened']} screening records ({summary['high']} in the Library) and {len(outputs)} generated files.")


if __name__ == '__main__':
    main()
