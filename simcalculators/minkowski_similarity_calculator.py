from utils import mathutils as m

from utils.fuzzyset import FuzzySet

from abstract_similarity_calculator import AbstractSimilarityCalculator
from utils import configuration_parameters_names as params
class MinkowskiSimilarityCalculator(AbstractSimilarityCalculator):

    def calculateSimilarity(self, A, B, configuration={'r': 2}):
        """Computes similarity of two fuzzy sets A, B represented as arrays of floating points numbers
        r - parameter of Minkowski metric"""
        return 1 / (1 + self.metric(A, B, configuration[params.R]))


    def metric(self, A, B, r=2):
        """Calculates Minkowski metric of two fuzzy sets A and B. A and B are lists of floats from 0 to 1
         that are interpreted as fuzzy sets"""
        numberOfElements = max(len(A), len(B))
        fuzzySetA = FuzzySet(A)
        fuzzySetB = FuzzySet(B)
        sum = 0
        for i in range(numberOfElements):
            sum += abs(fuzzySetA.val(i) - fuzzySetB.val(i)) ** r

        return m.nthRoot(sum, r)
