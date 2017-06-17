# -*- coding: utf-8 -*-

import unittest

from utils.fuzzyset import FuzzySet


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""
    maxError = 0.000001;
    fuzzySetOne = FuzzySet([0, 0.2, 0.5, 0.9, 1])
    fuzzySetTwo = FuzzySet([1, 0.5, 0.5, 0, 1])

    def test_val(self):
        self.assertEqual(0, self.fuzzySetOne.val(0))
        self.assertEqual(0.5, self.fuzzySetOne.val(2))
        self.assertEqual(0, self.fuzzySetOne.val(10))

    def test_sum_with_default_tNorm(self):
        fuzzySum = self.fuzzySetOne.sum(self.fuzzySetTwo)
        self.assertEqual(1, fuzzySum.val(0))
        self.assertEqual(0.5,fuzzySum.val(1))
        self.assertEqual(0.5, fuzzySum.val(2))
        self.assertEqual(0.9, fuzzySum.val(3))
        self.assertEqual(1, fuzzySum.val(4))

if __name__ == '__main__':
    unittest.main()