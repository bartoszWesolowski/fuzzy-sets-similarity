from abstract_implication import AbstractImplication
from utils import tkonorm


class LukasiewiczImplication(AbstractImplication):

    NAME = "lukasiewicz"

    def implicationValue(self, a, b):
        return tkonorm.lukasiewicz(1 - a, b)

    def getName(self):
        return LukasiewiczImplication.NAME
