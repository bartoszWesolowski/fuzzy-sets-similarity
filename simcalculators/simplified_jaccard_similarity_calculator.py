from abstract_similarity_calculator import AbstractSimilarityCalculator
from utils.fuzzyset import FuzzySet
from implications.implication_factory import ImplicationFactory
from aggregators.aggregators_factory import AggregatorFactory
from tnorms.t_norm_factory import TnormFactory
from tkonorms.t_konorm_factory import TkonormFactory
from utils import configuration_parameters_names as paramNames
from utils import paramethers as params

class SimplifiedJaccardSimilarityCalculator(AbstractSimilarityCalculator):


    def __init__(self):
        self.implicationFactory = ImplicationFactory()
        self.aggregatorFactory = AggregatorFactory()
        self.tNormFactory = TnormFactory()
        self.tkonormFactory = TkonormFactory()

    # TODO: fix this formula!
    def calculateSimilarity(self, A, B, config):
        """Jaccard similarity index"""

        fuzzyA = FuzzySet(A)
        fuzzyB = FuzzySet(B)
        aggregator = self.getAggregator(config)
        tnorm = self.getTNorm(config)
        tkonorm = self.getTkonorm(config)

        intersect = fuzzyA.intersect(fuzzyB, tKonorm=tkonorm.tkonormValue)
        sum = fuzzyB.sum(fuzzyB, tNorm=tnorm.tnormValue)

        aggregatedSum = aggregator.aggregate(sum().elements)
        aggregatedIntersection = aggregator.aggregate(intersect.elements)
        if aggregatedSum == 0:
            return 0

        return aggregatedIntersection / float(aggregatedSum)

    def getAggregator(self, configuration):
        aggregatorName = configuration[paramNames.AGGREGATOR]
        return self.aggregatorFactory.getAggregator(aggregatorName)

    def getTNorm(self, configuration):
        tNormName = configuration[paramNames.TNORM]
        return self.tNormFactory.getTNorm(tNormName)

    def getTkonorm(self, configuration):
        konorm = configuration[paramNames.TKNORM]
        return self.tkonormFactory.getTkonorm(konorm)

