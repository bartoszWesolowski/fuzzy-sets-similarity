from utils.fuzzyset import FuzzySet
from utils import fuzzysetevaluator
from utils import mathutils as m
from utils import paramethers as params

from abstract_similarity_calculator import AbstractSimilarityCalculator

class JaccardSimilarityCalculator(AbstractSimilarityCalculator):

    # TODO: fix this formula!
    def calculateSimilarity(self, A, B, config={
        params.ALPHA: 1,
        params.BETA: 1,
        params.GAMMA: 1,
        params.EVALUATOR: fuzzysetevaluator.sup
    }):
        """Jaccard similarity index"""

        fuzzyA = FuzzySet(A)
        fuzzyB = FuzzySet(B)
        universe = fuzzyA.getUniverse(fuzzyB)

        alpha = config[params.ALPHA]
        beta = config[params.BETA]
        gamma = config[params.GAMMA]
        evaluatorName = config[params.EVALUATOR]
        evaluator = fuzzysetevaluator.getEvaluator(evaluatorName, universe)
        nominator = m.sum(evaluator.evaluate(fuzzyA.intersect(fuzzyB)),
                          gamma * evaluator.evaluate(fuzzyA.complement().intersect(fuzzyB.complement())))
        denominator1 = evaluator.evaluate(fuzzyA.intersect(fuzzyB))
        denominator2 = m.multiply(alpha, evaluator.evaluate(fuzzyA.intersect(fuzzyB.complement())))
        denominator3 = m.multiply(beta, evaluator.evaluate(fuzzyA.complement().intersect(fuzzyB)))

        mainDenominator = denominator1 + denominator2 + denominator3
        if mainDenominator == 0:
            return 0.0
            #raise AttributeError("Can not calculate Jaccard similarity. Denominator can not be zero.")

        return m.divide(nominator, mainDenominator)
