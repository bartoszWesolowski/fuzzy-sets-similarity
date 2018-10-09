import argparse
import json

# TODO: really ugly but any other way did not work
import sys, os

sys.path.insert(0, os.path.abspath('..'))

from aggregators.aggregators_factory import AggregatorFactory
from tnorms.t_norm_factory import TnormFactory
from implications.implication_factory import ImplicationFactory

from fuzzyfacades.similarity_calculator_facade import SimilarityFacade
from utils import configuration_parameters_names as params
from utils import parse

METHOD_PARAMETER = "method"

FILE_NAME_PARAMETER = "fn"

DEFAULT_FILE_NAME = "config.txt"

similarityFacade = SimilarityFacade()
aggregatorFactory = AggregatorFactory()
tNormFactory = TnormFactory()
implicationFactory = ImplicationFactory()

parser = argparse.ArgumentParser(
    description='Tool for generating configurations for similarity calculators.' +
                ' Configurations generated by this tool are save in file specified in one of the params')

parser.add_argument('-' + METHOD_PARAMETER, help="Method config name. Must be one of: {}".format(
    similarityFacade.getSupportedMethods()))
parser.add_argument('-file', help="Name of the file that will be used to save generated configuration object. " +
                                  "Default value: {}".format(DEFAULT_FILE_NAME), default=DEFAULT_FILE_NAME)

parser.add_argument('-' + params.R,
                    help="Parameter used by minkowski similarity. Its value should be a float or an int.")

parser.add_argument('-' + params.AGGREGATOR,
                    help="Parameter pointing to aggregator function. List of supported aggregator values: {}".format(
                        aggregatorFactory.getSupportedAggregators())
                    )

parser.add_argument('-' + params.TNORM,
                    help="Parameter pointing to t-norm function. List of supported t-norms values: {}".format(
                        tNormFactory.getSupportedTNorms())
                    )

parser.add_argument('-' + params.IMPLICATION,
                    help="Parameter pointing to implication function. List of supported implications: {}".format(
                        implicationFactory.getSupportedImplications())
                    )

parser.add_argument('args', nargs=argparse.REMAINDER)

def getConfigFilePath(rawConfig):
    return rawConfig.get(FILE_NAME_PARAMETER, DEFAULT_FILE_NAME)


def validateConfigMethod(rawConfig):
    print "Validating config method"
    if METHOD_PARAMETER not in rawConfig.keys():
        raise AttributeError(
            "No method defined! No argument" + METHOD_PARAMETER + " available. Supported methods " + str(
                similarityFacade.getSupportedMethods()))


def parseArgumentsToMethodConfig(rawArgumentsMap):
    print "Raw arguments: {}".format(rawArgumentsMap)
    validateConfigMethod(rawArgumentsMap)
    method = rawArguments[METHOD_PARAMETER]
    configParser = similarityFacade.getParser(method)
    parsedConfig = configParser.parse(rawArguments)
    print "Parsed config {}".format(parsedConfig)
    return parsedConfig


def saveToFile(config, filePath):
    with open(filePath, "a") as myfile:
        myfile.write(json.dumps(config) + "\n")


try:
    # Used only for displaying simple manual, parser is not used as this script needs to allow all argument names
    args = parser.parse_known_args()
    rawArguments = parse.parseArguments(sys.argv)
    configFile = getConfigFilePath(rawArguments)
    config = parseArgumentsToMethodConfig(rawArguments)
    saveToFile(config, configFile)
except AttributeError as error:
    print "ERROR OCCURED: " + error.message
