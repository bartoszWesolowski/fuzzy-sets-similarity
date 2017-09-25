import json
import re

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
    with open(configFileName) as f:
        content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]
    configs = []
    for conf in content:
        parsed = json.loads(conf)
        configs.append(parsed)

    return configs