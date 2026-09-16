# A finite precision–heat separation

[Home](../README.md) · [Model](MODEL.md) · [Theorem](THEOREM.md#finite-bound) · [Reproduce](REPRODUCIBILITY.md)

<a id="comparison"></a>
## Compare two accuracy specifications

Fix the target overlap at $s=0.05$. The target states and thermal resource convention stay the same. Heat values below use $k_{\mathrm B}T\ln2$ as one unit. Every number is a theoretical calculation.

| Device specification | Heat in these units |
|---|---:|
| Strict: branch error at most $0.0001$ | At least **0.498044180** |
| Relaxed: branch error $0.0025$ | **0.311484646** |
| Strict, with the workspace allowance below | At least **0.496180457** |

The strict values are universal finite **lower bounds**. The relaxed value is the complete heat of **one explicit construction**. Neither is asserted to be the exact finite optimum. The strict lower bound already exceeds the relaxed construction's cost, establishing a finite separation without solving either optimization problem.

<a id="relaxed-device"></a>
## The relaxed device

Its initial bath populations are approximately $0.723943$ and $0.276057$. Both are positive. Its energy gap is

```math
\frac{\Delta}{k_{\mathrm B}T}\simeq0.964105468.
```

The [collision unitary](CONSTRUCTION.md#collision) preserves the intended common transverse polarization exactly. No recovery ladder is used in this comparison. The bath is spent, and its entire mean energy increase is charged.

The final average excited population is $1/2$. Multiplying its increase by the calibrated gap gives the displayed heat:

```math
Q=\Delta\left(\frac12-p_1\right).
```

The [tutorial calculation](tutorial/02_device.md#energy) derives the bath populations, system errors, and energy together.

## Workspace return

For the strict device, consider a 16-level auxiliary whose **ensemble-average marginal** returns within trace distance $0.0001$ of its initial state. Its entropy-capacity allowance is approximately $0.001863722588$ bits. Subtracting this allowance from the strict lower bound gives the third row.

The allowance applies to the whole auxiliary marginal, not separately to each small subsystem. Any auxiliary boundary-energy change must also be included before interpreting heat as work. See the [return correction](THEOREM.md#workspace-return) and [boundary energy convention](MODEL.md#heat-work).

## What is finite here

No parameter tends to zero. The relaxed device uses one finite thermal qubit. The strict class is nonempty: the same construction at the stricter error has a full-rank finite thermal input, although its bare cost is higher.

The input preparations and ideal joint unitary are specified mathematically. These values are not experimental observations, certified hardware tolerances, or a wall-plug saving. A platform-specific error budget must account for these state tests; replacing their metric by average gate fidelity changes the specification.

## Reproduce the values

From the repository root, run

```bash
python scripts/reproduce.py
```

The script also evaluates selected crossover points and a finite recovery ladder. Its output is written separately from the committed [reference data](../results/reference.json). The checks compare against independently retained values from the source calculations. The [claim map](CLAIMS.md) connects these computed examples to the proof and named tests.
