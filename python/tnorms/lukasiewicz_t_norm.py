from abstract_t_norm import AbstractTnorm


class LukasiewiczTnorm(AbstractTnorm):
    NAME = "lukasiewicz"

    def tnormValue(self, a, b):
        return max(0, a + b - 1)

    def getName(self):
        return LukasiewiczTnorm.NAME
