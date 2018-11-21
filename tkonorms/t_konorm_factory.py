from lukasiewicz_t_konorm import LukasiewiczTkonorm
from maximum_t_konorm import MaxiumumTkonorm
from probabilistic_t_konorm import AlgebraicTkonorm


class TkonormFactory(object):
    def __init__(self):
        self.tNorms = [
            LukasiewiczTkonorm(),
            MaxiumumTkonorm(),
            AlgebraicTkonorm()
        ]

        self.tNormsMap = {}
        for tNorm in self.tNorms:
            self.tNormsMap[tNorm.getName()] = tNorm

    def getSupportedTkonorms(self):
        """Returns array containing names for all supported implications"""
        return [x.getName() for x in self.tNorms]

    def isTkonormSupported(self, tNormName):
        return tNormName in self.getSupportedTkonorms()

    def getTkonorm(self, name):
        """Returns t-norm object for given name"""
        if not self.isTkonormSupported(name):
            raise AttributeError("Can not create tNorm for name: {}. Supported t-norms names: {}".format(
                name, self.getSupportedTkonorms()))

        return self.tNormsMap[name]
