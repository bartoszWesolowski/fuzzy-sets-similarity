from comparators.methods_comparison_result import MethodsComparisonResultBuilder
from fuzzyfacades.similarity_calculator_wrapper import SimilarityCalculatorFacade


class MethodsComparator(object):
    """Class that compares two sets using N similarity measures"""

    def __init__(self):
        self.similarityCalculatorWrapper = SimilarityCalculatorFacade()

    def compareTwoSetsUsingMultipleMethods(self, A, B, listOfMethodsConfigurations):
        """
        Compare two sets using N similarity calculation methods
        :param A: first fuzzy set
        :param B: second fuzzy set
        :param listOfMethodsConfigurations: list of configurations of Similarity Calculators
        :return: MethodsComparisonResult object representing result
        """
        resultBuilder = MethodsComparisonResultBuilder(A, B, listOfMethodsConfigurations)
        for index, config in enumerate(listOfMethodsConfigurations):
            result = self.similarityCalculatorWrapper.calculateSimilarityFromParsedConfig(A, B, config)
            resultBuilder.addResultEntry(index, result)

        return resultBuilder.build()
