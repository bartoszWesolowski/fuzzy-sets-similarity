from sklearn import datasets

import os
import sys

sys.path.insert(0, os.path.abspath('..\..'))

from comparators.sets_comparator import SetsComparator
from simcalculators.minkowski_similarity_calculator import MinkowskiSimilarityCalculator


class IrisDataSet(object):
    def __init__(self, irisDataSet):
        self.irises = []
        for index, irisData in enumerate(irisDataSet.data):
            self.irises.append(Iris(irisData, irisDataSet.target[index]))

    def getSepalLenghts(self):
        return map(lambda i: i.sepalLen, self.irises)

    def getSepalWidths(self):
        return map(lambda i: i.sepalWidth, self.irises)

    def getPetalLengths(self):
        return map(lambda i: i.petalLen, self.irises)

    def getPetalWidths(self):
        return map(lambda i: i.petalWidth, self.irises)


class Iris(object):
    def __init__(self, data, irisType):
        self.data = data
        self.type = irisType
        self.sepalLen = data[0]  # 4.3 - 7.9
        self.sepalWidth = data[1]
        self.petalLen = data[2]
        self.petalWidth = data[3]


class AroundValueFuzzySet(object):
    """Triangular set representing 'around x'"""

    def __init__(self, range):
        """
        :param range: length of trieangular set base 
        """
        # type: (object) -> object
        self.range = range

    def valueFor(self, actualValue, possibleValue):
        a = actualValue - (self.range / 2.0)
        b = actualValue + (self.range / 2.0)
        if possibleValue == actualValue:
            return 1
        if a < possibleValue < actualValue:
            return (possibleValue - a) / float(actualValue - a)
        if actualValue < possibleValue < b:
            return (b - possibleValue) / float(b - actualValue)

        return 0


class PossibleAttributeValuesCalculator(object):
    def __init__(self, attributesList):
        self.attributesList = attributesList
        self.min = min(attributesList)
        self.max = max(attributesList)
        self.attributeRange = abs(self.min - self.max)
        extendRange = self.attributeRange / 2.0
        self.start = self.min - extendRange
        self.end = self.max + extendRange
        self.extendedAttributeRange = abs(self.min - self.max)
        # print "Attributes: \n\tMin: {},\n \tmax: {},\n \trange: {}".format(self.min, self.max, self.attributeRange)

    def getPossibleValues(self, numberOfPossibleValues):
        offset = abs(self.start - self.end) / float(numberOfPossibleValues - 1)

        possibleValues = []
        for n in range(numberOfPossibleValues):
            possibleValues.append(self.start + n * offset)

        # print "Possible values: {}".format(possibleValues)
        return possibleValues


class FuzzyIris(object):
    def __init__(self, sepalLen=[], sepalWidth=[], petalLen=[], petalWidth=[], irisType=0):
        """
        
        :param sepalLen: 
        :param sepalWidth: 
        :param petalLen: 
        :param petalWidth: 
        :param irisType: 
        """
        self.type = irisType
        self.sepalLen = sepalLen  # 4.3 - 7.9
        self.sepalWidth = sepalWidth
        self.petalLen = petalLen
        self.petalWidth = petalWidth

    def fuzzySetArray(self):
        allAttributes = []
        allAttributes.extend(self.sepalLen)
        allAttributes.extend(self.sepalWidth)
        allAttributes.extend(self.petalLen)
        allAttributes.extend(self.petalWidth)
        return allAttributes

    def toFuzzySetRow(self):
        allAttributes = self.fuzzySetArray()
        return map(lambda x: "{0:.4f}".format(x), allAttributes)


class IrisDataSetFuzyficator(object):
    def __init__(self, wrappedIrisDataSet, numberOfPossibleValuesForEachFeature=20,
                 rangeOfAroudValueFuzzySetScalar=1.0):
        self.numberOfPossibleValuesSamples = numberOfPossibleValuesForEachFeature

        print "Fuzzyficating sepal length attribute with number of samples per attribute {} and attribute range factor: {}".format(
           numberOfPossibleValuesForEachFeature, rangeOfAroudValueFuzzySetScalar)
        print "\nSepal length:\n"
        self.sepalLengthPossibleValueCalculator = PossibleAttributeValuesCalculator(
            wrappedIrisDataSet.getSepalLenghts())
        sepalLengthPossibleValues = self.sepalLengthPossibleValueCalculator.getPossibleValues(
            self.numberOfPossibleValuesSamples)
        aroundSepalTriangularBase = self.sepalLengthPossibleValueCalculator.attributeRange * rangeOfAroudValueFuzzySetScalar
        self.aroundSepalLengthFuzzySet = AroundValueFuzzySet(aroundSepalTriangularBase)
        self.printMetadata(self.sepalLengthPossibleValueCalculator)
        print "Universal: "
        print self.formatUniverse(sepalLengthPossibleValues)

        print "\nSepal width:\n"
        self.sepalWidthPossibleValueCalculator = PossibleAttributeValuesCalculator(wrappedIrisDataSet.getSepalWidths())
        aroundSepalWidthTriangularBase = self.sepalWidthPossibleValueCalculator.attributeRange * rangeOfAroudValueFuzzySetScalar
        sepalWidthPossibleValues = self.sepalWidthPossibleValueCalculator.getPossibleValues(
            self.numberOfPossibleValuesSamples)
        self.aroundSepalWidthFuzzySet = AroundValueFuzzySet(aroundSepalWidthTriangularBase)
        self.printMetadata(self.sepalWidthPossibleValueCalculator)
        print "Universal: "
        print self.formatUniverse(sepalWidthPossibleValues)

        print "\nPetal Length:\n"
        self.petalLenPossibleValueCalculator = PossibleAttributeValuesCalculator(wrappedIrisDataSet.getPetalLengths())
        petalLengthTriangularBase = self.petalLenPossibleValueCalculator.attributeRange * rangeOfAroudValueFuzzySetScalar
        petalLenPossibleValues = self.petalLenPossibleValueCalculator.getPossibleValues(
            self.numberOfPossibleValuesSamples)
        self.aroundPetalLenFuzzySet = AroundValueFuzzySet(petalLengthTriangularBase)
        self.printMetadata(self.petalLenPossibleValueCalculator)
        print "Universal: "
        print self.formatUniverse(petalLenPossibleValues)

        self.fuzzyfiedDataset = []
        for iris in wrappedIrisDataSet.irises:
            fuzzyficateSepalLength = self.fuzzyficateAttributeValue(iris.sepalLen, sepalLengthPossibleValues,
                                                                    self.aroundSepalLengthFuzzySet)

            fuzzyficateSepalWidth = self.fuzzyficateAttributeValue(iris.sepalWidth,
                                                                   sepalWidthPossibleValues,
                                                                   self.aroundSepalWidthFuzzySet)

            fuzzyficatePetalLen = self.fuzzyficateAttributeValue(iris.petalLen, petalLenPossibleValues,
                                                                 self.aroundPetalLenFuzzySet)

            self.fuzzyfiedDataset.append(
                FuzzyIris(sepalLen=fuzzyficateSepalLength, sepalWidth=fuzzyficateSepalWidth,
                          petalLen=[],
                          irisType=iris.type))

    def printMetadata(self, possibleValuesCalculator):
        print "Metadata: [{}, {}], range: {}".format(possibleValuesCalculator.min,
                                                     possibleValuesCalculator.max,
                                                     possibleValuesCalculator.attributeRange)

    def formatUniverse(self, universe):
        return map(lambda x: float("{0:.2f}".format(x)), universe)

    def fuzzyficateAttributeValue(self, attributeActualValue, attributePossibleValues, aroundValueFuzzySet):
        fuzzyficate = []
        for possibleValue in attributePossibleValues:
            fuzzyficate.append(aroundValueFuzzySet.valueFor(attributeActualValue, possibleValue))
        return fuzzyficate

    def toFuzzySetFileFormat(self):
        result = ""
        for fuzzyIris in self.fuzzyfiedDataset:
            result += " ".join(fuzzyIris.toFuzzySetRow())
            result += "\n"
        return result

    def getIrisesWithType(self, irisType):
        return filter(lambda iris: iris.type == irisType, self.fuzzyfiedDataset)


def getFuzzyficatedIrisDataSet(numberOfPossibleValuesForEachFeature=20,
                               rangeOfAroudValueFuzzySetScalar=1.0):
    """
    
    :return: IrisDataSetFuzyficator
    """
    rawIrisDataset = datasets.load_iris()
    irisDataset = IrisDataSet(rawIrisDataset)
    return IrisDataSetFuzyficator(irisDataset,
                                  numberOfPossibleValuesForEachFeature=numberOfPossibleValuesForEachFeature,
                                  rangeOfAroudValueFuzzySetScalar=rangeOfAroudValueFuzzySetScalar)


""" Copmaring set with set - probably will not be used
fuzzyficatedIrisDataSet = getFuzzyficatedIrisDataSet()

print fuzzyficatedIrisDataSet.toFuzzySetFileFormat()

minkowskiCalculator = MinkowskiSimilarityCalculator()
setsComparator = SetsComparator()


# comparing same types:
def compareIrisesWithComparionMethod(methodConfig):
    comparisonOfIrisesWithSameType = []
    comparisonOfIrisesWithDifferent = []
    print "###########################"
    print "Comparing irises for similarity method: {}".format(methodConfig)
    for firstIrisType in [0, 1, 2]:
        for secondIrisType in [0, 1, 2]:
            print "\n\n Compare irises with types: {} x {}".format(firstIrisType, secondIrisType)
            fuzzyIrisesWithFirstType = map(lambda fuzzyIris: fuzzyIris.fuzzySetArray(),
                                           fuzzyficatedIrisDataSet.getIrisesWithType(firstIrisType))
            fuzzyIrisesWithSecondType = map(lambda fuzzyIris: fuzzyIris.fuzzySetArray(),
                                            fuzzyficatedIrisDataSet.getIrisesWithType(secondIrisType))
            comparisonResult = setsComparator.compareTwoSets(fuzzyIrisesWithFirstType, fuzzyIrisesWithSecondType,
                                                             methodConfig)
            resultArray = comparisonResult.resultArray
            if firstIrisType == secondIrisType:
                comparisonOfIrisesWithSameType.extend(resultArray)
            else:
                comparisonOfIrisesWithDifferent.extend(resultArray)
            print "Max similarity: {}".format(max(resultArray))
            print "Average similarity: {}".format(sum(resultArray) / float(len(resultArray)))
            print "Min similarity: {}".format(min(resultArray))

    print "###########################"
    print "Summary:"
    print "\n\nGeneral summary for comparising sets of same types:"
    print "Max similarity: {}".format(max(comparisonOfIrisesWithSameType))
    print "Average similarity: {}".format(
        sum(comparisonOfIrisesWithSameType) / float(len(comparisonOfIrisesWithSameType)))
    print "Min similarity: {}".format(min(comparisonOfIrisesWithSameType))

    print "\n\nGeneral summary for comparising sets of different types:"
    print "Max similarity: {}".format(max(comparisonOfIrisesWithDifferent))
    print "Average similarity: {}".format(
        sum(comparisonOfIrisesWithDifferent) / float(len(comparisonOfIrisesWithDifferent)))
    print "Min similarity: {}".format(min(comparisonOfIrisesWithDifferent))


methods = [
    {"r": 1, "method": "minkowski"},
    {"r": 2, "method": "minkowski"},
    {"method": "angular-distance"},
    {
        "alpha": 1,
        "beta": 1,
        "evaluator": "average",
        "gamma": 0,
        "method": "jaccard-index"
    },
    {
        "aggregator": "average",
        "method": "simplified-jaccard-index",
        "tknorm": "maxiumum",
        "tnorm": "minimum"
    },
]

methods = []
for configMap in methods:
    compareIrisesWithComparionMethod(configMap)
"""
