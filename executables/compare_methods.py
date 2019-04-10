import argparse
# really ugly but any other way did not work
import os
import sys

sys.path.insert(0, os.path.abspath('..'))

from comparators.methods_comparator import MethodsComparator
from comparators.resultprocessors.methodscomparison.console_result_processor import \
    MethodsComparisonConsoleResultProcessor
from utils import fileparser
from comparators.resultprocessors.setscomparison.console_comparison_result_processor import \
    ConsoleComparisonResultProcessor
from fuzzyfacades.similarity_calculator_wrapper import SimilarityCalculatorFacade

# TODO: add result configurable result processor
# Script that calculate similarity of two sets using methods defined in confifurations passed as separate file

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

similarityCalculatorWrapper = SimilarityCalculatorFacade()

args = parser.parse_args()
setsFile, configFile = args.setsFile, args.configFile
print "Sets file: {}, config file: {}".format(setsFile, configFile)

setsList = fileparser.readSets(setsFile)
if len(setsList) < 2:
    raise AttributeError("File providing sets does not contain two sets.")
A, B = setsList[0], setsList[1]  # assumes that file with sets definition has at least two sets, and uses only those sets
print "Parsed sets: \n\tA: {} \n\tB: {}".format(A, B)

configs = fileparser.readAndParseConfigs(configFile)

# TODO: Implement result processors for this case, extract result processors for comparing sets to different namespace
methodsComparator = MethodsComparator()
resultProcessor = MethodsComparisonConsoleResultProcessor()

comparisonResult = methodsComparator.compareTwoSetsUsingMultipleMethods(A, B, configs)
# TODO: Pass all arguments passed from console, manually parsed map of arguments or args from parser.parse_args()
resultProcessor.processComparisonResult(comparisonResult, {})
