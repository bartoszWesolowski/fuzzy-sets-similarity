from abstract_similarity_calculator import AbstractSimilarityCalculator
from utils.fuzzyset import FuzzySet
from implications.implication_factory import ImplicationFactory
from aggregators.aggregators_factory import AggregatorFactory
from tnorms.t_norm_factory import TnormFactory
from utils import configuration_parameters_names as paramNames
#TODO: Nazwa
class ElementsSimilarityByImplicationCalculator(object):
    def __init__(self, implication, tNorm):
        self.implication = implication
        self.tNorm = tNorm

    def similarityOfTwoElements(self, a, b):
        aImplicateB = self.implication.implicationValue(a, b)
        bImplicatesA = self.implication.implicationValue(b, a)
        return self.tNorm.tnormValue(aImplicateB, bImplicatesA)

    def generalSimilarity(self, a, b):
        aSimilarToB = self.similarityOfTwoElements(a, b)
        aPrimSimilarToBPrim = self.similarityOfTwoElements(1 - a, 1 - b)
        return 0.5 * (aSimilarToB + aPrimSimilarToBPrim)

class ImplicationSimilarityCalculator(AbstractSimilarityCalculator):

    def __init__(self):
        super(ImplicationSimilarityCalculator, self).__init__()
        self.implicationFactory = ImplicationFactory()
        self.aggregatorFactory = AggregatorFactory()
        self.tNormFactory = TnormFactory()

    def calculateSimilarity(self, A, B, configuration):
        """Calculates similarity of two sets using implication.
        Configuration must contain:
            implication: name of the implication operation
            evaluator: name of the function that will be used to evaluate set that will be created by calculating 
            implication between elements of set A and B into one value"""

        fuzzyA = FuzzySet(A)
        fuzzyB = FuzzySet(B)
        implication = self.getImplication(configuration)
        tNorm = self.getTNorm(configuration)
        elementsSimilarityCalculator = ElementsSimilarityByImplicationCalculator(implication, tNorm)

        transformedFuzzySet = fuzzyA.binaryOperation(fuzzyB, elementsSimilarityCalculator.generalSimilarity)

        aggregator = self.getAggregator(configuration)

        similarity = transformedFuzzySet.accumulate(lambda x: x, aggregator.aggregate)
        return similarity

    def getImplication(self, configuration):
        implicationName = configuration[paramNames.IMPLICATION]
        return self.implicationFactory.getImplication(implicationName)

    def getAggregator(self, configuration):
        aggregatorName = configuration[paramNames.AGGREGATOR]
        return self.aggregatorFactory.getAggregator(aggregatorName)

    def getTNorm(self, configuration):
        tNormName = configuration[paramNames.TNORM]
        return self.tNormFactory.getTNorm(tNormName)