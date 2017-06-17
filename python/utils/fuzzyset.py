import numpy
class FuzzySet:
    elements = []

    '''konsrtuktor przyjmujacy wektor reprezentujacy zbior rozmyty'''
    def __init__(self, elements):
        self.elements = elements

    '''zwraca stopien z jakim element o podanym indexie nalezy do tego zbioru'''
    def val(self, index):
        val = 0
        if index < len(self.elements):
            val = numpy.clip(self.elements[index], 0, 1)

        return val


    #TODO: tnorma czy snorma?
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

    #TODO: jak to sie powinno nazywac?
    def intersect(self, otherFuzzySet, tConorm=min):
        """Returns intersection of this set and the OtherFuzyzSet, using sNorm (min as the default value).
        tNorm has to be a function that takes two floating point arguments and returns one floating point number.
        Return new fuzzy set as a result.
        """
        return self.binaryOperation(otherFuzzySet, tConorm)

    def getLenght(self, otherFuzzySet):
        """Returns max(number of elements of this set, number of elements of other set)"""
        return max(len(self.elements), len(otherFuzzySet.elements))

