from abstract_t_konorm import AbstractTkonorm


class LukasiewiczTkonorm(AbstractTkonorm):
    NAME = "lukasiewicz"

    def tkonormValue(self, a, b):
        return min(1, a + b)

    def getName(self):
        return LukasiewiczTkonorm.NAME
