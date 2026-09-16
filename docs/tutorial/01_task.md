# 1. States, the task, and what the device receives

[Tutorial home](README.md) · [Next: the device](02_device.md)

## A state is more than one measurement average

A qubit state can be written using three real Bloch-vector components:

```math
\rho=\frac{I+r_xX+r_yY+r_zZ}{2},\qquad |\boldsymbol r|\le1.
```

The components are the mean outcomes of the Pauli measurements. A pure state has vector length one; a shorter vector describes a mixed state. The maximally mixed state has all three components zero.

For two qubit states with Bloch vectors r and t, their trace distance is half their Euclidean separation:

```math
D(\rho,\sigma)=\tfrac12\|\rho-\sigma\|_1
=\tfrac12|\boldsymbol r-\boldsymbol t|.
```

It bounds the difference in the probability of any measurement event. Requiring a small trace distance is therefore a whole-state requirement, not just a demand on one chosen observable. These are density-operator foundations associated with Chapter 8 of the textbook.

## Two alternatives, one physical device

The input is either the north-pole state |0> or the south-pole state |1>, each with probability one half. The device knows the two possibilities but receives no extra label telling its controller which arrived.

The desired output vectors are

```math
(-s,0,+c),\qquad(-s,0,-c),\qquad c=\sqrt{1-s^2}.
```

Both remain pure. Each gains the same negative transverse component. Their state-vector overlap has magnitude s, so they are not orthogonal when s is positive.

The device must satisfy both conditional tasks. Producing only their correct average is insufficient. For example, an operation that always outputs the average has the correct mean state but generally fails both branch tests.

## The average entropy is a different piece of information

The input average is I/2. The target average is (I-sX)/2, with eigenvalues (1+s)/2 and (1-s)/2. Its entropy decrease in bits is

```math
1-h_2\!\left(\frac{1+s}{2}\right).
```

This tends to zero quadratically as s tends to zero. It is a lower-bound ingredient, not the complete cost of performing both conditional transformations. An arbitrary channel must still do the correct thing on each allowed input.

## Draw the resource boundary before calculating cost

```text
unknown input S  ─────┐
                     │ one fixed joint interaction ──> output S
workspace A     ─────┤                             ──> restored marginal A
                     │
thermal bath B  ─────┘                             ──> spent bath B
```

All three begin independently. The bath begins at thermal equilibrium. Its final mean energy increase is the heat counted here. Additional thermal recovery systems belong inside the same boundary.

The workspace can start in any fixed state, but it must be returned or its consumed entropy capacity must be charged. External driving is allowed. Building the source and controller is outside this particular model. Those choices define the question; they do not describe every possible state-preparation apparatus.

## Checkpoint

**Why can an encoder that keeps the input label be a different task?**

A controlled map can keep |x> in one register and write the desired state into another initially pure register. The complete outputs remain orthogonal because the retained labels are orthogonal. This consumes or preserves resources absent from an uncharged consumed-register description. It does not contradict a heat bound that charges workspace restoration.

**Verify the target overlap.**

For pure qubits, the squared overlap is (1+r·t)/2. Here r·t = s²-c² = 2s²-1, giving squared overlap s² and overlap magnitude s.

Proceed to [an explicit device](02_device.md). The formal resource statement is available independently in the [model](../MODEL.md).
