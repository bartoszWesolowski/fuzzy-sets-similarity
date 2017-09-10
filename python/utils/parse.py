import paramethers as param
import constants as const

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


def jaccardIndexConfigParser(config):
    print "Parsing config for jaccard_index"


"""Map where key is a name of a fuzzy similarity calculation method
and a value is a function that parses a raw parameter map to map with required types.
Parsing method performs validation.
"""
CONFIG_PARSERS = {
    const.MINKOWSKI: minkowskiConfigParser,
    const.ANGULAR_DISTANCE: angularDistanceConfigParser,
    const.JACCARD_INDEX: jaccardIndexConfigParser
}