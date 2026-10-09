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

The Python wheel contains the numerical package and its license. The source distribution additionally includes the documentation, reference data, scripts, and test inputs needed to reproduce the repository checks. Continuous integration builds both formats, reruns the tests and documentation checks from the extracted source distribution, and verifies a wheel import outside the checkout.

## What the calculation checks

- [Core formulas and matrix implementation](../qph/core.py): finite lower bound, entropy allowance, limiting function, explicit collision, bath heat, spectral information, and finite recovery sum.
- [Named tests](../tests/test_core.py): deterministic scalar regressions and finite matrices, including noncommuting and rank-deficient states, singular unitary blocks, actual-environment disturbance, auxiliary controls, and the full heat ledger.
- [Channel conversion tests](../tests/test_channel_conversion.py): the degenerate Gibbs dephasing unitary, unchanged basis-input joint states and charged heat, ensemble workspace return, and reference-entangled output errors. The diamond identity and exact-output obstruction have [analytic proofs](PROOF.md#channel-equivalence).
- [Reproduction script](../scripts/reproduce.py): evaluates the finite benchmark and selected limiting-function and recovery values.
- [Reference record](../results/reference.json): unchanged expected values, compared recursively with a numerical tolerance by the repository checker.

The [claim map](CLAIMS.md) links each test to the mathematical step it supports. Finite computations check the implementation and selected identities. The arbitrary-dimensional result rests on the [proof](PROOF.md).

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

The [source script](../scripts/make_figures.py) writes accessible SVGs under `docs/figures`. The logarithmic plot shows the optimal limiting law at positive finite error ratios; its caption separately gives the endpoint. The resource diagram includes all thermal recovery systems in the charged reservoir. Both figures have an explicit light background so their labels remain readable on dark pages.

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
