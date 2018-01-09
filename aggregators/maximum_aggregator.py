from abstract_aggregator import AbstractAggregator


class MaximumAggregator(AbstractAggregator):
    NAME = "maximum"

    def getName(self):
        return MaximumAggregator.NAME

    def aggregate(self, values):
        return max(values)
