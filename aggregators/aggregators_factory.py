from average_aggregator import AverageAggregator
from minimum_aggregator import MinimumAggregator
from maximum_aggregator import MaximumAggregator


class AggregatorFactory(object):
    def __init__(self):
        super(AggregatorFactory, self).__init__()
        self.aggregators = [
            AverageAggregator(),
            MinimumAggregator(),
            MaximumAggregator()
        ]

        self.aggregatorsMap = {}
        for aggregator in self.aggregators:
            self.aggregatorsMap[aggregator.getName()] = aggregator

    def getSupportedAggregators(self):
        """returns list of all supported aggregators"""
        return [aggregator.getName() for aggregator in self.aggregators]

    def getAggregator(self, name):
        if name not in self.getSupportedAggregators():
            raise AttributeError(
                "Can not create aggregator for name: {}. Supported aggregators: {}".format(
                    name, self.getSupportedAggregators()))

        return self.aggregatorsMap[name]

    def isAggregatorSupported(self, aggregatorName):
        return aggregatorName in self.getSupportedAggregators()