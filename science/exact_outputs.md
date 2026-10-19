# The obstruction to exact pure outputs

[Science](README.md#dependencies) · [Model](model.md) · [Theorem](theorem.md) · [Notation](notation.md) · [Thermal construction](thermal_implementation.md)

Finite reservoir rank and exact ensemble-average workspace return exclude exactly nonorthogonal pure outputs. Positive error at each finite stage is therefore part of the limiting theorem, including its high-precision endpoint.

Entropies are in bits unless a natural-log calculation is explicitly marked. All states and unitaries are finite dimensional.

<a id="exact-output-obstruction"></a>
## Exact-output obstruction with returned workspace

Fix $`0<s<1`$ and suppose both branch system outputs are exactly $`\phi_x(s)`$. Let $`k=\mathrm{rank}\,\tau_A`$, $`d_B=\dim\mathcal H_B`$, and let $`P_A`$ project onto $`\mathrm{supp}\,\tau_A`$. Put

```math
\mathcal K=\mathrm{supp}(\tau_A)\otimes\mathcal H_B,
\qquad
\mathrm{rank}(\tau_A\otimes\gamma_B)=k d_B=\dim\mathcal K.
```

The rank identity uses the full rank of the finite Gibbs state. The following elementary support fact will be used below: if $`M\ge0`$ and $`P`$ is a projector, then

```math
\mathrm{Tr}[(I-P)M]
=\|M^{1/2}(I-P)\|_2^2=0
\quad\Longrightarrow\quad M=PMP,
```

where $`\|\cdot\|_2`$ is the Hilbert–Schmidt norm. Exact purity of the system marginal applies this fact with $`P=\phi_x\otimes I_{AB}`$. The final joint state must therefore factor as

```math
\rho'_{SAB,x}=\phi_x\otimes\omega_x,
\qquad \mathrm{rank}\,\omega_x=k d_B,
```

where rank follows from the common unitary and the rank-one system factor. This factorization is forced by purity; correlations within $`AB`$ are still allowed.

Write $`\eta_x=\mathrm{Tr}_B\omega_x`$. Exact ensemble-average return gives $`(\eta_0+\eta_1)/2=\tau_A`$, so

```math
0=\frac12\sum_x\mathrm{Tr}[(I_A-P_A)\eta_x].
```

Each summand is nonnegative. Hence each vanishes, and the support fact gives $`\eta_x=P_A\eta_xP_A`$. Also

```math
\mathrm{Tr}[((I_A-P_A)\otimes I_B)\omega_x]=0,
```

so the same fact with projector $`P_A\otimes I_B`$ gives $`\mathrm{supp}\,\omega_x\subseteq\mathcal K`$. Since each rank equals $`\dim\mathcal K`$, both states are strictly positive on the same support. If $`\lambda>0`$ is the smallest eigenvalue of $`\omega_0`$ restricted to $`\mathcal K`$, then $`\mathrm{Tr}(\omega_0\omega_1)\ge\lambda\mathrm{Tr}\omega_1=\lambda>0`$.

The initial branch states have orthogonal supports because their system inputs are orthogonal. The common unitary preserves that orthogonality, whereas the final factorization implies

```math
0=\mathrm{Tr}(\rho'_{SAB,0}\rho'_{SAB,1})
=s^2\mathrm{Tr}(\omega_0\omega_1)>0.
```

This contradiction proves the [proposition](theorem.md#exact-output-obstruction). Only ensemble-average return was used; the conditional workspace marginals may differ. Positive error is therefore necessary at every finite stage of the cyclic construction, including sequences approaching $`r=0`$. The [consumed-workspace example](model.md#resource-boundary) evades this obstruction by changing the workspace's average marginal.

<a id="computational-support"></a>
## What the calculations check

The [claim-to-evidence map](../verification/CLAIMS.md) links each lemma to finite matrix checks, exact formulas, and numerical records where applicable. These calculations can detect algebra and implementation errors. Arbitrary-dimension validity rests on the lemmas above; the calculation of the upper bound additionally rests on the complete construction's energy ledger.
