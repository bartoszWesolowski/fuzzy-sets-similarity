from parsers.raw_configuration_parser import ConfigurationParser
from utils import constants
from simcalculators.similarity_calculator_factory import SimilarityCalculatorFactory

configurationParser = ConfigurationParser()

similarityCalculatorFactory = SimilarityCalculatorFactory()

def calculateSimilarityFromRawConfig(A, B, rawConfig):
    """Calculates similarity of two sets A and B using method declared in config map.
    Config map must contain all parameters used to calculate similarity, this map can be a simple string-string map,
    that will be parsed to desired format"""
    parsedConfig = configurationParser.validateAndParse(rawConfig)
    method = parsedConfig[constants.METHOD_PARAM_NAME]
    calculator = similarityCalculatorFactory.getSimilarityCalculator(method)
    result = calculator.calculateSimilarity(A, B, parsedConfig)
    return result


def calculateSimilarityFromParsedConfig(A, B, parsedConfig):
    """Calculates similarity of two sets A and B using method declared in config map.
    Config map must contain all parameters used to calculate similarity, has to be passed in format required
    by similarity calculator"""
    method = parsedConfig[constants.METHOD_PARAM_NAME]
    calculator = similarityCalculatorFactory.getSimilarityCalculator(method)
    result = calculator.calculateSimilarity(A, B, parsedConfig)
    return result
