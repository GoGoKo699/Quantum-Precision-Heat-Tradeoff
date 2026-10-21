#!/usr/bin/env python3
"""Audit an externally stored Overleaf ZIP without copying the manuscript into this repository."""
from __future__ import annotations
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import tempfile
import zipfile

ROOT = Path(__file__).resolve().parents[1]
TEX = "Quantum_Precision_Heat_Tradeoff_arXiv.tex"
GRAPH = "Graph/crossover.pdf"
EXPECTED = {TEX, GRAPH}


def uncomment(text: str) -> str:
    return re.sub(r"(?<!\\)%[^\n]*", "", text)


def read_package(path: Path) -> tuple[str, bytes]:
    with zipfile.ZipFile(path) as archive:
        entries = archive.infolist()
        files = [entry for entry in entries if not entry.is_dir()]
        if len(files) != 2 or {entry.filename for entry in files} != EXPECTED:
            raise ValueError("Expected exactly one named TeX source and Graph/crossover.pdf.")
        if any(entry.is_dir() and entry.filename != "Graph/" for entry in entries):
            raise ValueError("Unexpected directory in the archive.")
        if any((entry.external_attr >> 16) & 0o170000 == 0o120000 for entry in entries):
            raise ValueError("Symlinks are not allowed in the archive.")
        if sum(entry.file_size for entry in files) > 25_000_000:
            raise ValueError("Unexpectedly large archive.")
        source = archive.read(TEX).decode("utf-8")
        graph = archive.read(GRAPH)
    active = uncomment(source)
    if re.search(r"\\(?:input|include|bibliography|addbibresource|write18)\b", active):
        raise ValueError("External TeX/bibliography inputs or shell commands are not allowed.")
    if r"\usepackage{fontspec}" in active or r"\usepackage{unicode-math}" in active:
        raise ValueError("This source must use pdfLaTeX.")
    for name in ("document", "thebibliography"):
        if active.count(r"\begin{" + name + "}") != 1 or active.count(r"\end{" + name + "}") != 1:
            raise ValueError(f"Expected exactly one {name} environment.")
    images = re.findall(r"\\includegraphics(?:\[[^]]*\])?\{([^}]+)\}", active)
    if images != [GRAPH] or r"\begin{tikzpicture}" not in active:
        raise ValueError("The graph must be external and the schematic must remain inline TikZ.")
    if r"\today" in active or re.search(r"\\date\{[^}]+\}", active):
        raise ValueError("No displayed date is expected.")
    labels = re.findall(r"\\label\{([^}]+)\}", active)
    refs = set(re.findall(r"\\(?:eqref|ref)\{([^}]+)\}", active))
    if len(labels) != len(set(labels)) or not refs.issubset(labels):
        raise ValueError("Duplicate or unresolved source labels.")
    citations = {key.strip() for group in re.findall(r"\\cite\{([^}]+)\}", active) for key in group.split(",")}
    keys = set(re.findall(r"\\bibitem\s*(?:\[[\s\S]*?\])?\s*\{([^}]+)\}", active))
    if not citations.issubset(keys):
        raise ValueError("Unresolved source citation keys.")
    if not graph.startswith(b"%PDF-"):
        raise ValueError("The quantitative plot is not a PDF.")
    return source, graph


def check(path: Path) -> dict:
    source, graph = read_package(path)
    generator = ROOT / "verification/Graph/generate_plots.py"
    spec = importlib.util.spec_from_file_location("qph_delivery_plot", generator)
    if spec is None or spec.loader is None:
        raise RuntimeError("Plot generator could not be loaded.")
    plot = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(plot)
    with tempfile.TemporaryDirectory() as directory:
        regenerated = Path(directory) / "crossover.pdf"
        plot.draw(regenerated)
        if regenerated.read_bytes() != graph:
            raise ValueError("Packaged plot differs from the repository generator's output. Use the pinned dependencies.")
    digest = lambda data: hashlib.sha256(data).hexdigest()
    return {"status": "passed", "members": sorted(EXPECTED),
            "tex_sha256": digest(source.encode()), "plot_sha256": digest(graph),
            "generator_sha256": digest(generator.read_bytes()),
            "requirements_sha256": digest((generator.parent / "requirements.txt").read_bytes()),
            "plot_reproduced_byte_for_byte": True,
            "scope": "Archive structure, source closure and regenerated plot; not PDF compilation, scientific proof, or visual approval."}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("package", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    encoded = json.dumps(check(args.package), indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(encoded, encoding="utf-8")
    print(encoded, end="")
