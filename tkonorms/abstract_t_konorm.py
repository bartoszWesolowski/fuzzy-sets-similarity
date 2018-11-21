import abc as abstract


class AbstractTkonorm(object):
    @abstract.abstractmethod
    def tkonormValue(self, a, b):
        """Calculates t-norm value for two numbers"""
        pass

    @abstract.abstractmethod
    def getName(self):
        """Returns unique name of t-norm"""
        pass
