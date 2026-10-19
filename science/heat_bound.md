# Heat accounting and the optimal limiting law

[Science](README.md#dependencies) · [Model](model.md) · [Theorem](theorem.md) · [Notation](notation.md) · [Thermal construction](thermal_implementation.md)

The environmental entropy bound becomes a heat bound only after the actual Gibbs reservoir and workspace are accounted for. The universal lower direction is then matched by the fully charged thermal construction.

Entropies are in bits unless a natural-log calculation is explicitly marked. All states and unitaries are finite dimensional.

<a id="heat-ledger"></a>
## Lemma 7: Gibbs and workspace accounting

**Input.** The environment entropy bound and the [physical model](model.md#apparatus), with $`\Omega=\tau_A\otimes\gamma_B`$.

**Output.** Every implementation obeys the finite theorem, including its retained nonnegative terms.

**Proof.** Apply Gibbs structure only to $`B`$. Its logarithm gives the exact identity

```math
q=\Delta H_B+D_2(\rho'_B\Vert\gamma_B),
```

where $`\Delta H_B=H(\rho'_B)-H(\gamma_B)`$. This is the reservoir form of the microscopic heat identity in [Reeb–Wolf, Theorem 3, Equations (21)–(22)](../references/LITERATURE.md#r1).

Initial independence of $`A,B`$ implies

```math
\Delta H_E=\Delta H_A+\Delta H_B-I(A:B)'.
```

Substitute this expression for $`\Delta H_B`$:

```math
q+\Delta H_A=\Delta H_E+I(A:B)'+D_2(\rho'_B\Vert\gamma_B).
```

Mutual information and relative entropy are nonnegative. Lemma 6 therefore proves both finite inequalities. Exact ensemble-marginal return sets $`\Delta H_A=0`$. Approximate return uses [Audenaert, Theorem 1, Equation (6)](../references/LITERATURE.md#r6), with the capped allowance in the [theorem](theorem.md#workspace-return).

The necessary information concerns $`E=AB`$. When a workspace is marginally returned but correlated, the record need not be in $`B`$ alone. Applying a Gibbs identity to a possibly nonthermal $`\tau_A`$, or ignoring a consumed positive $`\Delta H_A`$, would change the resource model.

<a id="matching-limit"></a>
## The limiting match

**Lower direction.** Let $`s\to0`$ along any sequence with $`\epsilon>0`$ and $`\epsilon/s^2\to r<\infty`$. The finite definitions give

```math
\frac d{s^2}\longrightarrow\frac14+r,
\qquad b_0\longrightarrow\frac1{\sqrt{1+4r}},
\qquad g(f(d))+h_2(\epsilon)\longrightarrow0.
```

The lower bound holds for every finite returned-workspace device and has no dimension-dependent correction. It therefore survives taking the infimum over devices and gives $`\liminf q_{\min}\ge F(r)`$.

**Upper direction.** In the [explicit collision](thermal_implementation.md#collision), the construction parameter $`u`$ equals the theorem's $`d`$. Its thermal bias obeys

```math
b=\frac{s}{2\sqrt{d(1-d)}}
\longrightarrow\frac1{\sqrt{1+4r}}.
```

For each positive-error pair in the stated domain, $`0<b<1`$. The [charged recovery calculation](thermal_implementation.md#recovery) gives

```math
J_2(b)\le q_M
\le J_2(b)+\frac{b\,\mathrm{atanh}(b)}{M\ln2}.
```

For any desired positive residual, a finite integer $`M`$ makes the last term smaller than it. Along the parameter sequence, choose the residual to tend to zero and choose such a finite $`M`$ at each stage. This gives $`\limsup q_{\min}\le F(r)`$.

At $`r=0`$, the bias tends to one. The gap and the necessary recovery resources may grow, but every finite stage still has positive error, $`b<1`$, and a full-rank finite Gibbs bath. The proof never substitutes an exact pure bath resource. The two limits coincide.

Recovery is needed to approach the optimal curve. The [finite strict/relaxed separation](finite_benchmark.md#comparison) already uses the bare collision heat and requires no recovery claim.
