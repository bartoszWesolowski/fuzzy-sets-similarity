from abstract_aggregator import AbstractAggregator
from utils import constants as c


class MaximumAggregator(AbstractAggregator):

    def getName(self):
        return c.AGGREGATOR_MAXIMUM

    def aggregate(self, values):
        return max(values)
