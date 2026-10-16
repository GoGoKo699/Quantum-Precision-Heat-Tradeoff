"""Structural regression checks for the common tutorial map and entry points.

These checks do not grade learners or verify the mathematical research. The
repository's existing documentation checker validates local links and math.
"""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
TUTORIAL = ROOT / "docs" / "tutorial"


def milestone_sections(text):
    """Return numbered headings and their records, excluding the closing note."""
    matches = list(re.finditer(r"^### (M\d{2}) — (.+)$", text, re.MULTILINE))
    result = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        body = re.split(r"^## ", text[match.end():end], maxsplit=1,
                        flags=re.MULTILINE)[0]
        result.append((match.group(1), match.group(2), body))
    return result


class TutorialMapTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = (TUTORIAL / "MILESTONES.md").read_text(encoding="utf-8")
        cls.records = milestone_sections(cls.text)
        cls.protocol = (TUTORIAL / "COACHING.md").read_text(encoding="utf-8")

    def test_exact_stable_ids_and_anchors(self):
        expected = [f"M{i:02d}" for i in range(1, 31)]
        self.assertEqual([record[0] for record in self.records], expected)
        anchors = re.findall(r'<a id="(m\d{2})"></a>', self.text)
        self.assertEqual(anchors, [item.lower() for item in expected])
        self.assertEqual(len({record[1] for record in self.records}), 30)

    def test_phase_allocation(self):
        parts = re.split(r"^## Phase (?:I|II) — .+$", self.text,
                         flags=re.MULTILINE)
        self.assertEqual(len(parts), 3)
        self.assertEqual([item[0] for item in milestone_sections(parts[1])],
                         [f"M{i:02d}" for i in range(1, 15)])
        self.assertEqual([item[0] for item in milestone_sections(parts[2])],
                         [f"M{i:02d}" for i in range(15, 31)])

    def test_each_milestone_is_an_understanding_record(self):
        fields = ("Central question", "Understanding target", "Depends on",
                  "Story role", "Sources", "Learning block")
        for identifier, _, body in self.records:
            with self.subTest(milestone=identifier):
                for field in fields:
                    self.assertEqual(body.count(f"**{field}:**"), 1)
                sources = re.search(r"\*\*Sources:\*\* (.+)", body)
                self.assertIsNotNone(sources)
                self.assertRegex(sources.group(1), r"\[[^\]]+\]\([^)]+\)")
                self.assertRegex(body, r"\*\*Learning block:\*\* [1-3] rounds?\.")

    def test_dependencies_are_backward_and_connected(self):
        used = set()
        for identifier, _, body in self.records:
            number = int(identifier[1:])
            dependencies = re.search(r"\*\*Depends on:\*\* (.+)", body).group(1)
            links = re.findall(r"\[(M\d{2})\]\(#(m\d{2})\)", dependencies)
            with self.subTest(milestone=identifier):
                self.assertEqual(len(links), len({item[0] for item in links}))
                if number > 1:
                    self.assertTrue(links)
                for previous, anchor in links:
                    self.assertEqual(previous.lower(), anchor)
                    self.assertGreaterEqual(int(previous[1:]), 1)
                    self.assertLess(int(previous[1:]), number)
                    used.add(previous)
        # Every nonfinal milestone advances a later target, not an isolated pad.
        self.assertEqual(used, {f"M{i:02d}" for i in range(1, 30)})

    def test_phase_endpoints_are_syntheses(self):
        for identifier in ("M14", "M30"):
            record = next(item for item in self.records if item[0] == identifier)
            self.assertIn("Synthesis", record[1])

    def test_map_and_protocol_are_reachable(self):
        for path in (ROOT / "README.md", ROOT / "llms.txt", ROOT / "AGENTS.md",
                     TUTORIAL / "README.md"):
            with self.subTest(path=path.name):
                text = path.read_text(encoding="utf-8")
                self.assertIn("MILESTONES.md", text)
                self.assertIn("COACHING.md", text)

    def test_retry_table_and_completion_contract(self):
        rows = re.findall(r"^\| (0|1|2|3|4 or more) \| (\d+) \| All correct \|$",
                          self.protocol, re.MULTILINE)
        self.assertEqual(rows, [("0", "2"), ("1", "3"), ("2", "4"),
                                ("3", "5"), ("4 or more", "6")])
        self.assertIn("min(2 + f, 6)", self.protocol)
        self.assertIn("**all 30 milestones**", self.protocol)
        self.assertIn("**60 challenge questions**", self.protocol)
        self.assertIn("**immediately after each learning-test answer**", self.protocol)
        self.assertIn("**does not increase the next challenge size**", self.protocol)


if __name__ == "__main__":
    unittest.main()
