from sklearn import datasets

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
        self.sepalLen = data[0] #4.3 - 7.9
        self.sepalWidth = data[1]
        self.petalLen = data[2]
        self.petalWidth = data[3]


class AroundValueFuzzySet(object):
    """Triangular set representing 'around x'"""

    def __init__(self, range):
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
    def __init__(self, attributesList, minOffset, maxOffset):
        self.attributesList = attributesList
        self.min = min(attributesList)
        self.max = max(attributesList)
        self.start = self.min - minOffset
        self.end = self.max + maxOffset
        self.attibuteRange = abs(self.min - self.max)

    def getPossibleValues(self, numberOfPossibleValues):
        offset = abs(self.start - self.end) / float(numberOfPossibleValues - 1)

        possibleValues = []
        for n in range(numberOfPossibleValues):
            possibleValues.append(self.start + n * offset)

        return possibleValues

class FuzzyIris(object):
    def __init__(self, sepalLen, sepalWidth, petalLen = [], petalWidth = [], irisType = []):
        """
        
        :param sepalLen: 
        :param sepalWidth: 
        :param petalLen: 
        :param petalWidth: 
        :param irisType: 
        """
        self.type = irisType
        self.sepalLen = sepalLen #4.3 - 7.9
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
    def __init__(self, wrappedIrisDataSet):
        self.sepalLenghtPossibleValueCalculator = PossibleAttributeValuesCalculator(wrappedIrisDataSet.getSepalLenghts(), 2, 2)
        self.aroundSepalLengthFuzzySet = AroundValueFuzzySet(self.sepalLenghtPossibleValueCalculator.attibuteRange)

        self.sepalWidthPossibleValueCalculator = PossibleAttributeValuesCalculator(wrappedIrisDataSet.getSepalWidths(), 3, 3)
        self.aroundSepalWidthFuzzySet = AroundValueFuzzySet(self.sepalWidthPossibleValueCalculator.attibuteRange)

        self.petalLenPossibleValueCalculator = PossibleAttributeValuesCalculator(wrappedIrisDataSet.getPetalLengths(), 3, 3)
        self.aroundPetalLenFuzzySet = AroundValueFuzzySet(self.petalLenPossibleValueCalculator.attibuteRange)

        self.fuzzyfiedDataset = []
        self.numberOfPossibleValuesSamples = 20
        for iris in wrappedIrisDataSet.irises:
            fuzzyficateSepalLength = self.fuzzyficateAttributeValue(iris.sepalLen,
                                                                    self.sepalLenghtPossibleValueCalculator.getPossibleValues(self.numberOfPossibleValuesSamples ),
                                                                    self.aroundSepalLengthFuzzySet)

            fuzzyficateSepalWidth = self.fuzzyficateAttributeValue(iris.sepalWidth,
                                                                    self.sepalWidthPossibleValueCalculator.getPossibleValues(self.numberOfPossibleValuesSamples ),
                                                                    self.aroundSepalWidthFuzzySet)

            fuzzyficatePetalLen = self.fuzzyficateAttributeValue(iris.petalLen,
                                                                    self.petalLenPossibleValueCalculator.getPossibleValues(self.numberOfPossibleValuesSamples ),
                                                                    self.aroundPetalLenFuzzySet)

            self.fuzzyfiedDataset.append(FuzzyIris(fuzzyficateSepalLength, fuzzyficateSepalWidth, petalLen=fuzzyficatePetalLen, irisType=iris.type))


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



rawIrisDataset = datasets.load_iris()

irisDataset = IrisDataSet(rawIrisDataset)

fuzzyficatedIrisDataSet = IrisDataSetFuzyficator(irisDataset)

print fuzzyficatedIrisDataSet.toFuzzySetFileFormat()

minkowskiCalculator = MinkowskiSimilarityCalculator()
setsComparator = SetsComparator()

# comparing same types:
for firstIrisType in [0, 1, 2]:
    for secondIrisType in [0, 1, 2]:
        print "\n\n Compare irises with types: {} x {}".format(firstIrisType, secondIrisType)
        fuzzyIrisesWithFirstType = map(lambda fuzzyIris: fuzzyIris.fuzzySetArray(), fuzzyficatedIrisDataSet.getIrisesWithType(firstIrisType))
        fuzzyIrisesWithSecondType = map(lambda fuzzyIris: fuzzyIris.fuzzySetArray(), fuzzyficatedIrisDataSet.getIrisesWithType(secondIrisType))
        comparisonResult = setsComparator.compareTwoSets(fuzzyIrisesWithFirstType, fuzzyIrisesWithSecondType, {"r": 1, "method": "minkowski"})
        resultArray = comparisonResult.resultArray
        print "Max similarity: {}".format(max(resultArray))
        print "Average similarity: {}".format(sum(resultArray) / float(len(resultArray)))
        print "Min similarity: {}".format(min(resultArray))




