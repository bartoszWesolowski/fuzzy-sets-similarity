from parsers.raw_configuration_parser import ConfigurationParser
from similarity_calculator_factory import SimilarityCalculatorFactory
from utils import constants


class SimilarityCalculator(object):

    configurationParser = ConfigurationParser()

    similarityCalculatorFactory = SimilarityCalculatorFactory()

    def calculateSimilarityFromRawConfig(self, A, B, rawConfig):
        """Calculates similarity of two sets A and B using method declared in config map.
        Config map must contain all parameters used to calculate similarity, this map can be a simple string-string map,
        that will be parsed to desired format"""
        parsedConfig = self.configurationParser.validateAndParse(rawConfig)
        calculator = self.getSimilarityCalculator(parsedConfig)
        result = calculator.calculateSimilarity(A, B, parsedConfig)
        return result

    def calculateSimilarityFromParsedConfig(self, A, B, parsedConfig):
        """Calculates similarity of two sets A and B using method declared in config map.
        Config map must contain all parameters used to calculate similarity, has to be passed in format required
        by similarity calculator"""
        calculator = self.getSimilarityCalculator(parsedConfig)
        result = calculator.calculateSimilarity(A, B, parsedConfig)
        return result

    def getSimilarityCalculator(self, parsedConfig):
        method = parsedConfig[constants.METHOD_PARAM_NAME]
        calculator = self.similarityCalculatorFactory.getSimilarityCalculator(method)
        return calculator
