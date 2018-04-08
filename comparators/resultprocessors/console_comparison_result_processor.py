from result_processor import AbstractResultProcessor


class ConsoleComparisonResultProcessor(AbstractResultProcessor):
    NAME = 'console-result-processor'

    def processComparisonResult(self, resultComparatorResult, processingResultFile):
        print "Sets compared {}" \
            .format(resultComparatorResult.listOfSets)
        print "Matrix containing results: "
        print resultComparatorResult.resultMatrix

    def getName(self):
        return ConsoleComparisonResultProcessor.NAME


