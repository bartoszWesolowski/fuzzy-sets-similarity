import argparse

#really ugly but any other way did not work
import sys, os
sys.path.insert(0, os.path.abspath('..'))
import utils.fsgenerator as generator
import utils.fileutils as fileutils
import abc as abstract

class SetProcessor(object):
    @abstract.abstractmethod
    def processSet(self, fuzzyList, args):
        raise "Implement me"

    @abstract.abstractmethod
    def comment(self, args):
        raise "Implement me"

class PrintToConsoleSetProcessor(SetProcessor):
    def processSet(self, fuzzyList, args):
        print fuzzyList

    def comment(self, args):
        print args.comment

class AppendToFileSetProcessor(SetProcessor):
    def processSet(self, fuzzyList, args):
        generatedSetStringRepresentation = " ".join(map(str, fuzzyList))
        print "Appending result to file {}. Set created: {}".format(args.file, generatedSetStringRepresentation)
        fileutils.appendLine(args.file, generatedSetStringRepresentation)

    def comment(self, args):
        if (args.comment):
            fileutils.appendComment(args.file, args.comment)


def randomSet(args):
    return generator.randomFuzzyList(args.n, args.min, args.max)

def smoothRandom(args):
    return generator.smoothRandomFuzzySetList(args.n, args.min, args.max, args.maxDiff)

def randomWithRescaled(args):
    return generator.randomWithRescaled(n=args.n, minimalValue=args.min, maxValue=args.max, maxDiff=args.maxDiff, yScale=args.rescaleY)

def sigletonSet(args):
    return generator.singletonFuzzyList(args.n, args.value)

def symetricTriangular(args):
    return generator.symetricTriangular(args.n)

def symetricTriangularAndRescaled(args):
    original = generator.symetricTriangular(args.n)
    return generator.rescaleSymetricTriangularSets(original.wrappedSet, args.rescaleX, args.rescaleY)

def generateSet(arts):
    method = randomSet
    if args.method:
        method = args.method
    return method(args)

def printProcessor(set, args):
    print set

def processGeneratedSet(generatedSetWrapper, args):
    setProcessor = PrintToConsoleSetProcessor()
    if args.processGeneratedSet:
        setProcessor = args.processGeneratedSet
    generatedSet.process(setProcessor, args)


parser = argparse.ArgumentParser(description='Tool for generating fuzzy sets ')

# All allowed arguments
parser.add_argument('-n', type=int, help="Number of elements in generated set. Default value: 20.", default=20)
parser.add_argument('-min', type=float, help="Minimal value of each element in generated set. Default value: 0.0",
                    default=0.0, metavar='min')
parser.add_argument('-max', type=float, help="Maximal value of each element in generated set. Default value: 1.0",
                    default=1.0, metavar='max')
parser.add_argument('-value', type=float, help="Value used to generate singleton sets. Default value: 1.0",
                    default=1.0, metavar='value')
parser.add_argument('-rescaleX', type=float, help="Used for rescaling set by x axis",
                    default=1.0, metavar='rescaleX')
parser.add_argument('-rescaleY', type=float, help="Used for rescaling set by y axis",
                    default=1.0, metavar='rescaleY')
parser.add_argument('-comment', type=str, help="Comment describing generated result",
                    default=None, metavar='comment')
parser.add_argument('-maxDiff', type=float, help="Max difference between two elements in random fuzzy set",
                    default=0.2, metavar='maxDiff')
parser.add_argument('-file',
                    help="Path to the file that will be used to store the result. " +
                         "Generated set will be appended as last line of this file. Default: sets.txt",
                    default='sets.txt', metavar='file')

# allowed families of sets that can be generated using this tool
# const values should point to a funtion that returns generated set and takes parsedArgs object as argument

parser.add_argument('--random', dest='method', action='store_const',
                    const=randomSet,
                    help='Generates random set with n elements, each element is between min and max values')

parser.add_argument('--smoothRandom', dest='method', action='store_const',
                    const=smoothRandom,
                    help='Generates random set with n elements, each element is between min and max values. Diff '
                         'between two following values will be smaller then value specified by maxDiff param.')

parser.add_argument('--singleton', dest='method', action='store_const',
                    const=sigletonSet,
                    help='Generates singleton set with n elements, each element is equal to -value parameter.')

parser.add_argument('--triangular', dest='method', action='store_const',
                    const=symetricTriangular,
                    help='Generates triangular set with n elements.')

parser.add_argument('--triangularRescaled', dest='method', action='store_const',
                    const=symetricTriangularAndRescaled,
                    help='Generates triangular set with n elements and rescaled version of this set. Rescaling is '
                         'done along x axis (rescaleX parameter) and along yAxis (rescaleY)')

parser.add_argument('--randomWithRescaled', dest='method', action='store_const',
                    const=randomWithRescaled,
                    help='Creates two sets - using method provided by smoothRandom and second one created by rescaled by applying rescaleY value')

# Allowed ways to process generated set
# const should point to a function that process result, this function takes two arguments:
# generated Set amd parsed arguments object
parser.add_argument('--appendToFile', dest='processGeneratedSet', action='store_const',
                    const=AppendToFileSetProcessor(),
                    help='This flag allows to save generated set in file defined by -file parameter.')

args = parser.parse_args()
generatedSet = generateSet(args)
processGeneratedSet(generatedSet, args)
