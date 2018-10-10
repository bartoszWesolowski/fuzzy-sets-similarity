class MethodsComparisonResult(object):
    """Class representing result of comparing two fuzzy sets with N similarity measures"""

    def __init__(self, A, B, similarityMeasuresConfigurations, resultsList):
        """
        :param A: first fuzzy set to compare
        :param B: second fuzzy sets to compare
        :param similarityMeasuresConfigurations: list of fuzzy sets configuration objects (maps) 
        :param resultsList: list containing all results of comparing sets A and B with each configuration from similarityMeasuresConfigurations list
        """
        self.A = A
        self.B = B
        self.numberOfMethods = len(similarityMeasuresConfigurations)
        self.similarityMeasuresConfigurations = similarityMeasuresConfigurations
        self.resultsList = resultsList


class MethodsComparisonResultBuilder(object):
    def __init__(self, A, B, similarityMeasuresConfigurations):
        """
        :param A: first fuzzy set to compare
        :param B: second fuzzy sets to compare
        :param similarityMeasuresConfigurations: list of fuzzy sets configuration objects (maps) 
        """
        self.A = A
        self.B = B
        self.numberOfMethods = len(similarityMeasuresConfigurations)
        self.similarityMeasuresConfigurations = similarityMeasuresConfigurations
        self.results = [0 for i in range(self.numberOfMethods)]

    def addResultEntry(self, index, result):
        """
        Adds result entry for comparison of given sets with similarity measure with given index
        :param index: 
        :param result: 
        :return: Void
        """
        self.results[index] = result

    def build(self):
        """
        Creates MethodsComparisonResult based on this object current state
        :return: 
        """
        return MethodsComparisonResult(self.A, self.B, self.similarityMeasuresConfigurations, self.results)
