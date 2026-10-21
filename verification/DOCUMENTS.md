# Reproduce the explanatory report

[Home](../README.md) · [Explanatory report (PDF)](../learning/report/Quantum_Precision_Heat_Tradeoff_Report.pdf) · [LaTeX source](../learning/report/Quantum_Precision_Heat_Tradeoff_Report.tex)

The repository retains a self-contained, reference-free explanatory report. Its five sections and sixteen subsections present the complete scientific story; mathematical background is introduced where it is needed. The report intentionally has no author names, affiliations, correspondence address, ORCID links, or PDF author metadata. The accepted scientific narrative and equations are preserved.

The source is **one TeX file**. Its figure is created within that file using PGFPlots/TikZ; no external image, bibliography, manuscript, plot generator, or other publication source is required.

## Compile the report

Use pdfLaTeX and TeX Live 2025 (also available in the repository report workflow):

    cd learning/report
    pdflatex -interaction=nonstopmode -halt-on-error Quantum_Precision_Heat_Tradeoff_Report.tex
    pdflatex -interaction=nonstopmode -halt-on-error Quantum_Precision_Heat_Tradeoff_Report.tex

The second pass resolves the table of contents and cross-references. Check the resulting PDF by rendering the pages and inspecting the plot annotations, equations, headings, and page breaks. Compiler success is not a visual certificate.

To run the structural checks from the repository root:

    python -m unittest discover -s tests -v
    python scripts/reproduce.py
    python scripts/check_repository.py
    python scripts/make_figures.py

The mathematical proofs and numerical reproducibility package remain under science/, qph/, tests/, and verification/. This report is intended as a reading companion and is not a separate manuscript or proof certificate.
