"""Regression tests for private-package checks and the public report build target."""
from __future__ import annotations
import importlib.util
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import zipfile
import warnings

ROOT = Path(__file__).resolve().parents[1]


def load(name: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / (name + ".py"))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


package = load("check_overleaf_package")
report = load("check_report")
SAMPLE = r"""\documentclass{article}
\usepackage{graphicx,tikz}
\begin{document}
\begin{tikzpicture}\draw (0,0)--(1,1);\end{tikzpicture}
\includegraphics{Graph/crossover.pdf}
\begin{thebibliography}{1}\bibitem{example} Example.\end{thebibliography}
\end{document}
"""


class DeliveryChecks(unittest.TestCase):
    def make_zip(self, folder: Path, source: str = SAMPLE, extra: bool = False) -> Path:
        path = folder / "source.zip"
        with zipfile.ZipFile(path, "w") as archive:
            archive.writestr(package.TEX, source)
            archive.writestr(package.GRAPH, b"%PDF-1.7\n%%EOF\n")
            if extra:
                archive.writestr("Graph/generate_plots.py", "pass\n")
        return path

    def test_minimal_archive(self):
        with tempfile.TemporaryDirectory() as directory:
            source, _ = package.read_package(self.make_zip(Path(directory)))
            self.assertEqual(source, SAMPLE)

    def test_reject_packaged_python(self):
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaises(ValueError):
                package.read_package(self.make_zip(Path(directory), extra=True))

    def test_reject_external_input_or_unresolved_reference(self):
        for addition in (r"\input{other.tex}", r"\eqref{missing}", r"\cite{missing}"):
            with self.subTest(addition=addition), tempfile.TemporaryDirectory() as directory:
                with self.assertRaises(ValueError):
                    package.read_package(self.make_zip(Path(directory), SAMPLE.replace(r"\end{document}", addition + r"\end{document}")))

    def test_reject_duplicate_member(self):
        with tempfile.TemporaryDirectory() as directory:
            path = self.make_zip(Path(directory))
            with warnings.catch_warnings():
                warnings.simplefilter("ignore", UserWarning)
                with zipfile.ZipFile(path, "a") as archive:
                    archive.writestr(package.GRAPH, b"%PDF-1.7\n%%EOF\n")
            with self.assertRaises(ValueError):
                package.read_package(path)

    def test_compiled_target_is_not_the_committed_pdf(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "source" / "report"
            public = root / "public" / "report"
            source.parent.mkdir(); public.parent.mkdir()
            source.with_suffix(".tex").write_text(report.SOURCE_STEM.with_suffix(".tex").read_text())
            public.with_suffix(".pdf").write_bytes(b"%PDF-1.7\nstored\n%%EOF\n")
            with patch.object(report, "SOURCE_STEM", source), patch.object(report, "PDF_STEM", public):
                with self.assertRaises(FileNotFoundError):
                    report.check(compiled=True)
                source.with_suffix(".pdf").write_bytes(b"%PDF-1.7\nfresh\n%%EOF\n")
                source.with_suffix(".log").write_text("pdfTeX test\nOutput written on report.pdf (22 pages, 32 bytes).\n")
                self.assertNotEqual(report.check(True)["sha256"], report.check(False)["sha256"])
                self.assertEqual(report.check(True)["pages"], 22)

    def test_reject_bad_report_log(self):
        with tempfile.TemporaryDirectory() as directory:
            pdf = Path(directory) / "report.pdf"
            log = pdf.with_suffix(".log")
            pdf.write_bytes(b"%PDF-1.7\n%%EOF\n")
            for problem in ("Overfull \\hbox", "Missing character: ?", "Label(s) may have changed"):
                log.write_text("pdfTeX test\nOutput written on report.pdf (22 pages, 32 bytes).\n" + problem)
                with self.assertRaises(ValueError):
                    report.validate_pdf(pdf, log)
