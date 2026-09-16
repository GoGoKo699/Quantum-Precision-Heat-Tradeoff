# Literature, attribution, and assumption provenance

[Home](../README.md) · [Model](MODEL.md) · [Proof](PROOF.md)

The educational anchor is a textbook; the research foundations are primary papers. A source is credited only for the convention, theorem, or construction it actually supports. Sharing some assumptions is not equivalence of complete resource models, and a journal venue does not prove an assumption physically appropriate.

## Ingredients used in the proof

<a id="r1"></a>
**R1. Reeb and Wolf.** *An improved Landauer Principle with finite-size corrections*, New Journal of Physics 16, 103011 (2014). [Primary text](https://arxiv.org/abs/1306.4352v3). Supplies microscopic Gibbs/product-state/unitary heat accounting and successive-reservoir constructions. Its heat theorem does not identify heat with work for arbitrary system Hamiltonians.

<a id="r2"></a>
**R2. Aksak and Turgut.** *Heat Transfer Operators Associated with Quantum Operations*, Journal of Physics A 44, 275304 (2011). [Primary text](https://arxiv.org/abs/1002.0733v2). Theorem 4 gives the direct exact-operation restriction for this target. Its bath and isometry conventions are not identical to finite-dimensional positive-error unitary implementations. The exact restriction is inherited.

<a id="r3"></a>
**R3. Bedingham and Maroney.** *The thermodynamic cost of quantum operations*, New Journal of Physics 18, 113050 (2016). [Primary text](https://arxiv.org/abs/1604.03749). Direct predecessor for operation-dependent excess heat with an auxiliary restored on the ensemble average. Equations (3), (4), (9), and Appendix A are the relevant comparisons.

<a id="r4"></a>
**R4. Nishiyama.** *On Relations Between Tight Bounds for Symmetric f-Divergences and Binary Divergences*. [Primary text](https://arxiv.org/abs/2210.09571v2). Theorem 1 and Equation (29) supply the sharp classical Jensen–Shannon/triangular-discrimination inequality and mirrored binary equality cases. That scalar inequality is not claimed as new.

<a id="r5"></a>
**R5. Winter.** *Tight uniform continuity bounds for quantum entropies: conditional entropy, relative entropy distance and energy constraints*, Communications in Mathematical Physics 347, 291–313 (2016). [Primary text](https://arxiv.org/abs/1507.07775). Lemma 2, including its cq specialization, supplies continuity with the binary label as the bounded-dimensional subsystem.

<a id="r6"></a>
**R6. Audenaert.** *A sharp continuity estimate for the von Neumann entropy*, Journal of Physics A 40, 8127–8136 (2007). [Primary text](https://arxiv.org/abs/quant-ph/0610146). Supplies the dimension-dependent entropy allowance for approximately restored workspace.

<a id="r7"></a>
**R7. Sutton.** *Computing the Complete CS Decomposition*. [Primary text](https://arxiv.org/abs/0707.1838). Reference for the complete cosine–sine decomposition of block unitaries. The decomposition is a standard tool, not a new parametrization proposed here.

## What the present statement adds

The theorem connects the conditional output tests to an environmental record uniformly in finite environment dimension, converts that record into actual bath heat with charged workspace, and matches the limiting lower bound with a complete thermal construction.

Neither operation-dependent cost, approximate thermodynamic processing, catalytic return, nor work recovery is introduced by this repository. The exact finite-parameter optimum is not claimed.

For a directly checkable comparison, substituting the specified noisy output map into Bedingham–Maroney Equation (9) gives, in natural-log units,

```math
\beta Q\ge J(s)+\frac{s^2z^2}{32},\qquad
J(s)=\ln2-h\!\left(\frac{1+s}{2}\right),\quad
z=\sqrt{1-s^2}-2\epsilon.
```

That particular inequality vanishes in the crossover limit. This comparison concerns that explicit inequality on the specified map; it does not establish that every method in the predecessor is weaker or that no other theorem subsumes the result.

Battery-resource costs and collective work rates are not automatically the mean heat of the single-use microscopic device. Likewise, a theorem for one average state transition does not by itself implement both conditional transformations with the same input-independent apparatus. Relevant resource frameworks appear in P08–P11 below.

## Assumption register

The following register distinguishes direct microscopic precedents from component-level support. The complete conjunction is not called a community consensus.

| Modeling item | Primary precedents | Exact boundary |
|---|---|---|
| Initially independent Gibbs reservoir, joint unitary, complete mean reservoir-energy heat | P01–P05 | Five direct framework precedents, including PRLs P02 and P03. These papers study different tasks. |
| Finite-reservoir modeling | P01, P02, P04, P05, P22 | Four close-framework precedents and one neighboring finite-bath treatment, not five identical models. |
| Degenerate information-bearing boundary energies | P06, P08–P11 | Component-level support; their battery and auxiliary rules differ. |
| External predetermined driving | P04–P06, P12, P15 | A modeling convention, not evidence that control is cheap or autonomous. |
| Finite error and resource-dependent ideal endpoints | P01, P05, P12–P14, P21–P23 | Includes finite-time and measurement models with different allowed dynamics. |
| Trace-distance and stabilized worst-case accuracy | P16–P20 | Five quantum-information precedents, including PRL P17; they support the metric, not an application's need for this tolerance. |
| Returned auxiliary marginal, with possible correlations | P06 and C01–C04 | Five primary precedents, including three PRLs; a returned marginal is not arbitrary multi-use composability. |
| Approximate auxiliary return | R6, C05 | Dimension and entropy capacity must be charged. Trace distance alone is not dimension-uniform. |
| Exact boundary Hamiltonian conjunction and no uniform cap on optimizing resources | Related P01, P05, P06, P21, P22 | Five direct matches to the entire conjunction are not asserted. These remain visible model idealizations. |
| Two inputs, equal priors, particular pure targets, epsilon/s² scaling | P07 and P27 are close task precedents | A selected benchmark and a derived scaling law, not assumptions validated by counting publications. |

The original bath-only framework is enlarged here by the proved cyclic-workspace extension. Precedents that omit auxiliaries should not be counted as proofs of the extension. Conversely, papers permitting consumed batteries are not evidence that their entropy capacity is free in this heat model.

## Primary-paper register

Each P label identifies one paper, not separate counts for its versions or corrections. Links identify the primary texts underlying the source comparison. No paper or textbook content is redistributed.

| ID | Paper and publication | Primary text |
|---|---|---|
| P01 | Reeb–Wolf, *An improved Landauer Principle with finite-size corrections*. NJP 16, 103011 (2014). | [1306.4352](https://arxiv.org/abs/1306.4352v3) |
| P02 | Goold–Paternostro–Modi, *Nonequilibrium Quantum Landauer Principle*. PRL 114, 060602 (2015). | [1402.4499](https://arxiv.org/abs/1402.4499) |
| P03 | Timpanaro–Santos–Landi, *Landauer's Principle at Zero Temperature*. PRL 124, 240601 (2020). | [1911.00910](https://arxiv.org/abs/1911.00910) |
| P04 | Esposito–Lindenberg–Van den Broeck, *Entropy production as correlation between system and reservoir*. NJP 12, 013013 (2010). | [0908.1125](https://arxiv.org/abs/0908.1125) |
| P05 | Mohammady–Mohseni–Omar, *Minimising the heat dissipation of quantum information erasure*. NJP 18, 015011 (2016). | [1510.02062](https://arxiv.org/abs/1510.02062) |
| P06 | Bedingham–Maroney, *The thermodynamic cost of quantum operations*. NJP 18, 113050 (2016). | [1604.03749](https://arxiv.org/abs/1604.03749) |
| P07 | Aksak–Turgut, *Heat Transfer Operators Associated with Quantum Operations*. J. Phys. A 44, 275304 (2011). | [1002.0733](https://arxiv.org/abs/1002.0733v2) |
| P08 | del Rio et al., *The thermodynamic meaning of negative entropy*. Nature 474, 61–63 (2011). | [1009.1630](https://arxiv.org/abs/1009.1630v2) |
| P09 | Faist et al., *The Minimal Work Cost of Information Processing*. Nature Communications 6, 7669 (2015). | [1211.1037](https://arxiv.org/abs/1211.1037v2) |
| P10 | Faist–Renner, *Fundamental Work Cost of Quantum Processes*. PRX 8, 021011 (2018). | [1709.00506](https://arxiv.org/abs/1709.00506v2) |
| P11 | Chiribella et al., *The nonequilibrium cost of accurate information processing*. Nature Communications 13, 7155 (2022). | [2203.09369](https://arxiv.org/abs/2203.09369) |
| P12 | Browne et al., *Guaranteed Energy-Efficient Bit Reset in Finite Time*. PRL 113, 100603 (2014). | [1311.7612](https://arxiv.org/abs/1311.7612) |
| P13 | Zhen et al., *Universal Bound on Energy Cost of Bit Reset in Finite Time*. PRL 127, 190602 (2021). | [2106.00580](https://arxiv.org/abs/2106.00580) |
| P14 | Vu–Saito, *Finite-Time Quantum Landauer Principle and Quantum Coherence*. PRL 128, 010602 (2022). | [2106.05743](https://arxiv.org/abs/2106.05743) |
| P15 | Huber et al., *Thermodynamic cost of creating correlations*. NJP 17, 065008 (2015). | [1404.2169](https://arxiv.org/abs/1404.2169) |
| P16 | Gilchrist–Langford–Nielsen, *Distance measures to compare real and ideal quantum processes*. PRA 71, 062310 (2005). | [quant-ph/0408063](https://arxiv.org/abs/quant-ph/0408063) |
| P17 | Kueng et al., *Comparing Experiments to the Fault-Tolerance Threshold*. PRL 117, 170502 (2016). | [1510.05653](https://arxiv.org/abs/1510.05653) |
| P18 | Sanders–Wallman–Sanders, *Bounding quantum gate error rate based on reported average fidelity*. NJP 18, 012002 (2016). | [1501.04932](https://arxiv.org/abs/1501.04932) |
| P19 | Kretschmann–Schlingemann–Werner, *The Information-Disturbance Tradeoff and the Continuity of Stinespring's Representation*. IEEE TIT 54, 1708–1717 (2008). | [quant-ph/0605009](https://arxiv.org/abs/quant-ph/0605009) |
| P20 | Watrous, *Semidefinite programs for completely bounded norms*. Theory of Computing 5, 217–238 (2009). | [0901.4709](https://arxiv.org/abs/0901.4709) |
| P21 | Masanes–Oppenheim, *A general derivation and quantification of the third law of thermodynamics*. Nature Communications 8, 14538 (2017). | [1412.3828](https://arxiv.org/abs/1412.3828) |
| P22 | Scharlau–Mueller, *Quantum Horn's lemma, finite heat baths, and the third law of thermodynamics*. Quantum 2, 54 (2018). | [1605.06092](https://arxiv.org/abs/1605.06092) |
| P23 | Guryanova–Friis–Huber, *Ideal Projective Measurements Have Infinite Resource Costs*. Quantum 4, 222 (2020). | [1805.11899](https://arxiv.org/abs/1805.11899) |
| P24 | Yan et al., *Single-Atom Demonstration of the Quantum Landauer Principle*. PRL 120, 210601 (2018). | [1803.10424](https://arxiv.org/abs/1803.10424) |
| P25 | Scandi et al., *Minimally Dissipative Information Erasure in a Quantum Dot via Thermodynamic Length*. PRL 129, 270601 (2022). | [2209.01852](https://arxiv.org/abs/2209.01852) |
| P26 | Fellous-Asiani et al., *Optimizing Resource Efficiencies for Scalable Full-Stack Quantum Computers*. PRX Quantum 4, 040319 (2023). | [2209.05469](https://arxiv.org/abs/2209.05469) |
| P27 | Dunlop et al., *Thermodynamically Optimal Protocols for Dual-Purpose Qubit Operations*. The inspected arXiv version is used here without assigning a journal-level count. | [2306.09088v3](https://arxiv.org/abs/2306.09088v3) |
| P28 | Lostaglio–Mueller–Pastena, *Stochastic Independence as a Resource in Small-Scale Thermodynamics*. PRL 115, 150402 (2015). | [1409.3258](https://arxiv.org/abs/1409.3258) |

P24 and P25 establish related experimental primitives, not a demonstration of this crossover. P26 makes clear why microscopic heat cannot be converted directly into wall-plug savings. P27 uses a restricted primitive set; P28 illustrates the importance of correlation resources.

## Returned-workspace references

- **C01:** Boes et al., *Von Neumann entropy from unitarity*, PRL 122, 210402 (2019). [1807.08773](https://arxiv.org/abs/1807.08773). Reusable ancillary catalyst in a unitary/dephasing state-conversion framework.
- **C02:** Wilming, *Entropy and reversible catalysis*, PRL 127, 260402 (2021). [2012.05573](https://arxiv.org/abs/2012.05573). Exact catalyst marginal with approximate system conversion.
- **C03:** Shiraishi–Sagawa, *Quantum Thermodynamics of Correlated-Catalytic State Conversion at Small Scale*, PRL 126, 150502 (2021). [2010.11036](https://arxiv.org/abs/2010.11036). Returned marginal with correlations under Gibbs-preserving maps.
- **C04:** Henao–Uzdin, *Catalytic transformations with finite-size environments: applications to cooling and thermometry*, Quantum 5, 547 (2021). [2010.09070](https://arxiv.org/abs/2010.09070). Explicit finite-environment constructions with different objectives.
- **C05:** Ng et al., *Limits to catalysis in quantum thermodynamics*, NJP 17, 085004 (2015). [1405.3039](https://arxiv.org/abs/1405.3039). Approximate return and the need for dimension/energy restrictions.

These source roles, not similarity of titles alone, determine which assumptions and claims can be compared.
