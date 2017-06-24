from utils import constants as c
from utils import mathutils

class SimilarityRequest:
    setA = []
    setB = []
    method = ""
    config = {}

    def __init__(self, requestParametersDict):
        """Constructor: get dictionary as a input parameter
        Dictionary required fields:
            'method' - method used to calculate similarity, determinate what properties need to be added in config. 
            'setA' - string representing array of floating point numbers, for example [1, 0.1]
            'setB' - same as setA
            'config' - map containing key value pairs that will represent config object used to calculate similarity
        """
        self.setA = mathutils.clamp(requestParametersDict[c.SET_A_REQUEST_PARAMETER_NAME])
        self.setB = mathutils.clamp(requestParametersDict[c.SET_B_REQUEST_PARAMETER_NAME])
        self.method = requestParametersDict[c.METHOD_REQUEST_PARAMETER_NAME]
        self.config = requestParametersDict[c.CONFIG_REQUEST_PARAMETER_NAME]

    def getCalculationMethod(self):
        return c.SIMILARITY_METHODS_MAP[self.method]

    def calculate(self):
        calculationMethod = self.getCalculationMethod()
        return calculationMethod(self.setA, self.setB, self.config)
