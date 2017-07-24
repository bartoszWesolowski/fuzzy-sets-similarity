from utils import constants
from utils import fuzzysetevaluator

def extractConfig(method, configSet):
    if method == constants.MINKOWSKI:
        return configSet
    if method == constants.ANGULAR_DISTANCE:
        return {}
    if method == constants.JACCARD_INDEX:
        return {
            'alpha': configSet['alpha'],
            'beta': configSet['beta'],
            'gamma': configSet['gamma'],
            'evaluator': fuzzysetevaluator.sup
        }
