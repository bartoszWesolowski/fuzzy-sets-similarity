from patient_fuzzy_result import PatientResultReader
from comparators.sets_comparator import SetsComparator

setsComparator = SetsComparator()
fuzzyResultReader = PatientResultReader()
fuzzyPatients = fuzzyResultReader.readFuzzyPatientResults('input/fuzzy_patient_results.xlsx')
patientsData = fuzzyResultReader.readPatients('input/patient_data.xlsx', sheetName='patients')

class PatientComparison(object):
    """
    Class stores a source patient with a list of other patients with similarity between those two
    """
    def __init__(self, sourcePatient):
        self.sourcePatient = sourcePatient
        self.comparisonResults = []

    def comparedWithPatient(self, otherPatient, similarity):
        self.comparisonResults.append((otherPatient, similarity))

    def getMostSimilarPatients(self, numberOfPatientsToReturn=5):
        self.comparisonResults.sort(key=lambda comparisonResult: comparisonResult[1], reverse=True)
        return self.comparisonResults[:numberOfPatientsToReturn]


class PatientsComparisonResult(object):
    # noinspection PyNoneFunctionAssignment
    def __init__(self, fuzzyPatients, comparisonResult):
        self.fuzzyPatients = fuzzyPatients
        self.comparisonResult = comparisonResult
        self.patientsComparisons = []
        for patientIndex in range(len(self.fuzzyPatients)):
            patientComparison = self.__getPatientComparison__(patientIndex)
            self.patientsComparisons.append(patientComparison)


    def __getPatientComparison__(self, consideredPatientIndex):
        similarities = self.comparisonResult.resultMatrix[consideredPatientIndex]
        patient = self.fuzzyPatients[consideredPatientIndex]
        patientComparison = PatientComparison(patient)
        for index, element in enumerate(similarities):
            if index != consideredPatientIndex:
                patientComparison.comparedWithPatient(self.fuzzyPatients[index], similarities[index])

        return patientComparison


def comparePatients(fuzzyPatients, similarityMethodConfig):
    fuzyPatientsAsFuzzySets = map(lambda fuzzyPatient: fuzzyPatient.getNumericValues(), fuzzyPatients)
    comparisonResult = setsComparator.compareSets(fuzyPatientsAsFuzzySets, similarityMethodConfig)
    return PatientsComparisonResult(fuzzyPatients, comparisonResult)


patientsComparisonResult = comparePatients(fuzzyPatients, {"r": 2, "method": "minkowski"})


for patientComparison in patientsComparisonResult.patientsComparisons:
    patients = []
    sourcePatientData = patientsData.getPatientWithId(patientComparison.sourcePatient.id)
    patients.append(sourcePatientData)
    print "Fuzzy patients result most similar to: "
    print patientComparison.sourcePatient.toString()
    for similarPatients in patientComparison.getMostSimilarPatients():
        fuzzyPatient = similarPatients[0]
        patient = patientsData.getPatientWithId(fuzzyPatient.id)
        patients.append(patient)
        print "{} -> {}".format(fuzzyPatient.toString(), similarPatients[1])

    print "Patients data: "
    print sourcePatientData.formatHeaders()
    for patient in patients:
        print patient.toString()
    print "\n\n\n"
