# Physical model and resource boundary

[Home](../README.md) · [Main result](THEOREM.md#optimal-crossover) · [Notation](NOTATION.md) · [Proof](PROOF.md)

The task specifies two conditional outputs of one fixed apparatus. Heat is the mean energy gained by its complete initially thermal reservoir. The [theorem](THEOREM.md) uses exactly the model below.

<a id="task"></a>
## Task and accuracy

The input system $S$ is a qubit supplied in $|x\rangle$, where $x\in\{0,1\}$ has equal prior probabilities. The label is a mathematical bookkeeping variable; no separate copy is supplied to the controls. Use Pauli matrices $X,Y,Z$ and define $c=\sqrt{1-s^2}$ for $0<s<1$.

The target density operators are

```math
\phi_x(s)=\frac{I-sX+(-1)^x cZ}{2}.
```

Each target is pure: $\phi_x=|\phi_x\rangle\langle\phi_x|$. Their state-vector overlap obeys $|\langle\phi_0|\phi_1\rangle|=s$. Actual output states $\sigma_x$ must satisfy

```math
\max_{x\in\{0,1\}}D(\sigma_x,\phi_x)\le\epsilon,
```

with trace distance

```math
D(\rho,\sigma)=\frac12\|\rho-\sigma\|_1.
```

Equal priors determine the **mean heat**; accuracy is the **maximum branch error**. The principal finite statement assumes $0<\epsilon<c/2$. These two branch tests do not specify an arbitrary channel's action on coherent or reference-entangled inputs. The explicit device has an additional [channel-error property](CONSTRUCTION.md#channel-error).

<a id="apparatus"></a>
## Complete finite apparatus

Every implementation has a finite workspace $A$ and a finite complete reservoir $B$. Its initial state on branch $x$ is

```math
|x\rangle\langle x|_S\otimes\tau_A\otimes\gamma_B,
```

where

```math
\gamma_B=\frac{e^{-\beta H_B}}{Z_B},
\qquad \beta=\frac1{k_{\mathrm B}T}.
```

Here $T>0$ and all reservoir energy levels are finite, so $\gamma_B$ has full rank. The workspace state $\tau_A$ is fixed but otherwise arbitrary; it can be nonthermal or rank deficient. Input, workspace, and reservoir start independently.

One input-independent unitary acts on $SAB$. Predetermined external driving is allowed: the unitary need not commute with the uncoupled Hamiltonian. Any fresh thermal components used later for recovery are already included in $B$ and in its initial Gibbs product state. The protocol can be described as one joint unitary on this complete apparatus.

For the proof, write $E=AB$ and $\Omega=\tau_A\otimes\gamma_B$. The kinematic argument allows rank-deficient $\Omega$; Gibbs structure is invoked only for $B$ in the [heat ledger](PROOF.md#heat-ledger).

<a id="workspace-return"></a>
## What workspace return means

The finite entropy-corrected bound allows arbitrary final workspace states. For the cyclic-device optimum, the final **ensemble-average marginal** must return exactly:

```math
\rho'_A=\frac{\rho'_{A,0}+\rho'_{A,1}}2=\tau_A.
```

The two conditional marginals need not each equal $\tau_A$. Final correlations with the system or bath are allowed. This return condition preserves the workspace marginal on this input ensemble; it does not guarantee independent reuse on arbitrarily correlated future inputs. The [approximate-return bound](THEOREM.md#workspace-return) charges residual entropy capacity explicitly.

<a id="heat-work"></a>
## Heat, work, and entropy

Positive heat means that the complete reservoir gains mean energy:

```math
Q=\mathrm{Tr}\,H_B(\rho'_B-\gamma_B).
```

Report heat in bit-erasure units:

```math
q=\frac{Q}{k_{\mathrm B}T\ln2}
=\frac{\beta Q}{\ln2}.
```

The reservoir Hamiltonian is unchanged at the boundaries, and interactions are off there. The system boundary Hamiltonian is zero. With an unchanged auxiliary Hamiltonian, the first law gives

```math
W=Q+\Delta E_A.
```

Thus net mean supplied work equals $Q$ when auxiliary energy is restored. An auxiliary energy change must otherwise be included in $W$; a heat bound alone is not a general work bound.

Entropy symbols $H$, $h_2$, $D_2$, and mutual information use **bits**. Natural-log expressions are explicitly identified; see [notation](NOTATION.md#entropies). Define

```math
\Delta H_A=H(\rho'_A)-H(\tau_A).
```

A positive $\Delta H_A$ consumes workspace entropy capacity. It is not a heat measurement. The microscopic Gibbs identity is inherited from [Reeb–Wolf, Theorem 3](LITERATURE.md#r1); its use here is spelled out in the [proof](PROOF.md#heat-ledger).

<a id="resource-boundary"></a>
## What is supplied and charged

There is no input-dependent bath preparation or free label supplied to the controls. A clean register that stores the input label and is not restored consumes a resource. A nonequilibrium bath at fixed Hamiltonian is not a free Gibbs reservoir. Spent reservoir components remain in the energy accounting after the device stops accessing them.

A mathematical purification used in a distance estimate is not a physical auxiliary. Its entropy and energy never enter the ledger. The source-preparation apparatus and construction of the controller are outside this single-use accounting.

Two useful boundary examples explain the workspace term. An encoder that retains $x$ in a separate register and consumes a fresh pure output qubit has retained the input orthogonality outside the specified system. A pure workspace qubit can likewise store $x$ while $S$ reaches its exact target with zero bath heat; its entropy increases by one bit. The [entropy-corrected bound](THEOREM.md#finite-bound) charges that increase.

Small trace-distance return does not guarantee small entropy consumption when workspace dimension grows. The [return allowance](THEOREM.md#workspace-return) states the necessary dimension dependence.

<a id="limits"></a>
## Finite implementations and ideal limits

Each implementation is finite. The infimum may use a sequence with increasing bath size, energy gaps, operation duration, or control complexity. No uniform cap on these resources is imposed. Exact pure output at nonzero overlap is not assumed attainable with a finite full-rank bath in the bath-only setting: the [crossover limit](THEOREM.md#optimal-crossover) uses positive errors at every finite stage.

This is a single-use, conditional-input task. It is not a many-copy amortized work rate, a general price per quantum gate, or a wall-plug energy estimate. The [source comparison](LITERATURE.md) records which assumptions and results are inherited; the [claim map](CLAIMS.md) separates proofs from computed examples.
