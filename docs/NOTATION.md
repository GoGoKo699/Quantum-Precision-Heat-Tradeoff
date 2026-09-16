# Notation and units

[Home](../README.md) · [Physical model](MODEL.md) · [Main result](THEOREM.md) · [Proof](PROOF.md)

This reference fixes conventions used throughout the repository. A prime means a final state; an unconditioned final marginal is averaged over the two equally likely inputs.

<a id="systems"></a>
## Systems, labels, and states

| Symbol | Meaning |
|---|---|
| $S$ | Input/output qubit. |
| $A$ | Finite internal workspace; initial state $\tau_A$. |
| $B$ | Complete finite reservoir; initial Gibbs state $\gamma_B$. |
| $E=AB$ | Complete physical environment; initial state $\Omega$. |
| $x\in\{0,1\}$ | Input label, with equal probabilities. |
| $X$ in $\chi(X:E')$ | Formal classical label register used in the proof, not a free physical controller record. |
| $X,Y,Z$ in a qubit operator | Pauli matrices; context distinguishes Pauli $X$ from the label. |
| $\phi_x(s)$ | Target density operator. |
| $\lvert\phi_x\rangle$ | A normalized state vector for the pure target. |
| $\sigma_x$ | Actual conditional system output. |
| $\rho'_{E,x}$ | Actual conditional environment output; also denoted $E'_x$. |
| $\tau_0,\tau_1$ | Unitary copies of $\Omega$ used for comparison in the proof. They need not be actual outputs. |

The overlap $s$ means $|\langle\phi_0|\phi_1\rangle|=s$; equivalently, $\mathrm{Tr}(\phi_0\phi_1)=s^2$. The target density operator is not itself a state vector.

<a id="distances"></a>
## Accuracy and proof parameters

Trace distance is

```math
D(\rho,\sigma)=\frac12\|\rho-\sigma\|_1.
```

The tolerance $\epsilon$ bounds the maximum of the two output trace distances. The separate tolerance $\delta$ bounds workspace return. Neither is an infidelity.

In the proof, $\delta_x$ is the probability that the output is in the wrong computational-basis state on input $x$, and $\bar\delta=(\delta_0+\delta_1)/2$. Its upper bound is $d=(1-c)/2+\epsilon$, with $c=\sqrt{1-s^2}$. The construction's parameter $u$ equals this same $d$.

The spectral quantity $\mathcal T$ is the normalized triangular discrimination defined in the [spectral lemma](PROOF.md#spectral-discrimination). The symbol $b_0$ bounds $\sqrt{\mathcal T}$ from below; the different symbol $b$ is the explicit construction's thermal bias. Their limiting value is $b_*(r)$, with $r=\lim\epsilon/s^2$.

<a id="entropies"></a>
## Entropies and information

Von Neumann entropy $H$ and binary entropy $h_2$ use base-two logarithms:

```math
H(\rho)=-\mathrm{Tr}\,\rho\log_2\rho,
```

```math
h_2(p)=-p\log_2p-(1-p)\log_2(1-p).
```

The convention is $0\log 0=0$. The natural-log binary entropy is $h(p)=(\ln2)h_2(p)$; entropy in nats is $(\ln2)H$.

Relative entropy uses a double bar and is distinct from trace distance:

```math
D_2(\rho\Vert\sigma)
=\mathrm{Tr}\,\rho(\log_2\rho-\log_2\sigma).
```

The natural-log version is $D(\rho\Vert\sigma)=(\ln2)D_2(\rho\Vert\sigma)$. The different punctuation distinguishes $D(\rho,\sigma)$, a trace distance, from $D(\rho\Vert\sigma)$, relative entropy in nats. Relative entropy is infinite unless the first state's support lies in the second's support. The Gibbs denominator in the heat ledger is full rank.

For equal-prior states $\rho_0,\rho_1$, let $\bar\rho=(\rho_0+\rho_1)/2$. Their Holevo information is

```math
\chi(\rho_0,\rho_1)
=H(\bar\rho)-\frac{H(\rho_0)+H(\rho_1)}2.
```

With a classical label it is also written $\chi(X:E')=I(X:E')$. The classical quantity $\mathrm{JS}(P,Q)$ is the analogous Jensen–Shannon divergence, in bits.

The binary information function is

```math
J_2(b)=1-h_2\!\left(\frac{1+b}2\right).
```

The construction and source comparisons also use $J(b)=(\ln2)J_2(b)$ in nats. Thus $J(s)$ and $J(b)$ are evaluations of the same function at different arguments. The subscript in $J_2$ labels the logarithm base; it does not denote a second derivative.

<a id="energy"></a>
## Energy and signs

| Symbol | Meaning |
|---|---|
| $Q$ | Mean energy gained by the complete reservoir. |
| $\beta$ | Inverse temperature $1/(k_{\mathrm B}T)$. |
| $q$ | Normalized heat $\beta Q/\ln2$. |
| $W$ | Net mean supplied work under the stated boundary conditions. |
| $\Delta H_A$ | Workspace entropy **increase**, final minus initial, in bits. |
| $\Delta H_E$ | Complete-environment entropy **increase**, in bits. |
| $\Delta S_S$ in the construction ledger | System entropy **decrease**, initial minus final, in nats. |

The sign difference in the last row follows the traditional Landauer heat identity. The [model](MODEL.md#heat-work) specifies when $W=Q$ and when the auxiliary boundary-energy change must also be charged.
