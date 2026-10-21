# Pre-release verification

[Home](../README.md) · [Scientific claim map](CLAIMS.md) · [Report and plot checks](DOCUMENTS.md)

## Scope and preserved sources

The 21 October 2026 check starts from repository revision `e2ca602397ea5dacf43f42c13c5b30b0b3d7731f`. The scientific account, numerical core, committed reference values, thirty-milestone map, selected textbook bridge, and anonymous report source/PDF are unchanged. The maintenance changes clarify the public document boundary and strengthen delivery checks; they do not introduce a new scientific result.

The source-preservation check retains 12 protected files, 17 mathematical source records, and 42 bibliography labels. The current tree holds the explanatory report and the Python plot source, not the unpublished manuscript or its source archive. The README report entry links only the PDF.

## Executed local checks

- All 39 Python unit tests passed, including numerical, channel, report, plotting, and delivery-check tests.
- Reference reproduction and source-preservation checks passed. The original repository figures were regenerated without changing their retained content.
- The independent plot generator reproduced the externally supplied vector graph byte-for-byte with the pinned plotting dependency. It was compared against the canonical crossover over the displayed range and extreme finite-ratio cases.
- A separate retained numerical check passed 1,747 deterministic scalar and finite-matrix assertions. These checks support the documented formulas and examples, not arbitrary-dimensional proof validity.
- The accepted report's 22 rendered pages were inspected, including its equations, table, final synthesis, and plot labels. Its author metadata is empty. A released TeX Live 2025 rebuild also produced 22 pages.

## Corrected checking boundary

The report checker now distinguishes the committed reader-facing PDF from the freshly built PDF beside the TeX source. The report workflow uses `--compiled` and requires both the new PDF and its final log. A missing fresh output cannot pass by checking the older stored PDF. Regression tests cover this failure mode and reject problematic logs.

The external-package checker accepts exactly one named TeX source and its generated graph PDF. It checks source reference closure, rejects extra files and external inputs, and regenerates the plot from this repository. It does not copy the manuscript into the repository, execute untrusted TeX, or replace a clean build and visual review.

## Repeatable remote checks

The [repository workflow](../.github/workflows/checks.yml) checks the full numerical and documentation suite, reference values, source distribution, installed wheel outside the checkout, and original figure regeneration. The [report workflow](../.github/workflows/report.yml) builds with TeX Live 2025 and retains the fresh PDF, final log, and checker record. Their status must be checked on the exact pull-request head before merging.

## Limits

Numerical sampling does not prove an arbitrary-dimensional theorem. Source equivalence, compiler checks, and image inspection have different scopes; none is independent expert review or experimental validation. The literature comparison remains the attributed scientific account, not a newly exhaustive priority audit.

Local Node dependency installation was unavailable from the offline cache; documentation and distribution checks are therefore repeated in GitHub CI. The fetched public README was checked for correct links and content, but no new live-browser visual certification is claimed. No hosted Overleaf/arXiv submission, release tag, or metadata update was performed by this verification.
