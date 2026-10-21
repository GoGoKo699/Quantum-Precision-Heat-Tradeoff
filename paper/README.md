# Complete manuscript

[Home](../README.md) · [Read the PDF](Quantum_Precision_Heat_Tradeoff_arXiv.pdf) · [Scientific account](../science/README.md) · [Document reproduction](../verification/DOCUMENTS.md)

The complete article, End Matter, detailed derivations, and bibliography are in `Quantum_Precision_Heat_Tradeoff_arXiv.tex`. It compiles with pdfLaTeX under TeX Live 2025. All diagram code is inline TikZ. The quantitative panel is generated directly by `Graph/generate_plots.py`; its values are checked against the canonical implementation in `qph/core.py`.

## Minimal Overleaf project

The exported ZIP contains exactly:

```text
Quantum_Precision_Heat_Tradeoff_arXiv.tex
Graph/
  crossover.pdf
  generate_plots.py
  requirements.txt
```

Upload the ZIP as a new project, select the named TeX file as the main document, and select pdfLaTeX / TeX Live 2025. The plot PDF is already included: Python is not run by Overleaf. No separate bibliography file, macro file, supplemental TeX file, custom class, or shell escape is required.

To regenerate the plot locally:

```bash
python -m pip install -r paper/Graph/requirements.txt
python paper/Graph/generate_plots.py
```

To compile and export from the repository root:

```bash
python scripts/build_documents.py
```

The output ZIP and isolated build records are written under `build/documents`. The [verification guide](../verification/DOCUMENTS.md) distinguishes numerical, source, compilation, and visual checks. Building the manuscript is not independent scientific validation or submission to a journal or arXiv.
