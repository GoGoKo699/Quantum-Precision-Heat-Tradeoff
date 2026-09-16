# A finite precision–heat separation

[Home](../README.md) · [Model](MODEL.md) · [Theorem](THEOREM.md) · [Reproduce](REPRODUCIBILITY.md)

Fix the target overlap at s = 0.05. Compare two output-accuracy specifications for exactly the same target states and thermal resource convention.

| Specification | Heat in units of k_B T ln 2 | Meaning |
|---|---:|---|
| Strict branch trace error at most 0.0001 | At least 0.498044180 | Universal finite lower bound |
| Relaxed branch trace error 0.0025 | 0.311484646 | Explicit one-bath-qubit construction |
| Strict specification, plus 16-level auxiliary returned within trace distance 0.0001 | At least 0.496180457 | Lower bound with charged return allowance |

Neither displayed cost is asserted to be the exact finite optimum. The strict lower bound already exceeds the complete cost of the relaxed construction, which establishes the ordering without solving either finite optimization.

## The relaxed device

Its initial bath populations are approximately 0.723943 and 0.276057. The energy gap is approximately 0.964105468 k_B T. Both levels have positive thermal population. The unitary is given in the [construction](CONSTRUCTION.md).

There is no recovery ladder in this comparison. The bath is spent, and its entire mean energy increase is charged. Its final average excited population is one half, so the heat follows directly from the calibrated gap times the change in that population. The intended common transverse polarization remains exactly s.

## Workspace return

For the strict device, a 16-level auxiliary with return tolerance 0.0001 has an entropy-capacity allowance of approximately 0.001863722588 bits. Subtracting it from the strict lower bound gives the third row. This applies to the whole auxiliary marginal, not independently to each small subsystem. Any auxiliary boundary-energy change must be included before interpreting heat as work.

## What is and is not finite here

No parameter tends to zero and the relaxed device uses a single finite thermal qubit. The strict class is nonempty: the same construction at the stricter error has full-rank finite thermal input, although its bare cost is higher.

The comparison is theoretical. The input preparations and ideal joint unitary are specified mathematically. These numbers are not experimental observations, certified hardware tolerances, or a wall-plug saving. Platform-specific error budgets require additional accounting rather than substituting an average gate fidelity for a trace-distance or operator-norm condition.

## Reproduce the values

```bash
python scripts/reproduce.py
```

The script also evaluates selected points on the crossover curve and a finite recovery ladder. Its output is written separately from the committed reference data. The checks compare against independently retained numeric values from the source calculations, not against a newly fitted curve.
