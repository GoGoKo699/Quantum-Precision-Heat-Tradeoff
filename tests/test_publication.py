"""Source and numerical regression checks for reproducible public documents."""
from __future__ import annotations
import importlib.util
import math
from pathlib import Path
import re
import tempfile
import unittest
import zipfile
from qph.core import crossover as canonical_crossover

ROOT = Path(__file__).resolve().parents[1]

def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

plot = load_module("paper_plot", ROOT/"paper/Graph/generate_plots.py")
build = load_module("build_documents", ROOT/"scripts/build_documents.py")

class PublicationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tex = (ROOT/"paper"/(build.ARTICLE+".tex")).read_text()

    def test_single_tex_and_inline_inputs(self):
        self.assertEqual([p.name for p in (ROOT/"paper").rglob("*.tex")], [build.ARTICLE+".tex"])
        self.assertNotRegex(self.tex, r"\\(?:input|include|bibliography)\s*\{")
        self.assertEqual(self.tex.count(r"\begin{thebibliography}"), 1)
        self.assertEqual(self.tex.count(r"\begin{tikzpicture}"), 1)
        self.assertEqual(re.findall(r"\\includegraphics(?:\[[^]]*\])?\{([^}]+)\}",self.tex), ["Graph/crossover.pdf"])

    def test_approved_geometry(self):
        for line in [r"(.35,1.23)", r"(.35,-1.23)",
                     r"(90:1.05) arc[start angle=90,end angle=117,radius=1.05]",
                     r"(270:1.05) arc[start angle=270,end angle=243,radius=1.05]"]:
            self.assertIn(line, self.tex)
        self.assertNotIn("bend right=30", self.tex)
        self.assertNotIn("bend left=30", self.tex)

    def test_authors_and_no_date(self):
        self.assertLess(self.tex.index(r"\author{Ranyiliu Chen"), self.tex.index(r"\author{Ruge Lin"))
        for token in ["0000-0001-6060-6192", "0000-0002-9297-7622", "ranyiliu.chen@outlook.com",
                      "Guangzhou 511453", "Shenzhen 518045"]:
            self.assertIn(token, self.tex)
        self.assertNotIn(r"\today", self.tex)
        self.assertNotRegex(self.tex, r"\\date\{[^}]+\}")

    def test_citations_and_labels(self):
        citations = {x.strip() for g in re.findall(r"\\cite\{([^}]+)\}",self.tex) for x in g.split(',')}
        keys = set(re.findall(r"\]\{([^}]+)\}%\s*\\BibitemOpen",self.tex))
        self.assertTrue(citations.issubset(keys), citations-keys)
        labels = re.findall(r"\\label\{([^}]+)\}",self.tex)
        self.assertEqual(len(labels),len(set(labels)))
        refs = set(re.findall(r"\\(?:eqref|ref)\{([^}]+)\}",self.tex))
        self.assertTrue(refs.issubset(set(labels)), refs-set(labels))

    def test_plot_values_against_canonical_code(self):
        values = [0., 1e-12, .01, .1, 1., 100., 1e12, 1e100, 1e300]
        values += plot.sample_curve()[0]
        for r in values:
            with self.subTest(r=r):
                self.assertAlmostEqual(plot.crossover(r), canonical_crossover(r), delta=max(1e-300,1e-14*canonical_crossover(r)))
        self.assertAlmostEqual(plot.crossover(1), .1495103748978384, places=14)
        self.assertEqual(plot.crossover(0), 1.)

    def test_plot_domain_and_monotonicity(self):
        for r in [-1, math.inf, -math.inf, math.nan]:
            with self.assertRaises(ValueError): plot.crossover(r)
        r, y = plot.sample_curve()
        self.assertEqual((r[0],r[-1]), (1e-3,100.))
        self.assertTrue(all(0 < v < 1 for v in y))
        self.assertTrue(all(a > b for a,b in zip(y,y[1:])))

    def test_minimal_package_and_deterministic_plot(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp=Path(tmp)
            plot.draw(tmp/"one.pdf"); plot.draw(tmp/"two.pdf")
            self.assertEqual((tmp/"one.pdf").read_bytes(), (tmp/"two.pdf").read_bytes())
            self.assertEqual((tmp/"one.pdf").read_bytes(), (ROOT/"paper/Graph/crossover.pdf").read_bytes())
            build.package(tmp/"one.zip"); build.package(tmp/"two.zip")
            self.assertEqual((tmp/"one.zip").read_bytes(), (tmp/"two.zip").read_bytes())
            with zipfile.ZipFile(tmp/"one.zip") as z:
                self.assertEqual(set(z.namelist()),set(build.PACKAGE_FILES))

    def test_report_source_is_self_contained(self):
        src=(ROOT/"learning/report"/(build.REPORT+".tex")).read_text()
        self.assertNotRegex(src,r"\\(?:input|include|includegraphics|bibliography)\s*(?:\[[^]]*\])?\{")
        self.assertNotIn(r"\usepackage{fontspec}",src)
        self.assertEqual(len(re.findall(r"\\section\{",src)),5)
        self.assertEqual(len(re.findall(r"\\subsection\{",src)),16)
        self.assertNotRegex(src,r"\\cite\{")
        self.assertNotIn(r"\today",src)

if __name__ == "__main__": unittest.main()
