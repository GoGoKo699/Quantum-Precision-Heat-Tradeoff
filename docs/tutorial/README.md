# Learn the physics

[Home](../../README.md) · [Exact result](../THEOREM.md)

The tutorial begins with a device and its resources, not with the limiting formula. Familiarity with undergraduate linear algebra and basic quantum mechanics is enough to work through the explicit two-qubit operation. The universal optimality proof uses additional tools, which are identified rather than silently assumed.

## One educational anchor

Benjamin Schumacher and Michael D. Westmoreland, *Quantum Processes, Systems, and Information*, Cambridge University Press (2010).

The publisher describes the book as an undergraduate quantum-mechanics text integrating the physical meaning of information. See the [publisher's preface](https://www.cambridge.org/core/books/quantum-processes-systems-and-information/preface/5A98A47E9AB01E1E30541E0C5779F43C) and [book information](https://doi.org/10.1017/CBO9780511814006).

| Foundation | Textbook route | Used here for |
|---|---|---|
| Qubits, states, distinguishability, dynamics | Chapters 2–5 | Input alternatives, output tests, unitary evolution |
| Composite systems | Chapter 6 | Joint states and reduced states |
| Density operators | Chapter 8 | Mixtures, Bloch vectors, thermal populations |
| Open systems | Chapter 9 | Coupling a system to a reservoir |
| Quantum information processing | Chapter 18, as needed | Reading the two-qubit circuit |
| Classical and quantum entropy | Chapter 19 | Information, correlations, and thermodynamic bookkeeping |

This is a reading map, not a requirement to read the book cover to cover. For a reader already familiar with qubits, Chapters 8, 9, and 19 are the main bridge. No textbook pages, scans, or copied exercises are included.

## The tutorial route

1. [States, the task, and the resource boundary](01_task.md): distinguish the two conditional outputs from their average and define the error.
2. [Calculate one complete thermal device](02_device.md): obtain output states, bath populations, and heat from matrices.
3. [Why precision changes the lower bound](03_precision.md): see the second-order scale and the additional steps needed for optimality.

Each chapter includes a short checkpoint with a worked answer. The tutorial is self-contained at the level of its calculations. It does not treat an intuitive argument as the proof of a universal optimum.

## Beyond the textbook

The research proof additionally uses a complete cosine–sine decomposition, a spectral information inequality, and a dimension-independent entropy-continuity estimate. These are stated and explained in the [proof](../PROOF.md), with primary attribution in the [literature guide](../LITERATURE.md).

One textbook organizes the learning path. It does not replace the primary literature supporting the model or the comparison with previous results.
