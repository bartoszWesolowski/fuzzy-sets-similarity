from utils import constants
from utils.parsers.parserFactory import ConfigurationParserFactory


class ConfigurationParser(object):
    """
    Object used for validating and parsing raw config to a config object understandable by similarity calculators
    """
    configParserFactory = ConfigurationParserFactory()

    def validateAndParse(self, rawConfig):
        """Validates and parsers raw config map to map understandable by similarity calculator"""

        method = self.getConfigMethodOrThrowErrorIfNotExisting(rawConfig)
        configParser = self.configParserFactory.getParser(method)
        parsedConfig = configParser.parse(rawConfig)

        return parsedConfig

    def getConfigMethodOrThrowErrorIfNotExisting(self, rawConfig):
        methodKey = constants.METHOD_PARAM_NAME

        self.ensureMethodKeyIsPresent(methodKey, rawConfig)
        self.ensureConfigMethodIsSupported(methodKey, rawConfig)

        return rawConfig[methodKey]

    @staticmethod
    def ensureConfigMethodIsSupported(methodKey, rawConfig):
        if rawConfig[methodKey] not in constants.IMPLEMENTED_METHODS:
            raise AttributeError(
                "Unrecognized method: {} found while parsing configuration object. List of supported methods: {}".format(
                    rawConfig[methodKey],
                    constants.IMPLEMENTED_METHODS))

    @staticmethod
    def ensureMethodKeyIsPresent(methodKey, rawConfig):
        if methodKey not in rawConfig.keys():
            raise AttributeError(
                "Config {} is missing {} key with value equal to one of the following: ".format(config, methodKey,
                                                                                                constants.IMPLEMENTED_METHODS))
