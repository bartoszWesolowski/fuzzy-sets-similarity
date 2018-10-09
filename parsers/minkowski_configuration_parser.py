import abstract_configuration_parser
from utils import constants as const
from utils import paramethers as param


class MinkowskiConfigParser(abstract_configuration_parser.AbstractConfigurationParser):
    def parse(self, rawConfigMap):
        print "Parsing config for minkowski"
        if param.R not in rawConfigMap.keys():
            raise AttributeError("Missing " + param.R + " parameter for minkowski method")

        rawR = rawConfigMap[param.R]
        r = self.parseToIntOrRaiseAttributeError(rawConfigMap[param.R],
                                                 "Wrong parameter {} = {} for minkowski method. Expected number and got: {}".format(param.R, rawR, type(rawR)))
        if r <= 0:
            raise AttributeError("Minkowski R parameter must be greater than 0.")

        return {
            param.R: r,
            const.METHOD_PARAM_NAME: const.MINKOWSKI
        }
