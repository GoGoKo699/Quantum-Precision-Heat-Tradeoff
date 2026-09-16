"""Finite precision–heat formulas and explicit matrix implementations.

Entropy and public heat values are in bits / bit-erasure units. Hamiltonians
returned by collision are divided by k_B T. This module implements the stated
formulas; a numerical evaluation is not an optimality proof.
"""
from __future__ import annotations

import math
from numbers import Integral
import numpy as np
from scipy.linalg import expm

LN2 = math.log(2.0)
I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.diag([1.0, -1.0]).astype(complex)
CNOT = np.array([[1, 0, 0, 0], [0, 1, 0, 0],
                 [0, 0, 0, 1], [0, 0, 1, 0]], dtype=complex)


def h2(p: float) -> float:
    """Binary entropy in bits, including both endpoints."""
    p = float(p)
    if not math.isfinite(p) or not 0 <= p <= 1:
        raise ValueError("Probability must be finite and in [0, 1].")
    if p in (0.0, 1.0):
        return 0.0
    return -(p * math.log(p) + (1 - p) * math.log1p(-p)) / LN2


def j2(b: float) -> float:
    """1-h2((1+b)/2), evaluated without small-b cancellation."""
    b = float(b)
    if not math.isfinite(b) or not 0 <= b <= 1:
        raise ValueError("Bias must be finite and in [0, 1].")
    if b == 1.0:
        return 1.0
    return ((1+b)*math.log1p(b) + (1-b)*math.log1p(-b)) / (2*LN2)


def _parameters(s: float, epsilon: float) -> tuple[float, float]:
    s, epsilon = float(s), float(epsilon)
    if not math.isfinite(s) or not 0 < s < 1:
        raise ValueError("Require 0 < s < 1.")
    c = math.sqrt((1-s)*(1+s))
    if not math.isfinite(epsilon) or not 0 < epsilon < c/2:
        raise ValueError("Require positive epsilon < sqrt(1-s^2)/2.")
    return c, s*s/(2*(1+c)) + epsilon


def crossover(r: float) -> float:
    r = float(r)
    if not math.isfinite(r) or r < 0:
        raise ValueError("Use a finite, nonnegative crossover ratio.")
    return j2(1/math.sqrt(1+4*r))


def disturbance(d: float) -> float:
    d = float(d)
    if not math.isfinite(d) or not 0 <= d <= 1:
        raise ValueError("Disturbance probability must lie in [0, 1].")
    return math.sqrt(d*(1-0.75*d)) + d/2


def continuity(eta: float) -> float:
    eta = float(eta)
    if not math.isfinite(eta) or not 0 <= eta <= 1:
        raise ValueError("Trace distance must lie in [0, 1].")
    return min(1.0, eta + (1+eta)*h2(eta/(1+eta)))


def lower_bound(s: float, epsilon: float) -> float:
    """Universal finite lower bound for exactly returned workspace."""
    _, d = _parameters(s, epsilon)
    b0 = max(0.0, s-2*epsilon-2*d)/(2*math.sqrt(d))
    return max(0.0, j2(min(1.0, b0))-continuity(disturbance(d))-h2(epsilon))


def auxiliary_allowance(n: int, delta: float) -> float:
    if not isinstance(n, Integral) or isinstance(n, bool) or n < 1:
        raise ValueError("Auxiliary dimension must be a positive integer.")
    delta = float(delta)
    if not math.isfinite(delta) or not 0 <= delta <= 1:
        raise ValueError("Return tolerance must lie in [0, 1].")
    if n == 1:
        return 0.0
    t = min(delta, 1-1/n)
    return h2(t) + t*math.log2(n-1)


def target(s: float, x: int) -> np.ndarray:
    if not 0 < s < 1 or x not in (0, 1):
        raise ValueError("Require 0 < s < 1 and binary x.")
    return (I2-s*X+(-1)**x*math.sqrt((1-s)*(1+s))*Z)/2


def collision(s: float, epsilon: float):
    """Return U, Gibbs state, H/(k_B T), and finite thermal bias."""
    _, u = _parameters(s, epsilon)
    b = s/(2*math.sqrt(u*(1-u)))
    if not 0 < b < 1:
        raise FloatingPointError("Thermal bias rounded to an endpoint; use higher precision.")
    theta = math.asin(math.sqrt(u))
    gamma = (I2+b*Z)/2
    hamiltonian = np.diag([0.0, 2*math.atanh(b)])
    unitary = CNOT @ expm(1j*theta*np.kron(X, Y))
    return unitary, gamma, hamiltonian, b


def partial_trace(state: np.ndarray, dims, keep) -> np.ndarray:
    dims, keep = list(dims), list(keep)
    if (not dims or any(not isinstance(d, Integral) or d < 1 for d in dims)
            or len(set(keep)) != len(keep) or any(k < 0 or k >= len(dims) for k in keep)):
        raise ValueError("Invalid tensor dimensions or subsystem selection.")
    state = np.asarray(state, dtype=complex)
    size = math.prod(dims)
    if state.shape != (size, size):
        raise ValueError("Matrix shape does not match tensor dimensions.")
    tensor = state.reshape(dims+dims)
    for k in reversed(range(len(dims))):
        if k not in keep:
            tensor = np.trace(tensor, axis1=k, axis2=k+len(dims))
            dims.pop(k)
    size = math.prod(dims)
    return tensor.reshape(size, size)


def entropy(state: np.ndarray) -> float:
    state = np.asarray(state, dtype=complex)
    p = np.linalg.eigvalsh((state+state.conj().T)/2)
    if p.min() < -1e-9 or abs(p.sum()-1) > 1e-8:
        raise ValueError("Expected a normalized positive density matrix.")
    p = p[p > 1e-15]
    return float(-np.sum(p*np.log2(p)))


def trace_distance(a: np.ndarray, b: np.ndarray) -> float:
    difference = np.asarray(a)-np.asarray(b)
    return float(np.abs(np.linalg.eigvalsh((difference+difference.conj().T)/2)).sum()/2)


def holevo(a: np.ndarray, b: np.ndarray) -> float:
    return entropy((a+b)/2)-(entropy(a)+entropy(b))/2


def spectral_information(a: np.ndarray, b: np.ndarray) -> tuple[float, float]:
    """Return spectral triangular discrimination and classical JS (bits)."""
    p, u = np.linalg.eigh((a+a.conj().T)/2)
    q, v = np.linalg.eigh((b+b.conj().T)/2)
    p, q = np.maximum(p, 0), np.maximum(q, 0)
    w = abs(u.conj().T@v)**2
    den = p[:, None]+q[None, :]
    term = np.divide((p[:, None]-q[None, :])**2, den,
                     out=np.zeros_like(den), where=den > 0)
    discrimination = float(np.sum(w*term)/2)
    def xlog2(x):
        result = np.zeros_like(x)
        positive = x > 0
        result[positive] = x[positive]*np.log2(x[positive])
        return result
    js = float(np.sum(w*((xlog2(p)[:, None]+xlog2(q)[None, :])/2-xlog2(den/2))))
    return discrimination, js


def recovery_heat(b: float, steps: int) -> float:
    """Exact finite energy sum; does not simulate the global bath density matrix."""
    if not 0 < b < 1:
        raise ValueError("Recovery requires a finite full-rank bias.")
    if not isinstance(steps, Integral) or isinstance(steps, bool) or steps < 1:
        raise ValueError("Recovery steps must be a positive integer.")
    total = 0.0
    for first in range(1, steps+1, 65536):
        index = np.arange(first, min(first+65536, steps+1), dtype=float)
        total += float(np.arctanh(b*(index/steps)).sum())
    return b*total/(steps*LN2)


def device_metrics(s: float, epsilon: float) -> dict:
    U, gamma, H, b = collision(s, epsilon)
    outputs, baths, errors = [], [], []
    for x in (0, 1):
        input_state = np.diag([1-x, x]).astype(complex)
        joint = U@np.kron(input_state, gamma)@U.conj().T
        output = partial_trace(joint, [2, 2], [0])
        bath = partial_trace(joint, [2, 2], [1])
        outputs.append(output)
        baths.append(bath)
        errors.append(trace_distance(output, target(s, x)))
    heat = float(np.trace(H@((baths[0]+baths[1])/2-gamma)).real/LN2)
    return {"s": float(s), "epsilon": float(epsilon), "heat": heat,
            "thermal_bias": float(b), "gap_over_kBT": float(H[1, 1]),
            "branch_errors": errors,
            "transverse_components": [float(np.trace(X@a).real) for a in outputs],
            "minimum_initial_bath_population": float(np.linalg.eigvalsh(gamma).min())}
