import abc as abstract


class MethodsComparisonAbstractResultProcessor(object):

    @abstract.abstractmethod
    def processComparisonResult(self, resultComparatorResult, processorConfigurationMap):
        """
        Method that process the result of comparing two sets using N similarity measures
        :param resultComparatorResult: MethodsComparisonResult object
        :param processorConfigurationMap: map containing configuration
        :return: 
        """
        raise "Parse result method not implemented"

    @abstract.abstractmethod
    def getName(self):
        """Returns unique name of this resut processor"""
        raise "Get name not implemented"
