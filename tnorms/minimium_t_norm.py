from abstract_t_norm import AbstractTnorm


class MinimumTnorm(AbstractTnorm):
    NAME = "minimum"

    def tnormValue(self, a, b):
        return min(a, b)

    def getName(self):
        return MinimumTnorm.NAME
