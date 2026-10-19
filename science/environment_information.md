# The information retained by the environment

[Science](README.md#dependencies) · [Model](model.md) · [Theorem](theorem.md) · [Notation](notation.md) · [Thermal construction](thermal_implementation.md)

Lemmas 4–6 turn the spectral separation into information in the actual environment and then an entropy increase. The continuity correction depends on the binary label, not on the environment dimension.

Entropies are in bits unless a natural-log calculation is explicitly marked. All states and unitaries are finite dimensional.

<a id="information-bound"></a>
## Lemma 4: spectral discrimination implies information

**Input.** Any two finite density operators $`\tau_0,\tau_1`$, including noncommuting or rank-deficient ones.

**Output.** With the mixed-spectral weights from Lemma 3,

```math
\chi(\tau_0,\tau_1)
\ge \mathrm{JS}(P,Q)
\ge J_2(\sqrt{\mathcal T}),
```

where $`P_{ij}=p_iw_{ij}`$ and $`Q_{ij}=q_jw_{ij}`$. Hence the kinematic states satisfy $`\chi(\tau_0,\tau_1)\ge J_2(b_0)`$.

### Noncommuting comparison and its direction

The matrix $`w`$ is doubly stochastic, so $`P,Q`$ are normalized distributions. They are algebraic comparison distributions; the proof does not assume that one measurement simultaneously reveals both eigenbases.

Let $`M=(\tau_0+\tau_1)/2`$ and $`m_{ij}=(p_i+q_j)/2`$. Work in natural logarithms just in this calculation. Put

```math
A_0=\frac12\sum_i p_i\ln p_i
+\frac12\sum_j q_j\ln q_j.
```

The two information quantities are

```math
\begin{aligned}
(\ln2)\chi&=A_0-\mathrm{Tr}(M\ln M),\\
(\ln2)\mathrm{JS}&=A_0-\sum_{ij}w_{ij}m_{ij}\ln m_{ij}.
\end{aligned}
```

It therefore suffices to prove an **upper** bound on $`\mathrm{Tr}(M\ln M)`$. The inherited [Golden–Thompson inequality](../references/LITERATURE.md#r8) gives, for $`t>0`$,

```math
\begin{aligned}
\mathrm{Tr}(e^{-tM})
&\le\mathrm{Tr}(e^{-t\tau_0/2}e^{-t\tau_1/2})\\
&=\sum_{ij}w_{ij}e^{-tm_{ij}}.
\end{aligned}
```

To convert this into the needed entropy comparison, define

```math
R_t(x)=e^{-tx}-e^{-t}+(x-1)t e^{-t}.
```

The scalar identity is

```math
x\ln x=x-1+
\int_0^\infty\frac{R_t(x)}{t^2}\,dt.
```

For $`x>0`$, it follows by differentiating twice: the integral has second derivative $`1/x`$, and value and first derivative zero at $`x=1`$. The affine term supplies the first derivative of $`x\ln x`$ there. Also $`R_t(x)\ge0`$ by convexity of the exponential.

Apply the identity to the eigenvalues of $`M`$ and to the $`m_{ij}`$. The constant and linear terms cancel because $`\sum_{ij}w_{ij}=\dim E`$ and both weighted traces equal one. Integrating the Golden–Thompson inequality with its positive weight yields

```math
\mathrm{Tr}(M\ln M)
\le\sum_{ij}w_{ij}m_{ij}\ln m_{ij}.
```

The two preceding expressions now give $`\chi\ge\mathrm{JS}`$, with the stated direction. Zero eigenvalues follow by continuity: replace both states by their mixtures with the same maximally mixed state, keep complete eigenbases, and let the mixing weight vanish. In finite dimension, $`x\ln x`$ is continuous at zero.

Golden–Thompson is the inherited trace inequality; the integral conversion above spells out its use for this spectral-information comparison.

### Sharp scalar inequality and equality cases

On cells with $`P_{ij}+Q_{ij}>0`$, define

```math
\mu_{ij}=\frac{P_{ij}+Q_{ij}}2,
\qquad
a_{ij}=\frac{P_{ij}-Q_{ij}}{P_{ij}+Q_{ij}}.
```

Then $`\sum_{ij}\mu_{ij}=1`$, $`|a_{ij}|\le1`$, and

```math
\mathrm{JS}(P,Q)=\sum_{ij}\mu_{ij}J_2(a_{ij}),
\qquad \mathcal T=\sum_{ij}\mu_{ij}a_{ij}^2.
```

The formula for $`J_2`$ is even, so here it also applies to negative $`a_{ij}`$. The power series

```math
J_2(a)=\frac1{\ln2}
\sum_{k=1}^{\infty}\frac{a^{2k}}{(2k)(2k-1)}
```

shows that $`t\mapsto J_2(\sqrt t)`$ is convex on $`[0,1]`$, with the endpoints defined by continuity. Jensen's inequality proves $`\mathrm{JS}\ge J_2(\sqrt{\mathcal T})`$.

This is the inherited sharp classical inequality in [Nishiyama, Theorem 1 and Equation (29)](../references/LITERATURE.md#r4), using the same factor $`1/2`$ in triangular discrimination. Mirrored binary distributions attain it:

```math
P=\left(\frac{1+b}2,\frac{1-b}2\right),
\qquad Q=\left(\frac{1-b}2,\frac{1+b}2\right).
```

They have $`\mathcal T=b^2`$ and $`\mathrm{JS}=J_2(b)`$. More generally, scalar equality requires constant $`a_{ij}^2`$ on positive-weight cells, as follows from strict convexity. Commuting mirrored binary density operators attain both information comparisons. These equality cases do not assert equality in every earlier finite kinematic estimate.

<a id="environment-transfer"></a>
## Lemma 5: transfer to the physical environment

**Input.** The arbitrary-unitary decomposition from Lemma 2, with actual conditional environment states $`E'_x=\rho'_{E,x}`$.

**Output.** The actual environment retains

```math
\chi(X:E')\ge J_2(b_0)-g(f(d)).
```

The correction is independent of $`\dim E`$.

### Distance from each comparison state

Purify $`\Omega`$ for a mathematical estimate only. In the frame of the appropriate $`V_x`$, let $`v`$ be a unit purification of the comparison state and $`a=(C_x\otimes I)v`$ its unnormalized survival vector. For $`\delta=\delta_x`$,

```math
\langle a|a\rangle=1-\delta,
\qquad
\langle v|a\rangle\ge1-\delta.
```

The second inequality follows from $`0\le C_x\le I`$ and $`C_x\ge C_x^2`$. Set $`N=\||v\rangle\langle v|-|a\rangle\langle a|\|_1`$. The rank-one trace-norm identity gives

```math
N^2=(2-\delta)^2-4|\langle v|a\rangle|^2
\le4\delta-3\delta^2.
```

The failed-branch operator is positive with trace $`\delta`$. Adding it, dividing the trace norm by two, and tracing out the formal purification yields

```math
D(E'_x,\tau_x)\le f(\delta_x),
```

with $`f`$ defined in the theorem. The function $`f`$ is increasing and concave on $`[0,1]`$. For example, in the interior,

```math
f''(t)=-\frac1{4[t(1-3t/4)]^{3/2}}<0,
```

and $`f'(1)=0`$. Consequently the mean branch distance is at most $`f(\bar\delta)\le f(d)`$.

### Continuity with a binary classical label

Append the formal label to each pair of environment states:

```math
\omega_{XE}=\frac12\sum_x|x\rangle\langle x|\otimes\tau_x,
\qquad \zeta_{XE}=\frac12\sum_x|x\rangle\langle x|\otimes E'_x.
```

Their block-diagonal structure makes their trace distance the mean branch distance. Write this distance as $`\eta\le f(d)`$.

[Winter, Lemma 2, cq specialization](../references/LITERATURE.md#r5) bounds the conditional-entropy difference by

```math
\eta\log_2\dim X+
(1+\eta)h_2\!\left(\frac{\eta}{1+\eta}\right).
```

Here the bounded-dimensional subsystem is **the classical label** $`X`$, with $`\dim X=2`$. The conditioning subsystem is the entire environment. Both states have $`H(X)=1`$, so this is also a bound on the difference of their Holevo informations. Since $`0\le H(X|E)\le1`$, that difference is additionally capped at one bit. Monotonicity of the correction in $`\eta`$ gives $`g(f(d))`$ and proves the lemma.

The inspected source, arXiv:1507.07775v6, explicitly treats both qc and cq states in Lemma 2. No entropy-continuity factor involving the reservoir dimension enters here, and the formal purification is not a charged physical resource.

<a id="environment-entropy"></a>
## Lemma 6: entropy increase of the complete environment

**Input.** Lemma 5, a pure input system on each branch, and an initially independent environment $`\Omega`$.

**Output.**

```math
\Delta H_E
=H(\rho'_E)-H(\Omega)
\ge L(s,\epsilon).
```

**Proof.** Each branch starts with total entropy $`H(\Omega)`$, which the joint unitary preserves. Subadditivity gives

```math
H(E'_x)\ge H(\Omega)-H(\sigma_x).
```

A qubit within trace distance $`\epsilon<1/2`$ of a pure state has entropy at most $`h_2(\epsilon)`$; this is also the dimension-two case of [Audenaert's sharp continuity bound](../references/LITERATURE.md#r6). Averaging the branch inequality and adding the Holevo information yields

```math
\Delta H_E\ge\chi(X:E')-h_2(\epsilon).
```

There is a second bound, $`\Delta H_E\ge0`$, specific to the equally likely orthogonal inputs. The entropy of the initial averaged joint state $`(I/2)\otimes\Omega`$ is $`1+H(\Omega)`$. The final system entropy is at most one bit, so subadditivity after the same unitary gives

```math
1+H(\Omega)\le1+H(\rho'_E).
```

Taking the maximum of this zero bound and the information bound proves exactly the function $`L`$ in the theorem.
