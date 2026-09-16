# Precision–heat theorem

[Home](../README.md) · [Model](MODEL.md) · [Proof](PROOF.md) · [Construction](CONSTRUCTION.md)

All statements use the resource and error conventions in the model. Entropies below are in bits; heat is q = Q/(k_B T ln 2).

## Finite lower bound

For 0 < s < 1 and 0 < epsilon < c/2, define

```math
c=\sqrt{1-s^2},\qquad
d=\frac{s^2}{2(1+c)}+\epsilon,\qquad
b_0=\frac{[s-2\epsilon-2d]_+}{2\sqrt d}.
```

Here [v]_+ = max(0,v). The stable expression for d avoids subtracting two nearly equal numbers when s is small. Define

```math
J_2(b)=1-h_2\!\left(\frac{1+b}{2}\right),
\qquad f(d)=\sqrt{d(1-3d/4)}+d/2,
```

```math
g(\eta)=\min\!\left\{1,\ \eta+(1+\eta)h_2\!\left(\frac{\eta}{1+\eta}\right)\right\},
```

```math
L(s,\epsilon)=\max\{0,\ J_2(b_0)-g(f(d))-h_2(\epsilon)\}.
```

Every allowed implementation obeys

```math
q+\Delta H_A\ge L(s,\epsilon).
```

A stronger ledger retains nonnegative final terms:

```math
q+\Delta H_A\ge L(s,\epsilon)+I(A:B)'+D_2(\rho'_B\Vert\gamma_B).
```

In particular, exact marginal return of A gives q >= L. The constants are independent of the dimensions of A and B. This is a finite bound, not a claim of finite optimality.

## Optimal crossover

Let q_min be the infimum over allowed finite implementations with exact ensemble-marginal return of the auxiliary. Then

```math
\lim_{s\to0,\;\epsilon/s^2\to r}q_{\min}(s,\epsilon)
=F(r)=1-h_2\!\left(\frac{1+(1+4r)^{-1/2}}{2}\right),
\qquad 0\le r<\infty.
```

Errors are positive along the sequence, including the r = 0 endpoint. The lower bound is uniform in environment dimension. The matching construction uses no auxiliary, so it also establishes the upper bound in the larger cyclic-device class.

This is not an exact finite-s optimum. The large-r expansion of F is not automatically a uniform theorem over every path with epsilon/s² tending to infinity.

## Approximate workspace return

For an n-dimensional auxiliary with return trace distance at most delta, define, for n >= 2,

```math
t=\min\{\delta,1-1/n\},\qquad
a_n(\delta)=h_2(t)+t\log_2(n-1).
```

Set a_1 = 0. The sharp entropy-continuity inequality [R6](LITERATURE.md) gives

```math
q\ge L(s,\epsilon)-a_n(\delta).
```

This lower bound may be negative when entropy capacity is consumed; it should not be clipped to zero without another argument. The limiting curve is unchanged if the actual auxiliary entropy increase vanishes. For fixed n, delta tending to zero is sufficient.

## Finite values

At s = 0.05 and strict error 0.0001, L is approximately 0.498044180. At the same s and relaxed error 0.0025, the one-bath-qubit construction costs approximately 0.311484646. A 16-level strict-device auxiliary returned within 0.0001 reduces the strict bound to approximately 0.496180457.

See [the finite benchmark](FINITE_BENCHMARK.md) for the comparison and [the claim map](CLAIMS.md) for code and proof locations.
