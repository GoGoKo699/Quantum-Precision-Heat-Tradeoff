# Thirty milestones for understanding the project

[Tutorial home](README.md) · [Model](../science/model.md) · [Theorem](../science/theorem.md) · [Proof](../science/README.md)

This is the common understanding map for this project, for human readers and LLMs. It contains exactly **30 milestones**, with stable IDs M01–M30. The targets and phase allocation depend on the science, not on a particular learner's background, answers, or pace. Together they convey the whole argument and its physical meaning, without claiming coverage of every technical detail.

## How the map fits together

**Background/preliminaries: M01–M14.** Fourteen milestones connect state geometry and operational accuracy to entropy, finite thermal apparatuses, workspace return, and limiting optimization. This bridge is substantial because the result joins quantum information with microscopic heat accounting. The phase moves from individual mathematical and physical objects to the complete conditional thermodynamic task.

**Narrative/innovation: M15–M30.** Sixteen milestones move from a concrete device and the precision scale through the universal converse, charged recovery, matching limit, and its consequences. The final milestones connect the result to finite evidence, prior work, and its scientific meaning. This is a local-to-global argument, not a second list of prerequisites.

The single educational anchor remains Schumacher and Westmoreland, *Quantum Processes, Systems, and Information* (2010). Chapter references use the existing [textbook map](SCHUMACHER_WESTMORELAND_BRIDGE.md#textbook). Primary research sources supply additional proof ingredients; they are not extra educational anchors. The [model](../science/model.md), [theorem](../science/theorem.md), [proof](../science/README.md), and [construction](../science/thermal_implementation.md) take precedence over this teaching map.

Each milestone specifies an understanding target, its earlier dependencies, its role in the argument, a conceptual connection, and source pointers. The sources provide the definitions and derivations needed to understand that target.

Map version: **1**. The settled scientific targets and 14/16 allocation are retained. This common map contains no individual assessment or progress records.

## Phase I — Background and preliminaries

<a id="m01"></a>
### M01 — Qubit states and Bloch geometry

**Central question:** What information is contained in a qubit density operator?

**Understanding target:** Translate between a density operator and its Bloch vector, distinguish pure and mixed states, and interpret polarization as measurement expectation rather than the complete state.

**Depends on:** No earlier milestone; supply the necessary finite-dimensional linear algebra and elementary quantum notation locally.

**Story role:** Establishes the object whose entire output accuracy will be constrained.

**Conceptual connection:** Connects density operators to the observable polarization constrained by the task.

**Sources:** [States](01_task.md#states); [textbook](SCHUMACHER_WESTMORELAND_BRIDGE.md#textbook), Chapters 2–5 and 8.


<a id="m02"></a>
### M02 — Joint systems, marginals, and conditional ensembles

**Central question:** How can the same marginal hide different conditional states or correlations?

**Understanding target:** Use tensor products, partial traces, and equal-prior mixtures; distinguish a conditional joint output from its subsystem marginal and from the ensemble-average state.

**Depends on:** [M01](#m01).

**Story role:** Provides the language for following the system, workspace, and reservoir without discarding branch information.

**Conceptual connection:** Connects conditional ensembles to the marginals used in workspace return and heat accounting.

**Sources:** [Conditional task](01_task.md#conditional-task); [apparatus](../science/model.md#apparatus); [textbook](SCHUMACHER_WESTMORELAND_BRIDGE.md#textbook), Chapters 6 and 8.


<a id="m03"></a>
### M03 — Unitarity and the destination of distinguishability

**Central question:** Where can orthogonality go when a subsystem's outputs become nonorthogonal?

**Understanding target:** Explain preservation of distinguishability in complete unitary outputs and why a pure subsystem marginal forces product form. Use the pure-environment illustration without treating a formal purification or a fresh pure memory as a free thermal resource.

**Depends on:** [M01](#m01), [M02](#m02).

**Story role:** Introduces the information-record mechanism before its quantitative and finite-rank versions.

**Conceptual connection:** Connects unitary information preservation to the environment required by nonorthogonal outputs.

**Sources:** [Exact-output illustration](03_precision.md#exact-illustration); [resource boundary](../science/model.md#resource-boundary); [textbook](SCHUMACHER_WESTMORELAND_BRIDGE.md#textbook), Chapters 5–6 and 8–9.


<a id="m04"></a>
### M04 — Operational error and trace distance

**Central question:** What does the output error guarantee operationally?

**Understanding target:** Interpret half the trace norm as a bound on measurement-probability error, use the qubit Bloch-distance formula, and distinguish maximum branch error from average error, fidelity, and accuracy of one observable.

**Depends on:** [M01](#m01), [M02](#m02).

**Story role:** Fixes the error convention before comparing accuracy scales or costs.

**Conceptual connection:** Connects a norm-defined tolerance to measurement probabilities and the complete output state.

**Sources:** [Trace distance](01_task.md#states); [accuracy convention](../science/model.md#task); [textbook](SCHUMACHER_WESTMORELAND_BRIDGE.md#textbook), Chapters 2–5 and 8, with the local trace-distance derivation.


<a id="m05"></a>
### M05 — Target geometry and the average-state trap

**Central question:** Why is reproducing the average output not the specified task?

**Understanding target:** Interpret the pure target vectors $`(-s,0,\pm\sqrt{1-s^2})`$, their overlap magnitude $`s`$, and their common transverse component. Explain why always preparing their average gives the correct average but branch error $`c/2`$.

**Depends on:** [M01](#m01), [M04](#m04).

**Story role:** Makes the conditional-versus-average distinction concrete before introducing entropy costs.

**Conceptual connection:** Connects Bloch geometry to the distinction between conditional accuracy and an average-state task.

**Sources:** [Targets](01_task.md#conditional-task); [average-state counterexample](01_task.md#average-state); [model](../science/model.md#task).


<a id="m06"></a>
### M06 — Entropy, correlations, and input records

**Central question:** How is information about the input represented without adding a physical label register?

**Understanding target:** Distinguish state entropy, mutual information, and equal-prior Holevo information. Interpret the binary label as bookkeeping, and explain why information in correlations is not determined by either marginal alone. Keep bits separate from natural-log units.

**Depends on:** [M02](#m02), [M03](#m03), [M05](#m05).

**Story role:** Supplies the information quantities needed to connect conditional outputs to environmental change.

**Conceptual connection:** Connects correlations and label information to entropy without supplying an extra physical register.

**Sources:** [Notation](../science/notation.md); [environment-entropy identity](../science/environment_information.md#environment-entropy); [textbook](SCHUMACHER_WESTMORELAND_BRIDGE.md#textbook), Chapter 19, especially Sections 19.1 and 19.3.


<a id="m07"></a>
### M07 — Finite Gibbs reservoirs and thermal bias

**Central question:** What makes a reservoir state thermal rather than a supplied pure memory?

**Understanding target:** Relate Gibbs populations, temperature, gap, and qubit bias. Explain why a finite reservoir with finite energies at positive temperature has full rank, and why approaching a pure thermal qubit may require a growing gap.

**Depends on:** [M01](#m01), [M06](#m06).

**Story role:** Identifies the physical resource used by the construction and a load-bearing assumption of the exact-output obstruction.

**Conceptual connection:** Connects Gibbs populations to a finite thermal resource and its rank.

**Sources:** [Thermal qubit](02_device.md#thermal-qubit); [finite apparatus](../science/model.md#apparatus); [textbook](SCHUMACHER_WESTMORELAND_BRIDGE.md#textbook), Chapters 8–9 and 19.


<a id="m08"></a>
### M08 — Mean heat, driving, and work

**Central question:** Which energy change is counted, and when does it equal supplied work?

**Understanding target:** Read $`Q`$ as the complete reservoir's mean energy increase and $`q=Q/(k_{\mathrm B}T\ln2)`$ as its dimensionless value. Apply the boundary first law $`W=Q+\Delta E_A`$ and distinguish an allowed driven unitary from an energy-conserving operation or a battery-cost model.

**Depends on:** [M02](#m02), [M07](#m07).

**Story role:** Fixes the cost currency before interpreting an entropy inequality as a heat bound.

**Conceptual connection:** Connects reservoir energy changes to heat and the boundary conditions for work equality.

**Sources:** [Heat and work](../science/model.md#heat-work); [direct bath-energy calculation](02_device.md#energy); [textbook](SCHUMACHER_WESTMORELAND_BRIDGE.md#textbook), Chapter 9 and Sections 19.5–19.6.


<a id="m09"></a>
### M09 — Workspace return and consumed entropy capacity

**Central question:** What is restored when the workspace is called returned?

**Understanding target:** Distinguish exact ensemble-average marginal return from conditional return and decorrelation. Explain how an unreturned pure workspace can store the input label and why its positive entropy change must be charged; marginal return alone is not arbitrary correlated multi-use composability.

**Depends on:** [M02](#m02), [M06](#m06), [M08](#m08).

**Story role:** Prevents workspace from becoming an uncharged information sink.

**Conceptual connection:** Connects reusable marginal state resources to the entropy capacity that must be charged.

**Sources:** [Workspace return](../science/model.md#workspace-return); [consumed-workspace example](../science/model.md#resource-boundary); [return precedents](../references/RELATED_WORK.md#returned-workspace).


<a id="m10"></a>
### M10 — Approximate return and growing dimension

**Central question:** Why can a small marginal error hide appreciable entropy consumption?

**Understanding target:** Interpret the dimension-dependent entropy allowance for approximate return. Distinguish fixed workspace dimension with vanishing return error from growing dimension, and identify vanishing allowed entropy increase as a sufficient condition for retaining the same limiting converse.

**Depends on:** [M04](#m04), [M06](#m06), [M09](#m09).

**Story role:** Introduces the uniformity issue that cannot be settled by trace-distance return alone.

**Conceptual connection:** Connects approximate return to the dimension dependence of entropy continuity.

**Sources:** [Approximate-return statement](../science/theorem.md#workspace-return); [sharp continuity source](../references/LITERATURE.md#r6); [workspace comparisons](../references/RELATED_WORK.md#returned-workspace).


<a id="m11"></a>
### M11 — The complete finite apparatus and resource boundary

**Central question:** What must be included before claiming a device has a given heat cost?

**Understanding target:** Assemble the independent input, fixed workspace, and complete Gibbs reservoir under one input-independent unitary. Include all fresh and spent recovery components; exclude a supplied input label, uncharged clean memory, and a mathematical purification from the stated resources. Identify the external source/controller boundary.

**Depends on:** [M03](#m03), [M07](#m07), [M08](#m08), [M09](#m09).

**Story role:** Combines the local resource conventions into one physical implementation class.

**Conceptual connection:** Connects the separate resources into one complete, input-independent finite apparatus.

**Sources:** [Complete apparatus](../science/model.md#apparatus); [charged resources](../science/model.md#resource-boundary); [tutorial boundary](01_task.md#resource-boundary).


<a id="m12"></a>
### M12 — Branch tests and reference-sensitive channel accuracy

**Central question:** What additional inputs does a full-channel accuracy requirement test?

**Understanding target:** Distinguish two basis-output tests from half-diamond distance to the target measure-and-prepare channel, including reference-entangled inputs. Explain input dephasing and why an unmodified channel's coherent action is not determined by its basis outputs.

**Depends on:** [M02](#m02), [M04](#m04), [M05](#m05), [M11](#m11).

**Story role:** Prepares the channel-equivalence consequence without assuming that branch accuracy already certifies it.

**Conceptual connection:** Connects branch tests to channel distinguishability while retaining coherent-reference inputs.

**Sources:** [Channel definitions and scope](../science/theorem.md#channel-equivalence); [dephased-channel identity](../science/channel_accuracy.md#dephased-channel-distance); [textbook](SCHUMACHER_WESTMORELAND_BRIDGE.md#textbook), Chapter 9 for reduced dynamics. The half-diamond bridge is supplied locally, with primary attribution in the proof.


<a id="m13"></a>
### M13 — Infima, positive-error limits, and uniformity

**Central question:** How can finite devices have an optimal limit without an attained finite optimum?

**Understanding target:** Distinguish an infimum from a minimizer, a finite bound from a joint limiting law, and a dimension-uniform estimate from a fixed-dimension result. Keep positive error at each stage separate from its limiting ratio, and track resources that may grow along a sequence.

**Depends on:** [M04](#m04), [M07](#m07), [M10](#m10), [M11](#m11).

**Story role:** Supplies the optimization language needed to combine a universal converse with increasingly accurate constructions.

**Conceptual connection:** Connects finite estimates and resource growth to an infimum over parameter-dependent devices.

**Sources:** [Finite implementations and limits](../science/model.md#limits); [precise crossover statement](../science/theorem.md#optimal-crossover); [limiting procedure](03_precision.md#crossover).


<a id="m14"></a>
### M14 — Synthesis of the conditional thermodynamic task

**Central question:** What exactly is optimized, constrained, supplied, and restored?

**Understanding target:** State the two-input task, maximum branch trace-distance constraint, equal-prior mean heat, complete finite apparatus, and ensemble-marginal workspace return in one coherent account. Explain why the small average-state entropy decrease does not settle this conditional task, and identify the difference between constructing an example and proving a universal bound.

**Depends on:** [M05](#m05), [M06](#m06), [M08](#m08), [M09](#m09), [M10](#m10), [M11](#m11), [M12](#m12), [M13](#m13).

**Story role:** Integrates the background into the precise question answered by the research.

**Conceptual connection:** Connects all background concepts into the conditional thermodynamic optimization.

**Sources:** [Model](../science/model.md); [task and average](01_task.md); [proof dependencies](../science/README.md#dependencies).


## Phase II — Narrative and innovation

<a id="m15"></a>
### M15 — A finite collision that meets both output tests

**Central question:** How does one fixed thermal interaction produce the two required approximate outputs?

**Understanding target:** Follow the rotation and controlled flip using the supplied basis action. Connect the chosen angle and Gibbs bias to the correct transverse polarization, trace error exactly $`\epsilon`$, conditional bath populations, and directly calculated bare heat. Recognize this as an achievable upper bound, not optimality.

**Depends on:** [M14](#m14).

**Story role:** Starts the narrative with a complete physical example rather than an abstract lower-bound formula.

**Conceptual connection:** Connects a specified unitary and Gibbs state to outputs, error, and measured reservoir energy.

**Sources:** [Worked device](02_device.md); [collision construction](../science/thermal_implementation.md#collision); [textbook](SCHUMACHER_WESTMORELAND_BRIDGE.md#textbook), Chapter 18 only as needed for the circuit notation.


<a id="m16"></a>
### M16 — Why squared overlap sets the precision scale

**Central question:** Why does error relative to squared overlap matter even when the leading polarization is exact?

**Understanding target:** Relate the first-order transverse shift to the second-order departure from the pole required by purity. Interpret the constructed bias $`b=s/[2\sqrt{u(1-u)}]`$ with $`u=(1-c)/2+\epsilon`$, and explain why $`\epsilon\ll s`$ alone does not fix the limiting cost.

**Depends on:** [M05](#m05), [M13](#m13), [M15](#m15).

**Story role:** Extracts the controlling scale from the example while keeping geometric motivation distinct from a universal proof.

**Conceptual connection:** Connects first-order polarization and second-order population changes to the governing ratio.

**Sources:** [Two precision scales](03_precision.md#two-scales); [collision parameters](../science/thermal_implementation.md#collision); [crossover interpretation](03_precision.md#crossover).


<a id="m17"></a>
### M17 — Turning output accuracy into kinematic constraints

**Central question:** What must every accurate device satisfy before thermodynamics enters?

**Understanding target:** Explain the wrong-basis probability bound $`\bar\delta\le d`$ and the common-coherence constraint $`|z_0+z_1|\ge s-2\epsilon`$, with their notation supplied. Distinguish actual errors from their upper bound and identify exactly where the two conditional tests are used.

**Depends on:** [M14](#m14), [M16](#m16).

**Story role:** Begins the converse with consequences of the task shared by all implementations.

**Conceptual connection:** Connects operational accuracy to the kinematic constraints common to every implementation.

**Sources:** [Lemma 1](../science/kinematics.md#output-tests); [finite parameters](../science/theorem.md#finite-bound).


<a id="m18"></a>
### M18 — Covering every allowed unitary

**Central question:** How does the converse avoid depending on the chosen two-qubit circuit?

**Understanding target:** Interpret the complete cosine–sine decomposition, transition contraction, and comparison states $`\tau_i=V_i\Omega V_i^\dagger`$. Explain coverage of singular blocks and rank-deficient environment states, distinguish comparison states from physical outputs, and identify why the coherence replacement error must be of order $`d`$ rather than $`\sqrt d`$.

**Depends on:** [M03](#m03), [M11](#m11), [M17](#m17).

**Story role:** Upgrades output constraints to an exhaustive apparatus-independent kinematic description.

**Conceptual connection:** Connects those constraints to a complete parametrization rather than a chosen circuit family.

**Sources:** [Lemma 2](../science/kinematics.md#unitary-reduction); [complete CS source](../references/LITERATURE.md#r7). This is a research bridge beyond the textbook device calculation.


<a id="m19"></a>
### M19 — Spectral separation forced by coherent outputs

**Central question:** Why must the comparison environment states differ appreciably at high precision?

**Understanding target:** Interpret the mixed-eigenbasis triangular discrimination $`\mathcal T`$ and the weighted Cauchy–Schwarz step $`|\ell|^2\le4\bar\delta\mathcal T`$. Combine its direction with the coherence lower bound to obtain $`\mathcal T\ge b_0^2`$, including zero spectral weights without division by zero.

**Depends on:** [M18](#m18).

**Story role:** Converts required coherence with small transition probability into quantitative environmental separation.

**Conceptual connection:** Connects coherence with small transition probabilities to environmental spectral separation.

**Sources:** [Lemma 3](../science/kinematics.md#spectral-discrimination); [bias bound](../science/theorem.md#finite-bound).


<a id="m20"></a>
### M20 — From noncommuting comparison states to information

**Central question:** How does spectral separation force an input record without assuming commuting states?

**Understanding target:** Explain the chain $`\chi\ge\mathrm{JS}(P,Q)\ge J_2(\sqrt{\mathcal T})`$. Distinguish algebraic comparison distributions from a jointly measurable pair of eigenbases, identify the direction of the Golden–Thompson entropy comparison, and interpret the sharp scalar step and mirrored-binary equality example.

**Depends on:** [M06](#m06), [M19](#m19).

**Story role:** Turns the kinematic quantity into information while preserving the sharp limiting function.

**Conceptual connection:** Connects noncommuting spectral data to a sharp information bound through attributed inequalities.

**Sources:** [Lemma 4](../science/environment_information.md#information-bound); [scalar inequality source](../references/LITERATURE.md#r4); [Golden–Thompson source](../references/LITERATURE.md#r8).


<a id="m21"></a>
### M21 — Transfer to the actual environment without a dimension penalty

**Central question:** Why does information in comparison states imply information in the physical outputs?

**Understanding target:** Follow the disturbance estimate and the correction $`g(f(d))`$. Explain why conditional-entropy continuity is applied to the binary classical label, not bounded using the reservoir dimension, and why the purification used in the estimate adds no physical resource.

**Depends on:** [M04](#m04), [M06](#m06), [M18](#m18), [M20](#m20).

**Story role:** Closes the gap between an algebraic comparison and an actual environmental record uniformly over apparatus size.

**Conceptual connection:** Connects algebraic comparison states to physical reservoir outputs without a size-dependent error.

**Sources:** [Lemma 5](../science/environment_information.md#environment-transfer); [conditional-entropy continuity source](../references/LITERATURE.md#r5); [resource boundary](../science/model.md#resource-boundary).


<a id="m22"></a>
### M22 — Converting retained information into the finite heat bound

**Central question:** Which steps turn the environmental record into unavoidable charged heat?

**Understanding target:** Trace the route from actual Holevo information to $`\Delta H_E\ge L(s,\epsilon)`$ and then to the Gibbs/workspace ledger. Interpret the kinematic bias bound, transfer correction, output-entropy correction, independent nonnegative entropy bound, and retained correlation and disequilibrium terms. Distinguish exact return, consumed workspace, and the approximate-return allowance, whose resulting heat bound is not automatically clipped to zero.

**Depends on:** [M06](#m06), [M08](#m08), [M09](#m09), [M10](#m10), [M21](#m21).

**Story role:** Completes the universal finite converse and its resource-sensitive interpretation.

**Conceptual connection:** Connects environmental information to actual bath heat after all workspace resources are charged.

**Sources:** [Lemma 6](../science/environment_information.md#environment-entropy); [Lemma 7](../science/heat_bound.md#heat-ledger); [finite theorem](../science/theorem.md#finite-bound); [approximate return](../science/theorem.md#workspace-return).


<a id="m23"></a>
### M23 — Recovering work without hiding reservoir costs

**Central question:** How can recovery lower the collision cost while preserving the specified system outputs?

**Understanding target:** Follow the finite ladder of Gibbs qubits and successive swaps. Count the working and all spent qubits, explain where correlations move, and interpret the finite right-Riemann-sum error. Distinguish restoring the working bath qubit from restoring the complete reservoir or erasing its record.

**Depends on:** [M15](#m15), [M16](#m16), [M22](#m22).

**Story role:** Supplies the improved achievable cost required to match the converse rather than merely exhibit a finite device.

**Conceptual connection:** Connects the explicit collision to a better upper bound through fully counted thermal recovery.

**Sources:** [Recovery and finite residual](../science/thermal_implementation.md#recovery); [complete ledger](../science/thermal_implementation.md#heat-ledger); [successive-swap source](../references/LITERATURE.md#r1).


<a id="m24"></a>
### M24 — Matching the bounds to obtain the optimal crossover

**Central question:** Why do the converse and construction determine the same optimal limiting heat?

**Understanding target:** Assemble the lower and upper limiting arguments for finite $`r=\lim\epsilon/s^2`$. Explain $`b_0,b\to(1+4r)^{-1/2}`$, vanishing finite corrections, and a finite recovery length chosen for each positive-error stage. Conclude $`q_{\min}\to F(r)`$ without claiming a finite-parameter formula or exchanging limits without uniform control.

**Depends on:** [M13](#m13), [M16](#m16), [M19](#m19), [M21](#m21), [M22](#m22), [M23](#m23).

**Story role:** Integrates the two directions into the main optimality statement.

**Conceptual connection:** Connects the universal converse and construction into the same optimal limiting function.

**Sources:** [Matching-limit proof](../science/heat_bound.md#matching-limit); [canonical crossover](../science/theorem.md#optimal-crossover).


<a id="m25"></a>
### M25 — The surviving cost and the singular endpoint

**Central question:** What remains costly when the average entropy decrease vanishes?

**Understanding target:** Interpret the persistent correlation contribution in the bath-only construction and the complete-environment record when workspace is present. Explain $`F(0)=1`$ through positive-error finite stages, the possible growth of gaps and recovery resources, and the difference between a large-ratio expansion of the curve and a uniform theorem on arbitrary divergent-ratio paths.

**Depends on:** [M06](#m06), [M08](#m08), [M09](#m09), [M24](#m24).

**Story role:** Gives the limiting law its physical interpretation and guards its endpoint and resource qualifications.

**Conceptual connection:** Connects the limit to surviving correlations, positive finite errors, and growing resources.

**Sources:** [Cost location](03_precision.md#cost-location); [construction ledger](../science/thermal_implementation.md#heat-ledger); [limit scope](../science/theorem.md#optimal-crossover); [finite resources](../science/model.md#limits).


<a id="m26"></a>
### M26 — Full-channel accuracy at exactly the same heat infimum

**Central question:** Why does a stronger accuracy criterion have the same optimal cost here?

**Understanding target:** Explain the degenerate Gibbs qubit that dephases the input at unchanged equal-prior heat and workspace return. Use the dephased-channel distance identity and both directions of the infimum comparison. Distinguish equality of optimal costs from certification of an arbitrary unmodified apparatus, and keep the heat ensemble fixed even though accuracy includes entangled references.

**Depends on:** [M12](#m12), [M22](#m22), [M24](#m24).

**Story role:** Extends the operational meaning of the crossover through a physically charged, model-preserving conversion.

**Conceptual connection:** Connects branch-feasible devices to full-channel accuracy through an allowed thermal conversion.

**Sources:** [Channel corollary](../science/theorem.md#channel-equivalence); [physical conversion and norm proof](../science/channel_accuracy.md#channel-equivalence); [construction channel](../science/thermal_implementation.md#channel-error).


<a id="m27"></a>
### M27 — Why exact targets cannot be produced cyclically

**Central question:** Why is exactly zero error impossible even with nonthermal returned workspace?

**Understanding target:** Connect pure system outputs, rank preservation, full bath rank, and positivity of the returned average. Explain why both environmental branches must occupy the same support although unitarity would require their orthogonality. Include rank-deficient workspace, unequal conditional marginals, and allowed final correlations; distinguish an empty exact-output feasible set from a heat value attained by a device.

**Depends on:** [M03](#m03), [M07](#m07), [M09](#m09), [M11](#m11), [M25](#m25).

**Story role:** Closes the exact-versus-limiting distinction using the complete finite apparatus rather than a pure-environment analogy.

**Conceptual connection:** Connects purity, rank, support, and marginal return to the impossibility of an exact finite device.

**Sources:** [Exact-output proposition](../science/theorem.md#exact-output-obstruction); [support-and-rank proof](../science/exact_outputs.md#exact-output-obstruction); [consumed-workspace boundary](../science/model.md#resource-boundary).


<a id="m28"></a>
### M28 — Finite consequences and implementation evidence

**Central question:** What does the finite strict-versus-relaxed comparison actually establish?

**Understanding target:** Interpret the same-overlap comparison of a strict universal lower bound with one relaxed device's calculated heat. Explain why the separation needs no recovery claim, neither number is a finite optimum, and workspace allowances must be charged. Distinguish analytic proofs, deterministic numerical checks, and experimental measurements.

**Depends on:** [M22](#m22), [M23](#m23), [M24](#m24), [M26](#m26), [M27](#m27).

**Story role:** Connects the limiting story to a finite consequence and the exact evidential role of the runnable repository.

**Conceptual connection:** Connects the analytical result to a finite comparison and the distinct role of numerical evidence.

**Sources:** [Finite benchmark](../science/finite_benchmark.md); [claim-to-evidence map](../verification/CLAIMS.md); [reproducibility guide](../verification/README.md).


<a id="m29"></a>
### M29 — Inherited ingredients and the project's contribution

**Central question:** What is specific to this result rather than already supplied by established thermodynamics?

**Understanding target:** Separate inherited heat identities, recovery, operation-dependent cost, return conventions, and information inequalities from the dimension-uniform positive-error crossover for this task. Compare microscopic mean heat with battery cost and collective work rates. State the significance of precision-dependent heat while retaining single-use, driving, resource-growth, and return qualifications rather than asserting device-independent engineering performance.

**Depends on:** [M14](#m14), [M24](#m24), [M26](#m26), [M27](#m27), [M28](#m28).

**Story role:** Places the integrated result in its scientific context without treating an adjacent theorem or a model precedent as its proof.

**Conceptual connection:** Connects the contribution to its predecessors without equating different resource models.

**Sources:** [Direct comparisons](../references/RELATED_WORK.md); [assumptions and primary sources](../references/LITERATURE.md); [claim boundaries](../verification/CLAIMS.md).


<a id="m30"></a>
### M30 — Synthesis of the full result and its boundaries

**Central question:** Can the entire precision–heat story be explained and interrogated as one argument?

**Understanding target:** Connect the conditional task, squared-overlap precision scale, forced record, heat ledger, matching finite construction, and optimal limit. Incorporate channel equivalence, exact-output impossibility, and the finite benchmark. Reason about a changed assumption—such as consumed workspace, average-only accuracy, or a fixed resource cap—without transferring a theorem beyond its hypotheses, and locate the canonical evidence for each claim.

**Depends on:** [M14](#m14), [M24](#m24), [M25](#m25), [M26](#m26), [M27](#m27), [M28](#m28), [M29](#m29).

**Story role:** Completes global project understanding. This integrative milestone connects the complete scientific argument and its boundaries.

**Conceptual connection:** Connects the task, proof mechanism, attainable limit, consequences, and resource boundaries.

**Sources:** [Model](../science/model.md); [theorem](../science/theorem.md); [proof](../science/README.md); [construction](../science/thermal_implementation.md); [claim map](../verification/CLAIMS.md); [comparisons](../references/RELATED_WORK.md).

## Coverage

The final synthesis connects the whole project. Technical details remain in the linked scientific arguments, and this map does not assert exhaustive mastery or independent validation.
