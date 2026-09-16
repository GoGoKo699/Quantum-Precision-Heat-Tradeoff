# Reproduce the calculations

[Home](../README.md) · [Claim map](CLAIMS.md)

## Environment

The recorded calculation environment is Python 3.13.5, NumPy 2.3.5, and SciPy 1.17.0. The two numerical dependencies are pinned in `requirements.txt`. The package metadata permits Python 3.11 and later; the recorded execution below is on 3.13, not a claim that every interpreter/platform combination was tested.

From the repository root:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
python scripts/reproduce.py
python scripts/check_repository.py
```

For PowerShell, replace the activation command by `.venv\Scripts\Activate.ps1`. An editable install with `python -m pip install -e .` is optional. No website build, proprietary software, dataset download, or previous research archive is required.

## Files and outputs

`qph/core.py` contains the finite bound, entropy allowance, crossover function, explicit two-qubit unitary, bath-energy calculation, spectral information quantity, and finite recovery sum.

`tests/test_core.py` contains deterministic regression and finite-matrix tests. Randomized cases use fixed seeds. The test groups include noncommuting and rank-deficient states, singular unitary-block examples, complete auxiliary/bath ledgers, and resource-boundary controls. Failures produce a nonzero exit status.

`scripts/reproduce.py` writes `results/generated.json` by default. The committed `results/reference.json` records the expected calculation and environment. Generated output does not overwrite that reference. Use `--output PATH` for a different destination.

`scripts/check_repository.py` checks repository-local Markdown destinations, supported display-math delimiters, citation metadata, and reference-number reproduction. It does not certify external link availability or perform a live GitHub visual inspection.

## Units and numerical domains

Public numerical heat values are in units of k_B T ln 2. Entropies in the code are bits. The collision Hamiltonian is returned in units of k_B T, so its directly calculated energy change is divided by ln 2 before comparison with the bounds.

The supported finite collision domain is 0 < s < 1 and 0 < epsilon < sqrt(1-s²)/2. A finite thermal bias that rounds to exactly one causes an explicit error; the code never silently treats a numerically pure bath as a full-rank Gibbs resource. Extremely small errors require higher-precision arithmetic beyond this double-precision reference implementation.

The recovery routine evaluates the exact finite sum in bounded-memory chunks. It does not simulate the exponentially large joint density matrix of a long recovery ladder.

## Scope of the checks

Numerical checks support implementation and consistency of the displayed formulas. They are not a proof of global optimality, a novelty assessment, or an experimental validation. The universal result rests on `docs/PROOF.md` and its stated assumptions.

The current commands reproduce the current canonical package. They do not claim to replay every earlier exploratory script. Source-file hashes are recorded separately in the provenance inventory so that the consolidation has an identifiable input without requiring readers to reconstruct the project history.
