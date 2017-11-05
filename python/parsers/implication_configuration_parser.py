from abstract_configuration_parser import AbstractConfigurationParser
from utils import constants as const
from utils import configuration_parameters_names as params
from implications.implication_factory import ImplicationFactory
from aggregators.aggregators_factory import AggregatorFactory
from tnorms.t_norm_factory import TnormFactory


class ImplicationConfigurationParser(AbstractConfigurationParser):
    requiredParameters = [params.AGGREGATOR, params.IMPLICATION, params.TNORM]

    def __init__(self):
        self.implicationFactory = ImplicationFactory()
        self.aggregatorFactory = AggregatorFactory()
        self.tNormFactory = TnormFactory()

    def parse(self, rawConfigMap):
        self.validateRequiredParametersExistence(rawConfigMap)
        self.validateThatImplicationIsSupported(rawConfigMap[params.IMPLICATION])
        self.validateThatAggregatorIsSupported(rawConfigMap[params.AGGREGATOR])
        self.validateThatTNormIsSupported(rawConfigMap[params.AGGREGATOR])
        return rawConfigMap

    def validateRequiredParametersExistence(self, rawConfigMap):
        for param in self.requiredParameters:
            if param not in rawConfigMap.keys():
                raise AttributeError(
                    "Missing {} parameter in implication configuration. All required parameters: ".format(
                        param, self.requiredParameters
                    ))

    def validateThatImplicationIsSupported(self, implicationName):
        if not self.implicationFactory.isSupported(implicationName):
            raise AttributeError(
                "Not supported implication: {} found while parsing configuration for implication similarity calculator."
                " List of supported implications: {}.".format(
                    implicationName, self.implicationFactory.getSupportedImplications()
                )
            )

    def validateThatAggregatorIsSupported(self, aggregatorName):
        if not self.aggregatorFactory.isAggregatorSupported(aggregatorName):
            raise AttributeError(
                "Not supported aggregator found: {}. List of supported aggregators: {}".format(
                    aggregatorName, self.aggregatorFactory.supportedAggregators()
                )
            )

    def validateThatTNormIsSupported(self, tNormName):
        if not self.tNormFactory.isTnormSupported(tNormName):
            raise AttributeError(
                "T-norm name not supported: {}. List of supported t-norms: {}".format(
                    tNormName, self.tNormFactory.getSupportedTNorms()
                )
            )
