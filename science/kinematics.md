# Output accuracy and arbitrary-unitary kinematics

[Science](README.md#dependencies) · [Model](model.md) · [Theorem](theorem.md) · [Notation](notation.md) · [Thermal construction](thermal_implementation.md)

The two output tests constrain every allowed joint unitary before Gibbs structure is used. Lemmas 1–3 translate the required coherence and small transition probabilities into spectral separation of comparison environment states.

Entropies are in bits unless a natural-log calculation is explicitly marked. All states and unitaries are finite dimensional.

<a id="output-tests"></a>
## Lemma 1: conditional output constraints

**Input.** The two output tests in the [model](model.md#task), with $`0<s<1`$ and $`0<\epsilon<c/2`$.

**Output.** Let $`\delta_0=\langle1|\sigma_0|1\rangle`$ and $`\delta_1=\langle0|\sigma_1|0\rangle`$ be wrong-basis probabilities. Let $`z_x=\langle0|\sigma_x|1\rangle`$. Then

```math
\bar\delta=\frac{\delta_0+\delta_1}{2}\le d,
\qquad |z_0+z_1|\ge s-2\epsilon.
```

Here $`d=(1-c)/2+\epsilon`$ is the [finite theorem's parameter](theorem.md#finite-bound).

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
\qquad
\begin{aligned}
C_0&=\sqrt{I-K^\dagger K},\\
C_1&=\sqrt{I-KK^\dagger}.
\end{aligned}
```

Define comparison states and a transition operator by

```math
\tau_i=V_i\Omega V_i^\dagger,
\qquad T=V_1KV_0^\dagger,
```

and put $`\ell=\mathrm{Tr}[(\tau_0-\tau_1)T^\dagger]`$. Then

```math
\begin{gathered}
\delta_0=\mathrm{Tr}(\tau_0T^\dagger T),
\qquad \delta_1=\mathrm{Tr}(\tau_1TT^\dagger),\\
|\ell-z_0-z_1|\le\delta_0+\delta_1.
\end{gathered}
```

In particular, Lemma 1 gives

```math
|\ell|\ge[s-2\epsilon-2d]_+.
```

**Why every unitary is included.** The complete cosine–sine decomposition [Sutton, Equation (1.1)](../references/LITERATURE.md#r7), specialized to two equally sized block rows and columns, writes $`U=\mathsf L\mathsf C\mathsf R^\dagger`$. The outer factors are block-diagonal unitaries with blocks $`L_i,R_i`$. After an allowed sign convention for those factors, the central matrix is

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
\begin{aligned}
z_0&=\mathrm{Tr}(V_0C_0\Omega K^\dagger V_1^\dagger),\\
z_1&=-\mathrm{Tr}(V_0K^\dagger\Omega C_1V_1^\dagger).
\end{aligned}
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
\qquad \mathcal T=\frac12\sum_{ij}
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
&=\mathrm{Tr}(\tau_0T^\dagger T)+\mathrm{Tr}(\tau_1TT^\dagger)\\
&=2\bar\delta.
\end{aligned}
```

Terms whose denominator vanishes also have zero numerator and zero weight in this bound. Thus $`|\ell|^2\le4\bar\delta\mathcal T\le4d\mathcal T`$. Combine with Lemma 2 and the definition of $`b_0`$.

This particular spectral expression is used throughout the argument. Another quantum divergence with the same classical specialization cannot be substituted without proof.
