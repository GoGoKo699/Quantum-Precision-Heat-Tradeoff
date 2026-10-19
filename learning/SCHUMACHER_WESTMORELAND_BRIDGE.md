# From Schumacher–Westmoreland to the precision–heat task

[Learning route](README.md) · [Milestones](MILESTONES.md) · [Science](../science/README.md)

<a id="textbook"></a>
## One educational anchor

Benjamin Schumacher and Michael D. Westmoreland, *Quantum Processes, Systems, and Information*, Cambridge University Press (2010).

The book develops quantum mechanics alongside the physical meaning of information. Its [publisher's preface](https://www.cambridge.org/core/books/quantum-processes-systems-and-information/preface/5A98A47E9AB01E1E30541E0C5779F43C) describes the undergraduate teaching approach. The chapter references below follow the [publisher's contents](https://www.cambridge.org/core/product/identifier/CBO9780511814006A005/type/BOOK_PART); Cambridge also provides a [contents-only PDF](https://assets.cambridge.org/97805218/75349/toc/9780521875349_toc.pdf). The print publication year is 2010; the publisher's online publication date is later.

| Foundation used here | Textbook route |
|---|---|
| Qubits, states, distinguishability, and unitary dynamics | Chapters 2–5 |
| Joint systems and conditional states | Chapter 6 |
| Mixed states, Bloch vectors, and Gibbs populations | Chapter 8 |
| Reduced dynamics and heat/work accounting | Chapter 9 |
| Understanding the two-qubit circuit | Chapter 18, as needed |
| Entropy, correlations, and thermodynamic cost | Chapter 19 |

For a reader who already knows qubits, Chapters 8, 9, and 19 are the main bridge. In Chapter 19, sections 19.1 and 19.3 provide the classical and quantum entropy foundations; sections 19.5–19.6 connect them to thermodynamics and work. These chapters form the targeted reading route.

## Translate the foundations into the project

| Foundation | Local translation | Scientific destination |
|---|---|---|
| States and Bloch vectors | The system is $`S`$; the two prescribed targets are $`\phi_x(s)`$, and their overlap magnitude is $`s`$. | [Task and target geometry](../science/model.md#task) |
| Composite systems and reduced states | $`A`$ is workspace, $`B`$ the complete thermal reservoir, and $`E=AB`$ the environment used in the information argument. | [Apparatus](../science/model.md#apparatus) and [notation](../science/notation.md) |
| Statistical mixtures | Equal priors determine mean heat; each conditional output must separately meet its error bound. A correct average alone is insufficient. | [Conditional task](01_task.md#conditional-task) |
| Thermal equilibrium | A qubit's gap and Gibbs populations determine its bias. Finite gaps at positive temperature give full rank. | [Thermal qubit](02_device.md#thermal-qubit) |
| Dynamics and energy | The fixed joint unitary may be externally driven. Heat is the reservoir energy increase, not an assumed entropy difference. | [Worked device](02_device.md) and [energy boundary](../science/model.md#heat-work) |
| Entropy and correlations | Research entropies use bits; explicitly marked thermodynamic expressions use natural logarithms. Auxiliary entropy increase and system entropy decrease have different signs and roles. | [Notation](../science/notation.md#entropies) and [heat ledger](../science/heat_bound.md#heat-ledger) |

The [task chapter](01_task.md) develops conditional states and operational accuracy. The [device chapter](02_device.md) calculates outputs and heat for one finite implementation. The [precision chapter](03_precision.md) relates the small signal and the smaller population displacement to the limiting question. These explanations use the source as a foundation, not as a requirement to read the entire book first.

<a id="beyond-textbook"></a>
## The locally supplied research bridge

The textbook supplies the quantum-mechanical and thermodynamic language. It does not supply this project's universal converse. The additional steps are linked to their exact arguments and primary attribution:

| Additional step | Why it is needed | Read |
|---|---|---|
| Trace distance and reference-sensitive channel error | States the operational accuracy convention and distinguishes branch tests from channel certification. | [Task](../science/model.md#task), [channel equivalence](../science/channel_accuracy.md) |
| Complete cosine–sine decomposition | Covers every finite joint unitary, including singular blocks. | [Kinematic reduction](../science/kinematics.md#unitary-reduction) |
| Noncommuting spectral information comparison | Converts environmental separation into Holevo information with the required inequality direction. | [Information bound](../science/environment_information.md#information-bound) |
| Dimension-uniform continuity | Transfers the comparison to actual outputs without a growing-reservoir loophole. | [Actual environment](../science/environment_information.md#environment-transfer) |
| Gibbs and workspace accounting | Applies thermality only to the physical bath and charges consumed auxiliary entropy. | [Heat bound](../science/heat_bound.md#heat-ledger) |
| Matching finite constructions and limiting optimization | Establishes the infimum using positive-error, finite devices at every stage. | [Recovery](../science/thermal_implementation.md#recovery), [limiting match](../science/heat_bound.md#matching-limit) |

These primary research dependencies are not additional educational anchors. The [source register](../references/LITERATURE.md) preserves their attribution and exact locators. The [30 milestones](MILESTONES.md) supply the single project-defined route through the background and the complete argument.
