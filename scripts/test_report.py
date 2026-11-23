"""Check that future sources join the one Library without ID collisions or code changes."""
import copy
from pathlib import Path
import shutil
import tempfile
import unittest

from build_report import ROOT, build_shared, dump, load


class MultipleSources(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        shutil.copytree(ROOT / 'collections', self.root / 'collections')
        shutil.copytree(ROOT / 'core', self.root / 'core')
        (self.root / 'scripts').mkdir()
        shutil.copy(ROOT / 'scripts/report-template.html', self.root / 'scripts/report-template.html')
        shutil.copy(ROOT / 'collections.json', self.root / 'collections.json')
        self.registry = load(self.root / 'collections.json')
        original = self.registry[0]
        screen = load(self.root / original['path'] / 'screening.json')['episodes']
        # Reuse a real high-priority entry under a second source: same local ID, different key.
        self.item = copy.deepcopy(next(e for e in screen if e['screening'].get('priority') == 'high'))
        self.item['published_at'] = '2030-01-02'  # Synthetic fixture, never published.
        self.id = self.item['id']
        fixture = self.root / 'collections/test-lectures'
        fixture.mkdir(parents=True)
        (fixture / 'episodes.json').write_text('[]\n')
        (fixture / 'sources.json').write_text('[]\n')
        (fixture / 'screening.json').write_text(dump({'episodes': [self.item]}))
        self.registry.append({'id': 'test-lectures', 'name': 'Test lecture series', 'short_name': 'Test',
                              'url': 'https://example.org/lectures', 'format': 'Lecture',
                              'path': 'collections/test-lectures', 'snapshot_date': '2030-01-03',
                              'coverage_note': 'Synthetic test fixture.'})
        (self.root / 'collections.json').write_text(dump(self.registry))

    def test_source_addition_shares_the_library(self):
        before = build_shared(ROOT)[1]
        links = load(self.root / 'core/links.json')
        links['test-lectures:' + self.id] = [{'id': 'L1', 'relation': 'EXTENSION'}]
        (self.root / 'core/links.json').write_text(dump(links))
        outputs, data = build_shared(self.root)
        self.assertEqual(len(data['backlog']), len(before['backlog']) + 1)
        self.assertEqual(data['summary']['inventory_range']['last'], '2030-01-02')
        copies = [b for b in data['backlog'] if b['key'].split(':', 1)[1] == self.id]
        self.assertEqual(len(copies), 2)
        self.assertEqual(len({b['key'] for b in copies}), 2)
        self.assertEqual(copies[-1]['format'], 'Lecture')
        self.assertEqual(copies[-1]['core'], [{'id': 'L1', 'relation': 'EXTENSION'}])
        self.assertEqual(data['collections'][0]['snapshot_date'], before['collections'][0]['snapshot_date'])
        self.assertEqual({p.suffix for p in outputs}, {'.html', '.json'})
        self.assertEqual(sum(p.suffix == '.html' for p in outputs), 1)
        page = next(text for p, text in outputs.items() if p.suffix == '.html')
        self.assertNotIn('"episodes"', page)

    def test_duplicate_source_is_rejected(self):
        self.registry.append(self.registry[0])
        (self.root / 'collections.json').write_text(dump(self.registry))
        with self.assertRaisesRegex(AssertionError, 'duplicate sources'):
            build_shared(self.root)

    def test_broken_core_link_is_rejected(self):
        links = load(self.root / 'core/links.json')
        links['missing:item'] = [{'id': 'L1', 'relation': 'EXTENSION'}]
        (self.root / 'core/links.json').write_text(dump(links))
        with self.assertRaisesRegex(AssertionError, 'not in the Library'):
            build_shared(self.root)

    def test_unknown_core_idea_is_rejected(self):
        links = load(self.root / 'core/links.json')
        key = next(iter(links))
        links[key] = [{'id': 'L999', 'relation': 'EXTENSION'}]
        (self.root / 'core/links.json').write_text(dump(links))
        with self.assertRaisesRegex(AssertionError, 'unknown core id'):
            build_shared(self.root)


if __name__ == '__main__':
    unittest.main()
