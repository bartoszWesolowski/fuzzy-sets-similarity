from utils import parse
import sys
import re
import json
import simCalculator

SETS_PARAM_NAME = 's'
DEFAULT_SETS_FILE_NAME = "sets.txt"

CONFIG_FILE_PARAM_NAME = 'c'
DEFAULT_CONFIG_FILE_NAME = "config.txt"


def parseParams():
    rawParams = parse.parseArguments(sys.argv)
    return rawParams.get(SETS_PARAM_NAME, DEFAULT_SETS_FILE_NAME), rawParams.get(CONFIG_FILE_PARAM_NAME,
                                                                                 DEFAULT_CONFIG_FILE_NAME)

def parseSet(rawSet):
    splittedSet = re.split("[\s+|,;]", rawSet)
    result = []
    for x in splittedSet:
        try:
            result.append(float(x))
        except ValueError:
            print "Ignoring: {} while parsing set".format(x)

    return result

def readSets(setsFileName):
    with open(setsFileName) as f:
        content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]
    rawA = content[0]
    rawB = content[1]
    A = parseSet(rawA)
    B = parseSet(rawB)
    return A, B

def readConfigs(configFileName):
    with open(configFileName) as f:
        content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]
    configs = []
    for conf in content:
        parsed = json.loads(conf)
        configs.append(parsed)

    return configs

setsFile, configFile = parseParams()
print "Sets file: {}, config file: {}".format(setsFile, configFile)
A, B = readSets(setsFile)
print "Parsed sets: \n\tA: {} \n\tB: {}".format(A, B)
configs = readConfigs(configFile)
for config in configs:
    simCalculator.calculateSimilarity(A, B, config)

