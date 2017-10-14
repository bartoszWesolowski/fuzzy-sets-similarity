from utils import constants
from utils import parse

CONFIG_METADATA_PARAM_NAME = 'config'


def validateAndParse(rawConfig):
    """Validates and parsers raw config map to map understandable by similarity calculator"""
    validateConfigMethod(rawConfig)
    method = rawConfig[constants.METHOD_PARAM_NAME]
    configParser = parse.CONFIG_PARSERS[method]
    parsedConfig = configParser(rawConfig)
    return parsedConfig


def validateConfigMethod(config):
    methodKey = constants.METHOD_PARAM_NAME
    if methodKey not in config.keys():
        raise AttributeError(
            "Config {} is missing {} key with value equal to one of the following: ".format(config, methodKey,
                                                                                            constants.IMPLEMENTED_METHODS))
    elif config[methodKey] not in constants.IMPLEMENTED_METHODS:
        raise AttributeError(
            "Unrecognized method: {} found while parsing configuration object. List of supported methods: {}".format(config[methodKey],
                                                                             constants.IMPLEMENTED_METHODS))
