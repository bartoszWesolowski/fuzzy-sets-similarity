from abstract_aggregator import AbstractAggregator


class AverageAggregator(AbstractAggregator):

    NAME = "average"

    def getName(self):
        return AverageAggregator.NAME

    def aggregate(self, values):
        numberOfElements = float(len(values))
        avg = 0
        if numberOfElements > 0:
            avg = sum(values) / numberOfElements
        return avg
