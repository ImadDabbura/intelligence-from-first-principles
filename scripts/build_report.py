#!/usr/bin/env python3
"""Build one offline research report from all registered source collections."""
import argparse
from collections import Counter
from datetime import date
import json
from pathlib import Path
import re
from urllib.parse import urlparse

import build_mlst

ROOT = Path(__file__).resolve().parents[1]
DECISIONS = {'core', 'worthwhile', 'selected_passages', 'drop'}
REVIEW_FIELDS = {'id', 'title', 'decision', 'coverage', 'confidence', 'thesis', 'contributions', 'mathematical_anatomy', 'evidence_and_limits', 'first_principles_value', 'watch_guidance', 'counterarguments', 'exercise', 'connections'}


def load(path):
    return json.loads(path.read_text(encoding='utf-8'))


def dump(value):
    return json.dumps(value, ensure_ascii=False, indent=2) + '\n'


def local(root, relative):
    path = (root / relative).resolve()
    assert path.is_relative_to(root.resolve()), f'Path outside repository: {relative}'
    assert path.exists(), f'Missing source record: {relative}'
    return path


def web(url):
    assert urlparse(url).scheme in {'http', 'https'} and urlparse(url).netloc, f'Invalid public URL: {url}'


def publication_range(entries):
    dates = []
    for item in entries:
        value = str(item.get('published_at') or '')[:10]
        if re.fullmatch(r'\d{4}-\d{2}-\d{2}', value):
            date.fromisoformat(value)
            dates.append(value)
    return {'first': min(dates) if dates else None, 'last': max(dates) if dates else None}


def build_shared(root=ROOT):
    registry = load(root / 'collections.json')
    assert registry and len({c['id'] for c in registry}) == len(registry), 'Missing or duplicate sources'
    episodes, collections, screened = [], [], []
    for collection in registry:
        cid = collection['id']
        assert re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', cid), cid
        for key in ['name', 'short_name', 'url', 'format', 'path', 'snapshot_date', 'coverage_note']:
            assert collection.get(key), f'{cid}: missing {key}'
        web(collection['url'])
        date.fromisoformat(collection['snapshot_date'])
        base = local(root, collection['path'])
        metadata = load(base / 'episodes.json')
        screen = load(base / 'screening.json')['episodes']
        ledger = load(base / 'sources.json')
        reviews = {p.stem: load(p) for p in (base / 'reviews').glob('*.json')}
        ids = {e['id'] for e in metadata}
        sources = {s['id']: s for s in ledger}
        assert len(ids) == len(metadata), f'{cid}: duplicate episode IDs'
        assert len(sources) == len(ledger), f'{cid}: duplicate source records'
        assert ids == set(reviews) == set(sources), f'{cid}: metadata, reviews and source records disagree'
        screen_ids = {e['id'] for e in screen}
        assert len(screen_ids) == len(screen), f'{cid}: duplicate screening IDs'
        assert ids <= screen_ids, f'{cid}: reviewed item missing from first filter'
        publisher = {k: collection[k] for k in ['id', 'name', 'short_name', 'url', 'format']}
        for e in metadata:
            i = e['id']
            assert re.fullmatch(r'[A-Za-z0-9_-]+', i), f'Unsafe episode ID: {i}'
            web(e['url'])
            r, s = reviews[i], sources[i]
            assert REVIEW_FIELDS <= r.keys() and r['id'] == i, f'{cid}:{i}: incomplete review'
            assert r['decision'] in DECISIONS, f'{cid}:{i}: unknown decision'
            assert re.fullmatch('[a-f0-9]{64}', s['sha256']), f'{cid}:{i}: missing source hash'
            assert s['words_in_selected_file'] > 0
            for resource in e.get('publisher_resources', []):
                web(resource['url'])
            episodes.append(dict(e, key=f'{cid}:{i}', publisher=publisher, review=r, source=s,
                                 decision=r['decision'], review_link=f"{collection['path']}/reviews/{i}.json"))
        for key in ['screening_link', 'scope_link']:
            if collection.get(key):
                local(root, collection[key])
        collections.append(dict(collection, screened=len(screen), reviewed=len(metadata),
                                inventory_range=publication_range(screen), reviewed_range=publication_range(metadata)))
        screened.extend(screen)

    by_key = {e['key']: e for e in episodes}
    assert len(by_key) == len(episodes), 'Duplicate global episode keys'
    roadmap = load(root / 'learning-path.json')
    refs = list(roadmap['start'])
    for module in roadmap['modules']:
        refs += module['anchors'] + module['deepen']
    for key in ['reconciled_findings', 'overlap_guidance']:
        for item in roadmap[key]:
            refs += item['episodes']
    assert set(refs) <= set(by_key), f'Unresolved learning-path references: {set(refs) - set(by_key)}'
    payload = {
        'schema_version': 1,
        'collections': collections,
        'summary': {'screened': len(screened), 'reviewed': len(episodes),
                    'decisions': dict(Counter(e['decision'] for e in episodes)),
                    'inventory_range': publication_range(screened), 'reviewed_range': publication_range(episodes)},
        'episodes': episodes, 'roadmap': roadmap,
    }
    template = (root / 'scripts/report-template.html').read_text(encoding='utf-8')
    assert template.count('__PAYLOAD__') == 1
    outputs = {
        root / 'report.json': dump(payload),
        root / 'index.html': template.replace('__PAYLOAD__', json.dumps(payload, ensure_ascii=False).replace('</', '<\\/')),
    }

    def episode_link(key):
        e = by_key[key]
        title = e['title'].replace('[', '\\[').replace(']', '\\]')
        path = e['review_link']
        markdown = str(Path(path).with_suffix('.md'))
        if (root / markdown).exists():
            path = markdown
        return f"[{title}]({path}) — {e['publisher']['name']} · {e['publisher']['format']}"

    content = '# My learning path\n\n' + roadmap['premise'] + '\n\n' + roadmap['how_to_use']
    content += '\n\n' + roadmap['orientation_note'] + '\n\n## Orientation\n\n'
    content += '\n'.join(f'{n}. {episode_link(k)}' for n, k in enumerate(roadmap['start'], 1)) + '\n\n'
    for module in roadmap['modules']:
        content += f"## {module['title']}\n\n{module['question']}\n\n{module['lesson']}\n\n### Starting episodes\n\n"
        content += '\n'.join('- ' + episode_link(k) for k in module['anchors']) + '\n\n### Deeper branches\n\n'
        content += '\n'.join('- ' + episode_link(k) for k in module['deepen'])
        content += f"\n\n### An experiment I could try\n\n{module['exercise']}\n\n"
    for title, key in [('Working conclusions', 'reconciled_findings'), ('Overlap between episodes', 'overlap_guidance')]:
        content += f'## {title}\n\n'
        for item in roadmap[key]:
            content += build_mlst.md({k: v for k, v in item.items() if k != 'episodes'}) + '\n\n'
            content += '\n'.join('- ' + episode_link(k) for k in item['episodes']) + '\n\n'
    content += '[Report](index.html) · [Methodology](README.md#methodology)\n'
    outputs[root / 'learning-path.md'] = content
    for filename, text in outputs.items():
        assert not re.search(r'/Users/|/private/(?:tmp|var)/|file://', text), f'Local path in {filename}'
    return outputs, payload


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Validate records and generated files without writing.')
    args = parser.parse_args()
    outputs, payload = build_shared()
    # Preserve the historical MLST Markdown views; they are not a second HTML report.
    if any(c['id'] == 'mlst' and c['path'] == 'collections/mlst' for c in payload['collections']):
        archived, _ = build_mlst.build()
        outputs.update(archived)
    stale = [str(p.relative_to(ROOT)) for p, content in outputs.items() if not p.exists() or p.read_text(encoding='utf-8') != content]
    if args.check and stale:
        raise SystemExit('Generated files need rebuilding:\n' + '\n'.join(stale))
    if not args.check:
        for p, content in outputs.items():
            p.write_text(content, encoding='utf-8')
    print(f"{'Checked' if args.check else 'Built'} one report: {len(payload['collections'])} sources, {len(payload['episodes'])} reviews.")


if __name__ == '__main__':
    main()
