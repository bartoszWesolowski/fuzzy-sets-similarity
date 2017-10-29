from abstract_implication import AbstractImplication
from utils import tkonorm


class MaximumImplication(AbstractImplication):

    NAME = "maximum"
    def implicationValue(self, a, b):
        return tkonorm.max(1 - a, b)

    def getName(self):
        return MaximumImplication.NAME
