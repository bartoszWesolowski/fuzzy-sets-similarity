import abc as abstract


class AbstractConfigurationParser(object):
    @abstract.abstractmethod
    def parse(self, rawConfigMap):
        return {}

    def parseToIntOrRaiseAttributeError(self, value, errorMessage="Could not parse value to int."):
        """Returns value parsed to int or raises an AttributeError with error message."""
        try:
            return int(value)
        except Exception:
            raise AttributeError(errorMessage)

