import sys

from utils import parse, fileparser, simCalculator
from utils.calculationmetadata import SimilarityCalculationMetaData
from utils.resultprocessor import ConnsoleResultProcessor

#Script that calculate similarity of two sets using methods defined in confifurations passed as separate file
SETS_PARAM_NAME = 's'
DEFAULT_SETS_FILE_NAME = "sets.txt"

CONFIG_FILE_PARAM_NAME = 'c'
DEFAULT_CONFIG_FILE_NAME = "config.txt"


def parseParams():
    rawParams = parse.parseArguments(sys.argv)
    return rawParams.get(SETS_PARAM_NAME, DEFAULT_SETS_FILE_NAME), rawParams.get(CONFIG_FILE_PARAM_NAME,
                                                                                 DEFAULT_CONFIG_FILE_NAME)
resultProcessor = ConnsoleResultProcessor()

setsFile, configFile = parseParams()
print "Sets file: {}, config file: {}".format(setsFile, configFile)
setsList = fileparser.readSets(setsFile)
if len(setsList) < 2:
    raise AttributeError("File providing sets does not contain two sets.")
A, B = setsList[0], setsList[1] #assumes that file with sets definition has at least two sets, and uses only those sets
print "Parsed sets: \n\tA: {} \n\tB: {}".format(A, B)
configs = fileparser.readAndParseConfigs(configFile)
for index, config in enumerate(configs):
    result = simCalculator.calculateSimilarityFromParsedConfig(A, B, config)
    resultProcessor.processResult(result, SimilarityCalculationMetaData(config, A, B, index, 0, 1))

