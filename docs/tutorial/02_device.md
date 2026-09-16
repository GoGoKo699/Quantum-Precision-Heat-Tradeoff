# 2. Calculate one complete thermal device

[Previous: the task](01_task.md) · [Tutorial home](README.md) · [Next: precision](03_precision.md)

This calculation uses density matrices, tensor products, and partial traces. It demonstrates an allowed device. Establishing that no other device can do better is a separate argument.

## Prepare a real thermal resource

A bath qubit with energy levels 0 and Delta has equilibrium excited-state probability

```math
p_1=\frac{e^{-\beta\Delta}}{1+e^{-\beta\Delta}},\qquad
\beta=\frac1{k_{\mathrm B}T}.
```

Write its population bias as b = p_0-p_1. Then

```math
\gamma_b=\begin{pmatrix}(1+b)/2&0\\0&(1-b)/2\end{pmatrix},
\qquad \beta\Delta=2\,\mathrm{atanh}(b).
```

For 0 < b < 1 the resource is thermal and full rank, not a free pure auxiliary. This connects the textbook's canonical ensemble to the device's actual input state.

## Choose the operation

For target s and positive design error epsilon, set

```math
u=\frac{s^2}{2(1+\sqrt{1-s^2})}+\epsilon,
\qquad \theta=\arcsin\sqrt u,
\qquad b=\frac{s}{2\sqrt{u(1-u)}}.
```

Use epsilon < sqrt(1-s²)/2. Apply a joint rotation and then a controlled flip:

```math
U=\mathrm{CNOT}_{S\to B}\exp(i\theta X_S\otimes Y_B).
```

The control is the physical system qubit. No external observer supplies the unknown label to the gate. The full basis action is written in the [construction](../CONSTRUCTION.md).

## Follow one branch

Let C = cos(theta) and v = sin(theta). For input |0>, the two possible bath basis components evolve as

```math
|0,0\rangle\mapsto(C|0\rangle-v|1\rangle)|0\rangle,
\qquad
|0,1\rangle\mapsto(C|0\rangle+v|1\rangle)|1\rangle.
```

Their probabilities are (1+b)/2 and (1-b)/2. Tracing out the bath leaves a system with transverse component -2bCv = -s and vertical component C²-v² = c-2epsilon.

For input |1>, the same unitary gives vertical component -(c-2epsilon) and again transverse component -s. Thus

```math
\sigma_x=\frac{I-sX+(-1)^x(c-2\epsilon)Z}{2}.
```

Each Bloch vector differs from its target only in a vertical component of magnitude 2epsilon. By the trace-distance formula, each error is exactly epsilon. The desired transverse polarization is preserved exactly.

## Measure energy, rather than infer it from entropy

The two conditional bath states have mirrored populations. Their equal-prior average is I/2. The bath's excited-state probability therefore rises from (1-b)/2 to 1/2. Its heat is

```math
Q=\Delta\left(\tfrac12-\tfrac{1-b}{2}\right),
\qquad \frac{Q}{k_{\mathrm B}T\ln2}
=\frac{b\,\mathrm{atanh}(b)}{\ln2}.
```

This is a complete energy calculation for the spent bath. It is not obtained by assuming that a desired entropy decrease is attainable as work.

At s = 0.05 and epsilon = 0.0025, it gives approximately 0.311485 bit-erasure units. The corresponding bath gap is approximately 0.964105 k_B T. Run `python scripts/reproduce.py` from the repository root to calculate the matrices and numbers.

## Why recovery can reduce the cost further

The final bath is maximally mixed, but its Hamiltonian has unequal energies. It is therefore out of equilibrium. Additional thermal interactions can recover some supplied work while leaving the system output unchanged.

Such recovery is optional for the finite separation. It is necessary to reach the limiting optimum. The [complete construction](../CONSTRUCTION.md) includes every fresh reservoir component, its energy change, and restoration of the working bath qubit. The recovery technique uses the microscopic thermal framework of [Reeb and Wolf](https://arxiv.org/abs/1306.4352).

## Checkpoint

**Why is the bare heat larger than the reservoir's entropy increase?**

In natural-log units the Gibbs identity is beta Q = Delta S_B + D(B' || gamma_b). The relative entropy is positive because I/2 is not the initial Gibbs state. Recovery can reduce that nonequilibrium term; it does not make the original energy calculation wrong.

**Does the calculation prove optimality?**

No. It establishes an upper bound by exhibiting a device. A lower bound must cover every allowed interaction and every finite reservoir, not just this circuit. That is the subject of the [next chapter](03_precision.md).
