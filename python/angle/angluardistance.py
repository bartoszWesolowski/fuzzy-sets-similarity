from utils.fuzzyset import FuzzySet
from utils import mathutils as m
import math

def sim(A, B, config={}):
    """
    Returns similarity of two fuzzy sets represented as angular distance between them.
    :param A: list of numbers representing fuzzy set
    :param B: list of numbers representing fuzzy set
    :param config: empty config
    :return: a number from range [0, 1] representing the similarity of passed sets 
    """
    fuzzyA = FuzzySet(A)
    fuzzyB = FuzzySet(B)
    multiplied = multipliedElements(fuzzyA, fuzzyB)
    squereSumA = fuzzyA.accumulate(m.squere, m.sum)
    squereSumB = fuzzyB.accumulate(m.squere, m.sum)
    denominator = m.multiply(math.sqrt(squereSumA), math.sqrt(squereSumB))
    return m.divide(multiplied, denominator)

def multipliedElements(fuzzyA, fuzzyB):
    result = 0.0
    for i in range(fuzzyA.getLenght(fuzzyB)):
        result += fuzzyA.absoluteValue(i) * fuzzyB.absoluteValue(i)
    return result