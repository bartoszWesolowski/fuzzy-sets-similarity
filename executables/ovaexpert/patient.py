class Patient(object):
    def __init__(self, patientExcelRow):
        self.patientRow = patientExcelRow

    def toFuzzySet(self):
        return []