from abstract_t_norm import AbstractTnorm


class AlgebraicTnorm(AbstractTnorm):
    NAME = "algebraic"

    def tnormValue(self, a, b):
        return a * b

    def getName(self):
        return AlgebraicTnorm.NAME
