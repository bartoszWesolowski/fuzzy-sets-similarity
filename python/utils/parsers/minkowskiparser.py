import abstractparser
from utils import paramethers as param
from utils import constants as const


class MinkowskiConfigParser(abstractparser.AbstractConfigurationParser):
    def parse(self, rawConfigMap):
        print "Parsing config for minkowski"
        if param.R not in rawConfigMap.keys():
            raise AttributeError("Missing " + param.R + " parameter for minkowski method")

        rawR = rawConfigMap[param.R]
        r = self.parseToIntOrRaiseAttributeError(rawConfigMap[param.R],
                                                 "Wrong parameter {} = {} for minkowski method".format(param.R, rawR))
        return {
            param.R: r,
            const.METHOD_PARAM_NAME: const.MINKOWSKI
        }
