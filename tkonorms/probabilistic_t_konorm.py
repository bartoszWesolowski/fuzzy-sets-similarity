from abstract_t_konorm import AbstractTkonorm


class AlgebraicTkonorm(AbstractTkonorm):
    NAME = "probabilistic"

    def tkonormValue(self, a, b):
        return a * b

    def getName(self):
        return AlgebraicTkonorm.NAME
