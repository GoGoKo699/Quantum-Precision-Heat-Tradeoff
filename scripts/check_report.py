#!/usr/bin/env python3
"""Check report identity, self-contained source, and produced PDF (standard library)."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
STEM = ROOT / "learning/report/Quantum_Precision_Heat_Tradeoff_Report"
TEX = STEM.with_suffix(".tex")
PDF = STEM.with_suffix(".pdf")

def check() -> None:
    source = TEX.read_text(encoding="utf-8")
    assert source.count(r"\section{") == 5
    assert source.count(r"\subsection{") == 16
    assert not re.search(r"\\(?:input|include|includegraphics|bibliography)\s*(?:\[[^]]*\])?\{", source)
    assert not re.search(r"\\(?:author|affiliation|email|orcidlink)\b", source)
    for forbidden in ("Ranyiliu Chen", "Ruge Lin", "ranyiliu.chen@outlook.com", "0000-0001-6060-6192", "0000-0002-9297-7622"):
        assert forbidden not in source, forbidden
    assert "pdfauthor={}" in source
    assert PDF.read_bytes().startswith(b"%PDF-")
    log = STEM.with_suffix(".log")
    if log.exists():
        report = log.read_text(errors="replace")
        assert not any(msg in report for msg in ("Missing character:", "Overfull ", "multiply defined", "undefined references", "Rerun to get cross-references right"))
    print("Report source and PDF checks passed.")

if __name__ == "__main__":
    check()
