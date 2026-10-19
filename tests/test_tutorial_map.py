"""Check the common understanding map without embedding personal coaching."""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
TUTORIAL = ROOT / 'learning'


def milestone_sections(text):
    matches = list(re.finditer(r'^### (M\d{2}) — (.+)$', text, re.M))
    records = []
    for index, match in enumerate(matches):
        stop = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        body = re.split(r'^## ', text[match.end():stop], maxsplit=1, flags=re.M)[0]
        records.append((match[1], match[2], body))
    return records


class TutorialMapTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = (TUTORIAL/'MILESTONES.md').read_text(encoding='utf-8')
        cls.records = milestone_sections(cls.text)

    def test_exact_stable_ids_and_anchors(self):
        expected = [f'M{i:02d}' for i in range(1, 31)]
        self.assertEqual([record[0] for record in self.records], expected)
        self.assertEqual(re.findall(r'<a id="(m\d{2})"></a>', self.text),
                         [value.lower() for value in expected])
        self.assertEqual(len({record[1] for record in self.records}), 30)

    def test_phase_allocation(self):
        parts = re.split(r'^## Phase (?:I|II) — .+$', self.text, flags=re.M)
        self.assertEqual(len(parts), 3)
        self.assertEqual([r[0] for r in milestone_sections(parts[1])], [f'M{i:02d}' for i in range(1, 15)])
        self.assertEqual([r[0] for r in milestone_sections(parts[2])], [f'M{i:02d}' for i in range(15, 31)])

    def test_understanding_records(self):
        fields = ('Central question', 'Understanding target', 'Depends on', 'Story role', 'Conceptual connection', 'Sources')
        for identifier, _, body in self.records:
            with self.subTest(milestone=identifier):
                for field in fields:
                    self.assertEqual(body.count(f'**{field}:**'), 1)
                self.assertRegex(re.search(r'\*\*Sources:\*\* (.+)', body)[1], r'\[[^\]]+\]\([^)]+\)')

    def test_dependencies_are_backward_and_connected(self):
        used = set()
        for identifier, _, body in self.records:
            number = int(identifier[1:])
            dependencies = re.search(r'\*\*Depends on:\*\* (.+)', body)[1]
            links = re.findall(r'\[(M\d{2})\]\(#(m\d{2})\)', dependencies)
            self.assertEqual(len(links), len(set(links)))
            if number > 1:
                self.assertTrue(links)
            for previous, anchor in links:
                self.assertEqual(previous.lower(), anchor)
                self.assertTrue(1 <= int(previous[1:]) < number)
                used.add(previous)
        self.assertEqual(used, {f'M{i:02d}' for i in range(1, 30)})

    def test_phase_endpoints_are_syntheses(self):
        for identifier in ('M14', 'M30'):
            self.assertIn('Synthesis', next(r[1] for r in self.records if r[0] == identifier))

    def test_map_and_anchor_are_reachable(self):
        for name in ('README.md', 'llms.txt', 'AGENTS.md', 'learning/README.md'):
            self.assertIn('MILESTONES.md', (ROOT/name).read_text())
        bridge = (TUTORIAL/'SCHUMACHER_WESTMORELAND_BRIDGE.md').read_text()
        self.assertIn('Benjamin Schumacher and Michael D. Westmoreland', bridge)
        self.assertIn('Chapter 19', bridge)
        self.assertIn('beyond-textbook', bridge)

    def test_public_map_is_reader_independent(self):
        self.assertFalse((TUTORIAL/'COACHING.md').exists())
        for token in ('**Learning block:**', 'Revise → Learn → Test', 'failed challenge', '60 challenge questions'):
            self.assertNotIn(token, self.text)
        for name in ('README.md', 'llms.txt', 'learning/README.md', 'learning/MILESTONES.md'):
            self.assertNotIn('COACHING.md', (ROOT/name).read_text())


if __name__ == '__main__':
    unittest.main()
