from abstract_t_konorm import AbstractTkonorm


class MinimumTkonorm(AbstractTkonorm):
    NAME = "maxiumum"

    def tkonormValue(self, a, b):
        return max(a, b)

    def getName(self):
        return MinimumTkonorm.NAME
