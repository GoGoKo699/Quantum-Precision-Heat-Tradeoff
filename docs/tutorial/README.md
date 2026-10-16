# Learn the physics

[Home](../../README.md) · [Exact result](../THEOREM.md#optimal-crossover) · [Notation](../NOTATION.md)

Use the [30-milestone understanding map](MILESTONES.md) for the complete project story. Its common targets serve human readers and LLMs: **M01–M14** build the background from individual concepts to the full physical task, and **M15–M30** connect the finite device, converse, recovery, optimal limit, and consequences. Each milestone records its question, understanding target, dependencies, source pointers, and suggested learning intensity.

For interactive teaching, follow the [coaching protocol](COACHING.md). Each milestone starts with compact Revise → Learn preparation and a two-question challenge; targeted learning and capped retries respond to mistakes. The map is independent of learner background, while explanations and remediation adapt. Individual progress is not recorded in the common map.

The three worked chapters below introduce the two-input task, calculate a complete finite device, and explain what a universal lower bound needs beyond that example. Undergraduate linear algebra and basic quantum mechanics are enough for the device calculation. Additional research tools are taught locally when the milestone map needs them.

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

<a id="route"></a>
## Worked chapters supporting the map

1. [States, the task, and the resource boundary](01_task.md): write the two conditional targets, compare their average, and define the error and charged resources.
2. [Calculate one complete thermal device](02_device.md): obtain the system outputs and errors, then compute heat from the bath's gap and populations.
3. [Why precision changes the lower bound](03_precision.md): distinguish first-order polarization from second-order near-purity, interpret the crossover, and locate the universal converse.

These are supporting chapters, not three milestones or a second curriculum. The task chapter supports the background phase; the device and precision chapters introduce the narrative phase. The remaining milestone sources lead directly to the canonical proofs, consequences, and evidence. Their worked checkpoints are explanations, not automatically graded challenge attempts. Definitions and calculations are supplied locally, and the tutor provides the bridge to research-level arguments in the session.

<a id="beyond-textbook"></a>
## Beyond the textbook

The research proof additionally uses a complete cosine–sine decomposition, a noncommuting spectral information argument, and an entropy-continuity estimate that is uniform in reservoir dimension. These tools are stated in the [proof dependency map](../PROOF.md) with primary attribution in the [literature guide](../LITERATURE.md).

The textbook organizes the teaching route. The [model](../MODEL.md), [theorem](../THEOREM.md), and [direct source comparisons](../RELATED_WORK.md) provide the independent specialist route and the primary-research context.
