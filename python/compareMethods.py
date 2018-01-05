import argparse
from utils import fileparser
from utils.calculationmetadata import SimilarityCalculationMetaData
from utils.resultprocessor import ConnsoleResultProcessor
from facade.similarity_calculator_wrapper import SimilarityCalculatorWrapper

#Script that calculate similarity of two sets using methods defined in confifurations passed as separate file

DEFAULT_SETS_FILE_NAME = "sets.txt"

DEFAULT_CONFIG_FILE_NAME = "config.txt"

parser = argparse.ArgumentParser(
    description='Tool for calculating similarity between two sets using all methods defined in referenced file.' +
                'Sets must be defined in file, each set in separate line, each set element followed by blank character.' +
                'Two sets are expected to be present in sets file.' +
                'This script uses configurations defined in configuration file. Each configuration in separate line.'
)
parser.add_argument('-s',
                    help="Path to the file containing sets definition. Default to: " + DEFAULT_SETS_FILE_NAME,
                    default=DEFAULT_SETS_FILE_NAME, metavar='setsFile', dest='setsFile')
parser.add_argument('-c',
                    help="Path to the file containing configuration definition. Default value: " +
                         DEFAULT_CONFIG_FILE_NAME,
                    default=DEFAULT_CONFIG_FILE_NAME, metavar='configFile', dest='configFile')

resultProcessor = ConnsoleResultProcessor()
similarityCalculatorWrapper = SimilarityCalculatorWrapper()

args = parser.parse_args()
setsFile, configFile = args.setsFile, args.configFile
print "Sets file: {}, config file: {}".format(setsFile, configFile)

setsList = fileparser.readSets(setsFile)
if len(setsList) < 2:
    raise AttributeError("File providing sets does not contain two sets.")
A, B = setsList[0], setsList[1] #assumes that file with sets definition has at least two sets, and uses only those sets
print "Parsed sets: \n\tA: {} \n\tB: {}".format(A, B)

configs = fileparser.readAndParseConfigs(configFile)

for index, config in enumerate(configs):
    result = similarityCalculatorWrapper.calculateSimilarityFromParsedConfig(A, B, config)
    resultProcessor.processResult(result, SimilarityCalculationMetaData(config, A, B, index, 0, 1))

