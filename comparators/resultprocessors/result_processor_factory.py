from console_comparison_result_processor import ConsoleComparisonResultProcessor
from excel_comparison_result_processor import ExcelResultProcessor

class ResultProcessorFactory(object):

    PROCESSORS = [
        ConsoleComparisonResultProcessor(),
        ExcelResultProcessor()
    ]

    def createResultProcessor(self, name):
        for processor in ResultProcessorFactory.PROCESSORS:
            if processor.getName() == name:
                return processor

        raise AttributeError("Can not create result processor for name: {}".format(name))

    def supportedProcessorsNames(self):
        return [x.getName() for x in ResultProcessorFactory.PROCESSORS]