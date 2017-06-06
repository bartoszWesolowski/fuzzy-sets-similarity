from fuzzyset import FuzzySet
import mathutils as m

def sim(A, B, r=2):
    numberOfElements = max(len(A), len(B))
    return 1 - (metric(A, B, r) / float(numberOfElements))

def metric(A, B, r=2):
    """Calculates minkowski metric of two fuzzy sets A and B. A and B are lists of floats from 0 to 1 that are interpreted as fuzzy sets"""
    numberOfElements = max(len(A), len(B))
    fuzzySetA = FuzzySet(A)
    fuzzySetB = FuzzySet(B)
    sum = 0
    for i in range(numberOfElements):
        sum += abs(fuzzySetA.val(i) - fuzzySetB.val(i)) ** r

    return m.nthRoot(sum, r)
