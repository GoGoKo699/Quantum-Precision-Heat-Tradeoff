#!/usr/bin/env python3
"""Check the public report, or explicitly check a fresh report build."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SOURCE_STEM = ROOT / "learning/source/Quantum_Precision_Heat_Tradeoff_Report"
PDF_STEM = ROOT / "learning/report/Quantum_Precision_Heat_Tradeoff_Report"


def validate_source(source: str) -> None:
    if source.count(r"\section{") != 5 or source.count(r"\subsection{") != 16:
        raise ValueError("The report must retain five sections and sixteen subsections.")
    if re.search(r"\\(?:input|include|includegraphics|bibliography)\s*(?:\[[^]]*\])?\{", source):
        raise ValueError("The report source must remain self-contained.")
    if re.search(r"\\(?:author|affiliation|email|orcidlink)\b", source):
        raise ValueError("The public report must not contain an author block.")
    for value in ("Ranyiliu Chen", "Ruge Lin", "ranyiliu.chen@outlook.com",
                  "0000-0001-6060-6192", "0000-0002-9297-7622"):
        if value in source:
            raise ValueError("Author-identifying content remains in the report source.")
    if "pdfauthor={}" not in source:
        raise ValueError("The report must have empty PDF author metadata.")


def validate_pdf(path: Path, log_path: Path | None = None) -> dict:
    data = path.read_bytes()
    if not data.startswith(b"%PDF-") or b"%%EOF" not in data[-1024:]:
        raise ValueError(f"Not a complete PDF: {path}")
    result = {"file": path.name, "sha256": hashlib.sha256(data).hexdigest()}
    if log_path is not None:
        log = log_path.read_text(encoding="utf-8", errors="replace")
        forbidden = ("Missing character:", "Overfull ", "multiply defined",
                     "undefined references", "undefined citations",
                     "destination with the same identifier",
                     "Rerun to get cross-references right", "Label(s) may have changed")
        errors = [line for line in log.splitlines() if any(x in line for x in forbidden)]
        if errors:
            raise ValueError("Report build problems:\n" + "\n".join(errors))
        output = re.search(r"Output written on\s+([^\s]+)\s+\((\d+) pages?", log)
        if output is None or Path(output.group(1)).name != path.name:
            raise ValueError("The log does not identify the PDF being checked.")
        result.update(pages=int(output.group(2)), compiler=log.splitlines()[0],
                      notices=[line for line in log.splitlines() if "Warning:" in line])
    return result


def check(compiled: bool = False) -> dict:
    validate_source(SOURCE_STEM.with_suffix(".tex").read_text(encoding="utf-8"))
    stem = SOURCE_STEM if compiled else PDF_STEM
    result = validate_pdf(stem.with_suffix(".pdf"), stem.with_suffix(".log") if compiled else None)
    result.update(status="passed", target="fresh-build" if compiled else "committed-report",
                  scope="Source structure, PDF signature and optional compiler log; visual and semantic review are separate.")
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--compiled", action="store_true", help="Require the fresh PDF and its log beside the TeX source.")
    parser.add_argument("--output", type=Path, help="Optional JSON verification record.")
    args = parser.parse_args()
    record = check(args.compiled)
    encoded = json.dumps(record, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(encoded, encoding="utf-8")
    print(encoded, end="")
