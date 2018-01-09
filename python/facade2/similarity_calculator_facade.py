from facade2.similarity_method import SimilarityMethod
from utils import constants

from simcalculators.angluar_distance_similarity_calculator import AngularDistanceSimilarityCalculator
from simcalculators.minkowski_similarity_calculator import MinkowskiSimilarityCalculator
from simcalculators.jaccard_similarity_calculator import JaccardSimilarityCalculator
from simcalculators.implication_similaroty_calculator import ImplicationSimilarityCalculator

from parsers.angular_distance_configuration_parser import AngularDistanceConfigParser
from parsers.minkowski_configuration_parser import MinkowskiConfigParser
from parsers.jaccard_configuration_parser import JaccardConfigParser
from parsers.implication_configuration_parser import ImplicationConfigurationParser

class SimilarityFacade(object):

    similarityMethods = [
        SimilarityMethod(constants.ANGULAR_DISTANCE, AngularDistanceSimilarityCalculator(), AngularDistanceConfigParser()),
        SimilarityMethod(constants.MINKOWSKI, MinkowskiSimilarityCalculator(), MinkowskiConfigParser()),
        SimilarityMethod(constants.JACCARD_INDEX, JaccardSimilarityCalculator(), JaccardConfigParser()),
        SimilarityMethod(constants.IMPLICATION_SIMILARITY, ImplicationSimilarityCalculator(), ImplicationConfigurationParser()),
    ]

    def getSupportedMethods(self):
        return [methodConfig.name for methodConfig in self.similarityMethods]

    def getSimilarityMethod(self, methodName):
        if methodName not in self.getSupportedMethods():
            raise AttributeError(
                "Trying to get configuration parser for unsupported method {}. Allowed methods {}".format(
                    methodName, self.getSupportedMethods()
                )
            )

        for method in self.similarityMethods:
            if method.name == methodName:
                return method

    def getParser(self, methodName):
        method = self.getSimilarityMethod(methodName)
        return method.configurationParser

    def getSimilarityCalculator(self, calculatorName):
        method = self.getSimilarityMethod(calculatorName)
        return method.similarityCalculator
