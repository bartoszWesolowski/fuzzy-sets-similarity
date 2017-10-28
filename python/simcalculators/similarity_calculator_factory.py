from minkowski import minkowskisimilarity as minSim
from angle import angluardistance
from jaccard import jaccard
from utils import constants

from angluar_distance_similarity_calculator import AngularDistanceSimilarityCalculator
from jaccard_similarity_calculator import JaccardSimilarityCalculator
from minkowski_similarity_calculator import MinkowskiSimilarityCalculator

class SimilarityCalculatorFactory(object):
    """Object providing interface for retrieving similarity calculator object
    based on name"""
    SIMILARITY_METHODS_MAP = {
        constants.MINKOWSKI: MinkowskiSimilarityCalculator(),
        constants.ANGULAR_DISTANCE: AngularDistanceSimilarityCalculator(),
        constants.JACCARD_INDEX: JaccardSimilarityCalculator()
    }

    def getSupportedCalulatorsNames(self):
        return self.SIMILARITY_METHODS_MAP.keys()

    def getSimilarityCalculator(self, calculatorName):
        if calculatorName not in self.getSupportedCalulatorsNames():
            raise AttributeError(
                "Unknown similarity calculator name: {}. Can not provide similarity calculator for that name.".format(
                    calculatorName))

        return self.SIMILARITY_METHODS_MAP[calculatorName]
