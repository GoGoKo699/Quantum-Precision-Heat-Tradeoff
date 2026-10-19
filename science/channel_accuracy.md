# Conditional tests and full-channel accuracy

[Science](README.md#dependencies) · [Model](model.md) · [Theorem](theorem.md) · [Notation](notation.md) · [Thermal construction](thermal_implementation.md)

An additional degenerate Gibbs qubit converts any branch-feasible device into a channel-feasible device at the same equal-prior mean heat and workspace return. This identifies the two infima without claiming a finite optimum.

Entropies are in bits unless a natural-log calculation is explicitly marked. All states and unitaries are finite dimensional.

<a id="channel-equivalence"></a>
## Full-channel accuracy at unchanged mean heat

Use the two optimizations and target channel in the [channel-equivalence corollary](theorem.md#channel-equivalence), with $`0<s<1`$ and $`0<\epsilon<\sqrt{1-s^2}/2`$. The diamond norm is the completely bounded trace norm; see [Watrous](../references/LITERATURE.md#p20) for this standard metric. Diamond feasibility implies both branch tests, hence $`q_{\min}\le q_{\min}^{\diamond}`$.

**Physical dephasing.** Take any branch-feasible apparatus, with unitary $`U_{SAB}`$ and system channel $`\mathcal N`$. Add a reservoir qubit $`C`$ with $`H_C=0`$ and $`\gamma_C=I_C/2`$. At the same temperature the complete initial reservoir is

```math
\gamma_{BC}=\gamma_B\otimes\frac{I_C}{2},
\qquad H_{BC}=H_B\otimes I_C.
```

This is a finite full-rank Gibbs state. Apply the standard controlled-phase realization of dephasing,

```math
W_{CS}=|0\rangle\langle0|_C\otimes I_S
       +|1\rangle\langle1|_C\otimes Z_S,
```

then apply $`U_{SAB}`$, acting trivially on $`C`$. Their product is one input-independent joint unitary on the enlarged apparatus. Since $`Z|x\rangle=(-1)^x|x\rangle`$,

```math
W_{CS}\left(\frac{I_C}{2}\otimes|x\rangle\langle x|\right)W_{CS}^{\dagger}
=\frac{I_C}{2}\otimes|x\rangle\langle x|.
```

Thus each original branch enters $`U_{SAB}`$ unchanged, and its entire final state on $`SAB`$ is preserved, with an independent $`I_C/2`$ factor. Both branch outputs, their reservoir energy changes, and the ensemble-average workspace return are identical to those of the original device. The additional component has zero energy at all times because $`H_C=0`$, so the complete charged heat is unchanged. Adding this qubit is permitted because the optimization imposes no fixed reservoir dimension.

For a general system input, tracing out $`C`$ after the controlled phase gives

```math
\mathcal D_Z(\rho)=\frac{\rho+Z\rho Z}{2},
\qquad
\widetilde{\mathcal N}(\rho)
=(\mathcal N\circ\mathcal D_Z)(\rho)
=\sum_x\langle x|\rho|x\rangle\sigma_x.
```

The physical reservoir qubit supplies the dephasing; it is included in the initial Gibbs state and the heat ledger.

<a id="dephased-channel-distance"></a>
**Channel distance.** Write $`\Delta_x=\sigma_x-\phi_x`$ and $`e=\max_x\|\Delta_x\|_1/2`$. For any state $`\rho_{SR}`$ including a reference, its diagonal reference blocks $`R_x=\langle x|\rho_{SR}|x\rangle`$ are positive and have total trace one. Therefore

```math
\begin{aligned}
[(\widetilde{\mathcal N}-\mathcal T_s)\otimes\mathrm{id}_R](\rho_{SR})
&=\sum_x\Delta_x\otimes R_x,\\
\frac12\left\|\sum_x\Delta_x\otimes R_x\right\|_1
&\le\sum_x\frac{\|\Delta_x\|_1}{2}\,\mathrm{Tr}R_x\le e.
\end{aligned}
```

The bound also holds for the induced norm on arbitrary operators. For any operator $`M`$ on $`SR`$, with diagonal blocks $`M_{xx}`$, unitary invariance and convexity of trace norm give the pinching bound

```math
\sum_x\|M_{xx}\|_1
=\|(\mathcal D_Z\otimes\mathrm{id}_R)(M)\|_1
\le\|M\|_1.
```

Indeed, this pinching is the average of conjugation by the identity and by $`Z_S\otimes I_R`$. Multiplicativity of trace norm on tensor products and the triangle inequality then bound the output norm by $`2e\sum_x\|M_{xx}\|_1\le2e\|M\|_1`$, for every reference dimension. A basis input attaining the largest branch error supplies the reverse inequality. Thus

```math
\frac12\|\widetilde{\mathcal N}-\mathcal T_s\|_{\diamond}
=\max_x D(\sigma_x,\phi_x).
```

Every branch-feasible device consequently has a diamond-feasible implementation at the same mean heat. Taking infima gives $`q_{\min}^{\diamond}\le q_{\min}`$, proving equality without assuming attainment. The [existing limiting match](heat_bound.md#matching-limit) then supplies the same crossover. The conversion changes the channel on coherent inputs; it is not a certification of the unmodified device from its two branch outputs.
