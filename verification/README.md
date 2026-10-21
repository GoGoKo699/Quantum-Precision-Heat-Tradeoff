# Reproduce the calculations

[Home](../README.md) · [Claim map](CLAIMS.md) · [Finite benchmark](../science/finite_benchmark.md)

## Numerical environment

The committed [reference record](../results/reference.json) was produced with Python 3.13.5, NumPy 2.3.5, and SciPy 1.17.0. Its calculations also reproduce in a clean Python 3.12.14 environment on Linux x86-64 with the same pinned numerical dependencies. Package metadata permits Python 3.11 and later; these execution records do not establish support for every interpreter and platform combination.

Run these commands from the repository root:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
python scripts/reproduce.py
```

On Windows PowerShell, replace activation with `.venv\Scripts\Activate.ps1`. The tests use fixed seeds and run without external data. Generated results go to `results/generated.json`; the committed reference is preserved. Use `python scripts/reproduce.py --output PATH` to choose another destination.

## Install as a package

A regular installation makes `qph` available outside the checkout:

```bash
python -m pip install .
```

From another directory, with the same environment activated:

```bash
python -c 'from qph.core import crossover; print(crossover(1))'
```

The expected value is approximately $`0.1495103748978384`$. Both the regular wheel installation and this outside-checkout import were checked on Python 3.12.14. An editable development installation is also available with `python -m pip install -e .`.

The Python wheel contains the numerical package and its license. The source distribution additionally includes the documentation, reference data, scripts, and test inputs needed to reproduce the repository checks. Continuous integration builds both formats, reruns the tests and documentation checks from the extracted source distribution, and verifies a wheel import outside the checkout.

## What the calculation checks

- [Core formulas and matrix implementation](../qph/core.py): finite lower bound, entropy allowance, limiting function, explicit collision, bath heat, spectral information, and finite recovery sum.
- [Named tests](../tests/test_core.py): deterministic scalar regressions and finite matrices, including noncommuting and rank-deficient states, singular unitary blocks, actual-environment disturbance, auxiliary controls, and the full heat ledger.
- [Channel conversion tests](../tests/test_channel_conversion.py): the degenerate Gibbs dephasing unitary, unchanged basis-input joint states and charged heat, ensemble workspace return, and reference-entangled output errors. The diamond identity and exact-output obstruction have [analytic proofs](../science/channel_accuracy.md#channel-equivalence).
- [Reproduction script](../scripts/reproduce.py): evaluates the finite benchmark and selected limiting-function and recovery values.
- [Reference record](../results/reference.json): unchanged expected values, compared recursively with a numerical tolerance by the repository checker.

The [claim map](CLAIMS.md) links each test to the mathematical step it supports. Finite computations check the implementation and selected identities. The arbitrary-dimensional result rests on the [proof](../science/README.md).

## Documentation checks

Documentation tooling is separate from the numerical runtime. Install Node.js 22.12 or later and the exact development versions in `package-lock.json`:

```bash
npm ci
npm run docs:test
python scripts/check_repository.py
npm run docs:render
```

The checker validates Markdown syntax, inline and display mathematics, local links and anchors, images and alt text, equation widths, and displayed benchmark values. Its tests include deliberately broken documents to verify that failures are detected.

`npm run docs:render` writes an HTML preview of every active Markdown page and a validation manifest to `build/docs-preview`.

These local checks do not certify live GitHub layout or external link availability, and the notation checks do not replace visual inspection.

[Continuous integration](../.github/workflows/checks.yml) runs the numerical and documentation checks and makes the generated preview and manifest available as build artifacts.

## Regenerate the figures

The two figures use the existing limiting function and physical model. Install the separately pinned plotting dependency and run:

```bash
python -m pip install -r requirements-dev.txt
python scripts/make_figures.py
```

The [source script](../scripts/make_figures.py) writes accessible SVGs under `science/figures`. The logarithmic plot shows the optimal limiting law at positive finite error ratios; its caption separately gives the endpoint. The resource diagram includes all thermal recovery systems in the charged reservoir. Both figures have an explicit light background so their labels remain readable on dark pages.

## Units and numerical domains

Heat values are normalized as

```math
q=\frac{Q}{k_{\mathrm B}T\ln2}.
```

Code entropies are in bits. The collision Hamiltonian is returned in units of $`k_{\mathrm B}T`$, so its energy increase is divided by $`\ln2`$ before comparison with the public bounds.

The finite collision domain is $`0<s<1`$ and

```math
0<\epsilon<\frac{\sqrt{1-s^2}}2.
```

A computed thermal bias that rounds to one causes an explicit error. The implementation does not replace a tiny positive Gibbs population by zero. Extreme positive-error endpoints require higher-precision arithmetic beyond this double-precision implementation.

The recovery routine evaluates its exact finite sum in bounded-memory chunks. It does not construct an exponentially large joint density matrix. The source inventory and factual assistance disclosure are in [provenance](../provenance/README.md); those files are not runtime inputs.

## Source and structure checks

The [claim map](CLAIMS.md) links the current topic-based proof to its executable checks. The [source map](source_map.json) records the source revision, document destinations, retained scientific-code hashes, and unchanged mathematical expressions. `python scripts/check_structure.py` checks those preservation records and the active directory structure; it is also called by the repository checker.

The shared learning map has exactly 30 project-defined targets and the retained 14/16 allocation. Its tests check dependencies, conceptual connections, source links, and the absence of a public personal assessment contract. These structural checks do not assess a learner or prove the mathematical result.

The numerical tests, reference reproduction, local math compilation, and hosted rendering are separate checks. A local preview does not certify the actual GitHub renderer. The CI preview artifacts retain local rendering evidence; any hosted inspection must identify the pages and revision actually examined.

The [verification snapshot](INSPECTION.md) records source preservation, package execution, and the revision and pages examined in the actual GitHub renderer.


The [full sanity check](SANITY_CHECK.md) records the analytical consistency check, source recheck, numerical edge repairs, dependency audit, and fresh hosted-page inspection.

## Manuscript and explanatory report

The [document reproduction guide](DOCUMENTS.md) covers the single-file Overleaf package, Python-generated quantitative plot, inline TikZ diagrams, self-contained report, and clean pdfLaTeX builds. These checks supplement the scientific and repository checks above.
