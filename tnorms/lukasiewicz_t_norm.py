from abstract_t_norm import AbstractTnorm
from utils import constants as c


class LukasiewiczTnorm(AbstractTnorm):
    def tnormValue(self, a, b):
        return max(0, a + b - 1)

    def getName(self):
        return c.TNORM_LUKASIEWICZ
