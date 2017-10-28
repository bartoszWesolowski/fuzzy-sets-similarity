from utils import mathutils as m

from utils.fuzzyset import FuzzySet

from abstract_similarity_calculator import AbstractSimilarityCalculator

class MinkowskiSimilarityCalculator(AbstractSimilarityCalculator):

    def calculateSimilarity(self, A, B, r=2):
        """Computes similarity of two fuzzy sets A, B represented as arrays of floating points numbers
        r - parameter of Minkowski metric"""
        numberOfElements = max(len(A), len(B))
        return 1 - (self.metric(A, B, r) / float(numberOfElements))


    def generalSim(self, A, B, config={'r': 2}):
        """Computes similarity of two fuzzy sets A, B represented as arrays of floating points numbers
        config - map contating one entry with key equal to 'r' with numeric value - parameter of Minkowski metric"""
        numberOfElements = max(len(A), len(B))
        return 1 / (1 + self.metric(A, B, config['r']))

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
