"""Finite algebra and regression checks, not a numerical optimality proof."""
import math
import unittest
import numpy as np
from scipy.linalg import null_space, solve_sylvester
from qph.core import (I2, X, Z, LN2, auxiliary_allowance, collision, continuity,
                      crossover, device_metrics, disturbance, entropy, h2, holevo,
                      j2, lower_bound, partial_trace, recovery_heat,
                      spectral_information, target, trace_distance)


def unitary(rng, n):
    q, r = np.linalg.qr(rng.normal(size=(n, n))+1j*rng.normal(size=(n, n)))
    diagonal = np.diag(r)
    return q*(diagonal/abs(diagonal))[None, :]


def state(rng, n, rank=None):
    a = rng.normal(size=(n, rank or n))+1j*rng.normal(size=(n, rank or n))
    a = a@a.conj().T
    return a/np.trace(a)


class ReferenceTests(unittest.TestCase):
    def test_entropy_and_limits(self):
        self.assertEqual(h2(0), 0)
        self.assertEqual(h2(1), 0)
        self.assertEqual(h2(0.5), 1)
        self.assertEqual(crossover(0), 1)
        self.assertAlmostEqual(crossover(1), 0.1495103748978384, places=13)
        for b in [0, 0.01, 0.3, 0.8, 1]:
            self.assertAlmostEqual(j2(b), 1-h2((1+b)/2), places=13)

    def test_invalid_domains(self):
        for args in [(0, 0.01), (1, 0.01), (0.1, 0), (0.1, 0.6)]:
            with self.assertRaises(ValueError):
                collision(*args)
        with self.assertRaises(ValueError):
            h2(float('nan'))
        with self.assertRaises(ValueError):
            auxiliary_allowance(0, 0.1)
        with self.assertRaises(ValueError):
            recovery_heat(0.4, 0)
        with self.assertRaises(ValueError):
            crossover(-1)

    def test_targets_and_overlap(self):
        for s in [0.001, 0.05, 0.3, 0.9]:
            a, b = target(s, 0), target(s, 1)
            self.assertAlmostEqual(float(np.trace(a@a).real), 1, places=13)
            self.assertAlmostEqual(float(np.trace(a@b).real), s*s, places=13)

    def test_finite_regressions(self):
        strict = lower_bound(0.05, 0.0001)
        relaxed = device_metrics(0.05, 0.0025)
        self.assertAlmostEqual(strict, 0.4980441797133478, places=11)
        self.assertAlmostEqual(relaxed['heat'], 0.31148464627710154, places=11)
        allowance = auxiliary_allowance(16, 0.0001)
        self.assertAlmostEqual(allowance, 0.0018637225878890273, places=13)
        self.assertGreater(strict-allowance, relaxed['heat'])
        self.assertEqual(auxiliary_allowance(1, 0.2), 0)
        self.assertAlmostEqual(auxiliary_allowance(4, 1), 2, places=13)

    def test_explicit_device(self):
        for s in [0.001, 0.05, 0.2, 0.7]:
            for ratio in [0.0001, 0.01, 0.1]:
                e = ratio*math.sqrt(1-s*s)
                U, gamma, H, b = collision(s, e)
                self.assertLess(np.linalg.norm(U.conj().T@U-np.eye(4)), 1e-12)
                self.assertGreater(np.linalg.eigvalsh(gamma).min(), 0)
                stats = device_metrics(s, e)
                self.assertAlmostEqual(stats['heat'], b*math.atanh(b)/LN2, places=11)
                for x in (0, 1):
                    self.assertAlmostEqual(stats['branch_errors'][x], e, places=12)
                    self.assertAlmostEqual(stats['transverse_components'][x], -s, places=12)
                self.assertGreaterEqual(stats['heat']+1e-11, lower_bound(s, e))

    def test_recovery_sum(self):
        for b in [0.05, 0.4472135954999579, 0.9, 0.999]:
            last = float('inf')
            for m in [1, 2, 16, 2048]:
                q = recovery_heat(b, m)
                self.assertGreaterEqual(q+1e-13, j2(b))
                self.assertLessEqual(q, j2(b)+b*math.atanh(b)/(m*LN2)+1e-12)
                self.assertLessEqual(q, last+1e-12)
                last = q
        _, _, _, b = collision(1e-5, 1e-10)
        self.assertAlmostEqual(recovery_heat(b, 2048), 0.14958617576918243, places=12)

    def test_spectral_bridge(self):
        rng = np.random.default_rng(2026091601)
        for n in [2, 3, 4, 8]:
            for k in range(12):
                a, b = state(rng, n, 1 if k%3 == 0 else n), state(rng, n)
                t, js = spectral_information(a, b)
                self.assertGreaterEqual(holevo(a, b)+1e-9, js)
                self.assertGreaterEqual(js+1e-9, j2(math.sqrt(min(1, max(0, t)))))
                aa, bb = 0.999*a+0.001*np.eye(n)/n, 0.999*b+0.001*np.eye(n)/n
                y = solve_sylvester(aa, bb, aa-bb)
                via_equation = float(np.trace((aa-bb)@y.conj().T).real/2)
                via_spectrum, _ = spectral_information(aa, bb)
                self.assertAlmostEqual(via_equation, via_spectrum, places=9)

    def test_kinematic_steps(self):
        rng = np.random.default_rng(2026091602)
        for n in [1, 2, 3, 4]:
            for k in range(12):
                omega = state(rng, n, 1 if k%3 == 0 else n)
                v0, v1, w0, w1 = [unitary(rng, n) for _ in range(4)]
                values = rng.uniform(0, 1, n)
                if k%3 == 0:
                    values = np.linspace(0, 1, n)
                K = (w1*values)@w0.conj().T
                c0 = (w0*np.sqrt(1-values**2))@w0.conj().T
                c1 = (w1*np.sqrt(1-values**2))@w1.conj().T
                U = np.block([[v0@c0, -v0@K.conj().T], [v1@K, v1@c1]])
                states = [U@np.kron(np.diag([1-x, x]), omega)@U.conj().T for x in (0, 1)]
                ss = [partial_trace(a, [2, n], [0]) for a in states]
                ee = [partial_trace(a, [2, n], [1]) for a in states]
                delta = [float(ss[0][1, 1].real), float(ss[1][0, 0].real)]
                delta = [float(np.clip(x, 0, 1)) for x in delta]
                d = sum(delta)/2
                tau = [v0@omega@v0.conj().T, v1@omega@v1.conj().T]
                T = v1@K@v0.conj().T
                ell = np.trace((tau[0]-tau[1])@T.conj().T)
                z = ss[0][0, 1]+ss[1][0, 1]
                discr, _ = spectral_information(*tau)
                self.assertLessEqual(abs(ell-z), 2*d+1e-9)
                self.assertLessEqual(abs(ell)**2, 4*d*discr+1e-9)
                for x in (0, 1):
                    self.assertLessEqual(trace_distance(ee[x], tau[x]), disturbance(delta[x])+1e-9)
                self.assertLessEqual(abs(holevo(*ee)-holevo(*tau)), continuity(disturbance(d))+1e-9)

    def test_complete_auxiliary_ledger(self):
        rng = np.random.default_rng(2026091603)
        for da, db in [(1, 2), (2, 2), (3, 2), (2, 3)]:
            for k in range(8):
                a = state(rng, da, 1 if k%2 == 0 else da)
                energies = np.linspace(0, 3, db)
                gamma = np.diag(np.exp(-energies)/np.exp(-energies).sum())
                U = unitary(rng, 2*da*db)
                initial = np.kron(np.kron(I2/2, a), gamma)
                out = U@initial@U.conj().T
                aa = partial_trace(out, [2, da, db], [1])
                bb = partial_trace(out, [2, da, db], [2])
                ee = partial_trace(out, [2, da, db], [1, 2])
                delta_e = entropy(ee)-entropy(a)-entropy(gamma)
                delta_a = entropy(aa)-entropy(a)
                mutual = entropy(aa)+entropy(bb)-entropy(ee)
                relative = -entropy(bb)-float(np.trace(bb@np.diag(np.log2(np.diag(gamma)))).real)
                heat = float(np.trace(np.diag(energies)@(bb-gamma)).real/LN2)
                self.assertAlmostEqual(heat, delta_e-delta_a+mutual+relative, places=10)
                self.assertGreaterEqual(delta_e, -1e-9)
                self.assertGreaterEqual(heat+delta_a, -1e-9)

    def test_consumed_purity_control(self):
        s = 0.2
        c = math.sqrt(1-s*s)
        v0 = np.array([math.sqrt((1+c)/2), -math.sqrt((1-c)/2)])
        v1 = np.array([-math.sqrt((1-c)/2), math.sqrt((1+c)/2)])
        first = np.kron(v0, [1, 0])
        third = np.kron(v1, [0, 1])
        complement = null_space(np.column_stack([first, third]).conj().T)
        U = np.column_stack([first, complement[:, 0], third, complement[:, 1]])
        initial = np.kron(I2/2, np.diag([1, 0]))
        out = U@initial@U.conj().T
        self.assertLess(np.linalg.norm(U.conj().T@U-np.eye(4)), 1e-12)
        self.assertAlmostEqual(entropy(partial_trace(out, [2, 2], [1])), 1, places=12)

    def test_record_relocation(self):
        U, gamma, H, b = collision(0.05, 0.0025)
        swap = np.array([[1, 0, 0, 0], [0, 0, 1, 0],
                         [0, 1, 0, 0], [0, 0, 0, 1]])
        full = np.kron(U, I2)@np.kron(I2, swap)
        branches = [full@np.kron(np.kron(np.diag([1-x, x]), I2/2), gamma)@full.conj().T
                    for x in (0, 1)]
        average = sum(branches)/2
        aout = partial_trace(average, [2, 2, 2], [1])
        bout = [partial_trace(p, [2, 2, 2], [2]) for p in branches]
        self.assertLess(trace_distance(aout, I2/2), 1e-12)
        self.assertLess(trace_distance(bout[0], bout[1]), 1e-12)
        heat = float(np.trace(H@((bout[0]+bout[1])/2-gamma)).real/LN2)
        self.assertAlmostEqual(heat, b*math.atanh(b)/LN2, places=12)


if __name__ == '__main__':
    unittest.main()
