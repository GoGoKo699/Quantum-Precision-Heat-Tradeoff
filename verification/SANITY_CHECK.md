# Full sanity check

[Verification](README.md) · [Exact statements](../science/theorem.md) · [Claim map](CLAIMS.md)

The audit started from `139e74ec133369f63eba49df723e664c087fac5f`. The local baseline's Git tree was verified against the complete tree of that revision. This check covers scientific consistency, inherited ingredients, computational reproduction, learning structure, package behavior, dependencies, and presentation. Repairs concern numerical evaluation and maintenance, not the mathematical claims.

## Scientific consistency

The connected argument was read against the model, theorem, finite example, interpretation, and learning material. No invalid analytical step was identified in this pass. The following load-bearing distinctions were checked explicitly:

| Argument | Check |
|---|---|
| [Unitary reduction](../science/kinematics.md) | The complete cosine–sine decomposition covers all finite joint unitaries, including singular blocks. The coherence replacement error is first order in the wrong-basis probability, not its square root. |
| [Environmental information](../science/environment_information.md) | Mixed-spectral weights have the required normalization. The Golden–Thompson conversion has the correct inequality direction. Zero spectral weights and rank-deficient initial states are covered. |
| [Transfer to physical outputs](../science/environment_information.md#environment-transfer) | The trace-distance correction is applied before using the environmental record. Conditional-entropy continuity is controlled by the binary label dimension, not the bath dimension. |
| [Heat and workspace](../science/heat_bound.md) | Gibbs structure is applied only to the actual thermal reservoir. Consumed workspace entropy, final correlations, heat units, and boundary work are not interchanged. |
| [Matching limit](../science/heat_bound.md#matching-limit) | The converse is uniform before the infimum is taken. Every approximating device has positive error and finite resources; recovery resources may grow. The statement remains restricted to finite limiting error-to-squared-overlap ratios. |
| [Thermal construction](../science/thermal_implementation.md) | The gate order, conditional outputs, bath populations, direct heat, and complete recovery sum agree with the stated resource model. |
| [Channel accuracy](../science/channel_accuracy.md) | Both directions of the equality of infima are justified. Thermal dephasing preserves the charged input ensemble; it is not certification of an unmodified unknown channel from two tests. |
| [Exact-output obstruction](../science/exact_outputs.md) | Purity, full bath rank, and positive ensemble-average workspace return force the support contradiction even for rank-deficient workspace. An empty exact feasible set is not a heat value of a finite device. |

The finite strict-versus-relaxed comparison continues to compare a universal lower bound with one explicit upper construction, not two exact finite optima. Marginal workspace return still does not assert independent reuse on arbitrary correlated future inputs. The complete environment, not necessarily the thermal bath alone, carries the constrained information.

## Primary-source recheck

The recheck examined the specific imported statements rather than treating subject similarity as sufficient attribution: [Reeb–Wolf, Theorem 3 and Proposition 8](../references/LITERATURE.md#r1); [Aksak–Turgut, Theorem 4 and bath/isometry conventions](../references/LITERATURE.md#r2); [Bedingham–Maroney, Equation (9)](../references/LITERATURE.md#r3); [Nishiyama, Definition 3, Theorem 1 and Equation (29)](../references/LITERATURE.md#r4); [Winter, Lemma 2 and its classical–quantum specialization](../references/LITERATURE.md#r5); [Audenaert, Theorem 1](../references/LITERATURE.md#r6); [Sutton's complete CS decomposition](../references/LITERATURE.md#r7); and the [Golden–Thompson trace inequality](../references/LITERATURE.md#r8).

The scalar discrimination inequality is inherited, not a new divergence theorem. The exact-channel predecessor permits bath and isometry conventions different from this repository's finite unitary devices. The substitution into the published excess-heat inequality concerns that inequality, not every possible method of the earlier paper. These distinctions remain in the [direct comparisons](../references/RELATED_WORK.md).

This was a check of the declared proof dependencies and comparisons, not an exhaustive new literature search or a revalidation of every external link. The existing publisher-based textbook pointers were retained; access to the publisher's contents endpoint was unavailable during this pass.

## Repairs and regression checks

The audit found three numerical edge failures. The original logarithmic evaluation of `j2` could lose relative precision and return zero for small positive biases. Forming `4*r` in `crossover` could overflow for a finite representable ratio. The reference comparator could accept `NaN` because its tolerance comparison did not explicitly reject nonfinite values.

The repairs use the positive series already derived in the scientific account, an algebraically equivalent overflow-free bias expression, and explicit finiteness checks. Four additional tests in [test_numerical_edges.py](../tests/test_numerical_edges.py) compare small-bias and large-ratio outputs with 100-digit standard-library decimal calculations, check the series switch, and reject nonfinite nested reference values. These are numerical regressions, not an extension of the thermodynamic theorem to divergent-ratio paths.

All 28 Python tests pass, including the original scientific tests. Reference reproduction is byte-for-byte unchanged for the existing output record, and both figures regenerate without changes. The mathematical-source records and all 30 milestone understanding targets remain unchanged. The [source map](source_map.json) records old and new hashes for the three protected files that required maintenance; original preservation records have not been silently discarded.

The source-distribution manifest no longer requests nonexistent BibTeX files. The structured bibliography remains JSON. Local-render metadata now reports the installed parser versions rather than a hardcoded old version.

## Dependencies

The [baseline diagnostics](https://github.com/GoGoKo699/Quantum-Precision-Heat-Tradeoff/actions/runs/39290594290) found three moderate-severity advisories affecting the single `markdown-it` 14.1.0 package: [GHSA-38c4-r59v-3vqw](https://github.com/advisories/GHSA-38c4-r59v-3vqw), [GHSA-6v5v-wf23-fmfq](https://github.com/advisories/GHSA-6v5v-wf23-fmfq), and [GHSA-253c-mchw-3w2r](https://github.com/advisories/GHSA-253c-mchw-3w2r). They concern denial-of-service behavior in Markdown processing. The repository disables the optional typographer and linkify modes, but that is not a substitute for updating the affected package.

The targeted same-major update to **14.3.3** passed all 23 documentation regressions and all active-page checks. The [dependency-repair run](https://github.com/GoGoKo699/Quantum-Precision-Heat-Tradeoff/actions/runs/39291281757) reported zero known npm advisories for the resulting lockfile. The isolated Python dependency audit reported zero known advisories in the resolved development requirements. No claim of comprehensive security certification follows from those database checks. Deprecation notices for the retained MathJax version and Actions runtimes are distinct from reported dependency vulnerabilities.

## Learning, packaging, and display

The shared learning map still has exactly M01–M30 with the 14/16 phase allocation, backward dependencies, and one Schumacher–Westmoreland anchor. Its understanding targets remain learner independent. Personal coaching procedures and learner records are absent from the shared scientific tree.

Local Markdown and MathJax checks validate active pages, fragments, code-line links, images, and equation source. Package verification covers the extracted source distribution and an installed wheel imported outside the checkout. The numerical code remains double precision; improved small-bias evaluation does not remove the documented limitations near thermal endpoint rounding.

Fresh actual GitHub pages were loaded at revision `b96aeb6b003c3ed24599bce6d967b4a30171a8b5`, which adds diagnostics but leaves the inspected content identical to the audited main revision. Chromium used a **1440 by 1000** desktop viewport. The [run artifact](https://github.com/GoGoKo699/Quantum-Precision-Heat-Tradeoff/actions/runs/39290594290) retains the per-page DOM report and full-page and detail screenshots for these 20 pages:

- README; the learning entrance, textbook bridge, three worked chapters, and milestone map.
- The science entrance, model, theorem, kinematics, environmental information, heat bound, thermal implementation, channel accuracy, exact-output obstruction, finite benchmark, and interpretation.
- Direct related-work comparisons and the verification entrance.

The rendered DOM showed no mathematical errors, exposed protected delimiters, oversized mathematics, or unloaded content images. The detail screenshots were visually inspected for mathematical typography, tables, and navigation. This is a desktop check of identified pages, not a guarantee for every viewport or future renderer. The new maintenance report and appended verification link receive the local documentation checks separately.

## Assessment boundary

The scientific statements, proof equations, attribution, numerical reference values, and learning targets are unchanged. The repairs strengthen numerical and documentation reliability. This sanity check is an author-side analytical and reproducibility audit, not independent external validation, an experimental test, or a guarantee of publication novelty.
