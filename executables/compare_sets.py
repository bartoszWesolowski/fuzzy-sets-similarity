import argparse

#really ugly but any other way did not work
import sys, os
sys.path.insert(0, os.path.abspath('..'))

from fuzzyfacades.raw_configuration_parser import ConfigurationParser
from fuzzyfacades.similarity_calculator_wrapper import SimilarityCalculatorWrapper
from utils import fileparser
from comparators.resultprocessors.console_comparison_result_processor import ConsoleComparisonResultProcessor
from comparators.resultprocessors.result_processor_factory import  ResultProcessorFactory
from comparators.sets_comparator import SetsComparator

# Script that calculate similarity of N sets using method defined in confifuration passed as separate file
DEFAULT_SETS_FILE_NAME = "sets.txt"

DEFAULT_CONFIG_FILE_NAME = "config.txt"

DEFAULT_RESULT_FILE_NAME = 'comparison-result.xlsx'

configurationParser = ConfigurationParser()

similarityCalculatorWrapper = SimilarityCalculatorWrapper()

resultProcessorFactory = ResultProcessorFactory()

setsComparator = SetsComparator()

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
parser.add_argument('-resultParser',
                    help="Name of the result processor. If no specified result of comparison will be printed on the console. All supported values:  " +
                         str(resultProcessorFactory.supportedProcessorsNames()),
                    default=ConsoleComparisonResultProcessor.NAME, metavar='resultParser', dest='resultParser')


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
resultProcessor = resultProcessorFactory.createResultProcessor(args.resultParser)
parsedConfig = configurationParser.validateAndParse(config)

comparisonResult = setsComparator.compareSets(setsList, config)

resultProcessor.processComparisonResult(comparisonResult, args.resultFile)
