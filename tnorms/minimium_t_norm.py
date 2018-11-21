from abstract_t_norm import AbstractTnorm
from utils import constants as c


class MinimumTnorm(AbstractTnorm):

    def tnormValue(self, a, b):
        return min(a, b)

    def getName(self):
        return c.TNORM_MINIMUM
