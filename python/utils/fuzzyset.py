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