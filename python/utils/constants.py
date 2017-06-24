from minkowski import minkowskisimilarity as minSim

MINKOWSKI = "minkowski"

"""List of implemented similarity calculation methods"""
IMPLEMENTED_METHODS = [MINKOWSKI]


"""Methods map"""
SIMILARITY_METHODS_MAP = {
    MINKOWSKI: minSim.generalSim
}

"""Request parameters names"""
SET_A_REQUEST_PARAMETER_NAME = 'setA'
SET_B_REQUEST_PARAMETER_NAME = 'setB'
METHOD_REQUEST_PARAMETER_NAME = 'method'
CONFIG_REQUEST_PARAMETER_NAME = 'config'
RESULT_REQUEST_PARAMETER_NAME = 'result'
