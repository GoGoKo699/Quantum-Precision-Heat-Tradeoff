# Relation to existing results

[Home](../README.md) · [Physical model](MODEL.md) · [Main result](THEOREM.md) · [Source and assumption register](LITERATURE.md)

The contribution is the [positive-error precision–heat crossover](THEOREM.md#optimal-crossover) for the specified two-input task: a converse uniform in finite apparatus dimension, charged internal workspace, and a matching thermal construction. Operation-dependent cost, approximate processing, catalytic return, and work recovery have established predecessors. The comparisons below identify the particular results used; they do not establish an exhaustive novelty or subsumption theorem.

## Microscopic heat and recovery

<a id="reeb-wolf"></a>
### Reeb and Wolf

**Source:** [*An improved Landauer Principle with finite-size corrections*, arXiv:1306.4352v3](https://arxiv.org/abs/1306.4352v3), §2.1; Theorem 3, Eqs. (21)–(22); §6, Proposition 8.

**Task and resources.** A specified system state interacts unitarily with an independent Gibbs reservoir. The objective is its complete mean reservoir-energy increase. The principal model is finite dimensional; it neither specifies a two-branch accuracy tolerance nor adds an arbitrary nonthermal catalyst. Proposition 8 approaches the entropy bound for a prescribed rank-nondecreasing state transition using growing reservoirs and successive swaps.

**Role here.** The Gibbs heat identity and successive-reservoir idea are inherited. The [construction](CONSTRUCTION.md#recovery) specializes recovery to an explicit finite qubit ladder and counts every spent component. The [proof](PROOF.md) additionally derives a record forced by both conditional output tests. Optimizing a single average-state transition does not enforce those tests. Reeb–Wolf deliberately leave system energy unspecified; equating heat with supplied work additionally requires this repository's [boundary Hamiltonians](MODEL.md#heat-work).

## Operation-dependent restrictions

<a id="aksak-turgut"></a>
### Aksak and Turgut

**Source:** [*Heat Transfer Operators Associated with Quantum Operations*, arXiv:1002.0733v2](https://arxiv.org/abs/1002.0733v2), §2; Theorem 4(b), Eqs. (38)–(39).

**Task and resources.** A fixed quantum operation is implemented exactly using an input-independent canonical bath and an isometry. A heat-transfer operator specifies mean bath heat for each input state. Their finite-bath condition means a finite partition function, allowing infinitely many energy levels. No separately returned nonthermal workspace appears in this criterion.

**Role here.** For the exact pure-target channel, the Kraus products are linearly independent when the target overlap is nonzero. Theorem 4(b)'s heat-transfer-matrix criterion then requires $\beta Q>\ln 2$ for equal priors in its exact model. This inherited restriction does not by itself supply a uniform positive-error estimate as overlap and error vanish together. The present [finite converse](THEOREM.md#finite-bound) and [limiting law](THEOREM.md#optimal-crossover) address that joint limit; they do not reinterpret the exact criterion as an attainable finite-dimensional endpoint.

<a id="bedingham-maroney"></a>
### Bedingham and Maroney

**Source:** [*The thermodynamic cost of quantum operations*, arXiv:1604.03749v1](https://arxiv.org/abs/1604.03749v1), Eqs. (3)–(4), (9); Appendix A (notation) and Appendix E (analytical bound).

**Task and resources.** An ensemble of specified input/output pairs must be realized by one unitary on system, auxiliary, and independent canonical bath. Equation (4) restores the auxiliary's ensemble-average marginal. Mean bath heat is charged. The outputs are specified exactly; a noisy map can be inserted as that specification. No overlap/error joint limit is asserted there.

**Explicit comparison.** Substituting this repository's [constructed noisy outputs](CONSTRUCTION.md#collision) into Eq. (9) yields, in natural-log units,

```math
\beta Q\ge J(s)+\frac{s^2z^2}{32}.
```

Here the short definitions are

```math
J(s)=\ln 2-h\!\left(\frac{1+s}{2}\right),
```

```math
z=\sqrt{1-s^2}-2\epsilon,
```

with $h$ the binary entropy in nats. This particular bound tends to zero in the crossover limit. The present converse uses only the allowed output tests and retains a positive limiting heat when the error is of order $s^2$. This evaluates one explicit predecessor inequality, not all its methods or possible stronger consequences. Operation-specific excess heat and ensemble-marginal auxiliary restoration are inherited.

## Battery cost and collective work

<a id="faist-renner"></a>
### Faist and Renner

**Source:** [*Fundamental Work Cost of Quantum Processes*, arXiv:1709.00506v2](https://arxiv.org/abs/1709.00506v2), §§II–III.1, Eqs. (2)–(6); §III.2, Eq. (12).

**Task and resources.** A specified process acts on a specified input while preserving its prescribed correlations with a reference. Gibbs-preserving operations act on system and battery; trace-nonincreasing, Gibbs-sub-preserving maps provide an equivalent optimization description. The cost is battery depletion, with pure qubits convertible to work. Smoothing uses purified distance on the process state, rather than the maximum trace distance of two branch outputs. The battery may be consumed; it is not an exactly returned workspace.

**Role here.** The Main Result, Eq. (3), characterizes optimal battery yield through coherent relative entropy; Proposition I links exact implementation to Gibbs-sub-preservation. Equation (12) concerns an independent-copy limit. These establish process-level resource accounting and distinguish a channel implementation from an average-state transition. The present theorem instead bounds the complete microscopic bath's mean heat for a two-input task. No equality between these cost functions, nor reduction proving either complete framework stronger, is established here.

<a id="faist-berta-brandao"></a>
### Faist, Berta, and Brandão

**Source:** [*Thermodynamic Capacity of Quantum Processes*, arXiv:1807.05610v2](https://arxiv.org/abs/1807.05610v2), Eq. (3) and the sections “Implementation based on quantum typicality” and “Thermal Operations”.

**Task and resources.** Many independent uses of a specified channel are implemented universally, including reference-entangled inputs, with vanishing diamond-norm error. Equation (3) gives the asymptotic work rate as the largest input-to-output free-energy increase. The construction allows a work supply and Gibbs-preserving operations; the thermal-operation result is restricted to time-covariant channels. Its collective rate is not an exact-return condition on arbitrary single-use workspace.

**Role here.** This is a direct predecessor for input-independent thermodynamic channel implementation. Its many-copy limit and work currency differ from the single-use mean-heat infimum at positive error used here. Comparing an entropy difference or capacity alone does not identify the heat of the complete finite apparatus. The cited Letter separates its announced results from the technical proofs in its companion work; no stronger cross-framework claim is inferred from the Letter's rate formula.

## Accuracy as an operational task

<a id="chiribella"></a>
### Chiribella and collaborators

**Source:** [*The nonequilibrium cost of accurate information processing*, arXiv:2203.09369v2](https://arxiv.org/abs/2203.09369v2), §II, Eqs. (1)–(3), Theorem 1; Methods (task-cost optimization).

**Task and resources.** A task specifies input states and output test observables. Accuracy is the minimum expected test score over inputs, with a general enough specification to test several observables per input. Channels are optimized subject to that task, using Gibbs-preserving operations and an information battery. The objective counts clean qubits consumed. This is not automatically the same numerical error parameter as branch trace distance.

**Role here.** Equation (1) is an accuracy/nonequilibrium bound in terms of reverse entropy. Theorem 1 gives an attainability interval under its stated hypotheses. Its tradeoff varies task score and battery budget. Thus task-level optimization and thermodynamic accuracy tradeoffs are inherited concepts. Here the currency is actual bath heat, the workspace has a separate entropy ledger, and the limiting regime fixes error relative to squared overlap. Relating their exact task-cost optimization to this microscopic heat infimum would require an explicit matching of metrics and resource rules; that reduction is not established here.

## Returned workspace and correlations

<a id="returned-workspace"></a>
### Exact marginal return

The closest direct heat-model precedent is [Bedingham–Maroney Eq. (4)](#bedingham-maroney). The other papers clarify distinct return conventions:

- [Wilming, arXiv:2012.05573v2](https://arxiv.org/abs/2012.05573v2), Definition 1, Eqs. (2)–(3), and Theorem 2: one state transition under a unitary with an independent finite catalyst; catalyst marginal return is exact, system trace-distance error can be arbitrarily small, and correlations are allowed. The criterion is entropy increase, without a separate mean-heat objective. Catalyst size can depend on error.
- [Boes et al., arXiv:1807.08773v1](https://arxiv.org/abs/1807.08773v1), Theorem 1, Eqs. (1)–(2): a finite state-conversion problem uses a unitary **and dephasing of the catalyst**. Exact target conversion obeys entropy and rank conditions; lower-rank targets require approximation. This supports a related return convention, not unitary-only exact marginal return by itself.
- [Shiraishi–Sagawa, arXiv:2010.11036v3](https://arxiv.org/abs/2010.11036v3), Theorem 1 and Supplemental Material Theorem 3: Gibbs-preserving state conversion allows an exactly returned catalyst, arbitrarily small target trace distance and mutual information. Theorem 2 treats work investment through a separate storage system. These are state-conversion results with potentially growing catalysts, not a common device constrained on both input branches.
- [Henao–Uzdin, arXiv:2010.09070v3](https://arxiv.org/abs/2010.09070v3), §4.1, Eqs. (4)–(5): a global unitary returns a finite catalyst marginal while permitting correlations. The objective is cooling, later thermometry; §3 does not require a thermal hot object or count its energy as the objective. This is a finite-environment precedent, not the same heat ledger or error limit.

These are precedents for resource conventions, not ingredients proving the crossover. The [complete-environment argument](PROOF.md#environment-entropy) applies to the specified conditional task, including rank-deficient workspace, and then uses Gibbs structure only for the bath. Returning an ensemble marginal is weaker than returning every conditional marginal or removing all correlations. Reuse with fresh independent inputs does not imply arbitrary correlated multi-use composability.

### Approximate return

[Ng et al., arXiv:1405.3039v1](https://arxiv.org/abs/1405.3039v1), §II.1–II.2 and Supplemental Material Theorem II.3, examine approximate catalyst return under thermal operations. A small catalyst trace-distance change alone can permit otherwise forbidden state conversions when its dimension grows; dimension or energy constraints restrict this effect. Their objective is state-conversion feasibility, rather than this conditional task's mean heat.

The present [approximate-return statement](THEOREM.md#workspace-return) charges the workspace's possible entropy increase. Its quantitative dimension-dependent allowance comes from [Audenaert's entropy continuity theorem](LITERATURE.md#r6), not a new catalysis criterion.

## Mathematical ingredients

The [proof-source guide](LITERATURE.md#ingredients-used-in-the-proof) identifies the exact roles of Nishiyama's sharp scalar inequality, Winter's conditional-entropy continuity bound, Audenaert's entropy continuity bound, the complete CS decomposition, and Golden–Thompson. None of these standard ingredients is claimed as new. The noncommuting reduction and transfer to the actual environment are written out in the [proof](PROOF.md).
