import random

class FuzzySetWrapper(object):
    def __init__(self, toWrapp):
        self.wrappedSet = toWrapp

    def process(self, setProcessor, args):
        """
        Process this set with given set processor and arguments
        :param setProcessor: function that takes two arguments  as input: list of floats representing fuzzy set) and 
        argParser arguments
        :param args: argParser arg object
        :return: 
        """
        setProcessor.comment(args)
        setProcessor.processSet(self.wrappedSet, args)

class RescaledSets(FuzzySetWrapper):
    def __init__(self, original, rescaled):
        self.original = original
        self.rescaled = rescaled

    def process(self, setProcessor, args):
        """
        Process this set with given set processor and arguments
        :param setProcessor: function that takes two arguments  as input: list of floats representing fuzzy set) and 
        argParser arguments
        :param args: argParser arg object
        :return: 
        """
        setProcessor.comment(args)
        setProcessor.processSet(self.original, args)
        setProcessor.processSet(self.rescaled, args)

def randomFuzzyList(length=20, min=0, max=1, digits=4):
    """
    creates FuzzySetWrapper with an array of lenght with elements grater or equal to min and less or equal than max 
    - array represent random fuzzy set
    :param length: 
    :param min: 
    :param max: 
    :param digits: 
    :return: FuzzySetWrapper
    """
    result = []
    for i in range(length):
        randomValue = random.uniform(min, max)
        result.append(round(randomValue, digits))
    return FuzzySetWrapper(result)

def smoothRandomFuzzySetList(length=20, minimalValue=0, maxValue=1, maxDiff=0.1, digits=4):
    result = []
    first = random.uniform(minimalValue, maxValue)
    result.append(first)
    for i in range(1, length):
        previous = result[i - 1]
        smoothedRandomValue = random.uniform(max(minimalValue, previous - maxDiff), min(maxValue, previous + maxDiff))
        result.append(round(smoothedRandomValue, digits))
    return FuzzySetWrapper(result)


def singletonFuzzyList(length=20, value=1, digits=4):
    """create an array of length with elements equal to value"""
    result = []
    for i in range(length):
        result.append(round(value, digits))
    return FuzzySetWrapper(result)


def triangualrSetFunctionn(x):
    """Funkcja przynaleznosci elementu x do wzorcowego zbioru trojkatnego
    Definicja w pracy magisterskiej, strona 40. TODO: English wersion"""
    value = 0
    if x <= 0:
        value = max(0, (1 + x) / 2.0)
    else:
        value = max(0, (1 - x) / 2.0)
    return value


def symetricTriangular(numberOfElements):
    """
    Generates symetric triangular set, with higher value equal to 1 for element with index n/2
    :param n: number of elements, shold be even, if not it's increased with one
    :return: FuzzySetWrapper with triangular set inside
    """
    result = []
    n = numberOfElements if numberOfElements % 2 == 0 else numberOfElements + 1
    middle = (n - 1) / float(2)
    for x in range(n + 1):
        if x <= middle:
            value = x * 2 * (1 / float(n))
        else:
            value = ((-2 * x) / float(n)) + 2

        result.append(value)

    return FuzzySetWrapper(result)

def rescaleSymetricTriangularSets(originalSet, xScale=1.0, yScale=1.0):
    """
    Given a symetric triangular set (originalSet) it rescale it along x axis with xScale and y axis with yScale which creates rescaled set.
    It adjust original and rescaled sets to same length
    :param originalSet: 
    :param xScale: 
    :param yScale: 
    :return: pair of original and rescaled sets
    """
    originalSetSize = len(originalSet) - 1
    numberOfElementsInNewSet = int(originalSetSize * xScale)
    print "Number of elements in original and rescaled: {} -> {}".format(originalSet, numberOfElementsInNewSet)
    rescaled = symetricTriangular(numberOfElementsInNewSet).wrappedSet
    rescaled = map(lambda x: x * yScale, rescaled)
    sizeDifference = abs(originalSetSize - (len(rescaled) - 1))
    numberOfZerosToAddToSmallerSet = int(sizeDifference / float(2))#int((originalSetSize / 2.0) * abs(1 - xScale))
    setWithLeadingZeros = [0 for x in range(numberOfZerosToAddToSmallerSet)]
    if xScale >= 1:
        setWithLeadingZeros.extend(originalSet)
        originalSet = setWithLeadingZeros
    else:
        setWithLeadingZeros.extend(rescaled)
        rescaled = setWithLeadingZeros

    return RescaledSets(originalSet, rescaled)

def randomWithRescaled(n, minimalValue=0, maxValue=1, maxDiff=0.1, yScale=1, digits=4):
    """
    Creates random smooth set and it's rescaled by yScale version
    :param n: number of elements
    :param yScale: scale applied to all values of second set
    :return: two sets wrapped in RescaledSets object
    """
    randomSet = smoothRandomFuzzySetList(n, minimalValue, maxValue, maxDiff, digits=digits).wrappedSet
    scaled = [x * yScale for x in randomSet]
    return RescaledSets(randomSet, scaled)

def triangular(x, a, b, c):
    if a < b < c:
        first = (x - a) / (b - a)
        second = (c - x) / (c - b)
        minimum = min(first, second)
        return max(0, minimum)
    else:
        raise AttributeError(
            "Creating triangular function requires the following arguments: a < b < c but found a = {}, b = {}, c = {}. ".format(
                a, b, c))


def trapeze(x, a, b, c, d):
    if a < b <= c < d:
        first = (x - a) / (b - a)
        second = (d - x) / (d -c)
        minimum = min(1, first, second)
        return max(0, minimum)
        return 0
    else:
        raise AttributeError()

