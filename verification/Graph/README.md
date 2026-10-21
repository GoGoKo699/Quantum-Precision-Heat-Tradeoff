# Quantitative crossover plot

[Verification](../README.md) · [Exact limiting law](../../science/theorem.md#optimal-crossover) · [Asset checks](../DOCUMENTS.md)

`generate_plots.py` writes `crossover.pdf` directly from the analytical limiting function. `requirements.txt` pins the plotting dependency. The script has no external input data and does not require the manuscript, TeX, or repository imports. The test suite checks its portable formula against the canonical implementation in `qph.core`.

Run from the repository root:

```bash
python -m pip install -r verification/Graph/requirements.txt
python verification/Graph/generate_plots.py --output /path/to/Graph/crossover.pdf
```

Generated PDFs are not tracked here. The delivered manuscript package contains the resulting PDF only; its editable schematic remains inline TikZ. The explanatory report uses a separate inline PGFPlots figure, not this external asset.
