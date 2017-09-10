import sys
import json
from utils import parse
from utils import constants as const

METHOD_PARAMETER = "m"

FILE_NAME_PARAMETER = "fn"

SUPPORTED_METHODS = [const.MINKOWSKI, const.ANGULAR_DISTANCE, const.JACCARD_INDEX]

DEFAULT_FILE_NAME = "config.txt"

def parseArguments(listOfArguments):
    """Parse list of arguments to map"""
    lenght = len(listOfArguments)
    result = {}
    if lenght % 2 is 0:
        raise AttributeError("Invalid number of arguments! Required even number of arguments in key value form!")
    for i in range(1, lenght, 2):
        key = listOfArguments[i]
        value = listOfArguments[i + 1]
        if not key.startswith("-"):
            raise AttributeError("A key must start with '-'")

        key = key.partition("-")[2]  # removes the '-' from the argument
        result[key] = value

    return result

def getConfigFilePath(rawConfig):
    return rawConfig.get(FILE_NAME_PARAMETER, DEFAULT_FILE_NAME)

def validateConfigMethod(rawConfig):
    print "Validating config method"
    if METHOD_PARAMETER not in rawConfig.keys():
        raise AttributeError("No method defined! No argument" + METHOD_PARAMETER + " available.")
    elif rawConfig[METHOD_PARAMETER] not in SUPPORTED_METHODS:
        raise AttributeError("Unrecognized method: {} . List of supported methods: {}".format(rawConfig[METHOD_PARAMETER], SUPPORTED_METHODS))

def parseArgumentsToMethodConfig(rawArgumentsMap):
    print "Raw arguments: {}".format(rawArgumentsMap)
    validateConfigMethod(rawArgumentsMap)
    method = rawArguments[METHOD_PARAMETER]
    configParser = parse.CONFIG_PARSERS[method]
    parsedConfig = configParser(rawArguments)
    print "Parsed config {}".format(parsedConfig)
    return parsedConfig

def saveToFile(config, filePath):
    with open(filePath, "a") as myfile:
        myfile.write(json.dumps(config) + "\n")

try:
    print "Creating map of arguments."
    rawArguments = parseArguments(sys.argv);
    configFile = getConfigFilePath(rawArguments)
    config = parseArgumentsToMethodConfig(rawArguments)
    saveToFile(config, configFile)
except AttributeError as error:
    print "ERROR OCCURED: " + error.message