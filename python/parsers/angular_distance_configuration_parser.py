from abstract_configuration_parser import AbstractConfigurationParser
from utils import constants as const


class AngularDistanceConfigParser(AbstractConfigurationParser):
    def parse(self, rawConfigMap):
        print "Parsing config for angular_distance"
        return {
            const.METHOD_PARAM_NAME: const.ANGULAR_DISTANCE
        }
