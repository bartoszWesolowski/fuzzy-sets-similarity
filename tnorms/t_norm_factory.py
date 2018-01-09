from lukasiewicz_t_norm import LukasiewiczTnorm
from minimium_t_norm import MinimumTnorm
from algebraic_t_norm import AlgebraicTnorm


class TnormFactory(object):
    def __init__(self):
        self.tNorms = [
            LukasiewiczTnorm(),
            MinimumTnorm(),
            AlgebraicTnorm()
        ]

        self.tNormsMap = {}
        for tNorm in self.tNorms:
            self.tNormsMap[tNorm.getName()] = tNorm

    def getSupportedTNorms(self):
        """Returns array containing names for all supported implications"""
        return [x.getName() for x in self.tNorms]

    def isTnormSupported(self, tNormName):
        return tNormName in self.getSupportedTNorms()

    def getTNorm(self, name):
        """Returns t-norm object for given name"""
        if name not in self.getSupportedTNorms():
            raise AttributeError("Can not create tNorm for name: {}. Supported t-norms names: {}".format(
                name, self.getSupportedTNorms()))

        return self.tNormsMap[name]
