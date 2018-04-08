import numpy


def createMatrix(numberOfSets):
    return numpy.zeros((numberOfSets, numberOfSets))


class SetsComparisonResult(object):
    """Object representing result of comparison of list of sets everyone with everyone"""
    def __init__(self, listOfSets, config, resultsMatrix):
        self.listOfSets = listOfSets
        self.numberOfSets = len(listOfSets)
        self.config = config
        self.resultMatrix = resultsMatrix


class SetsComparisonResultBuilder(object):
    def __init__(self, listOfSets):
        self.listOfSets = listOfSets
        self.numberOfSets = len(listOfSets)
        self.results = createMatrix(self.numberOfSets)

    def withConfig(self, configuration):
        self.configuration = configuration
        return self

    def withResultEntry(self, resultCoordinates, result):
        self.results[resultCoordinates[0]][resultCoordinates[1]] = result

    def build(self):
        return SetsComparisonResult(self.listOfSets, self.configuration, self.results)
