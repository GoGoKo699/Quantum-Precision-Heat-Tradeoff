# Learn the physics

[Home](../../README.md) · [Exact result](../THEOREM.md#optimal-crossover) · [Notation](../NOTATION.md)

Start with the two-input task, calculate a complete finite device, and then examine what a universal lower bound needs beyond that example. Undergraduate linear algebra and basic quantum mechanics are enough for the device calculation. The additional research tools are introduced at the point where they become necessary.

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

For a reader who already knows qubits, Chapters 8, 9, and 19 are the main bridge. In Chapter 19, sections 19.1 and 19.3 provide the classical and quantum entropy foundations; sections 19.5–19.6 connect them to thermodynamics and work. This is a targeted reading route, not a requirement to read the book cover to cover. No textbook pages, scans, or copied exercises are included.

<a id="route"></a>
## The tutorial route

1. [States, the task, and the resource boundary](01_task.md): write the two conditional targets, compare their average, and define the error and charged resources.
2. [Calculate one complete thermal device](02_device.md): obtain the system outputs and errors, then compute heat from the bath's gap and populations.
3. [Why precision changes the lower bound](03_precision.md): distinguish first-order polarization from second-order near-purity, interpret the crossover, and locate the universal converse.

Each chapter includes short worked questions. Definitions and calculations are included locally, so the route can also be read as a compact introduction after studying the relevant textbook material.

<a id="beyond-textbook"></a>
## Beyond the textbook

The research proof additionally uses a complete cosine–sine decomposition, a noncommuting spectral information argument, and an entropy-continuity estimate that is uniform in reservoir dimension. These tools are stated in the [proof dependency map](../PROOF.md) with primary attribution in the [literature guide](../LITERATURE.md).

The textbook organizes the teaching route. The [model](../MODEL.md), [theorem](../THEOREM.md), and [direct source comparisons](../RELATED_WORK.md) provide the independent specialist route and the primary-research context.
