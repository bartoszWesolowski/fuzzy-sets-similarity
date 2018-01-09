import abc as abstract


class AbstractSimilarityCalculator(object):

    @abstract.abstractmethod
    def calculateSimilarity(self, A, B, configuration):
        pass
