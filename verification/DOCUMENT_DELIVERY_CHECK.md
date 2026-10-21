# Document delivery verification

[Home](../README.md) · [Build instructions](DOCUMENTS.md) · [Scientific claim map](CLAIMS.md)

## Inspected sources

The document integration was checked on 21 October 2026 against scientific baseline `f749753c5000bfa3efb3466d67c12b4b1befbb4b`. The complete article and explanatory report use the supplied two-author order, affiliations, ORCID identifiers, corresponding-author address, and no displayed date. The approved ket positions and circular arrows are retained. This pass changes packaging and plot generation, not the canonical scientific account.

The source transfer and built PDFs are recorded at `c41e3686b5028ea5466c7172c7b82a6f4b13c596`. All sixteen transferred source files were checksum-verified. The explanatory-report TeX is byte-identical to the approved source. All 84 displayed mathematical environments in the combined manuscript match the approved article, End Matter, and supporting-derivation inputs.

## Executed checks

- All 36 repository tests passed, including the original 28 tests and eight publication tests.
- The independent manuscript checker passed 1,747 deterministic scalar and finite-matrix assertions and reproduced the retained finite benchmark.
- Source-preservation, reference reproduction, documentation, local-link, and original-figure regeneration checks passed.
- The article and report compiled with released pdfLaTeX, `pdfTeX 3.141592653-2.6-1.40.28 (TeX Live 2025)`. The article has 15 pages; the report has 22.
- The minimal Overleaf archive was extracted into a clean directory and compiled successfully. It contains exactly one TeX file and `Graph/crossover.pdf`, `Graph/generate_plots.py`, and `Graph/requirements.txt`; no separate TeX inputs or bibliography files are needed.
- The archive's four files match the reviewed local sources and plot byte-for-byte. The plot regenerated identically in the local and GitHub environments.
- Released-2025 PDF text matches the local check after whitespace normalization. All page layouts were inspected as rendered images, with detailed inspection of the figure and representative dense equations. No clipping, missing glyphs, or unresolved references were found in that review.

The [executed build](https://github.com/GoGoKo699/Quantum-Precision-Heat-Tradeoff/actions/runs/39585804074) retains the compiler and numerical records. The permanent [document workflow](../.github/workflows/documents.yml) repeats the builds and clean-archive check without writing to the repository. The existing [repository workflow](../.github/workflows/checks.yml) additionally checks the source distribution and an installed wheel outside the checkout.

## Limits of this verification

Finite numerical checks are not a proof for arbitrary apparatus dimensions or an experiment. Compiler and source checks do not replace visual inspection. The article's log contains a nonfatal REVTeX/nameref notice and two underfull bibliography lines; no overfull boxes, missing-character warnings, unresolved references, or duplicate destinations were found. The report's released-2025 log contains no warnings.

No hosted Overleaf or arXiv submission was performed. The manuscript still retains the authors' outstanding research-stage disclosure confirmation rather than asserting completed author approval. Neither document is made submission-approved by this packaging check.
