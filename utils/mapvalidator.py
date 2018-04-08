class MapValidator(object):

    """
    Check if passed map contains all required parameters
    """
    @staticmethod
    def validateRequiredParametersExistence(mapToCheck, requiredParameters):
        for param in requiredParameters:
            if param not in mapToCheck.keys():
                raise AttributeError(
                    "Missing '{}' parameter in implication configuration. All required parameters: {}".format(
                        param, requiredParameters
                    ))