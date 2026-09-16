# Claim-to-evidence map

[Home](../README.md) · [Theorem](THEOREM.md) · [Proof](PROOF.md#dependencies) · [Reproduce](REPRODUCIBILITY.md)

The proof establishes implications of the physical model. The tests check finite matrices and implemented formulas; the committed result record contains computed examples. Source comparisons establish attribution and model distinctions. None of these is an experimental measurement.

<a id="finite-lower-bound"></a>
## Dimension-uniform finite lower bound

**Claim:** every allowed implementation satisfies the [finite lower bound](THEOREM.md#finite-bound), with its explicit workspace correction.

**Mathematical evidence:** [Lemmas 1–4](PROOF.md#output-tests) derive the information bound; [Lemma 5](PROOF.md#environment-transfer) transfers it to actual outputs; [Lemmas 6–7](PROOF.md#environment-entropy) establish environment entropy and heat accounting.

**Executable support:** [test_kinematic_steps](../tests/test_core.py#L104), [test_spectral_bridge](../tests/test_core.py#L90), and [test_complete_auxiliary_ledger](../tests/test_core.py#L134). These check finite unitary instances, including selected singular blocks and rank-deficient states, spectral inequalities, and the exact energy ledger. Finite samples do not establish arbitrary-dimensional validity.

<a id="optimal-limit"></a>
## Matching optimal limiting curve

**Claim:** the [positive-error joint limit](THEOREM.md#optimal-crossover) equals the established crossover function.

**Mathematical evidence:** the [limiting match](PROOF.md#matching-limit) combines the uniform lower bound with the [charged recovery construction](CONSTRUCTION.md#recovery).

**Executable support:** [test_entropy_and_limits](../tests/test_core.py#L25), [test_recovery_sum](../tests/test_core.py#L78), and the formula implementations in [qph/core.py](../qph/core.py). These check endpoint conventions and finite recovery sums and inequalities. They do not identify an exact finite-parameter optimum.

<a id="finite-device"></a>
## Explicit conditional outputs and energy cost

**Claim:** one fixed finite thermal device produces the prescribed conditional outputs with trace error exactly equal to the requested tolerance.

**Mathematical evidence:** the [collision calculation](CONSTRUCTION.md#collision), its [channel-error property](CONSTRUCTION.md#channel-error), and the [complete heat ledger](CONSTRUCTION.md#heat-ledger).

**Executable support:** [test_targets_and_overlap](../tests/test_core.py#L47) and [test_explicit_device](../tests/test_core.py#L64) directly evaluate states, unitarity, positive initial thermal populations, branch errors, polarization, and reservoir energy. The computed examples are in [results/reference.json](../results/reference.json).

<a id="finite-separation"></a>
## Finite strict and relaxed accuracy comparison

**Claim:** the established strict-error lower bound exceeds the heat of the displayed relaxed-error device at the stated overlap.

**Mathematical evidence:** the [finite benchmark](FINITE_BENCHMARK.md#comparison) compares the universal lower bound with the [bare relaxed device](FINITE_BENCHMARK.md#relaxed-device).

**Executable support:** [test_finite_regressions](../tests/test_core.py#L53), [scripts/reproduce.py](../scripts/reproduce.py), and [results/reference.json](../results/reference.json). The comparison uses a lower bound and one achievable upper bound; neither is described as the finite optimum.

<a id="workspace"></a>
## Returned and consumed workspace

**Claim:** approximate return has a dimension-dependent entropy allowance, and a consumed pure workspace must be charged.

**Mathematical evidence:** the [return statement](THEOREM.md#workspace-return), [resource boundary examples](MODEL.md#resource-boundary), and [Gibbs/workspace ledger](PROOF.md#heat-ledger). The [finite workspace comparison](FINITE_BENCHMARK.md#workspace-return) uses the stated allowance.

**Executable support:** [test_finite_regressions](../tests/test_core.py#L53), [test_consumed_purity_control](../tests/test_core.py#L156), and [test_record_relocation](../tests/test_core.py#L170). The controls illustrate entropy consumption and record relocation into workspace correlations; the bath alone need not retain the input record.

<a id="source-roles"></a>
## Inherited ingredients and comparisons

The [proof source register](LITERATURE.md#r1), [assumption register](LITERATURE.md#assumption-register), and [direct comparisons](RELATED_WORK.md) identify inherited identities, inequalities, constructions, and model conventions. Each cited theorem has a defined role. No numerical test certifies attribution or exhaustive novelty.

The [tutorial](tutorial/README.md) explains the task and finite device before introducing what a universal converse requires. It is an educational route, not a replacement for the canonical proof.
