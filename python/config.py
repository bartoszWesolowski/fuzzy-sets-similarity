import sys
import json
from utils import parse
from utils import constants as const

METHOD_PARAMETER = "m"

FILE_NAME_PARAMETER = "fn"

SUPPORTED_METHODS = [const.MINKOWSKI, const.ANGULAR_DISTANCE, const.JACCARD_INDEX]

DEFAULT_FILE_NAME = "config.txt"

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
    rawArguments = parse.parseArguments(sys.argv);
    configFile = getConfigFilePath(rawArguments)
    config = parseArgumentsToMethodConfig(rawArguments)
    saveToFile(config, configFile)
except AttributeError as error:
    print "ERROR OCCURED: " + error.message