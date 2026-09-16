# 3. Why precision changes the physical bound

[Previous: the device](02_device.md) · [Tutorial home](README.md) · [Full proof](../PROOF.md)

<a id="two-scales"></a>
## Two different small quantities

The target's common transverse polarization has magnitude $`s`$. Its vertical component differs from a pole by

```math
1-\sqrt{1-s^2}=\frac{s^2}{2}+O(s^4).
```

The notation $`O(s^4)`$ means a remainder bounded in magnitude by a constant times $`s^4`$ for sufficiently small $`s`$. The polarization is first order in $`s`$, while the change needed to keep the vector on the pure-state sphere is second order. An error small compared with $`s`$ can still affect that near-purity constraint.

The device calculation makes the two scales concrete. The target has transverse component $`-s`$ and vertical components $`\pm c`$. The device retains $`-s`$ exactly but replaces the vertical components by $`\pm(c-2\epsilon)`$. Accuracy at scale $`\epsilon\sim s^2`$ therefore resolves a different feature from accuracy at scale $`s`$.

This identifies the scale to inspect. It does not by itself prove a heat law.

<a id="exact-illustration"></a>
## What exact pure outputs would require

Consider a pure-environment illustration. Orthogonal complete input states remain orthogonal under a unitary. If each final system state is pure, each complete output is a product of that system state and an environment state. Inner-product preservation gives

```math
0=\langle\phi_0|\phi_1\rangle
\langle e_0|e_1\rangle.
```

Here $`|\phi_x\rangle`$ represents the pure target; the density operator is $`\phi_x=|\phi_x\rangle\langle\phi_x|`$. If the system overlap is nonzero, the environment vectors must be orthogonal. They hold a perfectly distinguishable input record.

A mixed thermal environment requires more work. Exact-operation restrictions have direct precedent in [Aksak–Turgut, Theorem 4(b)](../LITERATURE.md#r2). Finite error also changes the argument: slightly mixed system outputs no longer force those complete product states. The quantitative question is how much distinguishability must remain in the actual environment.

<a id="converse-boundary"></a>
## What the universal lower bound must establish

A calculation for one circuit cannot answer that question for every allowed apparatus. The [proof](../PROOF.md) supplies three additional arguments:

1. **All allowed interactions.** [Output tests](../PROOF.md#output-tests) and the [arbitrary-unitary reduction](../PROOF.md#unitary-reduction) relate the required coherence and wrong-basis population to a difference between environmental comparison states.
2. **Comparison states to real records.** The [information inequality](../PROOF.md#information-bound) bounds the information in those comparison states. The [environment transfer](../PROOF.md#environment-transfer) then passes to actual environmental outputs. Its continuity correction depends on the binary label dimension, not the reservoir dimension.
3. **Records to heat.** The [environment entropy step](../PROOF.md#environment-entropy) and [Gibbs ledger](../PROOF.md#heat-ledger) convert that record into a heat bound, charging any entropy capacity consumed in workspace. Gibbs structure is applied to the thermal bath; the workspace need not itself be thermal.

These are the extra tools beyond the undergraduate two-qubit calculation. They are stated with their source roles and assumptions in the proof.

<a id="crossover"></a>
## The crossover and its limiting procedure

Let $`r`$ describe the ratio $`\epsilon/s^2`$ along a limiting sequence. For finite $`r\ge0`$, define

```math
b_*(r)=\frac{1}{\sqrt{1+4r}},
\qquad F(r)=1-h_2\!\left(\frac{1+b_*(r)}2\right).
```

The [canonical theorem](../THEOREM.md#optimal-crossover) states that the infimum heat $`q_{\min}(s,\epsilon)`$ approaches $`F(r)`$ when

```math
s\to0,
\qquad \epsilon/s^2\to r.
```

The error stays positive at every finite stage, including paths with $`r=0`$. The infimum is over allowed finite devices with exact ensemble-marginal workspace return. Resource sizes and gaps may grow along the sequence.

As $`r\to0`$, $`F(r)`$ approaches one bit-erasure unit. At $`r=1`$ it is approximately $`0.149510`$. For any fixed positive $`r`$, choosing $`\epsilon=rs^2`$ gives

```math
\frac{\epsilon}{s}=rs\to0.
```

The full-state error is already much smaller than the leading polarization, yet the limiting heat depends on $`r`$. In the explicit device, the leading polarization is exact at every stage. Lower heat comes from relaxing the more demanding full-state specification.

The converse gives a lower bound for every allowed finite device. The [collision plus recovery](../CONSTRUCTION.md#recovery) supplies the matching upper bound along the limit. This pairing establishes the limiting optimum; it does not identify the exact optimum at fixed $`s`$ and $`\epsilon`$.

<a id="cost-location"></a>
## Where the cost goes

The [microscopic heat identity](../CONSTRUCTION.md#heat-ledger) separates average system-entropy decrease, output–reservoir correlations, and final reservoir disequilibrium. In the bath-only construction, the average entropy decrease becomes small and recovery reduces the avoidable disequilibrium toward zero. The correlation contribution remains.

With workspace, information can reside in the complete environment $`A+B`$. Restoring the workspace marginal permits final correlations. The [model](../MODEL.md#workspace-return) and [return theorem](../THEOREM.md#workspace-return) specify what is restored and what entropy capacity must be charged.

## Checkpoint

**Why does doing nothing fail the high-accuracy test?**

Leaving an input pole unchanged misses a transverse component of magnitude $`s`$. Its trace distance from the target is

```math
\sqrt{\frac{1-c}{2}}
=\frac{s}{2}+O(s^3).
```

That is much larger than an allowed error of order $`s^2`$. A fidelity-based score can scale differently; changing the metric changes the task.

**What has the theorem supplied?**

It supplies an optimal limiting statement for this single-use physical task, together with finite lower bounds and explicit devices. It does not supply an exact finite-parameter optimum, an autonomous implementation, an experimental realization, or a universal cost per quantum gate.

Continue directly to the [theorem](../THEOREM.md#optimal-crossover), [proof](../PROOF.md), or [finite benchmark](../FINITE_BENCHMARK.md#comparison).
