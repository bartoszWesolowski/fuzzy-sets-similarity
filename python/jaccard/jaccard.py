from utils.fuzzyset import FuzzySet
from utils import fuzzysetevaluator
from utils import mathutils as m
from utils import paramethers as params

# TODO: fix this formula!
def sim(A, B, config={
    params.ALPHA: 1,
    params.BETA: 1,
    params.GAMMA: 1,
    params.EVALUATOR: fuzzysetevaluator.sup
}):
    """Jaccard similarity index"""
    fuzzyA = FuzzySet(A)
    fuzzyB = FuzzySet(B)
    alpha = config[params.ALPHA]
    beta = config[params.BETA]
    gamma = config[params.GAMMA]
    evaluator = fuzzysetevaluator.getEvaluator([params.EVALUATOR])

    nominator = m.sum(evaluator(fuzzyA.intersect(fuzzyB)),
                      gamma * evaluator(fuzzyA.complement().intersect(fuzzyB.complement())))
    denominator1 = evaluator(fuzzyA.intersect(fuzzyB))
    denominator2 = m.multiply(alpha, evaluator(fuzzyA.intersect(fuzzyB.complement())))
    denominator3 = m.multiply(beta, evaluator(fuzzyA.complement().intersect(fuzzyB)))

    return m.divide(nominator, m.sum(m.sum(denominator1, denominator2), denominator3))
