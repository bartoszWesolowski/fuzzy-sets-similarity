from abstract_t_konorm import AbstractTkonorm
from utils import constants as c


class MaxiumumTkonorm(AbstractTkonorm):

    def tkonormValue(self, a, b):
        return max(a, b)

    def getName(self):
        return c.TKONORM_MAXIMUM
