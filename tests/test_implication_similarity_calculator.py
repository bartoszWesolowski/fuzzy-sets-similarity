# -*- coding: utf-8 -*-

import unittest

from simcalculators.implication_similaroty_calculator import ImplicationSimilarityCalculator
from utils import configuration_parameters_names as paramNames
from tnorms.minimium_t_norm import MinimumTnorm
from implications.maximum_implication import MaximumImplication
from aggregators.maximum_aggregator import MaximumAggregator
from aggregators.minimum_aggregator import MinimumAggregator
from aggregators.average_aggregator import AverageAggregator

class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""
    maxError = 0.000001;
    calculator = ImplicationSimilarityCalculator()
    A = [0, 0.2, 0.5, 0.9, 1]
    B = [1, 0.5, 0.5, 0.0, 1]
    configuration = {
        paramNames.TNORM: MinimumTnorm.NAME,
        paramNames.AGGREGATOR: MaximumAggregator.NAME,
        paramNames.IMPLICATION: MaximumImplication.NAME
    }

    def test_with_maximum_aggregator(self):
        self.configuration[paramNames.AGGREGATOR] = MaximumAggregator.NAME
        similarity = self.calculator.calculateSimilarity(self.A, self.B, self.configuration)
        self.assertAlmostEqual(1, similarity)

    def test_with_minimum_aggregator(self):
        self.configuration[paramNames.AGGREGATOR] = MinimumAggregator.NAME
        similarity = self.calculator.calculateSimilarity(self.A, self.B, self.configuration)
        self.assertAlmostEqual(0, similarity)

    def test_with_average_aggregator(self):
        self.configuration[paramNames.AGGREGATOR] = AverageAggregator.NAME
        similarity = self.calculator.calculateSimilarity(self.A, self.B, self.configuration)
        self.assertAlmostEqual(0.42, similarity)


if __name__ == '__main__':
    unittest.main()