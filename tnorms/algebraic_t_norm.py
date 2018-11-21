from abstract_t_norm import AbstractTnorm
from utils import constants as c


class AlgebraicTnorm(AbstractTnorm):

    def tnormValue(self, a, b):
        return a * b

    def getName(self):
        return c.TNORM_ALGEBRAIC
