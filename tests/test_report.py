"""The public repository retains the anonymous explanatory report, not a paper."""
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "learning/report/Quantum_Precision_Heat_Tradeoff_Report.tex"
PDF = ROOT / "learning/report/Quantum_Precision_Heat_Tradeoff_Report.pdf"

class ReportTests(unittest.TestCase):
    def test_report_structure_and_identity(self):
        text=SRC.read_text()
        self.assertEqual(text.count(r"\section{"),5)
        self.assertEqual(text.count(r"\subsection{"),16)
        for secret in ("Ranyiliu Chen","Ruge Lin","ranyiliu.chen@outlook.com","0000-0001-6060-6192","0000-0002-9297-7622"):
            self.assertNotIn(secret,text)
        self.assertNotRegex(text,r"\\(?:author|affiliation|email|orcidlink)\b")
        self.assertIn("pdfauthor={}",text)
        self.assertTrue(PDF.read_bytes().startswith(b"%PDF-"))

    def test_no_paper_or_manuscript_material_in_current_tree(self):
        self.assertFalse((ROOT/"paper").exists())
        for relative in ("scripts/verify_manuscript.py", "scripts/build_documents.py", "tests/test_publication.py"):
            self.assertFalse((ROOT/relative).exists(), relative)
        self.assertNotIn("paper/", (ROOT/"README.md").read_text())
        self.assertIn("learning/report/Quantum_Precision_Heat_Tradeoff_Report.pdf", (ROOT/"README.md").read_text())
