# Precision–heat theorem

[Home](../README.md) · [Physical model](MODEL.md) · [Notation](NOTATION.md) · [Proof](PROOF.md) · [Thermal implementation](CONSTRUCTION.md)

All statements use the [canonical model](MODEL.md): two equally likely basis inputs, maximum branch trace error, an input-independent unitary, and the complete initially Gibbs reservoir. Entropies are in bits and $`q=Q/(k_{\mathrm B}T\ln2)`$.

<a id="optimal-crossover"></a>
## Optimal limiting crossover

Let $`q_{\min}(s,\epsilon)`$ be the infimum of mean heat over allowed **finite** implementations whose workspace returns exactly on the ensemble-average marginal. For a finite ratio $`r\ge0`$, define

```math
b_*(r)=\frac1{\sqrt{1+4r}},
```

```math
F(r)=1-h_2\!\left(\frac{1+b_*(r)}2\right).
```

Here $`h_2`$ is binary entropy in bits. For every sequence satisfying

```math
s\to0,\qquad \epsilon>0,\qquad
\frac{\epsilon}{s^2}\to r,
```

the optimal heat obeys

```math
q_{\min}(s,\epsilon)\longrightarrow F(r).
```

Errors remain positive at every finite stage, including the endpoint $`r=0`$, where $`F(0)=1`$. A [dimension-uniform converse](PROOF.md#matching-limit) and a [thermal construction with recovery](CONSTRUCTION.md#recovery) establish the two directions. The construction uses no workspace, so it also supplies the upper bound when returned workspace is allowed.

This is an optimal **joint limiting law**, not an exact finite-$`s`$ optimum. The large-$`r`$ expansion of $`F`$ is not automatically a uniform theorem over every path with $`\epsilon/s^2\to\infty`$. Individual implementations remain finite, while the optimizing sequence can use [growing physical resources](MODEL.md#limits).

<a id="finite-bound"></a>
## Dimension-uniform finite lower bound

Assume $`0<s<1`$ and $`0<\epsilon<c/2`$, where $`c=\sqrt{1-s^2}`$. The mean wrong-basis probability is bounded by

```math
d=\frac{s^2}{2(1+c)}+\epsilon.
```

This equals $`(1-c)/2+\epsilon`$ and lies below $`1/2`$. The displayed form avoids cancellation for small $`s`$. Define the kinematic bias bound

```math
b_0=\frac{[s-2\epsilon-2d]_+}{2\sqrt d},
```

where $`[v]_+=\max\{0,v\}`$. The following functions specify the finite correction:

```math
J_2(b)=1-h_2\!\left(\frac{1+b}2\right),
```

```math
f(d)=\sqrt{d(1-3d/4)}+d/2.
```

For $`0\le\eta\le1`$, first set

```math
g_0(\eta)=\eta+(1+\eta)
h_2\!\left(\frac{\eta}{1+\eta}\right),
```

and then $`g(\eta)=\min\{1,g_0(\eta)\}`$. To keep the three corrections visible, write

```math
L_0(s,\epsilon)=J_2(b_0)-g(f(d))-h_2(\epsilon),
```

```math
L(s,\epsilon)=\max\{0,L_0(s,\epsilon)\}.
```

**Finite theorem.** Every allowed implementation satisfies

```math
q+\Delta H_A\ge L(s,\epsilon).
```

A stronger version retains the nonnegative final correlation and bath disequilibrium terms:

```math
\begin{aligned}
q+\Delta H_A\ge{}&L(s,\epsilon)+I(A:B)'\\
&+D_2(\rho'_B\Vert\gamma_B).
\end{aligned}
```

Here $`\Delta H_A`$ is the **increase** in workspace entropy. All final marginals and mutual information refer to the equal-prior ensemble average. Exact marginal return gives $`\Delta H_A=0`$ and hence $`q\ge L`$. The bound is independent of workspace and bath dimensions. It is not asserted to be the best bound at each finite parameter pair.

The [proof dependency map](PROOF.md#dependencies) leads directly to each ingredient; the final conversion is the [Gibbs/auxiliary ledger](PROOF.md#heat-ledger).

<a id="workspace-return"></a>
## Approximate workspace return

For a workspace of dimension $`n\ge2`$ with $`D(\rho'_A,\tau_A)\le\delta`$, define

```math
t=\min\{\delta,1-1/n\},
```

```math
a_n(\delta)=h_2(t)+t\log_2(n-1).
```

Set $`a_1(\delta)=0`$. The [sharp entropy-continuity inequality](LITERATURE.md#r6) bounds $`\Delta H_A\le a_n(\delta)`$ and yields

```math
q\ge L(s,\epsilon)-a_n(\delta).
```

This lower bound can be negative when entropy capacity is consumed; it should not be clipped to zero without an additional argument. The limiting curve remains unchanged for families in which the permitted auxiliary entropy increase vanishes uniformly. For fixed $`n`$, a return tolerance $`\delta\to0`$ is sufficient. More generally, a particular family with actual $`\Delta H_A\to0`$ obeys the same limiting converse.

<a id="finite-values"></a>
## One finite comparison

At $`s=0.05`$ and strict error $`\epsilon=0.0001`$, the universal bound is $`L\approx0.498044180`$. At the same overlap and relaxed error $`\epsilon=0.0025`$, the bare one-bath-qubit construction costs $`q\approx0.311484646`$. A 16-level strict-device workspace returned within $`0.0001`$ reduces the strict lower bound to approximately $`0.496180457`$.

The [finite benchmark](FINITE_BENCHMARK.md#comparison) compares a lower bound with the energy cost of one explicit device. It does not require recovery or identify either value as a finite optimum. See the [claim-to-evidence map](CLAIMS.md) for derivations, executable checks, and the committed result record.
