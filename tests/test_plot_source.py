"""Retained Python plot generator agrees with the canonical limiting law."""
from __future__ import annotations
import importlib.util
from pathlib import Path
import tempfile
import unittest

from qph.core import crossover as canonical_crossover

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "verification/Graph/generate_plots.py"
REQUIREMENTS = ROOT / "verification/Graph/requirements.txt"

spec = importlib.util.spec_from_file_location("retained_plot_generator", SOURCE)
plot = importlib.util.module_from_spec(spec)
spec.loader.exec_module(plot)

class PlotSourceTests(unittest.TestCase):
    def test_retained_dependencies(self):
        self.assertEqual(REQUIREMENTS.read_text().strip(), "matplotlib==3.10.8")

    def test_matches_scientific_function(self):
        for ratio in (0.0, 1e-12, .001, .01, .1, 1.0, 10.0, 100.0, 1e8):
            with self.subTest(ratio=ratio):
                self.assertAlmostEqual(plot.crossover(ratio), canonical_crossover(ratio), delta=1e-14)
        r,values=plot.sample_curve()
        self.assertEqual((r[0],r[-1]),(.001,100.0))
        self.assertTrue(all(x > y for x,y in zip(values,values[1:])))

    def test_generates_vector_pdf_directly(self):
        with tempfile.TemporaryDirectory() as d:
            one=Path(d)/"one.pdf"
            two=Path(d)/"two.pdf"
            plot.draw(one)
            plot.draw(two)
            self.assertTrue(one.read_bytes().startswith(b"%PDF-"))
            self.assertEqual(one.read_bytes(),two.read_bytes())
