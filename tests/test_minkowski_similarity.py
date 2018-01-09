# -*- coding: utf-8 -*-

import unittest

from minkowski import minkowskisimilarity as mink

from utils import fsgenerator as generator


class MinkowskiTestWithMinkowskiEuclidsMetric(unittest.TestCase):
    """Basic test cases."""

    def completly_different_sets(self, len, expected):
        zeros = generator.singletonFuzzyList(length=len, value=0)
        ones = generator.singletonFuzzyList(length=len, value=1)
        self.assertAlmostEqual(expected, mink.sim(zeros, ones), delta=0.0000001)

    def test_should_be_1_for_same_sets_with_static_sets(self):
        fSet = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        self.assertEqual(1, mink.sim(fSet, fSet))

        fSet = generator.randomFuzzyList(100)
        self.assertEqual(1, mink.sim(fSet, fSet))

    def test_should_be_1_for_same_sets_with_random_sets(self):
        fSet = generator.randomFuzzyList(100)
        self.assertEqual(1, mink.sim(fSet, fSet))
        fSet = generator.randomFuzzyList(1000)
        self.assertEqual(1, mink.sim(fSet, fSet))
        fSet = generator.randomFuzzyList(1000, 0.5, 0.7)
        self.assertEqual(1, mink.sim(fSet, fSet))

    def test_with_completly_opposite_sets_few_elements(self):
        zeros = [0, 0, 0, 0]
        ones = [1, 1, 1, 1]
        self.assertEqual(0.5, mink.sim(zeros, ones))

    def test_with_completly_different_setts_with_big_fuzzy_set(self):
        '''When there is a lot of elements in sets, and they are maximally different this measure 
        returns disturbing results'''
        self.completly_different_sets(100, 0.9)

    def test_with_completly_different_similarity_approach_one(self):
        '''When there is a lot of elements in sets, and they are maximally different this measure 
        returns approches one even though sets are not that similar'''
        self.completly_different_sets(10000, 0.99)

    def test_with_really_big_random_sets_value_will_still_approach_one(self):
        first = generator.randomFuzzyList(100000)
        second = generator.randomFuzzyList(100000)
        sim = mink.sim(first, second)
        print "Similarity of random sets of length 100k should approach 1. Calculated value: %s" % sim
        self.assertAlmostEqual(1.0, sim, delta=0.01)

if __name__ == '__main__':
    unittest.main()