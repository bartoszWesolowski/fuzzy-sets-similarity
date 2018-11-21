from abstract_aggregator import AbstractAggregator
from utils import constants as c

class AverageAggregator(AbstractAggregator):

    def getName(self):
        return c.AGGREGATOR_AVERAGE

    def aggregate(self, values):
        numberOfElements = float(len(values))
        avg = 0
        if numberOfElements > 0:
            avg = sum(values) / numberOfElements
        return avg
