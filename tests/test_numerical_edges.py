"""Numerical stability and comparison failures; not new optimality evidence."""
from decimal import Decimal, localcontext
import math
import sys
import unittest

from qph.core import crossover, j2
from scripts.check_repository import compare


def small_bias_reference(b):
    """Evaluate the existing positive series with high-precision arithmetic."""
    with localcontext() as ctx:
        ctx.prec = 100
        x = Decimal.from_float(b)
        return float(sum(x**(2*k)/(Decimal(2*k)*Decimal(2*k-1))
                         for k in range(1, 25)) / Decimal(2).ln())


class NumericalEdgeTests(unittest.TestCase):
    def test_small_bias_retains_relative_precision(self):
        for b in (0.009999, 1e-4, 1e-8, 1e-12, 1e-16, 1e-20, 1e-100, 1e-150):
            with self.subTest(b=b):
                expected = small_bias_reference(b)
                self.assertTrue(math.isclose(j2(b), expected, rel_tol=2e-15,
                                             abs_tol=0.0))
                self.assertGreater(j2(b), 0.0)

    def test_series_switch_is_continuous(self):
        for b in (math.nextafter(0.01, 0.0), 0.01, math.nextafter(0.01, 1.0)):
            self.assertTrue(math.isclose(j2(b), small_bias_reference(b),
                                         rel_tol=2e-13, abs_tol=0.0))

    def test_large_finite_ratio_does_not_overflow_to_zero(self):
        for ratio in (1e20, 1e100, 1e300, 1e308, sys.float_info.max):
            with self.subTest(ratio=ratio), localcontext() as ctx:
                ctx.prec = 100
                r = Decimal.from_float(ratio)
                b = 1 / (1 + 4*r).sqrt()
                expected = float(sum(b**(2*k)/(Decimal(2*k)*Decimal(2*k-1))
                                     for k in range(1, 15)) / Decimal(2).ln())
                self.assertGreater(crossover(ratio), 0.0)
                self.assertTrue(math.isclose(crossover(ratio), expected,
                                             rel_tol=5e-14, abs_tol=0.0))

    def test_nonfinite_reference_values_are_rejected(self):
        for invalid in (float('nan'), float('inf'), -float('inf')):
            for expected, actual in ((0.1, invalid), (invalid, 0.1), (invalid, invalid)):
                with self.subTest(expected=expected, actual=actual):
                    with self.assertRaises(AssertionError):
                        compare({'nested': [expected]}, {'nested': [actual]})


if __name__ == '__main__':
    unittest.main()
