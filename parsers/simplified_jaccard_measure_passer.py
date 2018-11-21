from abstract_configuration_parser import AbstractConfigurationParser
from aggregators.aggregators_factory import AggregatorFactory
from tkonorms.t_konorm_factory import TkonormFactory
from tnorms.t_norm_factory import TnormFactory
from utils import configuration_parameters_names as params


class SimplifiedJaccardConfigurationParser(AbstractConfigurationParser):
    requiredParameters = [params.AGGREGATOR, params.TKNORM, params.TNORM]

    def __init__(self):
        self.aggregatorFactory = AggregatorFactory()
        self.tNormFactory = TnormFactory()
        self.tkoNormFactory = TkonormFactory()

    def parse(self, rawConfigMap):
        self.validateRequiredParametersExistence(rawConfigMap)
        self.validateThatAggregatorIsSupported(rawConfigMap[params.AGGREGATOR])
        self.validateThatTNormIsSupported(rawConfigMap[params.TNORM])
        self.validateThatTkoNormIsSupported(rawConfigMap[params.TKNORM])
        return rawConfigMap

    def validateRequiredParametersExistence(self, rawConfigMap):
        for param in self.requiredParameters:
            if param not in rawConfigMap.keys():
                raise AttributeError(
                    "Missing '{}' parameter in implication configuration. All required parameters: {}".format(
                        param, self.requiredParameters
                    ))

    def validateThatAggregatorIsSupported(self, aggregatorName):
        if not self.aggregatorFactory.isAggregatorSupported(aggregatorName):
            raise AttributeError(
                "Not supported aggregator found: {} while parsing configuration for implication similarity calculator"
                " List of supported aggregators: {}".format(
                    aggregatorName, self.aggregatorFactory.getSupportedAggregators()
                )
            )

    def validateThatTNormIsSupported(self, tNormName):
        if not self.tNormFactory.isTnormSupported(tNormName):
            raise AttributeError(
                "Found T-norm name that is not supported: {}  while parsing configuration for implication similarity calculator."
                "List of supported t-norms: {}".format(
                    tNormName, self.tNormFactory.getSupportedTNorms()
                )
            )

    def validateThatTkoNormIsSupported(self, tkoNormName):
        if not self.tNormFactory.isTnormSupported(tkoNormName):
            raise AttributeError(
                "Found T-norm name that is not supported: {}  while parsing configuration for implication similarity calculator."
                "List of supported t-norms: {}".format(
                    tkoNormName, self.tkoNormFactory.getSupportedTkonorms()
                )
            )
