from utils import mathutils as m

from utils.fuzzyset import FuzzySet


def sim(A, B, r=2):
    """Computes similarity of two fuzzy sets A, B represented as arrays of floating points numbers
    r - parameter of Minkowski metric"""
    numberOfElements = max(len(A), len(B))
    return 1 - (metric(A, B, r) / float(numberOfElements))


def generalSim(A, B, config={'r': 2}):
    """Computes similarity of two fuzzy sets A, B represented as arrays of floating points numbers
    config - map contating one entry with key equal to 'r' with numeric value - parameter of Minkowski metric"""
    numberOfElements = max(len(A), len(B))
    return 1 / (1 + metric(A, B, config['r']))

def metric(A, B, r=2):
    """Calculates Minkowski metric of two fuzzy sets A and B. A and B are lists of floats from 0 to 1
     that are interpreted as fuzzy sets"""
    numberOfElements = max(len(A), len(B))
    fuzzySetA = FuzzySet(A)
    fuzzySetB = FuzzySet(B)
    sum = 0
    for i in range(numberOfElements):
        sum += abs(fuzzySetA.val(i) - fuzzySetB.val(i)) ** r

    return m.nthRoot(sum, r)
