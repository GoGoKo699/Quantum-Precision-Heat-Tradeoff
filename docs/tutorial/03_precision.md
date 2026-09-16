# 3. Why precision changes the physical bound

[Previous: the device](02_device.md) · [Tutorial home](README.md) · [Full proof](../PROOF.md)

## Two different small quantities

The common polarization has magnitude s. The target's vertical component differs from a pole by

```math
1-\sqrt{1-s^2}=\frac{s^2}{2}+O(s^4).
```

One quantity is first order and the other second order. An error small relative to s can still be large enough to affect the near-purity constraint at order s².

This explains why a second-order accuracy scale is worth inspecting. It does not, by itself, prove a heat law.

## The exact illustration

Consider first a pure-environment illustration. Unitary evolution preserves the inner product of two complete input states. If orthogonal inputs become nonorthogonal pure system outputs, the environment must compensate:

```math
0=\langle\phi_0|\phi_1\rangle\langle e_0|e_1\rangle.
```

For nonzero system overlap, the environment records must be orthogonal. A thermal mixed environment requires a more careful argument; the exact-operation restriction has direct prior work [R2](../LITERATURE.md).

Finite error matters because slightly mixed outputs no longer permit this pure-product argument. The correct question is quantitative: how distinguishable must the actual environmental records remain?

## The proof's three tasks

First, arbitrary-unitary kinematics relate the required output coherence and permitted wrong-basis population to a difference between environmental comparison states.

Second, an information inequality converts that difference into a lower bound on the record. The comparison states are not simply assumed to be the physical bath outputs. A continuity bound transfers the statement to the actual environment without introducing a penalty proportional to its dimension.

Third, Gibbs accounting converts the required environment entropy increase into bath heat, while charging any entropy capacity consumed in internal workspace.

These are the additional steps beyond the undergraduate device calculation. Their exact statements and primary attributions appear in the [proof](../PROOF.md).

## The crossover and its meaning

Write r = epsilon/s². The optimal limiting heat in bit-erasure units is

```math
F(r)=1-h_2\!\left(\frac{1+(1+4r)^{-1/2}}2\right).
```

For r tending to zero it approaches one. At r = 1 it is approximately 0.149510. For any fixed positive r, epsilon/s = rs tends to zero: the full-state error is already much smaller than the leading polarization, yet the heat depends on r.

The explicit device keeps that polarization exactly. Lower heat does not come from failing to produce the leading signal. It comes from relaxing the more demanding full-state specification.

## Where the cost goes

The complete microscopic heat identity separates average system-entropy decrease, output–reservoir correlations, and final reservoir disequilibrium [R1](../LITERATURE.md). In the bath-only achieving construction, the first becomes small and recovery removes the avoidable disequilibrium. The correlation contribution remains.

With internal workspace, the information can reside in the complete environment A+B rather than in the bath alone. Restoring only a workspace marginal is different from removing every correlation. The [model](../MODEL.md) and [theorem](../THEOREM.md) keep that distinction explicit.

## Checkpoint

**Why does doing nothing fail the stated high-accuracy test?**

Leaving an input pole unchanged misses a transverse component of magnitude s. Its trace distance from the target is approximately s/2, much larger than an allowed error of order s². A fidelity-based score can scale differently; changing the metric changes the task.

**What has this theorem not supplied?**

It has not supplied an exact finite-parameter optimum, an autonomous device, an experimental realization, or a universal cost per quantum gate. It supplies an optimal limiting statement for a specified single-use physical task, together with finite consequences.

Continue directly to the [theorem](../THEOREM.md), [proof](../PROOF.md), or [finite benchmark](../FINITE_BENCHMARK.md). No earlier research notes are needed.
