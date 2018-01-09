import abc as abstract


class AbstractAggregator(object):
    @abstract.abstractmethod
    def aggregate(self, values):
        """Aggregates all elements in values list into one element"""
        pass


    @abstract.abstractmethod
    def getName(self):
        """Returns unique name of this aggregator"""
        pass