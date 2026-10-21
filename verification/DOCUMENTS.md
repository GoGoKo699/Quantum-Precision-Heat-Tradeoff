# Reproduce the manuscript and explanatory report

[Home](../README.md) · [Manuscript](../paper/README.md) · [Report PDF](../learning/report/Quantum_Precision_Heat_Tradeoff_Report.pdf) · [Repository verification](README.md)

## Sources and preserved content

The manuscript is one TeX file at [paper/Quantum_Precision_Heat_Tradeoff_arXiv.tex](../paper/Quantum_Precision_Heat_Tradeoff_arXiv.tex). It contains the article, End Matter, supporting derivations, all TikZ diagrams, and the complete bibliography. Its quantitative plot is the vector PDF produced directly by [Graph/generate_plots.py](../paper/Graph/generate_plots.py). No data fitting or manual modification of a generated PDF is used. The Python implementation is portable with the Overleaf package and is regression-tested against `qph.core.crossover`.

The approved ket positions and circular arcs are explicitly tested in `tests/test_publication.py`. The two authors, supplied affiliations, ORCID identifiers, corresponding-author email, and no-date format are retained. The manuscript's disclosure retains the authors' outstanding confirmation rather than inventing a completed author verification.

The [report source](../learning/report/Quantum_Precision_Heat_Tradeoff_Report.tex) is self-contained and reference-free. Its own explanatory curve is rendered from its inline mathematical expression by PGFPlots. The source is unchanged from the approved report: five sections and sixteen subsections, with prerequisites introduced locally. Its [PDF](../learning/report/Quantum_Precision_Heat_Tradeoff_Report.pdf) is accessible from the repository README.

The scientific model, canonical proofs, numerical implementation, retained reference values, and thirty-milestone map are not changed by this document integration. The scientific baseline is revision `f749753c5000bfa3efb3466d67c12b4b1befbb4b`. The source-preservation checker continues to protect the original scientific records.

## Build and export

Use Python 3.11 or later with the repository's pinned dependencies, and pdfLaTeX with TeX Live 2025:

```bash
python -m pip install -r requirements-dev.txt
python -m unittest discover -s tests -v
python scripts/reproduce.py
python scripts/verify_manuscript.py
python scripts/build_documents.py
```

`build_documents.py` regenerates the plot, compiles each document in an isolated directory, exports the minimal ZIP, extracts it again, and rebuilds that extracted source. It stops on unresolved references, duplicate labels or destinations, missing-character warnings, and overflowing boxes. It requires neither BibTeX nor shell escape. The output includes:

```text
build/documents/Quantum_Precision_Heat_Tradeoff_Overleaf.zip
build/documents/article/Quantum_Precision_Heat_Tradeoff_arXiv.pdf
build/documents/report/Quantum_Precision_Heat_Tradeoff_Report.pdf
build/documents/build_check.json
build/documents/manuscript_numerics.json
```

Use `--refresh` only when intentionally updating the committed public PDFs after review. `--package-only` exports and extracts the identical ZIP without compiling; the document workflow uses it between clean compiler runs.

The archive has only the named TeX file at its root and one `Graph` folder. That folder contains the generated plot, its Python generator, and its dependency file. There are no stale PDFs of the manuscript, auxiliary files, external TeX inputs, or external bibliography dependencies in the source package. Python regenerates the plot locally; Overleaf compiles using the already included plot PDF.

## What the checks establish

The original 28 tests plus eight document tests cover numerical regressions, package contents, inline diagrams, authorship and date conventions, reference closure, report structure, deterministic plot regeneration, and a clean source archive. The portable plotted formula is compared with the canonical function throughout the displayed range and at endpoint and large-ratio test values.

`scripts/verify_manuscript.py` additionally executes 1,747 deterministic scalar and finite-matrix assertions with seed `20261021`. These cover noncommuting and rank-deficient states, singular transition blocks, coherence replacement, spectral and information inequalities, actual-environment disturbance, the complete heat ledger, collision outputs, recovery sums, and sampled reference-sensitive channel errors. It also reproduces the retained finite comparison. These finite checks do not prove arbitrary-dimensional statements or constitute a physical experiment.

The document workflow selects TeX Live 2025 explicitly, compiles both public PDFs, and recompiles the exported Overleaf source in a clean directory. Local Debian `2025/dev` output and the released TeX Live 2025 workflow are separate environments; neither is a claim that a hosted Overleaf or arXiv submission was performed.

Page renders must still be inspected, especially the diagram, axis labels, annotation leaders, wide equations, tables, and section transitions. Compiler success and local image inspection are different checks. Nonfatal REVTeX/nameref notices, disabled EPS-conversion notices, and loose bibliography lines are recorded rather than described as an entirely warning-free compilation.

## Full repository checks

Run the existing scientific and documentation checks as well:

```bash
npm ci --ignore-scripts
python scripts/check_repository.py
python scripts/make_figures.py
```

Source-distribution and outside-checkout wheel tests remain in the existing repository workflow. The separate document workflow is read-only and uploads build evidence; it does not commit automatically or change scientific source files.
