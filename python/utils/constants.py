from minkowski import minkowskisimilarity as minSim
from angle import angluardistance
from jaccard import jaccard

METHOD_PARAM_NAME = 'method'

MINKOWSKI = "minkowski"

ANGULAR_DISTANCE = "angular_distance"

JACCARD_INDEX = "jaccard_index"

"""List of implemented similarity calculation methods"""
IMPLEMENTED_METHODS = [MINKOWSKI, ANGULAR_DISTANCE, JACCARD_INDEX]

"""Methods map"""
SIMILARITY_METHODS_MAP = {
    MINKOWSKI: minSim.generalSim,
    ANGULAR_DISTANCE: angluardistance.sim,
    JACCARD_INDEX: jaccard.sim
}

"""Request parameters names"""
SET_A_REQUEST_PARAMETER_NAME = 'setA'
SET_B_REQUEST_PARAMETER_NAME = 'setB'
METHOD_REQUEST_PARAMETER_NAME = METHOD_PARAM_NAME
CONFIG_REQUEST_PARAMETER_NAME = 'config'
RESULT_REQUEST_PARAMETER_NAME = 'result'
