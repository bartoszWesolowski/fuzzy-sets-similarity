from utils import constants
from utils import parse
CONFIG_METADATA_PARAM_NAME = 'config'

def calculateSimilarity(A, B, config):
    """Calculates similarity of two sets A and B using method declared in config map.
    Config map must contain all parameters used to calculate similarity"""
    validateConfigMethod(config)
    method = config[constants.METHOD_PARAM_NAME]
    configParser = parse.CONFIG_PARSERS[method]
    parsedConfig = configParser(config)
    calculator = constants.SIMILARITY_METHODS_MAP[method]
    result = calculator(A, B, parsedConfig)
    return result

def validateConfigMethod(config):
    methodKey = constants.METHOD_PARAM_NAME
    if methodKey not in config.keys():
        raise AttributeError(
            "Config {} is missing {} key with value equal to one of the following: ".format(config, methodKey,
                                                                                            constants.IMPLEMENTED_METHODS))
    elif config[methodKey] not in constants.IMPLEMENTED_METHODS:
        raise AttributeError(
            "Unrecognized method: {} . List of supported methods: {}".format(config[methodKey],
                                                                             constants.IMPLEMENTED_METHODS))

