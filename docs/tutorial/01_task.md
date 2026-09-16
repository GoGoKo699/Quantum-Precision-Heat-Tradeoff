# 1. States, the task, and what the device receives

[Tutorial home](README.md) · [Next: the device](02_device.md) · [Formal model](../MODEL.md#task)

<a id="states"></a>
## A state is more than one measurement average

A density operator $`\rho`$ describes the probabilities of all measurements on a system. For one qubit it can be written using three real Bloch-vector components:

```math
\rho=\frac{I+r_xX+r_yY+r_zZ}{2},
\qquad |\boldsymbol r|\le1.
```

Here $`I`$ is the identity and $`X,Y,Z`$ are the Pauli matrices. The components are the mean outcomes of those three measurements. A pure state has vector length one; a shorter vector describes a mixed state. The maximally mixed state $`I/2`$ has all three components zero.

The trace distance is a whole-state error measure. With the convention used here,

```math
D(\rho,\sigma)
=\frac12\|\rho-\sigma\|_1.
```

The trace norm $`\|\cdot\|_1`$ is the sum of singular values. This $`D`$ with a comma denotes trace distance; later, $`D`$ with a double bar denotes relative entropy. For qubit states with Bloch vectors $`\boldsymbol r`$ and $`\boldsymbol t`$, this becomes

```math
D(\rho,\sigma)
=\frac12|\boldsymbol r-\boldsymbol t|.
```

It bounds the difference in the probability of any measurement event. A small trace distance therefore controls more than one chosen observable. Chapter 8 of the [textbook route](README.md#textbook) supplies the density-operator foundations.

<a id="conditional-task"></a>
## Two alternatives, one physical device

The input is either the north-pole state $`|0\rangle`$ or the south-pole state $`|1\rangle`$, each with probability one half. The device knows the two possibilities. It receives no extra label telling its controller which one arrived.

Choose an overlap parameter $`0<s<1`$ and define

```math
c=\sqrt{1-s^2}.
```

The two desired Bloch vectors are

```math
\boldsymbol r_0=(-s,0,c),
\qquad \boldsymbol r_1=(-s,0,-c).
```

Both have length one, so the targets remain pure. Each gains the same negative transverse component. Write the target density operator as $`\phi_x`$ and the actual output as $`\sigma_x`$. The device must satisfy both tests:

```math
D(\sigma_x,\phi_x)\le\epsilon
\quad\text{for }x=0,1.
```

The pure state vectors representing the targets have overlap magnitude $`s`$. The density operators $`\phi_x`$ and their representing state vectors are different mathematical objects; the [notation reference](../NOTATION.md) keeps this distinction explicit.

<a id="average-state"></a>
## Their average asks a different question

The input average is $`I/2`$. The target average is

```math
\bar\phi=\frac{\phi_0+\phi_1}{2}
=\frac{I-sX}{2}.
```

An operation that always outputs $`\bar\phi`$ would produce the correct average, but its error on **each** branch is $`c/2`$. For small $`s`$, that is close to one half. It fails an accuracy demand of order $`s^2`$ even though its average output is perfect.

The eigenvalues of $`\bar\phi`$ are $`(1+s)/2`$ and $`(1-s)/2`$. The entropy of a state is the Shannon entropy of its eigenvalues. For a binary probability distribution, define

```math
h_2(p)=-p\log_2p-(1-p)\log_2(1-p),
```

with $`0\log_2 0=0`$. The average system's entropy decrease in bits is

```math
J_2(s)=1-h_2\!\left(\frac{1+s}{2}\right).
```

It tends to zero quadratically as $`s\to0`$. This entropy decrease is a lower-bound ingredient. It does not alone specify the heat needed for one device to perform both conditional transformations.

<a id="resource-boundary"></a>
## Draw the resource boundary before calculating cost

The [canonical model](../MODEL.md#apparatus) contains three systems:

| System | Initially | Finally |
|---|---|---|
| Input/output qubit $`S`$ | Unknown input | Required output |
| Workspace $`A`$ | Fixed state | Returned marginal |
| Thermal reservoir $`B`$ | Gibbs state | Spent reservoir |

All three begin independently. One fixed joint unitary acts on them. The reservoir's final mean energy increase is the heat counted here. Any additional thermal recovery systems belong to the same reservoir boundary.

Workspace can start in any fixed state, but it must be returned or its consumed entropy capacity must be charged. Return means the **ensemble-average marginal** is restored; final correlations are allowed. It does not require the same auxiliary state on each input branch or guarantee independent reuse on arbitrarily correlated later inputs.

External driving is allowed. The system boundary Hamiltonian is zero, and interactions are off at the beginning and end. Building the source and controller is outside this model. The [heat and work convention](../MODEL.md#heat-work) states when the counted heat also equals net supplied work.

## Checkpoint

**Why can an encoder that keeps the input label be a different task?**

A controlled map can keep $`|x\rangle`$ in one register and write the desired state into another initially pure register. The complete outputs remain orthogonal because the retained labels are orthogonal. The extra register must be included in the resource accounting. Its restoration cannot be omitted when applying this theorem.

**Verify the target overlap.**

For pure qubits, the squared overlap is $`(1+\boldsymbol r_0\cdot\boldsymbol r_1)/2`$. Here

```math
\boldsymbol r_0\cdot\boldsymbol r_1
=s^2-c^2=2s^2-1.
```

The squared overlap is therefore $`s^2`$, giving overlap magnitude $`s`$.

Proceed to [an explicit thermal device](02_device.md). Specialists can go directly to the [theorem](../THEOREM.md#optimal-crossover).
