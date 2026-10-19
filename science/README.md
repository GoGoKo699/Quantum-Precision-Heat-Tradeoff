# The precision–heat result

[Home](../README.md) · [Physical model](model.md) · [Theorem](theorem.md) · [Notation](notation.md) · [Learning route](../learning/README.md)

The task converts two equally likely orthogonal qubit inputs into prescribed nearly orthogonal pure targets. The apparatus must satisfy both conditional output tests. Their small average entropy change does not determine the cost of the conditional operation.

The [theorem](theorem.md#optimal-crossover) identifies the optimal positive-error limiting heat as error divided by squared target overlap tends to a finite ratio. The bound allows arbitrary finite Gibbs reservoirs and input-independent workspace. Exact return concerns the workspace's ensemble-average marginal, with final correlations allowed.

Start with the [physical model](model.md), then the [formal statements](theorem.md). For a complete example before the converse, read the [thermal implementation](thermal_implementation.md) and [finite comparison](finite_benchmark.md). The [interpretation](interpretation.md) connects the arguments and their physical boundaries.

<a id="dependencies"></a>
## Proof dependencies

| Step | Authoritative argument | What it passes to the next step |
|---|---|---|
| 1. Conditional output requirements | [Lemma 1](kinematics.md#output-tests) | Small wrong-basis probability and a required common coherence. |
| 2. Every allowed interaction | [Lemma 2](kinematics.md#unitary-reduction) | A complete unitary parametrization and comparison environment states. |
| 3. Spectral separation | [Lemma 3](kinematics.md#spectral-discrimination) | A lower bound on the specified spectral discrimination. |
| 4. Noncommuting information comparison | [Lemma 4](environment_information.md#information-bound) | Holevo information bounded by the sharp binary function. |
| 5. Actual environment | [Lemma 5](environment_information.md#environment-transfer) | The physical record, with a dimension-uniform correction. |
| 6. Environment entropy | [Lemma 6](environment_information.md#environment-entropy) | A nonnegative entropy increase for the complete environment. |
| 7. Gibbs and workspace accounting | [Lemma 7](heat_bound.md#heat-ledger) | Actual bath heat, with consumed workspace entropy charged. |
| 8. Matching construction | [Limiting match](heat_bound.md#matching-limit) and [recovery](thermal_implementation.md#recovery) | The same optimal joint limiting law from below and above. |

The first six steps use a fixed input-independent environment state; they permit rank deficiency and do not invoke Gibbs structure. The thermal assumption enters only for the actual reservoir in the heat ledger. The [notation reference](notation.md) distinguishes comparison states from physical outputs and bits from natural-log units.

## Consequences and finite evidence

[Full-channel accuracy](channel_accuracy.md) has exactly the same optimal heat infimum as the two branch tests. Its physical dephasing conversion preserves the equal-prior heat and workspace return, without certifying an unmodified apparatus from two tests. The [support-and-rank argument](exact_outputs.md) excludes exact nonorthogonal pure outputs with a finite full-rank bath and exactly returned workspace.

The [finite comparison](finite_benchmark.md) contrasts a strict universal lower bound with one relaxed device's directly computed heat. Neither value is asserted to be a finite optimum. [Claims and supporting checks](../verification/CLAIMS.md) connect each statement to its argument and executable evidence.

The [related-work account](../references/RELATED_WORK.md) compares tasks, resources, costs, and error conventions. The [source register](../references/LITERATURE.md) attributes imported identities and inequalities. Finite tests support implementation checks; the general statement is established by the written arguments.
