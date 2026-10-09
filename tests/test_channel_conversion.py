"""Small matrix consistency checks for the finite Gibbs dephasing wrapper.

The diamond-norm identity and exact-output obstruction are proved in the
documentation; these examples check the physical implementation and accounting.
"""
import math
import unittest

import numpy as np

from qph.core import I2, Z, LN2, collision, partial_trace, target, trace_distance


P0 = np.diag([1.0, 0.0]).astype(complex)
P1 = np.diag([0.0, 1.0]).astype(complex)
GAMMA_C = I2 / 2
H_C = np.zeros((2, 2), dtype=complex)
W_CS = np.kron(P0, I2) + np.kron(P1, Z)
SWAP = np.array([[1, 0, 0, 0], [0, 0, 1, 0],
                 [0, 1, 0, 0], [0, 0, 0, 1]], dtype=complex)


class ChannelConversionTests(unittest.TestCase):
    def test_degenerate_gibbs_dephasing(self):
        np.testing.assert_array_equal(W_CS.conj().T @ W_CS, np.eye(4))
        weights = np.exp(-np.diag(H_C))
        np.testing.assert_array_equal(np.diag(weights / weights.sum()), GAMMA_C)
        self.assertGreater(np.linalg.eigvalsh(GAMMA_C).min(), 0)
        ket = np.array([math.sqrt(0.3), 1j * math.sqrt(0.7)])
        rho = np.outer(ket, ket.conj())
        joint = W_CS @ np.kron(GAMMA_C, rho) @ W_CS.conj().T
        np.testing.assert_allclose(partial_trace(joint, [2, 2], [1]),
                                   (rho + Z @ rho @ Z) / 2, atol=1e-14)
        cout = partial_trace(joint, [2, 2], [0])
        np.testing.assert_allclose(cout, GAMMA_C, atol=1e-14)
        self.assertEqual(np.trace(H_C @ (cout - GAMMA_C)), 0)

    def test_basis_joint_states_are_exactly_preserved(self):
        # Rank-deficient, nonthermal workspace with a finite full-rank bath.
        tau_a = np.diag([0.7, 0.3, 0.0])
        _, gamma_b, _, _ = collision(0.2, 0.01)
        wrapper = np.kron(W_CS, np.eye(6))
        for basis in (P0, P1):
            initial = np.kron(np.kron(GAMMA_C, basis), np.kron(tau_a, gamma_b))
            np.testing.assert_array_equal(wrapper @ initial @ wrapper.conj().T,
                                          initial)

    def test_collision_heat_and_return_are_preserved(self):
        s, epsilon = 0.2, 0.01
        collision_u, gamma_b, h_b, _ = collision(s, epsilon)
        # In S,A,B order, swap the thermal state into A and collide S with A.
        # This device returns only the average A marginal, not each branch.
        original_u = np.kron(collision_u, I2) @ np.kron(I2, SWAP)
        wrapper = np.kron(W_CS, np.eye(4))
        wrapped_u = np.kron(I2, original_u) @ wrapper
        h_bc = np.kron(I2, h_b)  # C,B order; C has identically zero energy.
        branches, wrapped_branches, old_heats, new_heats = [], [], [], []
        for x, basis in enumerate((P0, P1)):
            initial = np.kron(np.kron(basis, I2 / 2), gamma_b)
            old = original_u @ initial @ original_u.conj().T
            wrapped = wrapped_u @ np.kron(GAMMA_C, initial) @ wrapped_u.conj().T
            np.testing.assert_allclose(wrapped, np.kron(GAMMA_C, old), atol=1e-14)
            old_s = partial_trace(old, [2, 2, 2], [0])
            new_s = partial_trace(wrapped, [2, 2, 2, 2], [1])
            np.testing.assert_allclose(new_s, old_s, atol=1e-14)
            self.assertAlmostEqual(trace_distance(new_s, target(s, x)),
                                   epsilon, places=13)
            old_b = partial_trace(old, [2, 2, 2], [2])
            new_cb = partial_trace(wrapped, [2, 2, 2, 2], [0, 3])
            old_heats.append(float(np.trace(h_b @ (old_b - gamma_b)).real / LN2))
            new_heats.append(float(np.trace(h_bc @
                                    (new_cb - np.kron(GAMMA_C, gamma_b))).real / LN2))
            cout = partial_trace(wrapped, [2, 2, 2, 2], [0])
            self.assertEqual(np.trace(H_C @ (cout - GAMMA_C)), 0)
            branches.append(old)
            wrapped_branches.append(wrapped)
        np.testing.assert_allclose(new_heats, old_heats, atol=1e-14)
        self.assertGreater(sum(old_heats) / 2, 0)
        self.assertAlmostEqual(sum(new_heats) / 2, sum(old_heats) / 2, places=13)
        new_a = partial_trace(sum(wrapped_branches) / 2, [2, 2, 2, 2], [2])
        np.testing.assert_allclose(new_a, I2 / 2, atol=1e-14)
        conditional_a = [partial_trace(branch, [2, 2, 2], [1]) for branch in branches]
        self.assertGreater(trace_distance(*conditional_a), 0.01)

    def test_entangled_reference_error_expression(self):
        # A partial swap retains input coherences, unlike the collision channel.
        original_u = (np.eye(4) - 1j * SWAP) / math.sqrt(2)
        h_b = np.diag([0.0, 0.8])
        gibbs_weights = np.exp(-np.diag(h_b))
        gamma_b = np.diag(gibbs_weights / gibbs_weights.sum())
        np.testing.assert_allclose(original_u.conj().T @ original_u, np.eye(4),
                                   atol=1e-14)
        outputs = []
        for basis in (P0, P1):
            joint = original_u @ np.kron(basis, gamma_b) @ original_u.conj().T
            outputs.append(partial_trace(joint, [2, 2], [0]))
        plus = np.ones((2, 2)) / 2
        coherent_joint = original_u @ np.kron(plus, gamma_b) @ original_u.conj().T
        coherent_output = partial_trace(coherent_joint, [2, 2], [0])
        self.assertGreater(trace_distance(coherent_output, sum(outputs) / 2), 0.1)

        # Reorder U on S,B with spectator R to S,R,B, then prepend C.
        u_srb = np.kron(original_u, I2).reshape((2,) * 6).transpose(
            0, 2, 1, 3, 5, 4).reshape(8, 8)
        wrapper = np.kron(W_CS, np.eye(4))
        complete_u = np.kron(I2, u_srb) @ wrapper
        ket_sr = np.array([math.sqrt(0.4), 0, math.sqrt(0.3), math.sqrt(0.3)])
        self.assertGreater(abs(np.linalg.det(ket_sr.reshape(2, 2))), 0.1)
        rho_sr = np.outer(ket_sr, ket_sr.conj())
        initial = np.kron(GAMMA_C, np.kron(rho_sr, gamma_b))
        dephased = wrapper @ initial @ wrapper.conj().T
        z_sr = np.kron(Z, I2)
        np.testing.assert_allclose(partial_trace(dephased, [2, 2, 2, 2], [1, 2]),
                                   (rho_sr + z_sr @ rho_sr @ z_sr) / 2, atol=1e-14)
        final = complete_u @ initial @ complete_u.conj().T
        actual_sr = partial_trace(final, [2, 2, 2, 2], [1, 2])
        reference_blocks = [rho_sr[2*x:2*x+2, 2*x:2*x+2] for x in (0, 1)]
        for block in reference_blocks:
            self.assertGreaterEqual(np.linalg.eigvalsh(block).min(), -1e-14)
        self.assertAlmostEqual(sum(np.trace(block).real for block in reference_blocks), 1)
        s = 0.2
        target_sr = sum(np.kron(target(s, x), reference_blocks[x]) for x in (0, 1))
        expected_difference = sum(np.kron(outputs[x] - target(s, x), reference_blocks[x])
                                  for x in (0, 1))
        np.testing.assert_allclose(actual_sr - target_sr, expected_difference, atol=1e-14)
        branch_errors = [trace_distance(outputs[x], target(s, x)) for x in (0, 1)]
        self.assertLessEqual(trace_distance(actual_sr, target_sr), max(branch_errors) + 1e-14)

        # A basis input attaining the largest branch error witnesses the lower bound.
        x = int(np.argmax(branch_errors))
        basis = (P0, P1)[x]
        witness_in = np.kron(GAMMA_C, np.kron(np.kron(basis, plus), gamma_b))
        witness_final = complete_u @ witness_in @ complete_u.conj().T
        witness_sr = partial_trace(witness_final, [2, 2, 2, 2], [1, 2])
        self.assertAlmostEqual(trace_distance(witness_sr, np.kron(target(s, x), plus)),
                               max(branch_errors), places=13)


if __name__ == '__main__':
    unittest.main()
