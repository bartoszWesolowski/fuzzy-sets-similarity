from abstract_t_konorm import AbstractTkonorm
from utils import constants as c


class ProbabilisticTkonorm(AbstractTkonorm):

    def tkonormValue(self, a, b):
        return a + b - (a * b)

    def getName(self):
        return c.TKONORM_PROBABILISTIC
