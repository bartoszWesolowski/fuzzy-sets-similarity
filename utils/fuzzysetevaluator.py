import numpy

SUPREMUM = "sup"

AVERAGE = "average"


class FuzzyEvaluator(object):
    def __init__(self, universe):
        """

        :param universe: list representing all elements in U
        """
        self.universe = universe

    def evaluate(self, fuzzySet):
        raise "Not implemented"

    def getName(self):
        raise "Not implemented"


class AverageEvaluator(FuzzyEvaluator):
    def evaluate(self, fuzzySet):
        """
        :param fuzzySet: 
        :param universe: list containing all elements in universe, size of that list represent number of elements in U
        :return: 
        """
        if len(self.universe) == 0:
            raise AttributeError("Universe can not be empty.")

        fuzzySum = sum(fuzzySet.elements)
        return fuzzySum / float(len(self.universe))

    def getName(self):
        return AVERAGE


class SupremumEvaluator(FuzzyEvaluator):
    def evaluate(self, fuzzySet):
        return numpy.clip(max(fuzzySet.elements), 0, 1)

    def getName(self):
        return SUPREMUM


# Ewaluatory skalarne zbioru rozmytego
def sup(fuzzySet, universum):
    """
    
    :param fuzzySet: 
    :param universum: list containing all elements in uniwersum, size of that list represent number of elements in U
    :return: 
    """
    return numpy.clip(max(fuzzySet.elements), 0, 1)


def average(fuzzySet, universe):
    """
    :param fuzzySet: 
    :param universe: list containing all elements in universe, size of that list represent number of elements in U
    :return: 
    """
    if len(universe) == 0:
        raise AttributeError("Universe can not be empty.")

    fuzzySum = sum(fuzzySet.elements)
    return fuzzySum / float(len(universe))


SUPPORTED_EVALUATORS = [SUPREMUM, AVERAGE]

EVALUATORS = {
    SUPREMUM: sup,
    AVERAGE: average
}


def getSupportedEvaluators():
    return SUPPORTED_EVALUATORS


def getEvaluator(name, universe):
    if name not in SUPPORTED_EVALUATORS:
        raise AttributeError("Unknown evaluator name. Cant find evaluator for name: {}".format(name))

    if name == SUPREMUM:
        return SupremumEvaluator(universe)

    if name == AVERAGE:
        return AverageEvaluator(universe)
