import numpy


def createMatrix(width, height):
    return numpy.zeros((width, height))


class SetsComparisonResult(object):
    """Object representing result of comparison of list of sets everyone with everyone. 
    Wraps matrix NxN with similarities between tests"""
    def __init__(self, listOfSets, otherListOfSets, config, resultArray, resultsMatrix):
        self.listOfSets = listOfSets
        self.otherListOfSets = otherListOfSets
        self.config = config
        self.resultArray = resultArray
        self.resultMatrix = resultsMatrix

    def __str__(self):
        return str(self.resultMatrix)


class SetsComparisonResultBuilder(object):
    def __init__(self, listOfSets, otherListOfSets):
        self.listOfSets = listOfSets
        self.otherListOfSets = otherListOfSets
        self.numberOfSets = len(listOfSets)
        self.resultArray = []
        self.results = createMatrix(self.numberOfSets, len(self.otherListOfSets))

    def withConfig(self, configuration):
        self.configuration = configuration
        return self

    def withResultEntry(self, resultCoordinates, result):
        self.results[resultCoordinates[0]][resultCoordinates[1]] = result
        self.results[resultCoordinates[1]][resultCoordinates[0]] = result
        self.resultArray.append(result)

    def build(self):
        return SetsComparisonResult(self.listOfSets, self.otherListOfSets, self.configuration, self.resultArray, self.results)
