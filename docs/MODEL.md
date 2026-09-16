# Physical model and resource boundary

[Home](../README.md) · [Theorem](THEOREM.md) · [Proof](PROOF.md)

## Task

Use Pauli matrices X, Y, Z and inverse temperature beta = 1/(k_B T). The input label x is either 0 or 1, with equal probability. It is a mathematical bookkeeping variable, not a separately accessible controller record. The input system S is a qubit in the corresponding computational-basis state.

```math
\phi_x(s)=\frac{I-sX+(-1)^x cZ}{2},
\qquad c=\sqrt{1-s^2},\quad 0<s<1.
```

The targets are pure and their state-vector overlap has magnitude s. Actual outputs satisfy

```math
\max_{x=0,1}\frac12\|\sigma_x-\phi_x(s)\|_1\le\epsilon.
```

Equal priors determine the mean heat. They do not replace the maximum branch error by an average error. The principal finite bound uses positive error with epsilon < c/2.

## Allowed apparatus

The initial state on each branch is

```math
|x\rangle\langle x|_S\otimes\tau_A\otimes\gamma_B,
\qquad \gamma_B=\frac{e^{-\beta H_B}}{Z_B}.
```

A is finite internal workspace in an arbitrary fixed state, possibly nonthermal or rank deficient. B is the complete finite reservoir, initially Gibbs at positive temperature with finite energy levels. Thus its Gibbs state has full rank. A and B start independently of each other and of the input.

One input-independent joint unitary acts on SAB. Predetermined external driving is allowed; the interaction is not required to commute with the uncoupled Hamiltonian. Any fresh thermal systems later used for recovery already belong to B in this complete description.

For the cyclic-device optimum, the final **ensemble-average marginal** on A must equal its initial state. Final correlations are allowed. This is weaker than returning a fully decorrelated register and does not guarantee independent reuse on arbitrarily correlated future inputs.

## Heat, work, and entropy

```math
Q=\mathrm{Tr}\,H_B(\rho'_B-\gamma_B),
\qquad q=\frac{Q}{k_{\mathrm B}T\ln2}.
```

The reservoir Hamiltonian is unchanged at the boundaries; interactions are off there. The system boundary Hamiltonian is zero. With an unchanged auxiliary Hamiltonian and restored auxiliary energy, net mean supplied work equals Q. Otherwise its boundary-energy change must also be charged: W = Q + Delta E_A.

Except where beta Q is explicitly used, entropy formulas in the theorem and proof are in **bits**. Define Delta H_A = H(A') - H(A); a positive value consumes auxiliary entropy capacity. It is not a heat measurement.

The microscopic Gibbs identity and the distinction between an entropy bound and a realizable operation are inherited foundations; see [R1–R3](LITERATURE.md).

## What is not supplied for free

There is no input-dependent bath preparation or separate label supplied to the controls. A clean register that stores the label and is not restored consumes a resource. A nonequilibrium bath at a fixed Hamiltonian is likewise not a free Gibbs reservoir. Spent reservoir systems cannot be discarded from the energy accounting merely because the device stops accessing them.

A mathematical purification used to estimate a distance is not a physical auxiliary. Its entropy and energy never enter the heat ledger.

## Idealization and limits

Each implementation is finite. The infimum may use a sequence with increasing bath size, gaps, operation duration, or control complexity. No uniform cap on these resources is claimed. Exact pure output at nonzero overlap is not assumed attainable with a finite full-rank bath in the bath-only setting; the crossover uses positive errors.

This is a single-use, conditional-input task. It is not a many-copy amortized work rate, a general price per quantum gate, an experimentally verified device, or a wall-plug energy estimate. The source-preparation apparatus and construction of the controller are outside the accounting.

## Two boundary examples

An encoder that keeps x in a separate register and consumes a fresh pure output qubit is not this task. Orthogonality can remain in its retained label. Similarly, a pure auxiliary can store the label while the system becomes its exact target with zero bath heat; its entropy then increases by one bit. The auxiliary-corrected theorem charges that increase.

Small trace-distance return of an auxiliary is insufficient if its dimension is allowed to grow without an entropy-capacity bound. The [return correction](THEOREM.md) states the required resource dependence explicitly.
