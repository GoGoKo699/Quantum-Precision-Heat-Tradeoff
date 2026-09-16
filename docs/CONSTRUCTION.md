# A complete two-qubit implementation

[Home](../README.md) · [Tutorial calculation](tutorial/02_device.md) · [Theorem](THEOREM.md#optimal-crossover) · [Notation](NOTATION.md)

One system qubit and one thermal qubit give a finite upper bound. Optional recovery with more thermal qubits approaches the limiting optimum. Every reservoir component, including the spent ones, remains inside the energy accounting in the [physical model](MODEL.md#apparatus).

[Collision](#collision) · [Channel error](#channel-error) · [Recovery](#recovery) · [Heat ledger](#heat-ledger)

## Collision

Fix $`0<s<1`$, write $`c=\sqrt{1-s^2}`$, and choose a positive error $`\epsilon<c/2`$. Define

```math
u=\frac{s^2}{2(1+c)}+\epsilon,
```

```math
\theta=\arcsin\sqrt u,
\qquad b=\frac{s}{2\sqrt{u(1-u)}}.
```

The bath populations are $`p_0=(1+b)/2`$ and $`p_1=(1-b)/2`$. Its state and boundary Hamiltonian are

```math
\gamma_b=\begin{pmatrix}p_0&0\\0&p_1\end{pmatrix},
\qquad H_B=\begin{pmatrix}0&0\\0&\Delta\end{pmatrix},
```

```math
\beta\Delta=2\,\mathrm{atanh}(b).
```

Here $`\beta=1/(k_{\mathrm B}T)`$ and $`\mathrm{atanh}`$ is the inverse hyperbolic tangent. The domain gives $`(1-c)/2<u<1/2`$, hence $`0<b<1`$: both Gibbs populations are positive and the gap is finite.

Apply

```math
U=\mathrm{CNOT}_{S\to B}\,R,
\qquad R=e^{i\theta X_S\otimes Y_B}.
```

The rotation $`R`$ occurs first. This is one fixed unitary; no controller receives the unknown input label. Set $`C=\cos\theta`$ and $`v=\sin\theta`$. In system–bath order its basis action is

```math
\begin{aligned}
|0,0\rangle&\mapsto(C|0\rangle-v|1\rangle)|0\rangle,\\
|0,1\rangle&\mapsto(C|0\rangle+v|1\rangle)|1\rangle,\\
|1,0\rangle&\mapsto(-v|0\rangle+C|1\rangle)|1\rangle,\\
|1,1\rangle&\mapsto(v|0\rangle+C|1\rangle)|0\rangle.
\end{aligned}
```

Mixing with weights $`p_0,p_1`$ gives the system outputs. Write $`z_x=(-1)^x(c-2\epsilon)`$; then

```math
\sigma_x=\frac{I-sX+z_xZ}{2},
```

and conditional bath states

```math
B'_0=\gamma_b,
\qquad B'_1=X\gamma_bX.
```

Each system output has trace error exactly $`\epsilon`$, and the common transverse polarization remains $`-s`$. The final branch states are mixtures of product states with orthogonal bath basis states. They require no final system–bath entanglement. This observation concerns the two specified branches; it does not describe every intermediate state or establish a classical implementation of the complete task.

The equal-prior average bath is $`I/2`$. Its excited population rises by $`b/2`$, so its complete mean energy increase is

```math
Q_{\mathrm{bare}}=\frac{b\Delta}{2},
```

```math
\beta Q_{\mathrm{bare}}
=b\,\mathrm{atanh}(b).
```

The bare operation is a valid finite upper bound. The bath can be spent after this one use; no reuse assumption enters this calculation.

<a id="channel-error"></a>
## Channel versus two-input error

For either initial bath basis state, the basis action sends the two system inputs to orthogonal bath basis states. Tracing the bath therefore eliminates the input off-diagonal operator. This channel first dephases in the input basis and then prepares the corresponding $`\sigma_x`$.

Its half-diamond distance from the analogous target channel equals $`\epsilon`$. To see the upper bound, include a reference system and denote its unnormalized positive conditional blocks by $`R_x`$. The difference of the two channel outputs is

```math
\sum_{x=0}^1(\sigma_x-\phi_x)\otimes R_x,
```

```math
\sum_{x=0}^1\mathrm{Tr}\,R_x=1.
```

The trace-norm triangle inequality bounds half its norm by $`\epsilon`$. A basis input attains that value. This additional channel statement concerns this specified construction. The [universal lower bound](THEOREM.md#finite-bound) requires only the two branch tests; two observed outputs do not certify the full channel of an arbitrary unknown apparatus.

<a id="recovery"></a>
## Recover the available work

The spent bath $`I/2`$ is not at equilibrium with its nondegenerate Hamiltonian. Its excess energy includes a recoverable nonequilibrium contribution:

```math
b\,\mathrm{atanh}(b)=J(b)+D(I/2\Vert\gamma_b),
```

```math
J(b)=\ln2\,J_2(b),
```

```math
D(I/2\Vert\gamma_b)=-\frac12\ln(1-b^2).
```

Here $`J_2`$ is the [binary entropy deficit](THEOREM.md#optimal-crossover), and $`D`$ uses natural logarithms. Recovery exchanges states with a ladder of Gibbs qubits. It uses the successive-swap construction of [Reeb–Wolf, Proposition 8 and its proof](LITERATURE.md#r1).

Choose a finite positive integer $`M`$. Bring $`M`$ independent fresh Gibbs qubits, indexed by $`j=1,\ldots,M`$, with

```math
b_j=\frac{jb}{M},
\qquad \beta\Delta_j=2\,\mathrm{atanh}(b_j).
```

All these qubits are part of the complete initial thermal reservoir. Their engineered, unequal energy gaps are permitted resources. Swap each one sequentially with the working bath qubit, leaving the system untouched. Write $`b_0=0`$ for the working qubit's bias just after the collision; this local recovery index is unrelated to the finite theorem's lower-bound bias.

At step $`j`$, the working qubit receives bias $`b_j`$, and fresh qubit $`j`$ receives bias $`b_{j-1}`$. After the last step the working qubit has its initial state $`\gamma_b`$ and is decorrelated. The first spent qubit carries its earlier state and its correlations with the system; those correlations have moved, not disappeared.

The working qubit's energy change over collision plus recovery is zero. The final energy change of reservoir qubit $`j`$ is

```math
\Delta E_j=\frac{\Delta_j}{2}(b_j-b_{j-1}).
```

Summing over **every** reservoir qubit gives

```math
\beta Q_M=\frac bM
\sum_{j=1}^{M}\mathrm{atanh}(jb/M).
```

This includes the collision heat and the negative energy change of the working qubit during recovery. The swaps need not conserve the uncoupled energy; the model allows external driving. With the stipulated boundary Hamiltonians, the net supplied work has this same total energy balance.

The sum is a right Riemann sum for the increasing function $`\mathrm{atanh}`$:

```math
J(b)=\int_0^b\mathrm{atanh}(t)\,dt,
```

```math
0\le\beta Q_M-J(b)
\le\frac{b\,\mathrm{atanh}(b)}M.
```

Thus the recovered infimum is approached with full-rank finite Gibbs states at every stage. At fixed positive error, each chosen $`M`$ is finite. Along the high-precision limit, bath gaps and recovery resources need not remain bounded. The [matching-limit proof](PROOF.md#matching-limit) states how this construction meets the universal lower bound.

<a id="heat-ledger"></a>
## The complete ledger

For the bath-only construction, the microscopic identity of [Reeb–Wolf, Theorem 3, Eqs. (21)–(22)](LITERATURE.md#r1) reads

```math
\beta Q=\Delta S_S+I(S:B)'+D(B'\Vert\gamma_B).
```

Entropies in this identity use natural logarithms. Here $`\Delta S_S`$ means the system entropy **decrease**, initial minus final. The [notation reference](NOTATION.md) distinguishes this from the auxiliary entropy increase used in the theorem. Initially the system and complete reservoir are independent.

The averaged system output is $`(I-sX)/2`$, so

```math
\Delta S_S=J(s).
```

The post-collision average bath is maximally mixed. Unitary invariance of the joint entropy therefore gives

```math
I(S:B)'=J(b)-J(s).
```

Adding independent thermal components and applying unitaries on the complete reservoir preserves its mutual information with the system. Recovery reduces the disequilibrium term toward zero; the correlation term remains. In the presence of internal workspace, use the full $`A+B`$ [heat ledger](PROOF.md#heat-ledger): the bath alone need not hold the input record.

## Numerical boundaries

The reference implementation, [`collision`](../qph/core.py), rejects parameters whose finite bath bias has rounded to one in double precision. It never silently replaces a positive Gibbs population by zero. [`recovery_heat`](../qph/core.py) evaluates the finite sum without constructing an exponentially large density matrix. Small joint systems are checked directly in the [tests](../tests/test_core.py).
