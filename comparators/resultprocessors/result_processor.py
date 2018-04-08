import abc as abstract


class AbstractResultProcessor(object):

    @abstract.abstractmethod
    def processComparisonResult(self, resultComparatorResult, processingResultFile):
        """Processes the SetsComparisonResult object"""
        raise "Parse result method not implemented"

    @abstract.abstractmethod
    def getName(self):
        """Returns unique name of this resut processor"""
        raise "Get name not implemented"
