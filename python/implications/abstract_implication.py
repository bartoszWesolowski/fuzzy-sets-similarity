import abc as abstract


class AbstractImplication(object):
    @abstract.abstractmethod
    def implicationValue(self, a, b):
        """Calculates implication value for two floats, that is value of a -> b"""
        pass


    @abstract.abstractmethod
    def getName(self):
        """Returns unique name of implication"""
        pass