from comparators.resultprocessors.methodscomparison.result_processor import MethodsComparisonAbstractResultProcessor


class MethodsComparisonConsoleResultProcessor(MethodsComparisonAbstractResultProcessor):
    NAME = 'methods-comparison-console-result-processor'

    def processComparisonResult(self, resultComparatorResult, processorConfigurationMap):
        print "Compared fuzzy sets A and B using {} similarity methods".format(resultComparatorResult.numberOfMethods)
        print "A = {}".format(resultComparatorResult.A)
        print "B = {}".format(resultComparatorResult.A)
        print "Results: {}".format(resultComparatorResult.resultsList)
        print "Methods used:"
        for index, config in enumerate(resultComparatorResult.similarityMeasuresConfigurations):
            print "Config nr. {}:  Sim(A, B) = {} -> {}. ".format(index, resultComparatorResult.resultsList[index], config)

    def getName(self):
        return MethodsComparisonConsoleResultProcessor.NAME
