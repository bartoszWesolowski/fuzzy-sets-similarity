from abstract_t_konorm import AbstractTkonorm
from utils import constants as c


class AlgebraicTkonorm(AbstractTkonorm):

    def tkonormValue(self, a, b):
        return a * b

    def getName(self):
        return c.TKONORM_PROBABILISTIC
