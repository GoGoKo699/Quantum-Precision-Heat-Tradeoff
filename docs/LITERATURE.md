# Literature, attribution, and assumption provenance

[Home](../README.md) · [Direct comparisons](RELATED_WORK.md) · [Model](MODEL.md) · [Proof](PROOF.md)

The [direct comparisons](RELATED_WORK.md) explain the closest predecessors by task, allowed resources, cost, error, and limiting regime. This page retains the assumption register and source identifiers. The [single-textbook tutorial](tutorial/README.md) is a separate teaching route.

## Ingredients used in the proof

Version numbers below identify the inspected arXiv texts; equation numbers refer to those versions. A source is credited for its actual role, not for the complete conjunction of assumptions used here.

<a id="r1"></a>
**R1. Reeb and Wolf.** *An improved Landauer Principle with finite-size corrections*, New Journal of Physics 16, 103011 (2014). [1306.4352v3](https://arxiv.org/abs/1306.4352v3). Theorem 3, Eqs. (21)–(22): microscopic heat equality. Section 6, Proposition 8: successive-reservoir construction. [Comparison](RELATED_WORK.md#reeb-wolf).

<a id="r2"></a>
**R2. Aksak and Turgut.** *Heat Transfer Operators Associated with Quantum Operations*, Journal of Physics A 44, 275304 (2011). [1002.0733v2](https://arxiv.org/abs/1002.0733v2). Theorem 4(b), Eqs. (38)–(39): exact-operation heat restriction. [Bath and isometry conventions](RELATED_WORK.md#aksak-turgut) differ from finite-dimensional positive-error devices.

<a id="r3"></a>
**R3. Bedingham and Maroney.** *The thermodynamic cost of quantum operations*, New Journal of Physics 18, 113050 (2016). [1604.03749v1](https://arxiv.org/abs/1604.03749v1). Equations (3)–(4), (9), Appendix A and Appendix E: conditional tasks, ensemble-marginal auxiliary restoration, and an explicit excess-heat bound. [Specified-map comparison](RELATED_WORK.md#bedingham-maroney).

<a id="r4"></a>
**R4. Nishiyama.** *On Relations Between Tight Bounds for Symmetric f-Divergences and Binary Divergences*. [2210.09571v2](https://arxiv.org/abs/2210.09571v2). Definition 3 and Theorem 1, Eq. (8), give the mirrored binary equality case. Section IV-A, Eq. (29), is the sharp Jensen–Shannon/triangular-discrimination inequality. Equation (2) uses the same factor of one half as the proof. This scalar inequality is inherited.

<a id="r5"></a>
**R5. Winter.** *Tight uniform continuity bounds for quantum entropies: conditional entropy, relative entropy distance and energy constraints*, Communications in Mathematical Physics 347, 291–313 (2016). [1507.07775v6](https://arxiv.org/abs/1507.07775v6). Section II, Lemma 2, pp. 2–3, includes the improved bound for both cq and qc states. Here its bounded-dimensional subsystem is the classical binary label; the conditional quantum environment can have arbitrary finite dimension.

<a id="r6"></a>
**R6. Audenaert.** *A sharp continuity estimate for the von Neumann entropy*, Journal of Physics A 40, 8127–8136 (2007). The inspected preprint [quant-ph/0610146v1](https://arxiv.org/abs/quant-ph/0610146v1) is titled *A Sharp Fannes-type Inequality for the von Neumann Entropy*. Theorem 1, Eq. (6), gives the dimension-dependent entropy allowance for approximate workspace return, using half the trace norm and entropy in bits.

<a id="r7"></a>
**R7. Sutton.** *Computing the Complete CS Decomposition*. [0707.1838v3](https://arxiv.org/abs/0707.1838v3). Equation (1.1), p. 1, gives the complete block decomposition; its angles include both endpoints. The equal-block specialization supports the arbitrary-unitary reduction, including zero and unit singular values. The decomposition is a standard tool.

<a id="r8"></a>
**R8. Golden–Thompson inequality.** Golden, *Lower Bounds for the Helmholtz Function*, Physical Review 137, B1127 (1965), and Thompson, *Inequality with applications in statistical mechanics*, Journal of Mathematical Physics 6, 1812 (1965). The inspected proof source is Forrester and Thompson, [*The Golden-Thompson inequality — historical aspects and random matrix applications*, 1408.2008v1](https://arxiv.org/abs/1408.2008v1), Eq. (1.1) and §§2.2–2.3. It supplies the trace-exponential inequality; the integral conversion to the spectral-information comparison is written out in this repository's proof.

## What the present statement adds

The theorem connects the conditional output tests to an environmental record uniformly in finite environment dimension, converts that record into actual bath heat with charged workspace, and matches the limiting lower bound with a complete thermal construction. The exact finite-parameter optimum is not claimed.

The [direct comparison page](RELATED_WORK.md) separates that contribution from operation-dependent heat, battery cost, collective work rates, task accuracy, and catalytic state conversion. It includes the explicit Bedingham–Maroney substitution without asserting that every method in that predecessor gives a weaker result.

## Assumption register

The register distinguishes direct microscopic precedents from component-level support. A publication count is not community consensus, and journal venue alone does not establish physical suitability. The complete conjunction is not claimed to occur in every cited framework.

### Initially independent Gibbs reservoir, joint unitary, complete mean reservoir-energy heat

**Precedents:** [P01–P05](#p01).

Five direct framework precedents, including PRLs P02 and P03. These papers study different tasks.

### Finite-reservoir modeling

**Precedents:** [P01](#p01), [P02](#p02), [P04](#p04), [P05](#p05), [P22](#p22).

Four close-framework precedents and one neighboring finite-bath treatment, not five identical models.

### Degenerate information-bearing boundary energies

**Precedents:** [P06](#p06), [P08–P11](#p08).

Component-level support; their battery and auxiliary rules differ.

### External predetermined driving

**Precedents:** [P04–P06](#p04), [P12](#p12), [P15](#p15).

A modeling convention, not evidence that control is cheap or autonomous.

### Finite error and resource-dependent ideal endpoints

**Precedents:** [P01](#p01), [P05](#p05), [P12–P14](#p12), [P21–P23](#p21).

Includes finite-time and measurement models with different allowed dynamics.

### Trace-distance and stabilized worst-case accuracy

**Precedents:** [P16–P20](#p16).

Five quantum-information precedents, including PRL P17; they support the metric, not an application's need for this tolerance.

### Returned auxiliary marginal, with possible correlations

**Precedents:** [P06](#p06) and [C01–C04](#c01).

Five related primary precedents, including three PRLs. C01 includes catalyst dephasing; P06 and C02–C04 impose exact marginal return in their respective frameworks. These are not five identical resource models, and marginal return alone does not ensure arbitrary multi-use composability.

### Approximate auxiliary return

**Precedents:** [R6](#r6), [C05](#c05).

Dimension and entropy capacity must be charged. Trace distance alone is not dimension-uniform.

### Exact boundary Hamiltonian conjunction and no uniform cap on optimizing resources

**Precedents:** Related [P01](#p01), [P05](#p05), [P06](#p06), [P21](#p21), [P22](#p22).

Five direct matches to the entire conjunction are not asserted. These remain visible model idealizations.

### Two inputs, equal priors, particular pure targets, and error-to-overlap scaling

**Precedents:** [P07](#p07) and [P27](#p27) are close task precedents.

A selected benchmark and a derived scaling law, not assumptions validated by counting publications.

The bath-only framework is enlarged here by the proved cyclic-workspace extension. Papers that omit auxiliaries do not prove that extension. Papers allowing consumed batteries do not make their entropy capacity free in this heat model.

## Primary-paper register

Each P label identifies one paper, not separate counts for versions or corrections. The full original register is retained; the bounded direct comparisons use the versioned texts named above and on the comparison page. No paper or textbook content is redistributed.

<a id="p01"></a>
**P01.** Reeb–Wolf, *An improved Landauer Principle with finite-size corrections*. NJP 16, 103011 (2014). [1306.4352](https://arxiv.org/abs/1306.4352v3).

<a id="p02"></a>
**P02.** Goold–Paternostro–Modi, *Nonequilibrium Quantum Landauer Principle*. PRL 114, 060602 (2015). [1402.4499](https://arxiv.org/abs/1402.4499).

<a id="p03"></a>
**P03.** Timpanaro–Santos–Landi, *Landauer's Principle at Zero Temperature*. PRL 124, 240601 (2020). [1911.00910](https://arxiv.org/abs/1911.00910).

<a id="p04"></a>
**P04.** Esposito–Lindenberg–Van den Broeck, *Entropy production as correlation between system and reservoir*. NJP 12, 013013 (2010). [0908.1125](https://arxiv.org/abs/0908.1125).

<a id="p05"></a>
**P05.** Mohammady–Mohseni–Omar, *Minimising the heat dissipation of quantum information erasure*. NJP 18, 015011 (2016). [1510.02062](https://arxiv.org/abs/1510.02062).

<a id="p06"></a>
**P06.** Bedingham–Maroney, *The thermodynamic cost of quantum operations*. NJP 18, 113050 (2016). [1604.03749](https://arxiv.org/abs/1604.03749v1).

<a id="p07"></a>
**P07.** Aksak–Turgut, *Heat Transfer Operators Associated with Quantum Operations*. J. Phys. A 44, 275304 (2011). [1002.0733](https://arxiv.org/abs/1002.0733v2).

<a id="p08"></a>
**P08.** del Rio et al., *The thermodynamic meaning of negative entropy*. Nature 474, 61–63 (2011). [1009.1630](https://arxiv.org/abs/1009.1630v2).

<a id="p09"></a>
**P09.** Faist et al., *The Minimal Work Cost of Information Processing*. Nature Communications 6, 7669 (2015). [1211.1037](https://arxiv.org/abs/1211.1037v2).

<a id="p10"></a>
**P10.** Faist–Renner, *Fundamental Work Cost of Quantum Processes*. PRX 8, 021011 (2018). [1709.00506](https://arxiv.org/abs/1709.00506v2).

<a id="p11"></a>
**P11.** Chiribella et al., *The nonequilibrium cost of accurate information processing*. Nature Communications 13, 7155 (2022). [2203.09369](https://arxiv.org/abs/2203.09369v2).

<a id="p12"></a>
**P12.** Browne et al., *Guaranteed Energy-Efficient Bit Reset in Finite Time*. PRL 113, 100603 (2014). [1311.7612](https://arxiv.org/abs/1311.7612).

<a id="p13"></a>
**P13.** Zhen et al., *Universal Bound on Energy Cost of Bit Reset in Finite Time*. PRL 127, 190602 (2021). [2106.00580](https://arxiv.org/abs/2106.00580).

<a id="p14"></a>
**P14.** Vu–Saito, *Finite-Time Quantum Landauer Principle and Quantum Coherence*. PRL 128, 010602 (2022). [2106.05743](https://arxiv.org/abs/2106.05743).

<a id="p15"></a>
**P15.** Huber et al., *Thermodynamic cost of creating correlations*. NJP 17, 065008 (2015). [1404.2169](https://arxiv.org/abs/1404.2169).

<a id="p16"></a>
**P16.** Gilchrist–Langford–Nielsen, *Distance measures to compare real and ideal quantum processes*. PRA 71, 062310 (2005). [quant-ph/0408063](https://arxiv.org/abs/quant-ph/0408063).

<a id="p17"></a>
**P17.** Kueng et al., *Comparing Experiments to the Fault-Tolerance Threshold*. PRL 117, 170502 (2016). [1510.05653](https://arxiv.org/abs/1510.05653).

<a id="p18"></a>
**P18.** Sanders–Wallman–Sanders, *Bounding quantum gate error rate based on reported average fidelity*. NJP 18, 012002 (2016). [1501.04932](https://arxiv.org/abs/1501.04932).

<a id="p19"></a>
**P19.** Kretschmann–Schlingemann–Werner, *The Information-Disturbance Tradeoff and the Continuity of Stinespring's Representation*. IEEE TIT 54, 1708–1717 (2008). [quant-ph/0605009](https://arxiv.org/abs/quant-ph/0605009).

<a id="p20"></a>
**P20.** Watrous, *Semidefinite programs for completely bounded norms*. Theory of Computing 5, 217–238 (2009). [0901.4709](https://arxiv.org/abs/0901.4709).

<a id="p21"></a>
**P21.** Masanes–Oppenheim, *A general derivation and quantification of the third law of thermodynamics*. Nature Communications 8, 14538 (2017). [1412.3828](https://arxiv.org/abs/1412.3828).

<a id="p22"></a>
**P22.** Scharlau–Mueller, *Quantum Horn's lemma, finite heat baths, and the third law of thermodynamics*. Quantum 2, 54 (2018). [1605.06092](https://arxiv.org/abs/1605.06092).

<a id="p23"></a>
**P23.** Guryanova–Friis–Huber, *Ideal Projective Measurements Have Infinite Resource Costs*. Quantum 4, 222 (2020). [1805.11899](https://arxiv.org/abs/1805.11899).

<a id="p24"></a>
**P24.** Yan et al., *Single-Atom Demonstration of the Quantum Landauer Principle*. PRL 120, 210601 (2018). [1803.10424](https://arxiv.org/abs/1803.10424).

<a id="p25"></a>
**P25.** Scandi et al., *Minimally Dissipative Information Erasure in a Quantum Dot via Thermodynamic Length*. PRL 129, 270601 (2022). [2209.01852](https://arxiv.org/abs/2209.01852).

<a id="p26"></a>
**P26.** Fellous-Asiani et al., *Optimizing Resource Efficiencies for Scalable Full-Stack Quantum Computers*. PRX Quantum 4, 040319 (2023). [2209.05469](https://arxiv.org/abs/2209.05469).

<a id="p27"></a>
**P27.** Dunlop et al., *Thermodynamically Optimal Protocols for Dual-Purpose Qubit Operations*. The inspected arXiv version is used here without assigning a journal-level count. [2306.09088v3](https://arxiv.org/abs/2306.09088v3).

<a id="p28"></a>
**P28.** Lostaglio–Mueller–Pastena, *Stochastic Independence as a Resource in Small-Scale Thermodynamics*. PRL 115, 150402 (2015). [1409.3258](https://arxiv.org/abs/1409.3258).

<a id="p29"></a>
**P29.** Faist–Berta–Brandão, *Thermodynamic Capacity of Quantum Processes*. PRL 122, 200601 (2019). [1807.05610v2](https://arxiv.org/abs/1807.05610v2). [Collective-work comparison](RELATED_WORK.md#faist-berta-brandao).

P24 and P25 establish related experimental primitives, not a demonstration of this crossover. P26 makes clear why microscopic heat cannot be converted directly into wall-plug savings. P27 uses a restricted primitive set; P28 illustrates the importance of correlation resources. P29 supplies the collective-process comparison and is not an extra direct match to the entire microscopic model.

## Returned-workspace references

The [return-convention comparison](RELATED_WORK.md#returned-workspace) gives exact locators and distinguishes unitary, dephasing, Gibbs-preserving, and thermal-operation frameworks.

<a id="c01"></a>
**C01.** Boes et al., *Von Neumann entropy from unitarity*, PRL 122, 210402 (2019). [1807.08773v1](https://arxiv.org/abs/1807.08773v1). Theorem 1, Eqs. (1)–(2): catalyst return after dephasing.

<a id="c02"></a>
**C02.** Wilming, *Entropy and reversible catalysis*, PRL 127, 260402 (2021). [2012.05573v2](https://arxiv.org/abs/2012.05573v2). Definition 1 and Theorem 2: exact catalyst marginal with approximate system conversion.

<a id="c03"></a>
**C03.** Shiraishi–Sagawa, *Quantum Thermodynamics of Correlated-Catalytic State Conversion at Small Scale*, PRL 126, 150502 (2021). [2010.11036v3](https://arxiv.org/abs/2010.11036v3). Theorems 1–2 and Supplemental Material Theorem 3: correlated-catalytic state conversion and work investment under Gibbs-preserving maps.

<a id="c04"></a>
**C04.** Henao–Uzdin, *Catalytic transformations with finite-size environments: applications to cooling and thermometry*, Quantum 5, 547 (2021). [2010.09070v3](https://arxiv.org/abs/2010.09070v3). Section 4.1, Eqs. (4)–(5): marginal-return condition for finite-environment unitaries.

<a id="c05"></a>
**C05.** Ng et al., *Limits to catalysis in quantum thermodynamics*, NJP 17, 085004 (2015). [1405.3039v1](https://arxiv.org/abs/1405.3039v1). Section II.1–II.2 and Supplemental Material Theorem II.3: approximate return and dimension/energy restrictions.

The [source inventory](../provenance/README.md) preserves input identification and factual provenance separately from this scientific reading route.
