from utils import constants as c
from utils import mathutils
from utils.mapvalidator import MapValidator

from fuzzyfacades.similarity_calculator_wrapper import SimilarityCalculatorFacade

class SimilarityRequest:
    setA = []
    setB = []
    method = ""
    rawConfig = {}

    similarityCalculatorWrapper = SimilarityCalculatorFacade()

    requiredParameters = [c.SET_A_REQUEST_PARAMETER_NAME, c.SET_B_REQUEST_PARAMETER_NAME, c.METHOD_REQUEST_PARAMETER_NAME]

    def __init__(self, requestParametersDict):
        """Constructor: get dictionary as a input parameter
        Dictionary required fields:
            'method' - method used to calculate similarity, determinate what properties need to be added in config. 
            'setA' - string representing array of floating point numbers, for example [1, 0.1]
            'setB' - same as setA
            'rawConfig' - String:String map representing config parsed form json
        """

        #TODO: could also introduce some type validation in the future
        MapValidator.validateRequiredParametersExistence(requestParametersDict, self.requiredParameters)

        self.setA = mathutils.clamp(requestParametersDict[c.SET_A_REQUEST_PARAMETER_NAME])
        self.setB = mathutils.clamp(requestParametersDict[c.SET_B_REQUEST_PARAMETER_NAME])
        self.rawConfig = requestParametersDict
        self.method = requestParametersDict[c.METHOD_PARAM_NAME]

    def calculate(self):
        return self.similarityCalculatorWrapper.calculateSimilarityFromRawConfig(self.setA, self.setB, self.rawConfig)
