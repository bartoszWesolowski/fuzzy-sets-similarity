from utils import constants
from similarity_calculator_facade import SimilarityFacade


class ConfigurationParser(object):
    """
    Object used for validating and parsing raw config to a config object understandable by similarity calculators
    """
    similarityFacade = SimilarityFacade()
    methodKey = constants.METHOD_PARAM_NAME

    def validateAndParse(self, rawConfig):
        """Validates and parsers raw config map to map understandable by similarity calculator"""

        method = self.getConfigMethodOrThrowErrorIfNotExisting(rawConfig)
        configParser = self.similarityFacade.getParser(method)
        parsedConfig = configParser.parse(rawConfig)

        return parsedConfig

    def getConfigMethodOrThrowErrorIfNotExisting(self, rawConfig):

        self.ensureMethodKeyIsPresent(rawConfig)
        self.ensureConfigMethodIsSupported(rawConfig)

        return rawConfig[self.methodKey]

    def ensureConfigMethodIsSupported(self, rawConfig):
        if rawConfig[self.methodKey] not in self.similarityFacade.getSupportedMethods():
            raise AttributeError(
                "Unrecognized method: {} found while parsing configuration object. List of supported methods: {}".format(
                    rawConfig[self.methodKey],
                    self.similarityFacade.getSupportedMethods()))

    def ensureMethodKeyIsPresent(self, rawConfig):
        if self.methodKey not in rawConfig.keys():
            raise AttributeError(
                "Config {} is missing '{}' key with value equal to one of the following: {}".format(
                    rawConfig, self.methodKey, self.similarityFacade.getSupportedMethods()
                )
            )
