import abc as abstract
from utils import constants as const


class AngularDistanceConfigParser(abstract.AbstractConfigurationParser):
    def parse(self, rawConfigMap):
        print "Parsing config for angular_distance"
        return {
            const.METHOD_PARAM_NAME: const.ANGULAR_DISTANCE
        }
