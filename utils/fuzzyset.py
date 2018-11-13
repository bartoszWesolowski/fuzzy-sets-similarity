import numpy


class FuzzySet:
    elements = []

    '''konsrtuktor przyjmujacy wektor reprezentujacy zbior rozmyty'''

    def __init__(self, elements):
        self.elements = elements

    def val(self, index):
        """
        Zwraca stopien z jakim element o podanym indexie nalezy do tego zbioru. Wartosc jest obcinana jest do przedzialu [0, 1]
        :param index: 
        :return: 
        """
        val = 0
        if index < len(self.elements):
            val = numpy.clip(self.elements[index], 0, 1)

        return val


    def absoluteValue(self, index):
        val = 0
        if index < len(self.elements):
            val = self.elements[index]

        return val

    # TODO: tnorma, tkonorm
    def binaryOperation(self, otherFuzzySet, binaryOperator):
        """Perform operation on all elements of the set. BinaryOperation has to be a function
        that takes two floating point arguments and returns one floating point number."""
        lenght = self.getLenght(otherFuzzySet)
        result = []
        for i in range(lenght):
            s = binaryOperator(self.val(i), otherFuzzySet.val(i))
            result.append(s)

        return FuzzySet(result)

    def sum(self, otherFuzzySet, tNorm=max):
        """Returns sum of this set and the OtherFuzyzSet, using tNorm (max as the default value).
        tNorm has to be a function that takes two floating point arguments and returns one floating point number.
        Return new fuzzy set as a result.
        """
        return self.binaryOperation(otherFuzzySet, tNorm)

    # TODO: jak to sie powinno nazywac?
    def intersect(self, otherFuzzySet,
                  tConorm=min):
        """Returns intersection of this set and the OtherFuzyzSet, using sNorm (min as the default value).
        tNorm has to be a function that takes two floating point arguments and returns one floating point number.
        Return new fuzzy set as a result.
        """
        return self.binaryOperation(otherFuzzySet, tConorm)

    def getLenght(self, otherFuzzySet):
        """Returns max(number of elements of this set, number of elements of other set)"""
        return max(len(self.elements), len(otherFuzzySet.elements))

    def getUniverse(self, other):
        length = self.getLenght(other)
        return [1 for x in range(length)]

    def complement(self):
        """Compute complement (pol. doplnienie) of fuzzy set. Returns a fuzzy set object."""
        result = []
        for x in self.elements:
            result.append(1 - x)
        return FuzzySet(result)

    def accumulate(self, transformer, accumulator):
        """Accumulates all elements from this set to one value using transformer for transforming each value of set. 
        Transformer has to be a function that takes one floating point argument and return a floating point number.
        Accumulator function with that takes array of numbers as argument and produces single number out of it.
        """
        transformed = []
        for i in range(len(self.elements)):
            transformed.append(transformer(self.val(i)))
        return accumulator(transformed)

    def transform(self, transformer):
        """
        Transforms all elements in this fuzzy set using transformer.
        :param transformer: a function that has one floating point argument and returns floating point number as a result
        :return: FuzzySet with all elements transformed
        """
        result = []
        for x in self.elements:
            result.append(transformer(x))

        return FuzzySet(result)