# 2. Calculate one complete thermal device

[Previous: the task](01_task.md) · [Tutorial home](README.md) · [Next: precision](03_precision.md)

This calculation uses density matrices, tensor products, and partial traces. A tensor product describes a joint system; a partial trace gives one subsystem's state when the other is ignored. The calculation exhibits one allowed device and hence an upper bound on the minimum heat. A universal lower bound requires a separate proof.

<a id="thermal-qubit"></a>
## Prepare a thermal resource

A bath qubit with energy levels $`0`$ and $`\Delta`$ has equilibrium excited-state probability

```math
p_1=\frac{e^{-\beta\Delta}}{1+e^{-\beta\Delta}},
```

where $`\beta=1/(k_{\mathrm B}T)`$ and $`p_0=1-p_1`$. Write the population bias as $`b=p_0-p_1`$. Then

```math
p_0=\frac{1+b}{2},
\qquad p_1=\frac{1-b}{2},
```

```math
\gamma_b=\begin{pmatrix}p_0&0\\0&p_1\end{pmatrix}.
```

The ratio $`p_0/p_1=e^{\beta\Delta}`$ determines the gap:

```math
\beta\Delta=\ln\frac{1+b}{1-b}
=2\,\mathrm{atanh}(b).
```

The function $`\mathrm{atanh}`$ is the inverse hyperbolic tangent. For $`0<b<1`$, both populations are positive and the gap is finite. Thus this input is a full-rank Gibbs state. Chapter 8's canonical-ensemble material connects directly to these probabilities.

<a id="operation"></a>
## Choose the operation

For target $`s`$, define $`c=\sqrt{1-s^2}`$ and choose $`0<\epsilon<c/2`$. Set

```math
u=\frac{s^2}{2(1+c)}+\epsilon,
```

```math
\theta=\arcsin\sqrt u,
```

```math
b=\frac{s}{2\sqrt{u(1-u)}}.
```

The first term in $`u`$ equals $`(1-c)/2`$; its displayed form is numerically stable when $`s`$ is small. The chosen range gives $`0<b<1`$, as checked in the [construction](../CONSTRUCTION.md#collision).

First apply a joint rotation $`R`$, then a controlled flip:

```math
R=e^{i\theta X_S\otimes Y_B},
```

```math
U=\mathrm{CNOT}_{S\to B}\,R.
```

The controlled flip exchanges the bath's basis states when the physical system qubit is in $`|1\rangle`$. No external observer supplies the unknown label. Since $`(X\otimes Y)^2=I`$, the rotation can be evaluated as

```math
R=\cos\theta\,I+i\sin\theta\,X\otimes Y.
```

This identity and the controlled flip give the [four basis transformations](../CONSTRUCTION.md#collision).

<a id="branch-states"></a>
## Follow the conditional states

Let $`C=\cos\theta`$ and $`v=\sin\theta`$. For input $`|0\rangle`$, the two bath basis components evolve as

```math
|0,0\rangle\mapsto(C|0\rangle-v|1\rangle)|0\rangle,
```

```math
|0,1\rangle\mapsto(C|0\rangle+v|1\rangle)|1\rangle.
```

Their probabilities are $`p_0`$ and $`p_1`$. Form each output projector, multiply by its probability, and trace out the bath. This leaves

```math
\sigma_0=\begin{pmatrix}
C^2&-bCv\\-bCv&v^2
\end{pmatrix}.
```

Its transverse and vertical Bloch components are

```math
-2bCv=-s,
```

```math
C^2-v^2=1-2u=c-2\epsilon.
```

For input $`|1\rangle`$, the same unitary gives vertical component $`-(c-2\epsilon)`$ and again transverse component $`-s`$. Define $`z_x=(-1)^x(c-2\epsilon)`$. Both outputs are then

```math
\sigma_x=\frac{I-sX+z_xZ}{2}.
```

Each Bloch vector differs from its target only in a vertical component of magnitude $`2\epsilon`$. By the trace-distance formula, each error is exactly $`\epsilon`$. The desired transverse polarization is preserved exactly.

<a id="energy"></a>
## Calculate the bath energy

For input $`|0\rangle`$, the bath retains its populations. For input $`|1\rangle`$, the populations are exchanged. Their equal-prior average is therefore $`I/2`$. The average excited-state probability rises from $`(1-b)/2`$ to $`1/2`$.

With the same gap at the initial and final boundaries, heat is gap times the population change:

```math
Q=\Delta\left(\frac12-\frac{1-b}{2}\right)
=\frac{b\Delta}{2}.
```

In units of $`k_{\mathrm B}T\ln2`$, this becomes

```math
q=\frac{Q}{k_{\mathrm B}T\ln2},
```

```math
q=\frac{b\,\mathrm{atanh}(b)}{\ln2}.
```

This calculation charges the spent bath's complete energy increase. No assumption that an entropy decrease is attainable as work was used.

At $`s=0.05`$ and $`\epsilon=0.0025`$, it gives approximately $`0.311485`$ heat units. The bath gap is approximately $`0.964105\,k_{\mathrm B}T`$. The [finite benchmark](../FINITE_BENCHMARK.md#comparison) retains more digits and compares this construction with a stricter task's lower bound. Run `python scripts/reproduce.py` from the repository root to calculate the matrices and values.

<a id="recovery"></a>
## Why recovery can reduce the cost further

The final bath is maximally mixed, but its Hamiltonian has unequal energies. It is out of equilibrium. Further interactions with thermal qubits can recover some supplied work while leaving the system output unchanged.

Recovery is optional for the finite separation. It is necessary to reach the limiting optimum. The [complete recovery calculation](../CONSTRUCTION.md#recovery) includes every fresh reservoir component, every energy change, and restoration of the working bath qubit. The underlying successive-Gibbs-swap technique is from [Reeb–Wolf, Proposition 8](../LITERATURE.md#r1).

## Checkpoint

**Why does the bare heat exceed the reservoir entropy increase?**

In natural-log units, the Gibbs identity is

```math
\beta Q=\Delta S_B+D(B'\Vert\gamma_b).
```

Here $`\Delta S_B`$ is the bath entropy increase. Relative entropy $`D`$ measures departure from the reference Gibbs state and is nonnegative. It is positive here because $`B'=I/2`$ differs from $`\gamma_b`$. Recovery reduces this nonequilibrium term. See the [full heat ledger](../CONSTRUCTION.md#heat-ledger) for the role of final correlations.

**Does this device prove optimality?**

No. It establishes an upper bound. A lower bound must cover every allowed interaction and every finite reservoir, including nonthermal workspace with the specified return accounting. The [next chapter](03_precision.md) explains what that additional argument must accomplish.
