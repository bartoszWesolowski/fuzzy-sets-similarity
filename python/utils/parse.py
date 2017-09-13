import paramethers as param
import constants as const
import fuzzysetevaluator
def parseToIntOrRaiseAttributeError(value, errorMessage="Could not parse value to int."):
    """Returns value parsed to int or raises an AttributeError with error message."""
    try:
        return int(value)
    except ValueError:
        raise AttributeError(errorMessage)


def minkowskiConfigParser(config):
    print "Parsing config for minkowski"
    if param.R not in config.keys():
        raise AttributeError("Missing " + param.R + " parameter for minkowski method")

    rawR = config[param.R]
    r = parseToIntOrRaiseAttributeError(config[param.R],
                                        "Wrong parameter {} = {} for minkowski method".format(param.R, rawR))
    return {
        param.R: r,
        const.METHOD_PARAM_NAME: const.MINKOWSKI
    }


def angularDistanceConfigParser(config):
    print "Parsing config for angular_distance"
    return {
        const.METHOD_PARAM_NAME: const.ANGULAR_DISTANCE
    }


JACCARD_PARAMS = [param.ALPHA, param.BETA, param.GAMMA, param.EVALUATOR]
def jaccardIndexConfigParser(config):
    print "Parsing config for jaccard_index"
    for parameter in JACCARD_PARAMS:
        if parameter not in config.keys():
            raise AttributeError("Missing {} parameter for jaccards method. Required params: {}".format(parameter, JACCARD_PARAMS))

    alpha = parseToIntOrRaiseAttributeError(config[param.ALPHA], "Can parse alpha paramether {}".format(config[param.ALPHA]))
    beta = parseToIntOrRaiseAttributeError(config[param.BETA], "Can parse beta paramether {}".format(config[param.BETA]))
    gamma = parseToIntOrRaiseAttributeError(config[param.GAMMA], "Can parse alpha paramether {}".format(config[param.GAMMA]))
    evaluator = config[param.EVALUATOR]
    if evaluator not in fuzzysetevaluator.SUPPORTED_EVALUATORS:
        raise AttributeError(
            "Not supported evaluator found: {}. Supported evaluators: {}".format(evaluator, fuzzysetevaluator.SUPPORTED_EVALUATORS))

    return {
        const.METHOD_PARAM_NAME: const.JACCARD_INDEX,
        param.ALPHA: alpha,
        param.BETA : beta,
        param.GAMMA: gamma,
        param.EVALUATOR: evaluator
    }


"""Map where key is a name of a fuzzy similarity calculation method
and a value is a function that parses a raw parameter map to map with required types.
Parsing method performs validation.
"""
CONFIG_PARSERS = {
    const.MINKOWSKI: minkowskiConfigParser,
    const.ANGULAR_DISTANCE: angularDistanceConfigParser,
    const.JACCARD_INDEX: jaccardIndexConfigParser
}