# Precision and Heat in Quantum Operations

**How accurately must a quantum device reproduce its outputs before a finite heat cost becomes unavoidable?**

A device receives either of two orthogonal qubit states and must produce the corresponding prescribed output. The outputs are almost orthogonal, so their average entropy changes very little. Yet requiring sufficiently accurate outputs on **each input** forces a finite environmental information record. When internal workspace is returned, this also forces a finite mean heat cost. This repository gives the physical model, a universal lower bound, a matching limiting construction, and runnable finite examples.

## Explanatory report

Read the [complete explanatory report (PDF)](learning/report/Quantum_Precision_Heat_Tradeoff_Report.pdf) for a self-contained, reference-free explanation of the physical problem, the universal bound, the construction, and its consequences.

## Physical task

The inputs are $`|0\rangle`$ and $`|1\rangle`$, each supplied with probability one half. The same apparatus must work for either input; the control receives no separate label. The desired pure output density operators are

```math
\phi_x(s)=\frac{I-sX+(-1)^x cZ}{2}.
```

Here $`x\in\{0,1\}`$, $`X`$ and $`Z`$ are Pauli matrices, $`c=\sqrt{1-s^2}`$, and $`0<s<1`$. Their state-vector overlap has magnitude $`s`$. The actual conditional output $`\sigma_x`$ must pass both tests:

```math
\frac12\|\sigma_x-\phi_x(s)\|_1\le\epsilon.
```

The targets share transverse polarization $`-s`$, while their longitudinal polarizations have opposite signs. Their average is $`(I-sX)/2`$. As $`s`$ tends to zero, this average approaches the maximally mixed input average. An entropy bound based only on the average state therefore tends to zero. The conditional task retains information that this average-state calculation leaves out.

## Main result

Measure heat in bit-erasure units, $`q=Q/(k_{\mathrm B}T\ln2)`$. Let $`q_{\min}(s,\epsilon)`$ be the infimum over the finite devices in the [physical model](science/model.md), with exact return of the workspace's ensemble-average marginal. The optimal limiting heat depends on the ratio of error to **squared** overlap:

```math
\lim_{\substack{s\to0\\\epsilon/s^2\to r}}
q_{\min}(s,\epsilon)=F(r).
```

For each finite $`r\ge0`$, define

```math
b_*(r)=(1+4r)^{-1/2},
\qquad
F(r)=1-h_2\!\left(\frac{1+b_*(r)}{2}\right).
```

The binary entropy $`h_2`$ is measured in bits. Every finite stage has **positive error**, including sequences approaching $`r=0`$: [exact pure targets are impossible](science/theorem.md#exact-output-obstruction) with a finite full-rank Gibbs reservoir and exactly returned ensemble-average workspace. In that high-precision limit, $`F(0)=1`$: a full bit-erasure unit survives even as the average-state entropy loss vanishes. At $`r=1`$, the limiting heat is about $`0.149510`$ units.

![Optimal limiting heat F(r), in bit-erasure units, versus the finite error-to-squared-overlap ratio r. The curve approaches one as the ratio tends to zero and decreases as the allowed error ratio increases.](science/figures/limiting-crossover.svg)

Optimal limiting law computed from `qph.core.crossover`. The logarithmic axis shows positive finite ratios; the endpoint is $`F(0)=1`$. Each point specifies a joint small-overlap, positive-error limit, rather than a finite-device optimum. [Figure source](scripts/make_figures.py).

The [theorem](science/theorem.md) gives the complete finite bound before taking the limit. The [proof](science/README.md) covers arbitrary finite Gibbs reservoirs and input-independent workspace states. The [thermal construction](science/thermal_implementation.md) supplies the matching upper limit using a bath qubit followed by charged recovery swaps. Each implementation is finite; its bath size and energy gaps may grow along the optimizing sequence. The result identifies an **infimum**, without asserting an attained finite optimum.

The [same optimal mean-heat infimum](science/theorem.md#channel-equivalence) holds when accuracy is required in half-diamond norm for the target measure-and-prepare channel, including reference-entangled inputs. A finite degenerate Gibbs qubit converts any branch-feasible device at unchanged heat; the objective and workspace return remain evaluated on the equal-prior ensemble. Thus the same crossover governs full-channel accuracy.

## A finite comparison

Fix $`s=0.05`$ and use the same targets for both accuracy requirements:

| Conditional error tolerance | Heat in bit-erasure units |
|---|---|
| $`\epsilon=0.0001`$ | Every allowed cyclic device has $`q\ge0.498044`$. |
| $`\epsilon=0.0025`$ | One explicit bath-qubit device has $`q\simeq0.311485`$. |

The relaxed device retains the intended transverse polarization exactly. Its direct energy calculation already establishes this separation, without recovery. The first number is a proved lower bound; the second is the calculated heat of one construction. The [finite benchmark](science/finite_benchmark.md) gives the parameters, return correction, and reference values.

## Resource accounting

Heat is the mean energy increase of the **complete thermal reservoir**, including all fresh Gibbs systems used for recovery. The input, workspace, and reservoir start independently. Workspace can be nonthermal, but any increase in its entropy must be charged. For the cyclic optimum its ensemble-average marginal is restored exactly; final correlations are permitted.

![Resource boundary: an unknown input qubit, input-independent workspace, and complete Gibbs reservoir enter one fixed operation. The output qubit leaves, the workspace marginal returns, and all reservoir energy changes count as heat. Final correlations may remain.](science/figures/resource-boundary.svg)

The accounting is for one use. Returning a workspace marginal does not by itself establish independent reuse on arbitrary future inputs. [Diagram source](scripts/make_figures.py).

Predetermined external driving is allowed. Under the [boundary Hamiltonian conditions](science/model.md), heat equals mean supplied work. Controller construction and source preparation lie outside this accounting.

## Read the science

Start with the [connected scientific account](science/README.md), then the [model](science/model.md) and [exact statements](science/theorem.md). The proof route follows the output constraints, environmental information, heat ledger, and matching thermal construction. The [physical interpretation](science/interpretation.md) connects the pieces. The finite comparison and the two consequences remain directly accessible from the theorem.

| To inspect | Read |
|---|---|
| Main law, finite bounds, and exact scope | [Theorem](science/theorem.md) and [model](science/model.md) |
| Every-device converse and proof dependencies | [Scientific route](science/README.md#dependencies) |
| Explicit collision and charged recovery | [Thermal implementation](science/thermal_implementation.md) |
| Finite strict-versus-relaxed comparison | [Finite benchmark](science/finite_benchmark.md) |
| Attribution and nearby resource models | [Direct comparisons](references/RELATED_WORK.md) and [source register](references/LITERATURE.md) |
| Claims and executable evidence | [Claim map](verification/CLAIMS.md) and [verification](verification/README.md) |

## Learn the project

The [30-milestone understanding map](learning/MILESTONES.md) retains 14 background milestones and 16 narrative milestones. Its questions, understanding targets, dependencies, conceptual connections, and source pointers are independent of any learner's background or progress.

The [learning route](learning/README.md) uses one educational anchor: Benjamin Schumacher and Michael D. Westmoreland, *Quantum Processes, Systems, and Information* (2010). The [textbook bridge](learning/SCHUMACHER_WESTMORELAND_BRIDGE.md) connects selected chapters to the project's notation, resource assumptions, worked device, and additional research arguments.

The [LLM reading guide](llms.txt) maps scientific questions, study intentions, and reproduction tasks to their authoritative files.

## Reproduce

Run from the repository root with Python 3.11 or later:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
python scripts/reproduce.py
```

On Windows PowerShell, activate with `.venv\Scripts\Activate.ps1`. The calculation writes a separate generated result and preserves the committed [reference record](results/reference.json). The [reproducibility guide](verification/README.md) gives package installation, documentation checks, figure regeneration, numerical domains, and tested environments.

## Purpose and contact

The project is currently under collaboration, and the manuscript is being written. For questions, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).

Original code and documentation use the [MIT License](LICENSE), copyright 2026 Ruge Lin. Retain applicable third-party notices; scientific citations are scholarly attribution, not an added license condition. See [citation metadata](CITATION.cff) and the [source inventory and AI-assistance disclosure](provenance/README.md).
