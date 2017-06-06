# -*- coding: utf-8 -*-

import unittest
import minkowskisimilarity as mink
import fsgenerator as generator
class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_should_be_1_for_same_sets_with_static_sets(self):
        fSet = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        self.assertEqual(1, mink.sim(fSet, fSet))

        fSet = [1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0.4]
        self.assertEqual(1, mink.sim(fSet, fSet))

    def test_should_be_1_for_same_sets_with_random_sets(self):
        fSet = generator.randomFuzzyList(100)
        self.assertEqual(1, mink.sim(fSet, fSet))
        fSet = generator.randomFuzzyList(1000)
        self.assertEqual(1, mink.sim(fSet, fSet))
        fSet = generator.randomFuzzyList(1000, 0.5, 0.7)
        self.assertEqual(1, mink.sim(fSet, fSet))

if __name__ == '__main__':
    unittest.main()