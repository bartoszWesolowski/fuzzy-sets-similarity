from abstract_aggregator import AbstractAggregator


class MinimumAggregator(AbstractAggregator):
    NAME = "minimum"

    def getName(self):
        return MinimumAggregator.NAME

    def aggregate(self, values):
        return min(values)
