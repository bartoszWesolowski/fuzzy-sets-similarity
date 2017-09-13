import numpy

SUPREMUM = "sup"

#Ewaluatory skalarne zbioru rozmytego
def sup(fuzzySet):
    return numpy.clip(max(fuzzySet.elements), 0, 1)

SUPPORTED_EVALUATORS = [SUPREMUM]
EVALUATORS = {
    SUPREMUM: sup
}