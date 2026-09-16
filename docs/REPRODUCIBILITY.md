# Reproduce the calculations

[Home](../README.md) · [Claim map](CLAIMS.md) · [Finite benchmark](FINITE_BENCHMARK.md)

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

## What the calculation checks

- [Core formulas and matrix implementation](../qph/core.py): finite lower bound, entropy allowance, limiting function, explicit collision, bath heat, spectral information, and finite recovery sum.
- [Named tests](../tests/test_core.py): deterministic scalar regressions and finite matrices, including noncommuting and rank-deficient states, singular unitary blocks, actual-environment disturbance, auxiliary controls, and the full heat ledger.
- [Reproduction script](../scripts/reproduce.py): evaluates the finite benchmark and selected limiting-function and recovery values.
- [Reference record](../results/reference.json): unchanged expected values, compared recursively with a numerical tolerance by the repository checker.

The [claim map](CLAIMS.md) links each test to the mathematical step it supports. Finite computations check the implementation and selected identities. The arbitrary-dimensional result rests on the [proof](PROOF.md), with no experimental evidence implied by a passing test.

## Documentation checks

Documentation tooling is separate from the numerical runtime. Install Node.js 22.12 or later and the exact development versions in `package-lock.json`:

```bash
npm ci
npm run docs:test
python scripts/check_repository.py
npm run docs:render
```

The checker parses Markdown, compiles inline and display TeX with MathJax, resolves local destinations and fragments, checks heading and explicit anchors, checks image presence and alt text, rejects environment-specific markup, and compares displayed benchmark values with the reference. Deliberately broken fixtures verify that syntax, anchor, image, and excessive-width failures are detected.

The local renderer uses markdown-it and MathJax SVG output. It estimates intrinsic SVG widths at 8 pixels per ex unit, with 16-pixel surrounding text, against a 310-pixel reading column, corresponding to a 350-pixel stress viewport with 20-pixel side margins. It writes HTML and a manifest to `build/docs-preview`. Preview frames also allow inspection at 390 and 430 pixels, in light and dark presentation. Font sizes are not reduced to make long expressions pass.

**These are local checks.** They do not reproduce GitHub's entire styling or certify its live layout. Live GitHub visual inspection at desktop and phone widths is a separate acceptance step. External destination availability also requires a separate check. Rendering evidence belongs in build artifacts, rather than the scientific reference data.

[Continuous integration](../.github/workflows/checks.yml) runs the numerical and documentation checks and retains the generated preview and its validation manifest as build artifacts. The published [GitHub math guidance](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions) defines the supported inline delimiters and fenced display syntax.

## Regenerate the figures

The two figures use the existing limiting function and physical model. Install the separately pinned plotting dependency and run:

```bash
python -m pip install -r requirements-dev.txt
python scripts/make_figures.py
```

The [source script](../scripts/make_figures.py) writes accessible SVGs under `docs/figures`. The logarithmic plot shows positive finite error ratios; its caption separately gives the endpoint. It plots an optimal limiting law, with no finite optimization or experimental dataset. The resource diagram includes all thermal recovery systems in the charged reservoir. Both figures have an explicit light background so their labels remain readable on dark pages.

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
