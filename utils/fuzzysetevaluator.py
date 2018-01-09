import numpy

SUPREMUM = "sup"

#Ewaluatory skalarne zbioru rozmytego
def sup(fuzzySet):
    return numpy.clip(max(fuzzySet.elements), 0, 1)

SUPPORTED_EVALUATORS = [SUPREMUM]

EVALUATORS = {
    SUPREMUM: sup
}

def getEvaluator(name):
    if name not in SUPPORTED_EVALUATORS:
        raise AttributeError("Unknown evaluator name. Cant find evaluator for name: {}".format(name))

    return EVALUATORS[name]