#!/usr/bin/env python3
"""Build the single-file manuscript, explanatory report, and Overleaf ZIP.

Requires Python dependencies in requirements-dev.txt and pdfLaTeX (TeX Live 2025).
Run from the repository root: python scripts/build_documents.py
Pass --refresh to copy the newly compiled PDFs to their public repository paths.
No network, BibTeX, shell escape, or extra TeX inputs are used during compilation.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
ARTICLE = "Quantum_Precision_Heat_Tradeoff_arXiv"
REPORT = "Quantum_Precision_Heat_Tradeoff_Report"
PACKAGE_FILES = (ARTICLE+".tex", "Graph/crossover.pdf", "Graph/generate_plots.py", "Graph/requirements.txt")


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def package(destination: Path) -> dict[str, str]:
    """Deterministic minimal ZIP: one TeX file and one Graph directory."""
    destination.parent.mkdir(parents=True, exist_ok=True)
    hashes = {}
    with zipfile.ZipFile(destination, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for relative in PACKAGE_FILES:
            path = ROOT/"paper"/relative
            info = zipfile.ZipInfo(relative, date_time=(2026, 10, 21, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, path.read_bytes())
            hashes[relative] = digest(path)
    with zipfile.ZipFile(destination) as archive:
        assert sum(n.endswith(".tex") for n in archive.namelist()) == 1
        assert set(archive.namelist()) == set(PACKAGE_FILES)
    return hashes


def compile_tex(source: Path, directory: Path, extra: Path | None = None) -> dict:
    """Compile in an isolated directory so a stale local .bbl cannot mask a dependency."""
    if directory.exists():
        shutil.rmtree(directory)
    directory.mkdir(parents=True)
    shutil.copy2(source, directory/source.name)
    if extra:
        (directory/"Graph").mkdir()
        shutil.copy2(extra, directory/"Graph"/extra.name)
    executable = shutil.which("pdflatex")
    if not executable:
        raise RuntimeError("pdfLaTeX not found; install TeX Live 2025.")
    env = os.environ.copy()
    env.setdefault("SOURCE_DATE_EPOCH", "1792540800")
    command = [executable, "-no-shell-escape", "-interaction=nonstopmode", "-halt-on-error", "-file-line-error", source.name]
    # Three passes normally suffice for REVTeX, embedded references, and report TOC.
    for index in range(1, 5):
        run = subprocess.run(command, cwd=directory, env=env, text=True,
                             stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        (directory/f"pass-{index}.txt").write_text(run.stdout)
        if run.returncode:
            raise RuntimeError(f"Compilation failed: {directory}/pass-{index}.txt")
        log = (directory/(source.stem+".log")).read_text(errors="replace")
        if index >= 3 and "Rerun to get cross-references right" not in log:
            break
    failures = [line for line in log.splitlines() if
                "Overfull" in line or "Missing character:" in line or
                "undefined" in line.lower() or "multiply defined" in line.lower() or
                "destination with the same identifier" in line or
                "Rerun to get cross-references right" in line]
    if failures:
        raise RuntimeError("Unresolved PDF checks: " + "\n".join(failures))
    pages = re.search(r"Output written on .*?\((\d+) pages?,", log, re.S)
    notices = [line for line in log.splitlines() if "Warning:" in line or "Underfull" in line]
    return {"pages": int(pages.group(1)) if pages else None, "passes": index,
            "pdf_sha256": digest(directory/(source.stem+".pdf")),
            "nonfatal_notices": notices}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--refresh", action="store_true")
    parser.add_argument("--package-only", action="store_true")
    args = parser.parse_args()
    out = ROOT/"build"/"documents"
    out.mkdir(parents=True, exist_ok=True)
    if args.package_only:
        hashes = package(out/"Quantum_Precision_Heat_Tradeoff_Overleaf.zip")
        clean = out/"zip-extract"
        if clean.exists(): shutil.rmtree(clean)
        with zipfile.ZipFile(out/"Quantum_Precision_Heat_Tradeoff_Overleaf.zip") as archive:
            archive.extractall(clean)
        print(json.dumps(hashes, indent=2))
        return
    subprocess.run([sys.executable, str(ROOT/"paper/Graph/generate_plots.py")], check=True)
    paper = compile_tex(ROOT/"paper"/(ARTICLE+".tex"), out/"article", ROOT/"paper/Graph/crossover.pdf")
    report = compile_tex(ROOT/"learning/report"/(REPORT+".tex"), out/"report")
    hashes = package(out/("Quantum_Precision_Heat_Tradeoff_Overleaf.zip"))
    # Rebuild from the exported ZIP, not from the manuscript working directory.
    clean = out/"zip-extract"
    if clean.exists(): shutil.rmtree(clean)
    with zipfile.ZipFile(out/"Quantum_Precision_Heat_Tradeoff_Overleaf.zip") as archive:
        archive.extractall(clean)
    rebuilt = compile_tex(clean/(ARTICLE+".tex"), out/"zip-rebuild", clean/"Graph/crossover.pdf")
    assert paper["pages"] == rebuilt["pages"]
    if args.refresh:
        shutil.copy2(out/"article"/(ARTICLE+".pdf"), ROOT/"paper"/(ARTICLE+".pdf"))
        shutil.copy2(out/"report"/(REPORT+".pdf"), ROOT/"learning/report"/(REPORT+".pdf"))
    record = {"status": "passed", "compiler": subprocess.check_output(["pdflatex","--version"],text=True).splitlines()[0],
              "article": paper, "report": report, "zip_rebuild": rebuilt, "package_files_sha256": hashes,
              "scope": "Source isolation, compilation, log and archive checks; not visual or independent scientific review."}
    (out/"build_check.json").write_text(json.dumps(record, indent=2)+"\n")
    print(json.dumps(record, indent=2))

if __name__ == "__main__":
    main()
