from utils import constants as const
from minkowski_configuration_parser import MinkowskiConfigParser
from jaccard_configuration_parser import JaccardConfigParser
from angular_distance_configuration_parser import AngularDistanceConfigParser


class ConfigurationParserFactory(object):
    """Map where key is a name of a fuzzy similarity calculation method
    and a value is a function that parses a raw parameter map to map with required types.
    Parsing method performs validation.
    """
    CONFIG_PARSERS = {
        const.MINKOWSKI: MinkowskiConfigParser(),
        const.ANGULAR_DISTANCE: AngularDistanceConfigParser(),
        const.JACCARD_INDEX: JaccardConfigParser()
    }

    def getParser(self, methodName):
        keys = self.CONFIG_PARSERS.keys()
        if methodName not in keys:
            raise AttributeError(
                "Trying to get configuration parser for unsupported method {}. Allowed methods {}".format(methodName,
                                                                                                          keys))
        return self.CONFIG_PARSERS[methodName]

    def getSupportedMethods(self):
        return self.CONFIG_PARSERS.keys()
