from abstract_t_konorm import AbstractTkonorm
from utils import constants as c


class LukasiewiczTkonorm(AbstractTkonorm):

    def tkonormValue(self, a, b):
        return min(1, a + b)

    def getName(self):
        return c.TKONORM_LUKASIEWICZ
