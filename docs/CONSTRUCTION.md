# A complete two-qubit implementation

[Home](../README.md) · [Tutorial](tutorial/02_device.md) · [Theorem](THEOREM.md)

## Collision

Let c = sqrt(1-s²). For positive epsilon < c/2 set

```math
u=\frac{s^2}{2(1+c)}+\epsilon,\qquad
\theta=\arcsin\sqrt u,\qquad
b=\frac{s}{2\sqrt{u(1-u)}}.
```

The bath starts in gamma_b = diag((1+b)/2,(1-b)/2), with Hamiltonian

```math
H_B=\mathrm{diag}(0,\,2k_{\mathrm B}T\,\mathrm{atanh}(b)).
```

The domain guarantees 0 < b < 1, so the bath is full rank and the gap finite. Apply

```math
U=\mathrm{CNOT}_{S\to B}\exp(i\theta X_S\otimes Y_B).
```

The rightmost rotation occurs first. This is one fixed unitary, not a controller told which input was supplied. With C = cos(theta) and v = sin(theta), its basis action is

```math
\begin{aligned}
|0,0\rangle&\mapsto(C|0\rangle-v|1\rangle)|0\rangle,\\
|0,1\rangle&\mapsto(C|0\rangle+v|1\rangle)|1\rangle,\\
|1,0\rangle&\mapsto(-v|0\rangle+C|1\rangle)|1\rangle,\\
|1,1\rangle&\mapsto(v|0\rangle+C|1\rangle)|0\rangle.
\end{aligned}
```

Mixing over the thermal populations gives

```math
\sigma_x=\frac{I-sX+(-1)^x(c-2\epsilon)Z}{2},
\qquad B'_0=\gamma_b,\quad B'_1=X\gamma_bX.
```

Each branch output has trace error exactly epsilon and the common transverse polarization is unchanged. The final branch states are mixtures diagonal in the bath basis; no final system–bath entanglement is required on those branches. This is not a claim about all intermediate dynamics or a classical implementation of the complete task.

The average bath is I/2. Its mean energy increase is

```math
\beta Q_{\mathrm{bare}}=b\,\mathrm{atanh}(b).
```

The complete spent bath energy is charged. The bare operation is already a valid finite upper bound; it does not require the bath to be reused.

## Channel versus two-input error

Tracing the bath eliminates the input off-diagonal operator. This particular channel first dephases in the input basis and then prepares the corresponding sigma_x. Its half-diamond distance from the analogous target channel equals epsilon: reference inputs give positive conditional reference blocks whose traces sum to one, and a basis input attains the error.

The lower bound only requires the two branch tests. Two measured outputs alone do not certify the complete channel of an arbitrary unknown apparatus.

## Recover the available work

The maximally mixed spent bath is not in equilibrium with its nondegenerate Hamiltonian. Its excess energy includes a recoverable nonequilibrium contribution:

```math
b\,\mathrm{atanh}(b)
=J(b)+D(I/2\Vert\gamma_b),
\qquad J(b)=\ln2\,J_2(b),
```

```math
D(I/2\Vert\gamma_b)=-\tfrac12\ln(1-b^2).
```

Bring M fresh Gibbs qubits with biases b_j = jb/M, j = 1,...,M, and swap each sequentially with the working bath qubit. All are part of the complete initial thermal reservoir. Their different energy gaps are allowed engineered resources. The system is untouched during recovery.

After the last swap, the working qubit is restored to gamma_b and decorrelated. The first spent qubit carries its earlier state and correlations; these are not erased globally. Including every component's energy change gives

```math
\beta Q_M=\frac bM\sum_{j=1}^{M}\mathrm{atanh}(jb/M).
```

One way to verify the sum is to note that each spent qubit receives the preceding bias, while the working qubit returns to its initial bias. The bath energy changes telescope. Under the model's boundary conditions, the total switching work gives the same net energy balance. Successive-Gibbs-swap recovery is an established construction [R1](LITERATURE.md), not a new thermodynamic primitive.

As a right Riemann sum,

```math
J(b)\le\beta Q_M\le J(b)+\frac{b\,\mathrm{atanh}(b)}M.
```

Thus the infimum is approached without replacing finite bath states by pure resources. At fixed positive error, every chosen M is finite. Near the high-precision endpoint the bath gap and the recovery resources need not remain bounded.

## The complete ledger

For the bath-only construction,

```math
\beta Q=\Delta S_S+I(S:B)'+D(B'\Vert\gamma_B).
```

This microscopic identity is inherited [R1](LITERATURE.md); entropies in this display are in nats. Initially the system and complete reservoir are independent. Here Delta S_S = J(s), and the final system–complete-reservoir mutual information is J(b)-J(s). Adding independent thermal components and acting unitarily on the complete reservoir does not change that mutual information. Recovery removes its disequilibrium term, not its correlations with the output.

With internal workspace, replace this explanation by the full A+B ledger in the [proof](PROOF.md). The bath alone need not hold the label record.

## Numerical boundaries

The reference code rejects parameters whose finite bath bias has rounded to one in double precision. It does not silently replace a tiny positive Gibbs population by zero. Large recovery ladders use the exact sum, not an exponentially large density-matrix simulation. Small joint systems are checked directly.
