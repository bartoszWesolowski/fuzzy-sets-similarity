import abc as abstract


class AbstractConfigurationParser(object):
    @abstract.abstractmethod
    def parse(self, rawConfigMap):
        """
        Parses raw String -> String map to String -> Object map and validates the map attributes - for example it 
        could parse string parameter to int.
        This method should throw a AttributeError in case config state is not valid.
        Each implementation of this class is connected to one implementation of similarity calculator.
        Map returned by this method should be a valid configuration that will be used in connected similarity config. 
        :param rawConfigMap: string -> string map
        :return: string -> object map
        """
        return {}

    def parseToIntOrRaiseAttributeError(self, value, errorMessage="Could not parse value to int."):
        """Returns value parsed to int or raises an AttributeError with error message."""
        try:
            return int(value)
        except Exception:
            raise AttributeError(errorMessage)

