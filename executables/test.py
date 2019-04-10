from simcalculators.minkowski_similarity_calculator import MinkowskiSimilarityCalculator

minkowksiSimilarityMeasure = MinkowskiSimilarityCalculator()

configuration = {
    'r': 2
}

A = [0.0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.45, 0.4, 0.35, 0.3, 0.25, 0.2, 0.15, 0.1, 0.05, 0.0]
B = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.0]

similarity = minkowksiSimilarityMeasure.calculateSimilarity(A, B, configuration)
print "Similarity: {}".format(similarity)

from fuzzyfacades.similarity_calculator_wrapper import SimilarityCalculatorFacade

similarityCalculatorFacade = SimilarityCalculatorFacade()
A = [0.0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3]
B = [0.0, 0.10, 0.2, 0.31, 0.4, 0.55, 0.6]

similarityMethods = [
    {
        'method': 'minkowski',
        'r': 1
    },
    {
        'method': 'minkowski',
        'r': 2
    }
]

for method in similarityMethods:
    similarity = similarityCalculatorFacade \
        .calculateSimilarityFromRawConfig(A, B, method)
    print "Similarity for method {}: {}".format(method, similarity)

from simcalculators.abstract_similarity_calculator import AbstractSimilarityCalculator


class TestSimilarityCalculator(AbstractSimilarityCalculator):
    def calculateSimilarity(self, A, B, configuration):
        return 0


from parsers.abstract_configuration_parser import AbstractConfigurationParser


class TestSimilarityCalculatorConfigurationParser(AbstractConfigurationParser):

    def parse(self, rawConfigMap):
        return rawConfigMap
