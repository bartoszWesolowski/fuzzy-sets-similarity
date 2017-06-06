# -*- coding: utf-8 -*-

import unittest
import mathutils as mu

class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""
    maxError = 0.000001;
    def test_simple_cases(self):
        assert True

    def test_nth_root_simple_cases(self):
        print mu.nthRoot(125, 3)
        self.assertAlmostEqual(5.0, mu.nthRoot(125, 3), msg="3-th root of 125 should be 5")
        self.assertAlmostEqual(3.0, mu.nthRoot(27, 3), msg="3-th root of 27 should be 3")
        self.assertAlmostEqual(3.0, mu.nthRoot(81, 4), msg="4-th root of 81 should be 3")


if __name__ == '__main__':
    unittest.main()