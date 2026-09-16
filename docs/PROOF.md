# Proof of the precision–heat crossover

[Home](../README.md) · [Model](MODEL.md) · [Theorem](THEOREM.md) · [Construction](CONSTRUCTION.md)

This document gives the lower-bound argument and the passage to the optimal limit. The attaining operation and its complete thermal energy calculation are in the construction document. Entropies are in bits unless stated otherwise. Numbered source labels refer to the [literature guide](LITERATURE.md).

## 1. Separate state kinematics from thermodynamics

Set E = AB and Omega = tau_A tensor gamma_B. The first part of the argument uses only that Omega is a fixed finite density operator independent of the input. It may be rank deficient. Gibbs structure is used only after establishing an entropy increase of this complete environment.

The target tests imply a mean wrong-basis output probability at most d and a total output coherence of magnitude at least s - 2 epsilon, where d is defined in the theorem. If z_x is the off-diagonal element of the conditional system output and delta_x its wrong-basis probability, then

```math
\bar\delta=\frac{\delta_0+\delta_1}{2}\le d,
\qquad |z_0+z_1|\ge s-2\epsilon.
```

Trace distance controls each measurement probability and each off-diagonal error with the conventions used here.

## 2. Arbitrary-unitary reduction

A complete cosine–sine decomposition parametrizes a joint unitary on a qubit and E as

```math
U=\begin{pmatrix}V_0C_0&-V_0K^\dagger\\V_1K&V_1C_1\end{pmatrix},
\quad C_0=\sqrt{I-K^\dagger K},\quad C_1=\sqrt{I-KK^\dagger}.
```

V_0 and V_1 are unitaries and K is a contraction. Zero and unit singular values are allowed. This is not a restriction to commuting reservoirs or to the achieving circuit. A standard reference for the decomposition is [R7].

Put tau_i = V_i Omega V_i^dagger and T = V_1 K V_0^dagger. Define

```math
\ell=\mathrm{Tr}[(\tau_0-\tau_1)T^\dagger].
```

The block calculation gives

```math
\delta_0=\mathrm{Tr}(\tau_0T^\dagger T),\qquad
\delta_1=\mathrm{Tr}(\tau_1TT^\dagger),
\qquad |\ell-z_0-z_1|\le\delta_0+\delta_1.
```

For the last estimate, replace each survival factor C_i by I. Weighted Hilbert–Schmidt Cauchy–Schwarz bounds the replacement on branch i by delta_i, using (I - C_i)^2 <= I - C_i^2. Consequently

```math
|\ell|\ge[s-2\epsilon-2d]_+.
```

The order of this replacement error is d, not its square root. This distinction determines the useful limiting constant.

## 3. A spectral information quantity

For eigenpairs (p_i,u_i) and (q_j,v_j) of tau_0 and tau_1, define

```math
w_{ij}=|\langle u_i|v_j\rangle|^2,\qquad
\mathcal T=\frac12\sum_{ij}
\frac{(p_i-q_j)^2}{p_i+q_j}w_{ij}.
```

A term with p_i = q_j = 0 contributes zero. No inverse of a density matrix is required. Expand ell in the mixed eigenbases and apply weighted Cauchy–Schwarz:

```math
|\ell|^2\le4\bar\delta\,\mathcal T.
```

The second weighted sum is delta_0 + delta_1. Combining with the previous step yields

```math
\mathcal T\ge b_0^2.
```

This is a particular spectral discrimination. It must not be replaced by another quantum divergence with the same classical specialization without proof.

## 4. From spectral discrimination to information

Define classical distributions P_ij = p_i w_ij and Q_ij = q_j w_ij. Both are normalized. Their Jensen–Shannon divergence is bounded above by the quantum Holevo information:

```math
\chi(\tau_0,\tau_1)
=H((\tau_0+\tau_1)/2)-\tfrac12H(\tau_0)-\tfrac12H(\tau_1)
\ge\mathrm{JS}(P,Q).
```

For completeness, this follows from Golden–Thompson and a positive integral representation. In natural logarithms,

```math
x\ln x=x-1+\int_0^\infty
\frac{e^{-tx}-e^{-t}+(x-1)t e^{-t}}{t^2}\,dt.
```

Apply Golden–Thompson to -(t/2)(tau_0 + tau_1). The trace of the exponential of that sum is at most the mixed-spectral sum of exp[-t(p_i+q_j)/2]. Constant and linear terms cancel because w is doubly stochastic. Integration gives the upper bound on the trace of x ln x at the mean state, hence the required **lower** bound on Holevo information. Divide by ln 2 to convert to bits. Zero eigenvalues follow by continuity in finite dimension.

The sharp classical inequality [R4] is

```math
\mathrm{JS}(P,Q)\ge J_2(\sqrt{\mathcal T}).
```

One direct verification uses weights (P+Q)/2 and a = (P-Q)/(P+Q). Jensen–Shannon information is the weighted mean of J_2(a), while triangular discrimination is the weighted mean of a². Convexity in a² follows from

```math
J_2(a)=\frac1{\ln2}\sum_{k=1}^\infty
\frac{a^{2k}}{(2k)(2k-1)}.
```

Jensen's inequality then applies. The sharp scalar inequality and its mirrored binary equality cases are inherited, not a new information inequality of this repository. Altogether,

```math
\chi(\tau_0,\tau_1)\ge J_2(b_0).
```

## 5. Transfer to the actual environment

The comparison states tau_i are not automatically the actual conditional environment states E'_i. Their difference must be charged.

Purify Omega only as a mathematical device. Let v be a unit reference purification and a the survival vector for one branch. If its wrong-basis probability is delta, then

```math
\langle a|a\rangle=1-\delta,\qquad
\langle v|a\rangle=\mathrm{Tr}(\Omega C)\ge1-\delta,
```

because 0 <= C <= I and C >= C². The rank-one trace-norm formula gives

```math
\big\||v\rangle\langle v|-|a\rangle\langle a|\big\|_1
\le\sqrt{4\delta-3\delta^2}.
```

The failed-branch operator adds at most delta to the trace norm. Divide by two and discard the mathematical purification by trace-distance contraction:

```math
D(E'_i,\tau_i)\le f(\delta_i)
=\sqrt{\delta_i(1-3\delta_i/4)}+\delta_i/2.
```

The function f is increasing and concave, so the mean branch distance is at most f(d).

Compare the two classical–quantum states formed by appending a binary bookkeeping label. Winter's cq conditional-entropy continuity bound [R5] uses the **label dimension two**, not the environment dimension. Their Holevo informations differ by at most g(f(d)), with g as in the theorem. The cap at one bit follows from the range of binary-label conditional entropy. Therefore

```math
\chi(X:E')\ge J_2(b_0)-g(f(d)).
```

No energy or entropy of a formal purification has been charged, and no correction grows with the physical environment dimension.

## 6. An entropy increase of the complete environment

Each branch starts with a pure system, so global unitarity preserves total branch entropy H(Omega). Subadditivity gives

```math
H(E'_x)\ge H(\Omega)-H(\sigma_x).
```

A qubit within trace distance epsilon < 1/2 of a pure state has entropy at most h_2(epsilon). Using the definition of Holevo information,

```math
\Delta H_E\ge\chi(X:E')-h_2(\epsilon).
```

Also Delta H_E >= 0. Indeed, the average initial joint entropy is 1 + H(Omega), and the final qubit has entropy at most one bit. This proves

```math
\Delta H_E\ge L(s,\epsilon).
```

## 7. Convert that increase into actual bath heat

Only now use Gibbs structure, and only on B [R1]:

```math
q=H(B')-H(\gamma_B)+D_2(\rho'_B\Vert\gamma_B).
```

Initial independence of A and B implies the exact ledger

```math
q=\Delta H_E-\Delta H_A+I(A:B)'+D_2(\rho'_B\Vert\gamma_B).
```

The last two terms are nonnegative. Substituting the bound on Delta H_E proves both finite inequalities in the theorem. Exact average marginal return sets Delta H_A = 0. Approximate return is charged using [R6], with the dimension-dependent allowance stated there.

The required record concerns E = AB. With a correlated, marginally returned auxiliary, the record need not reside in B alone. A heat-only assertion that ignores consumed auxiliary entropy capacity would be false.

## 8. Take the limit and match it

For positive-error sequences with epsilon/s² tending to finite r,

```math
d/s^2\to\tfrac14+r,\qquad
b_0\to(1+4r)^{-1/2},\qquad
g(f(d))+h_2(\epsilon)\to0.
```

The correction is uniform in dimensions. This gives the required lower limit for the infimum over all finite cyclic devices.

The [construction](CONSTRUCTION.md) has thermal bias

```math
b=\frac{s}{2\sqrt{d(1-d)}}\to(1+4r)^{-1/2}.
```

After M charged recovery swaps its heat satisfies

```math
J_2(b)\le q_M\le J_2(b)+\frac{b\,\mathrm{atanh}(b)}{M\ln2}.
```

For each positive-error pair (s,epsilon), b < 1 and a finite M makes the residual arbitrarily small. Choose M along the sequence so that the residual tends to zero. This also covers r = 0, where b approaches one and M may need to grow faster. Every member remains finite; no exact pure bath is substituted.

The upper and lower limits coincide, proving the crossover. The construction uses no auxiliary, so it remains a valid upper bound when exactly returned auxiliaries are permitted.

## What the computation contributes

The tests check finite-dimensional instances of the unitary reduction, spectral information bridge, environment disturbance, Gibbs ledger, auxiliary controls, and explicit construction. These tests help detect implementation and algebra errors. Arbitrary-dimension validity rests on the argument above, not on sampling finite matrices.

[R1]: LITERATURE.md#r1
[R4]: LITERATURE.md#r4
[R5]: LITERATURE.md#r5
[R6]: LITERATURE.md#r6
[R7]: LITERATURE.md#r7
