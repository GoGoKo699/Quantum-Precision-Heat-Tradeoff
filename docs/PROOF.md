# Proof of the precision–heat crossover

[Home](../README.md) · [Model](MODEL.md) · [Theorem](THEOREM.md) · [Notation](NOTATION.md) · [Construction](CONSTRUCTION.md)

This document proves the dimension-uniform lower bound and its limiting match to the thermal construction. Entropies are in bits unless a natural-log calculation is explicitly marked. All states and unitaries below are finite dimensional.

<a id="dependencies"></a>
## Proof dependencies

Each step identifies its assumptions and the statement passed to the next step:

1. [Conditional output tests](#output-tests) bound wrong-basis probability and enforce common coherence.
2. [Arbitrary-unitary kinematics](#unitary-reduction) express those constraints through comparison environment states.
3. [Spectral discrimination](#spectral-discrimination) gives a quantitative separation between those states.
4. [Information bound](#information-bound) converts that separation to Holevo information without assuming commutation.
5. [Actual-environment transfer](#environment-transfer) charges the distance from comparison states to physical outputs.
6. [Environment entropy](#environment-entropy) turns the retained information into an entropy increase.
7. [Gibbs/auxiliary accounting](#heat-ledger) converts that increase into actual bath heat.
8. [Matching limit](#matching-limit) combines the uniform converse with the [thermal construction](CONSTRUCTION.md#recovery).

The first six steps use only $`E=AB`$ and its fixed input-independent initial state $`\Omega=\tau_A\otimes\gamma_B`$. They allow rank-deficient $`\Omega`$ and do not use Gibbs structure.

<a id="output-tests"></a>
## Lemma 1: conditional output constraints

**Input.** The two output tests in the [model](MODEL.md#task), with $`0<s<1`$ and $`0<\epsilon<c/2`$.

**Output.** Let $`\delta_0=\langle1|\sigma_0|1\rangle`$ and $`\delta_1=\langle0|\sigma_1|0\rangle`$ be wrong-basis probabilities. Let $`z_x=\langle0|\sigma_x|1\rangle`$. Then

```math
\bar\delta=\frac{\delta_0+\delta_1}{2}\le d,
```

```math
|z_0+z_1|\ge s-2\epsilon.
```

Here $`d=(1-c)/2+\epsilon`$ is the [finite theorem's parameter](THEOREM.md#finite-bound).

**Proof.** Each target has wrong-basis probability $`(1-c)/2`$. Trace distance bounds the difference of any measurement probability, giving $`\delta_x\le d`$. For a traceless Hermitian qubit difference with diagonal entry $`a`$ and off-diagonal entry $`z`$, the eigenvalues are $`\pm\sqrt{a^2+|z|^2}`$. Consequently, its trace distance from zero bounds the magnitude of its off-diagonal entry. Both target off-diagonal entries are $`-s/2`$, so $`|z_x+s/2|\le\epsilon`$. The triangle inequality gives the coherence claim.

These are elementary consequences of the specified error metric; no energy statement has yet been used.

<a id="unitary-reduction"></a>
## Lemma 2: exhaustive unitary reduction

**Input.** Any unitary $`U`$ on a qubit and the finite environment $`E`$, with a fixed initial state $`\Omega`$.

**Output.** There are environment unitaries $`V_0,V_1`$ and a contraction $`K`$ for which

```math
U=\begin{pmatrix}
V_0C_0&-V_0K^\dagger\\
V_1K&V_1C_1
\end{pmatrix},
```

```math
C_0=\sqrt{I-K^\dagger K},
```

```math
C_1=\sqrt{I-KK^\dagger}.
```

Define comparison states and a transition operator by

```math
\tau_i=V_i\Omega V_i^\dagger,
\qquad T=V_1KV_0^\dagger,
```

and put $`\ell=\mathrm{Tr}[(\tau_0-\tau_1)T^\dagger]`$. Then

```math
\delta_0=\mathrm{Tr}(\tau_0T^\dagger T),
```

```math
\delta_1=\mathrm{Tr}(\tau_1TT^\dagger),
```

```math
|\ell-z_0-z_1|\le\delta_0+\delta_1.
```

In particular, Lemma 1 gives

```math
|\ell|\ge[s-2\epsilon-2d]_+.
```

**Why every unitary is included.** The complete cosine–sine decomposition [Sutton, Equation (1.1)](LITERATURE.md#r7), specialized to two equally sized block rows and columns, writes $`U=\mathsf L\mathsf C\mathsf R^\dagger`$. The outer factors are block-diagonal unitaries with blocks $`L_i,R_i`$. After an allowed sign convention for those factors, the central matrix is

```math
\mathsf C=
\begin{pmatrix}\Gamma&-\Lambda\\
\Lambda&\Gamma\end{pmatrix}.
```

Here $`\Gamma`$ and $`\Lambda`$ are diagonal matrices with entries $`\cos\theta_j`$ and $`\sin\theta_j`$, for $`\theta_j\in[0,\pi/2]`$. Set

```math
V_i=L_iR_i^\dagger,
\qquad K=R_1\Lambda R_0^\dagger.
```

Then $`C_0=R_0\Gamma R_0^\dagger`$ and $`C_1=R_1\Gamma R_1^\dagger`$, giving the displayed parametrization. Angles zero and $`\pi/2`$ are included: zero singular values of $`K`$ give survival blocks, and unit singular values give zero survival factors. No block is inverted, no full-rank condition is imposed on $`\Omega`$, and no channel or bath basis is selected in advance.

**Coherence calculation.** Directly taking the system off-diagonal block gives

```math
z_0=\mathrm{Tr}(V_0C_0\Omega K^\dagger V_1^\dagger),
```

```math
z_1=-\mathrm{Tr}(V_0K^\dagger\Omega C_1V_1^\dagger).
```

Replacing each survival factor $`C_i`$ by $`I`$ makes their sum exactly $`\ell`$. To bound the error, write $`W=V_1^\dagger V_0`$. The first replacement error has magnitude

```math
|\mathrm{Tr}[\Omega K^\dagger W(I-C_0)]|.
```

Weighted Hilbert–Schmidt Cauchy–Schwarz bounds its square by

```math
\mathrm{Tr}(\Omega K^\dagger K)\,
\mathrm{Tr}[\Omega(I-C_0)^2].
```

Since $`(I-C_0)^2\le I-C_0^2=K^\dagger K`$, this is at most $`\delta_0^2`$. The second replacement error, written as $`\mathrm{Tr}[\Omega(I-C_1)WK^\dagger]`$, is similarly at most $`\delta_1`$. Adding the two errors proves the claim.

The error is of order $`d`$, rather than $`\sqrt d`$. Keeping this order is essential to the limiting constant.

<a id="spectral-discrimination"></a>
## Lemma 3: spectral discrimination from kinematics

**Input.** The comparison states, transition operator, and constraints from Lemma 2.

**Output.** If $`(p_i,u_i)`$ and $`(q_j,v_j)`$ are complete eigenpairs of $`\tau_0,\tau_1`$, define

```math
w_{ij}=|\langle u_i|v_j\rangle|^2,
```

```math
\mathcal T=\frac12\sum_{ij}
\frac{(p_i-q_j)^2}{p_i+q_j}\,w_{ij}.
```

A term with $`p_i=q_j=0`$ is defined to be zero. Then

```math
|\ell|^2\le4\bar\delta\,\mathcal T,
\qquad \mathcal T\ge b_0^2.
```

**Proof.** Let $`t_{ij}=\langle u_i|T^\dagger|v_j\rangle`$. Inserting complete eigenbases gives

```math
\ell=\sum_{ij}(p_i-q_j)
\langle v_j|u_i\rangle\,t_{ij}.
```

The two factors in weighted Cauchy–Schwarz are $`2\mathcal T`$ and

```math
\begin{aligned}
\sum_{ij}(p_i+q_j)|t_{ij}|^2
&=\mathrm{Tr}(\tau_0T^\dagger T)\\
&\quad+\mathrm{Tr}(\tau_1TT^\dagger)\\
&=2\bar\delta.
\end{aligned}
```

Terms whose denominator vanishes also have zero numerator and zero weight in this bound. Thus $`|\ell|^2\le4\bar\delta\mathcal T\le4d\mathcal T`$. Combine with Lemma 2 and the definition of $`b_0`$.

This particular spectral expression is used throughout the argument. Another quantum divergence with the same classical specialization cannot be substituted without proof.

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
(\ln2)\chi=A_0-\mathrm{Tr}(M\ln M),
```

```math
(\ln2)\mathrm{JS}
=A_0-\sum_{ij}w_{ij}m_{ij}\ln m_{ij}.
```

It therefore suffices to prove an **upper** bound on $`\mathrm{Tr}(M\ln M)`$. The inherited [Golden–Thompson inequality](LITERATURE.md#r8) gives, for $`t>0`$,

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
```

```math
\mathcal T=\sum_{ij}\mu_{ij}a_{ij}^2.
```

The formula for $`J_2`$ is even, so here it also applies to negative $`a_{ij}`$. The power series

```math
J_2(a)=\frac1{\ln2}
\sum_{k=1}^{\infty}\frac{a^{2k}}{(2k)(2k-1)}
```

shows that $`t\mapsto J_2(\sqrt t)`$ is convex on $`[0,1]`$, with the endpoints defined by continuity. Jensen's inequality proves $`\mathrm{JS}\ge J_2(\sqrt{\mathcal T})`$.

This is the inherited sharp classical inequality in [Nishiyama, Theorem 1 and Equation (29)](LITERATURE.md#r4), using the same factor $`1/2`$ in triangular discrimination. Mirrored binary distributions attain it:

```math
P=\left(\frac{1+b}2,\frac{1-b}2\right),
```

```math
Q=\left(\frac{1-b}2,\frac{1+b}2\right).
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
\omega_{XE}=\frac12\sum_x
|x\rangle\langle x|\otimes\tau_x,
```

```math
\zeta_{XE}=\frac12\sum_x
|x\rangle\langle x|\otimes E'_x.
```

Their block-diagonal structure makes their trace distance the mean branch distance. Write this distance as $`\eta\le f(d)`$.

[Winter, Lemma 2, cq specialization](LITERATURE.md#r5) bounds the conditional-entropy difference by

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

A qubit within trace distance $`\epsilon<1/2`$ of a pure state has entropy at most $`h_2(\epsilon)`$; this is also the dimension-two case of [Audenaert's sharp continuity bound](LITERATURE.md#r6). Averaging the branch inequality and adding the Holevo information yields

```math
\Delta H_E\ge\chi(X:E')-h_2(\epsilon).
```

There is a second bound, $`\Delta H_E\ge0`$, specific to the equally likely orthogonal inputs. The entropy of the initial averaged joint state $`(I/2)\otimes\Omega`$ is $`1+H(\Omega)`$. The final system entropy is at most one bit, so subadditivity after the same unitary gives

```math
1+H(\Omega)\le1+H(\rho'_E).
```

Taking the maximum of this zero bound and the information bound proves exactly the function $`L`$ in the theorem.

<a id="heat-ledger"></a>
## Lemma 7: Gibbs and workspace accounting

**Input.** The environment entropy bound and the [physical model](MODEL.md#apparatus), with $`\Omega=\tau_A\otimes\gamma_B`$.

**Output.** Every implementation obeys the finite theorem, including its retained nonnegative terms.

**Proof.** Apply Gibbs structure only to $`B`$. Its logarithm gives the exact identity

```math
q=\Delta H_B+D_2(\rho'_B\Vert\gamma_B),
```

where $`\Delta H_B=H(\rho'_B)-H(\gamma_B)`$. This is the reservoir form of the microscopic heat identity in [Reeb–Wolf, Theorem 3, Equations (21)–(22)](LITERATURE.md#r1).

Initial independence of $`A,B`$ implies

```math
\Delta H_E=\Delta H_A+\Delta H_B-I(A:B)'.
```

Substitute this expression for $`\Delta H_B`$:

```math
\begin{aligned}
q+\Delta H_A={}&\Delta H_E+I(A:B)'\\
&+D_2(\rho'_B\Vert\gamma_B).
\end{aligned}
```

Mutual information and relative entropy are nonnegative. Lemma 6 therefore proves both finite inequalities. Exact ensemble-marginal return sets $`\Delta H_A=0`$. Approximate return uses [Audenaert, Theorem 1, Equation (6)](LITERATURE.md#r6), with the capped allowance in the [theorem](THEOREM.md#workspace-return).

The necessary information concerns $`E=AB`$. When a workspace is marginally returned but correlated, the record need not be in $`B`$ alone. Applying a Gibbs identity to a possibly nonthermal $`\tau_A`$, or ignoring a consumed positive $`\Delta H_A`$, would change the resource model.

<a id="matching-limit"></a>
## The limiting match

**Lower direction.** Let $`s\to0`$ along any sequence with $`\epsilon>0`$ and $`\epsilon/s^2\to r<\infty`$. The finite definitions give

```math
\frac d{s^2}\longrightarrow\frac14+r,
```

```math
b_0\longrightarrow\frac1{\sqrt{1+4r}},
```

```math
g(f(d))+h_2(\epsilon)\longrightarrow0.
```

The lower bound holds for every finite returned-workspace device and has no dimension-dependent correction. It therefore survives taking the infimum over devices and gives $`\liminf q_{\min}\ge F(r)`$.

**Upper direction.** In the [explicit collision](CONSTRUCTION.md#collision), the construction parameter $`u`$ equals the theorem's $`d`$. Its thermal bias obeys

```math
b=\frac{s}{2\sqrt{d(1-d)}}
\longrightarrow\frac1{\sqrt{1+4r}}.
```

For each positive-error pair in the stated domain, $`0<b<1`$. The [charged recovery calculation](CONSTRUCTION.md#recovery) gives

```math
J_2(b)\le q_M
\le J_2(b)+\frac{b\,\mathrm{atanh}(b)}{M\ln2}.
```

For any desired positive residual, a finite integer $`M`$ makes the last term smaller than it. Along the parameter sequence, choose the residual to tend to zero and choose such a finite $`M`$ at each stage. This gives $`\limsup q_{\min}\le F(r)`$.

At $`r=0`$, the bias tends to one. The gap and the necessary recovery resources may grow, but every finite stage still has positive error, $`b<1`$, and a full-rank finite Gibbs bath. The proof never substitutes an exact pure bath resource. The two limits coincide.

Recovery is needed to approach the optimal curve. The [finite strict/relaxed separation](FINITE_BENCHMARK.md#comparison) already uses the bare collision heat and requires no recovery claim.

<a id="computational-support"></a>
## What the calculations check

The [claim-to-evidence map](CLAIMS.md) links each lemma to finite matrix checks, exact formulas, and numerical records where applicable. These calculations can detect algebra and implementation errors. Arbitrary-dimension validity rests on the lemmas above; the calculation of the upper bound additionally rests on the complete construction's energy ledger.
