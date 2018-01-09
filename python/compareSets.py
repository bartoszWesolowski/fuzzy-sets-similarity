import argparse

from facade2.raw_configuration_parser import ConfigurationParser
from facade2.similarity_calculator_wrapper import SimilarityCalculatorWrapper
from utils import fileparser
from utils.calculationmetadata import SimilarityCalculationMetaData
from utils.resultprocessor import ExcelResultProcessor

# Script that calculate similarity of N sets using method defined in confifuration passed as separate file
DEFAULT_SETS_FILE_NAME = "sets.txt"

DEFAULT_CONFIG_FILE_NAME = "config.txt"

DEFAULT_RESULT_FILE_NAME = 'sample.xlsx'

configurationParser = ConfigurationParser()

similarityCalculatorWrapper = SimilarityCalculatorWrapper()

parser = argparse.ArgumentParser(
    description='Tool for calculating similarity between number of sets using one similarity method' +
                'Sets must be defined in file, each set in separate line, each set element followed by blank character. ' +
                'This script uses configuration defined in first line of configuration file.'
)
parser.add_argument('-s',
                    help="Path to the file containing sets definition. Default to: " + DEFAULT_SETS_FILE_NAME,
                    default=DEFAULT_SETS_FILE_NAME, metavar='setsFile', dest='setsFile')
parser.add_argument('-c',
                    help="Path to the file containing configuration definition. Default value: " +
                         DEFAULT_CONFIG_FILE_NAME,
                    default=DEFAULT_CONFIG_FILE_NAME, metavar='configFile', dest='configFile')
parser.add_argument('-resultFile',
                    help="Path to the file that will store the result of comparision. Default value: " +
                         DEFAULT_RESULT_FILE_NAME,
                    default=DEFAULT_RESULT_FILE_NAME, metavar='resultFile', dest='resultFile')


args = parser.parse_args()
setsFile, configFile = args.setsFile, args.configFile
print "Sets file: {}, config file: {}".format(setsFile, configFile)

setsList = fileparser.readSets(setsFile)
numberOfSets = len(setsList)
print "Parsed {} sets".format(numberOfSets)

configs = fileparser.readConfigs(configFile)
config = configs[0]
print "Parsed {} configs. Remember that only first config is used by this script, in that case: {}".format(len(configs),
                                                                                                           config)
resultProcessor = ExcelResultProcessor(numberOfSets, args.resultFile)
parsedConfig = configurationParser.validateAndParse(config)
for i in range(numberOfSets):
    for j in range(i, numberOfSets):
        A = setsList[i]
        B = setsList[j]
        result = similarityCalculatorWrapper.calculateSimilarityFromParsedConfig(A, B, parsedConfig)
        resultProcessor.processResult(result, SimilarityCalculationMetaData(config, A, B, 0, i, j))

resultProcessor.appendSummary()
resultProcessor.save()
