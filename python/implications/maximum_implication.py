from abstract_implication import AbstractImplication


class MaximumImplication(AbstractImplication):

    NAME = "maximum"
    def implicationValue(self, a, b):
        return max(1 - a, b)

    def getName(self):
        return MaximumImplication.NAME
