from utils.fuzzyset import FuzzySet
from utils import mathutils as m
import math
from abstract_similarity_calculator import AbstractSimilarityCalculator

class AngularDistanceSimilarityCalculator(AbstractSimilarityCalculator):

    def calculateSimilarity(self, A, B, config={}):
        """
        Returns similarity of two fuzzy sets represented as angular distance between them.
        :param A: list of numbers representing fuzzy set
        :param B: list of numbers representing fuzzy set
        :param config: empty config
        :return: a number from range [0, 1] representing the similarity of passed sets 
        """
        fuzzyA = FuzzySet(A)
        fuzzyB = FuzzySet(B)
        multiplied = AngularDistanceSimilarityCalculator.multipliedElements(fuzzyA, fuzzyB)
        squereSumA = fuzzyA.accumulate(m.squere, sum)
        squereSumB = fuzzyB.accumulate(m.squere, sum)
        denominator = m.multiply(math.sqrt(squereSumA), math.sqrt(squereSumB))
        #TODO: what if denominator is equal to zero????
        if denominator == 0:
            print "Got denominator equal to zero while calculating angular distance for sets: " + str(
                fuzzyA.elements) + ", " + str(fuzzyB.elements)
            return 0

        return m.divide (multiplied, denominator)


    @staticmethod
    def multipliedElements(fuzzyA, fuzzyB):
        result = 0.0
        for i in range(fuzzyA.getLenght(fuzzyB)):
            result += fuzzyA.absoluteValue(i) * fuzzyB.absoluteValue(i)
        return result
