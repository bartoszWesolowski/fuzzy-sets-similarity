import json
import re

from fuzzyfacades.raw_configuration_parser import ConfigurationParser


def parseSet(rawSet):
    """Parse string representing fuzzy set to list of floats"""
    splittedSet = re.split("[\s+|,;]", rawSet)
    result = []
    for x in splittedSet:
        try:
            result.append(float(x))
        except ValueError:
            print "Ignoring: {} while parsing set".format(x)

    return result


def readSets(setsFileName):
    """Read sets defined in file that is referenced by passed setsFileName
    Each set has to be defined in separate line
    Returns list containing all parsed sets
    """
    with open(setsFileName) as f:
        content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]
    parsedSets = [parseSet(rawSet) for rawSet in content]
    return parsedSets


def readConfigs(configFileName):
    """Reads config files defined in filename defined by configFileName parameter.
    Each config should be available in separate line represented by json object.
    This method reads all lines and convert json object to python maps (does not parse configs)
    """
    with open(configFileName) as f:
        content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]
    configs = []
    for conf in content:
        parsed = json.loads(conf)
        configs.append(parsed)

    return configs

configParser = ConfigurationParser()

def readAndParseConfigs(configFileName):
    """Reads config files defined in filename defined by configFileName parameter.
    Each config should be available in separate line represented by json object.
    Each json config representation is parsed to internal format required by similarity calculators.
    In case config is not valid this method will trow Exception"""
    rawConfigs = readConfigs(configFileName)
    parsedConfigs = [configParser.validateAndParse(config) for config in rawConfigs]
    return parsedConfigs
