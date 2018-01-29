import argparse

#really ugly but any other way did not work
import sys, os
sys.path.insert(0, os.path.abspath('..'))
import utils.fsgenerator as generator
import utils.fileutils as fileutils

def randomSet(args):
    return generator.randomFuzzyList(args.n, args.min, args.max)


def sigletonSet(args):
    return generator.singletonFuzzyList(args.n, args.value)


def appendToFile(generatedSet, args):
    generatedSetStringRepresentation = " ".join(map(str,generatedSet))
    print "Appending result to file {}".format(args.file)
    fileutils.appendLine(args.file, generatedSetStringRepresentation)


def generateSet(arts):
    method = randomSet
    if args.method:
        method = args.method
    return method(args)


def processGeneratedSet(generatedSet, args):
    if args.processGeneratedSet:
        args.processGeneratedSet(generatedSet, args)
    print generatedSet


parser = argparse.ArgumentParser(description='Tool for generating fuzzy sets ')

# All allowed arguments
parser.add_argument('-n', type=int, help="Number of elements in generated set. Default value: 20.", default=20)
parser.add_argument('-min', type=float, help="Minimal value of each element in generated set. Default value: 0.0",
                    default=0.0, metavar='min')
parser.add_argument('-max', type=float, help="Maximal value of each element in generated set. Default value: 1.0",
                    default=1.0, metavar='max')
parser.add_argument('-value', type=float, help="Value used to generate singleton sets. Default value: 1.0",
                    default=1.0, metavar='value')
parser.add_argument('-file',
                    help="Path to the file that will be used to store the result. " +
                         "Generated set will be appended as last line of this file. Default: sets.txt",
                    default='sets.txt', metavar='file')

# allowed families of sets that can be generated using this tool
# const values should point to a funtion that returns generated set and takes parsedArgs object as argument

parser.add_argument('--random', dest='method', action='store_const',
                    const=randomSet,
                    help='Generates random set with n elements, each element is between min and max values')

parser.add_argument('--singleton', dest='method', action='store_const',
                    const=sigletonSet,
                    help='Generates singleton set with n elements, each element is equal to -value parameter.')

# Allowed ways to process generated set
# const should point to a function that process result, this function takes two arguments:
# generated Set amd parsed arguments object
parser.add_argument('--appendToFile', dest='processGeneratedSet', action='store_const',
                    const=appendToFile,
                    help='This flag allows to save generated set in file defined by -file parameter.')

args = parser.parse_args()
generatedSet = generateSet(args)
processGeneratedSet(generatedSet, args)
