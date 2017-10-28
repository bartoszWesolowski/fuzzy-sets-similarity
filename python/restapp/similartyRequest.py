from utils import constants as c
from utils import mathutils
from utils import simCalculator


class SimilarityRequest:
    setA = []
    setB = []
    method = ""
    rawConfig = {}

    def __init__(self, requestParametersDict):
        """Constructor: get dictionary as a input parameter
        Dictionary required fields:
            'method' - method used to calculate similarity, determinate what properties need to be added in config. 
            'setA' - string representing array of floating point numbers, for example [1, 0.1]
            'setB' - same as setA
            'rawConfig' - String:String map representing config parsed form json
        """
        self.setA = mathutils.clamp(requestParametersDict[c.SET_A_REQUEST_PARAMETER_NAME])
        self.setB = mathutils.clamp(requestParametersDict[c.SET_B_REQUEST_PARAMETER_NAME])
        self.method = requestParametersDict[c.METHOD_REQUEST_PARAMETER_NAME]
        self.rawConfig = requestParametersDict[c.CONFIG_REQUEST_PARAMETER_NAME]
        self.rawConfig[c.METHOD_PARAM_NAME] = self.method

    def calculate(self):
        return simCalculator.calculateSimilarityFromRawConfig(self.setA, self.setB, self.rawConfig)
