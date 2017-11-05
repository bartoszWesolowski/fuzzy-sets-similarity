from parsers.parser_factory import ConfigurationParserFactory
from utils import constants


class ConfigurationParser(object):
    """
    Object used for validating and parsing raw config to a config object understandable by similarity calculators
    """
    configParserFactory = ConfigurationParserFactory()
    methodKey = constants.METHOD_PARAM_NAME

    def validateAndParse(self, rawConfig):
        """Validates and parsers raw config map to map understandable by similarity calculator"""

        method = ConfigurationParser.getConfigMethodOrThrowErrorIfNotExisting(rawConfig)
        configParser = self.configParserFactory.getParser(method)
        parsedConfig = configParser.parse(rawConfig)

        return parsedConfig

    def getConfigMethodOrThrowErrorIfNotExisting(self, rawConfig):

        self.ensureMethodKeyIsPresent(self.methodKey, rawConfig)
        self.ensureConfigMethodIsSupported(self.methodKey, rawConfig)

        return rawConfig[self.methodKey]

    def ensureConfigMethodIsSupported(self, rawConfig):
        if rawConfig[self.methodKey] not in self.configParserFactory.getSupportedMethods():
            raise AttributeError(
                "Unrecognized method: {} found while parsing configuration object. List of supported methods: {}".format(
                    rawConfig[self.methodKey],
                    self.configParserFactory.getSupportedMethods()))

    def ensureMethodKeyIsPresent(self, rawConfig):
        if self.methodKey not in rawConfig.keys():
            raise AttributeError(
                "Config {} is missing {} key with value equal to one of the following: ".format(
                    rawConfig, self.methodKey, self.configParserFactory.getSupportedMethods()
                )
            )
