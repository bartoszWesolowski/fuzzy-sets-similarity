from openpyxl import Workbook

class ConnsoleResultProcessor(object):
    def processResult(self, result, metadata):
        print "Result: {}, config: {} ".format(result, metadata.config)


class ExcelResultProcessor(ConnsoleResultProcessor):

    def __init__(self, numberOfSets, workbookFile='sample.xlsx'):
        self.workbook = Workbook()
        self.sheet = self.workbook.active
        self.sheet.title = 'Fuzzy set similarity result'
        self.sheet.append(range(numberOfSets))
        self.workbookFile = workbookFile

    def processResult(self, result, metadata):
        print "Result: {}, config: {}. Stored in cell: (row, col): ({}, {})".format(result, metadata.config,
                                                                                    metadata.setAindex,
                                                                                    metadata.setBindex)
        self.sheet.cell(column=metadata.setAindex + 1, row=metadata.setBindex + 1, value=result)

    def save(self):
        self.workbook.save(self.workbookFile)
