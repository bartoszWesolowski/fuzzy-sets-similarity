import abc as abstract


class AbstractTnorm(object):
    @abstract.abstractmethod
    def tnormValue(self, a, b):
        """Calculates t-norm value for two numbers"""
        pass

    @abstract.abstractmethod
    def getName(self):
        """Returns unique name of t-norm"""
        pass
