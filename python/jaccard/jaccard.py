from utils.fuzzyset import FuzzySet
from utils import fuzzysetevaluator
from utils import mathutils as m


def sim(A, B, config={
    'alfa': 1,
    'beta': 1,
    'gamma': 1,
    'g': fuzzysetevaluator.sup
}):
    """Jaccard similarity index"""
    fuzzyA = FuzzySet(A)
    fuzzyB = FuzzySet(B)
    alfa = config['alfa']
    beta = config['beta']
    gamma = config['gamma']
    evaluator = config['g']

    nominator = m.sum(evaluator(fuzzyA.intersect(fuzzyB)),
                      gamma * evaluator(fuzzyA.complement().intersect(fuzzyB.complement())))
    denominator1 = evaluator(fuzzyA.intersect(fuzzyB))
    denominator2 = m.multiply(alfa, evaluator(fuzzyA.intersect(fuzzyB.complement())))
    denominator3 = m.multiply(beta, evaluator(fuzzyA.complement().intersect(fuzzyB)))

    return m.divide(nominator, m.sum(m.sum(denominator1, denominator2), denominator3))
