import numpy
#Ewaluatory skalarne zbioru rozmytego
def sup(fuzzySet):
    return numpy.clip(max(fuzzySet.elements), 0, 1)