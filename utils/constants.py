METHOD_PARAM_NAME = 'method'

MINKOWSKI = "minkowski"

ANGULAR_DISTANCE = "angular-distance"

JACCARD_INDEX = "jaccard-index"

SIMPLIFIED_JACCARD_INDEX = "simplified-jaccard-index"

IMPLICATION_SIMILARITY = 'implication-similarity'

"""List of implemented similarity calculation methods"""
IMPLEMENTED_METHODS = [MINKOWSKI, ANGULAR_DISTANCE, JACCARD_INDEX, IMPLICATION_SIMILARITY]

"""Request parameters names"""
SET_A_REQUEST_PARAMETER_NAME = 'setA'
SET_B_REQUEST_PARAMETER_NAME = 'setB'
METHOD_REQUEST_PARAMETER_NAME = METHOD_PARAM_NAME
CONFIG_REQUEST_PARAMETER_NAME = 'config'
RESULT_REQUEST_PARAMETER_NAME = 'result'

TNORM_MINIMUM = 'minimum'
TNORM_ALGEBRAIC = 'algebraic'
TNORM_LUKASIEWICZ = 'lukasiewicz'

TKONORM_MAXIMUM = 'maxiumum'
TKONORM_LUKASIEWICZ = 'lukasiewicz'
TKONORM_PROBABILISTIC = 'probabilistic'


AGGREGATOR_AVERAGE = 'average'
AGGREGATOR_MINIMUM = 'minimum'
AGGREGATOR_MAXIMUM = 'maximum'

