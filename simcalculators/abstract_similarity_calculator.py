import abc as abstract


class AbstractSimilarityCalculator(object):

    @abstract.abstractmethod
    def calculateSimilarity(self, A, B, configuration):
        """
        Calculates similarity between two fuzzy sets.
        :param A: first fuzzy set to compare
        :param B: second fuzzy set to compare
        :param configuration: map containing all parameters of similarity method
        :return: a number from [0, 1] range that represents the similarity between two fuzzy sets
        """
        pass
