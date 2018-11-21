from abstract_aggregator import AbstractAggregator
from utils import constants as c


class MinimumAggregator(AbstractAggregator):

    def getName(self):
        return c.AGGREGATOR_MINIMUM

    def aggregate(self, values):
        return min(values)
