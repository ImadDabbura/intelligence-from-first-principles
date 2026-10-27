"""Check that future sources share the report without ID collisions or code changes."""
import copy
import json
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
        (self.root / 'scripts').mkdir()
        shutil.copy(ROOT / 'scripts/report-template.html', self.root / 'scripts/report-template.html')
        for name in ['collections.json', 'learning-path.json']:
            shutil.copy(ROOT / name, self.root / name)
        self.registry = load(self.root / 'collections.json')
        original = self.registry[0]
        source_dir = self.root / original['path']
        self.episode = copy.deepcopy(load(source_dir / 'episodes.json')[0])
        self.episode['published_at'] = '2030-01-02'  # Synthetic fixture, never published.
        self.id = self.episode['id']
        fixture = self.root / 'collections/test-lectures'
        (fixture / 'reviews').mkdir(parents=True)
        (fixture / 'episodes.json').write_text(dump([self.episode]))
        review = load(source_dir / 'reviews' / f'{self.id}.json')
        (fixture / 'reviews' / f'{self.id}.json').write_text(dump(review))
        source = next(s for s in load(source_dir / 'sources.json') if s['id'] == self.id)
        (fixture / 'sources.json').write_text(dump([source]))
        (fixture / 'screening.json').write_text(dump({'episodes': [self.episode]}))
        self.registry.append({'id': 'test-lectures', 'name': 'Test lecture series', 'short_name': 'Test',
                              'url': 'https://example.org/lectures', 'format': 'Lecture',
                              'path': 'collections/test-lectures', 'snapshot_date': '2030-01-03',
                              'coverage_note': 'Synthetic test fixture.'})
        (self.root / 'collections.json').write_text(dump(self.registry))

    def test_source_addition_and_shared_path(self):
        before = build_shared(ROOT)[1]
        roadmap = load(self.root / 'learning-path.json')
        roadmap['start'].append('test-lectures:' + self.id)
        (self.root / 'learning-path.json').write_text(dump(roadmap))
        outputs, data = build_shared(self.root)
        self.assertEqual(len(data['episodes']), len(before['episodes']) + 1)
        self.assertEqual(data['summary']['reviewed_range']['last'], '2030-01-02')
        copies = [e for e in data['episodes'] if e['id'] == self.id]
        self.assertEqual(len(copies), 2)
        self.assertEqual(len({e['key'] for e in copies}), 2)
        self.assertEqual(copies[-1]['publisher']['format'], 'Lecture')
        self.assertEqual(copies[0]['review'], copies[-1]['review'])
        self.assertEqual(data['collections'][0]['snapshot_date'], before['collections'][0]['snapshot_date'])
        self.assertEqual({p.suffix for p in outputs}, {'.html', '.json', '.md'})
        self.assertEqual(sum(p.suffix == '.html' for p in outputs), 1)

    def test_duplicate_source_is_rejected(self):
        self.registry.append(self.registry[0])
        (self.root / 'collections.json').write_text(dump(self.registry))
        with self.assertRaisesRegex(AssertionError, 'duplicate sources'):
            build_shared(self.root)

    def test_broken_learning_reference_is_rejected(self):
        path = load(self.root / 'learning-path.json')
        path['start'].append('missing:episode')
        (self.root / 'learning-path.json').write_text(dump(path))
        with self.assertRaisesRegex(AssertionError, 'Unresolved learning-path'):
            build_shared(self.root)


if __name__ == '__main__':
    unittest.main()
