from abstract_implication import AbstractImplication
from utils import tkonorms


class LukasiewiczImplication(AbstractImplication):

    NAME = "lukasiewicz"

    def implicationValue(self, a, b):
        return tkonorms.lukasiewicz(1 - a, b)

    def getName(self):
        return LukasiewiczImplication.NAME
