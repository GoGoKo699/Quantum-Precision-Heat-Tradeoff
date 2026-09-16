# Precision and Heat in Quantum Operations

**How accurately must a quantum device reproduce its outputs before a finite heat cost becomes unavoidable?**

This repository studies a single-use device that converts either of two orthogonal qubit inputs into prescribed, nearly orthogonal output states. It contains the physical model, the precision–heat theorem and proof, explicit thermal implementations, and reproducible calculations.

## Collaboration

**Manuscript preparation is currently on hold.** Researchers interested in collaborating on this project are welcome to contact **Ruge Lin** at **[gogoko699@gmail.com](mailto:gogoko699@gmail.com)**.

## Choose a starting point

| Your goal | Start here |
|---|---|
| Understand the physics from undergraduate foundations | [Tutorial](docs/tutorial/README.md) |
| Read the exact result and its assumptions | [Model](docs/MODEL.md) → [Theorem](docs/THEOREM.md) → [Proof](docs/PROOF.md) |
| Follow a complete physical implementation | [Two-qubit device and thermal recovery](docs/CONSTRUCTION.md) |
| Inspect a finite, non-asymptotic consequence | [Finite benchmark](docs/FINITE_BENCHMARK.md) |
| Separate inherited ingredients from this result | [Literature and assumption provenance](docs/LITERATURE.md) |
| Run the calculations | [Reproducibility guide](docs/REPRODUCIBILITY.md) |

## The physical question

The device receives either `|0>` or `|1>`, with equal probability. Its desired outputs share a small transverse polarization of magnitude **s**; their state-vector overlap also has magnitude **s**. Each actual output must be within trace distance **epsilon** of its target.

The average system-entropy change tends to zero as the targets approach orthogonality. Nevertheless, sufficiently precise conditional outputs force an environmental information record and an associated heat cost. The relevant scale is **epsilon / s²**, not error relative to the polarization alone.

The theorem gives the optimal small-overlap crossover:

```math
\lim_{s\to0,\;\epsilon/s^2\to r}
\frac{Q_{\min}(s,\epsilon)}{k_{\mathrm B}T\ln2}
=
1-h_2\!\left(\frac{1+(1+4r)^{-1/2}}{2}\right),
\qquad 0\le r<\infty.
```

Here **h₂** is binary entropy in bits. The optimization permits arbitrary finite thermal reservoirs and finite internal workspace whose average marginal state is restored. The [full statement](docs/THEOREM.md) specifies the error domain, return condition, and limiting procedure.

This is an optimal limiting law, **not** an exact finite-parameter optimum. Each implementation is finite, but resources need not remain uniformly bounded along the optimizing sequence.

## A finite consequence

For the same targets with **s = 0.05**, all devices meeting branch trace error at most **0.0001** obey a heat lower bound of **0.498044** bit-erasure units. An explicit device accepting error **0.0025** uses one thermal bath qubit and costs **0.311485** units, while preserving the intended transverse polarization exactly.

These are a proved lower bound and a calculated construction, respectively—not experimental measurements or claims that either finite optimum is attained. See the [derivation and resource accounting](docs/FINITE_BENCHMARK.md).

## What is counted

Heat is the mean energy increase of the **complete thermal reservoir**. The input, internal workspace, and reservoir start independently. All thermal recovery components are charged. Workspace may be nonthermal, but consumed entropy capacity is not free.

Predetermined external driving is allowed. Heat equals mean supplied work only under the stated boundary-energy conditions. Controller construction, wall-plug energy, hardware feasibility, and unrestricted many-copy processing are not conclusions of this model. The [model](docs/MODEL.md) makes these boundaries explicit.

## One textbook as the teaching foundation

The tutorial is anchored in **Benjamin Schumacher and Michael D. Westmoreland, _Quantum Processes, Systems, and Information_ (Cambridge University Press, 2010)**. It supplies a self-contained bridge from qubits, density operators, and open systems to the device and the theorem.

The textbook is the educational anchor, not the entire research bibliography. [The reading map](docs/tutorial/README.md) distinguishes undergraduate foundations from the additional inequalities used in the universal proof. No textbook text or scans are redistributed.

## Reproduce

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
python scripts/reproduce.py
python scripts/check_repository.py
```

On Windows, activate with `.venv\Scripts\Activate.ps1`. Commands are run from the repository root. The [guide](docs/REPRODUCIBILITY.md) explains outputs, numerical domains, and exactly what the tests establish.

## Repository scope

This is a theory and reproducibility repository. Mathematical arguments are in the proof documents; finite numerical checks test the implementation and selected identities. The [claim map](docs/CLAIMS.md) connects each central statement to its derivation and executable evidence.

Original code and documentation are available under the [MIT License](LICENSE), copyright 2026 Ruge Lin. Scientific attribution is documented in the [literature guide](docs/LITERATURE.md) and [citation metadata](CITATION.cff).
