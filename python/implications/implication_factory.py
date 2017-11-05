from lukasiewicz_implication import LukasiewiczImplication
from maximum_implication import MaximumImplication


class ImplicationFactory(object):
    IMPLICATIONS = [
        LukasiewiczImplication(),
        MaximumImplication()
    ]

    def implicationMap(self):
        implicationMap = {}
        for implication in self.IMPLICATIONS:
            implicationMap[implication.getName()] = implication
        return implicationMap

    def getSupportedImplications(self):
        """Returns array containing names for all supported implications"""
        return [x.getName() for x in self.IMPLICATIONS]

    def getImplication(self, name):
        """Returns implication object for given name"""
        if name not in self.getSupportedImplications():
            raise AttributeError("Can not create implication for name: {}. Supported implication names: {}".format(
                name, self.getSupportedImplications()))

        return self.implicationMap()[name]

    def isSupported(self, implicationName):
        return implicationName in self.IMPLICATIONS
