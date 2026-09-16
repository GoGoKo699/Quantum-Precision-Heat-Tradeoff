# Claim-to-evidence map

[Home](../README.md) · [Theorem](THEOREM.md) · [Reproduce](REPRODUCIBILITY.md)

| Claim | Mathematical location | Executable support | Boundary |
|---|---|---|---|
| Dimension-uniform finite lower bound | Proof, Sections 1–7 | `test_kinematic_steps`, `test_spectral_bridge`, `test_complete_auxiliary_ledger` | Finite matrix tests do not prove arbitrary-dimensional statements. |
| Matching optimal limiting curve | Proof, Section 8; Construction | `test_entropy_and_limits`, `test_recovery_sum` | Not the exact finite-parameter optimum. |
| Exact output polarization and prescribed error | Construction, Collision | `test_explicit_device` | Joint-unitary, full-rank thermal construction; not a hardware measurement. |
| Finite strict/relaxed separation | Finite benchmark | `test_finite_regressions`; `scripts/reproduce.py` | Universal lower bound compared with one explicit upper construction. |
| Approximately restored workspace allowance | Theorem, Approximate workspace return | `test_finite_regressions` | Return tolerance is dimension dependent. |
| Consumed purity and record relocation controls | Model and Proof, Section 7 | `test_consumed_purity_control`, `test_record_relocation` | Bath alone need not carry the record when auxiliary correlations are allowed. |
| Inherited theorem and model ingredients | Literature guide | No numerical test certifies attribution or novelty | Source roles and resource models must be compared explicitly. |

The elementary tutorial, formal proof, and executable calculations have different roles. The tutorial explains; the proof establishes mathematical implications of the model; the tests check finite implementations and algebra. The literature guide identifies the inherited foundations and the scope of direct comparisons.

No claim is made here of experimental realization, system-level power savings, an exact finite optimum, or unrestricted multi-use composition. Manuscript preparation remains on hold as stated in the README.
