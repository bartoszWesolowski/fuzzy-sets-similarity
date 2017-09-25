from utils import parse, fileparser, rawconfigparser
import sys
import simCalculator
from utils.calculationmetadata import SimilarityCalculationMetaData
from utils.resultprocessor import ExcelResultProcessor
import time

#Script that calculate similarity of N sets using method defined in confifuration passed as separate file
SETS_PARAM_NAME = 's'
DEFAULT_SETS_FILE_NAME = "sets.txt"

CONFIG_FILE_PARAM_NAME = 'c'
DEFAULT_CONFIG_FILE_NAME = "config.txt"


def parseParams():
    rawParams = parse.parseArguments(sys.argv)
    return rawParams.get(SETS_PARAM_NAME, DEFAULT_SETS_FILE_NAME), rawParams.get(CONFIG_FILE_PARAM_NAME,
                                                                                 DEFAULT_CONFIG_FILE_NAME)

setsFile, configFile = parseParams()
print "Sets file: {}, config file: {}".format(setsFile, configFile)
setsList = fileparser.readSets(setsFile)
numberOfSets = len(setsList)
print "Parsed {} sets".format(numberOfSets)
configs = fileparser.readConfigs(configFile)
config = configs[0]
print "Parsed {} configs. Remember that only first config is used by this script, in that case: {}".format(len(configs), config)

resultProcessor = ExcelResultProcessor(numberOfSets)
parsedConfig = rawconfigparser.validateAndParse(config)
for i in range(numberOfSets):
    for j in range(i, numberOfSets):
        A = setsList[i]
        B = setsList[j]
        result = simCalculator.calculateSimilarityFromParsedConfig(A, B, parsedConfig)
        resultProcessor.processResult(result, SimilarityCalculationMetaData(config, A, B, 0, i, j))

resultProcessor.save()
