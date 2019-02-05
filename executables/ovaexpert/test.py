from patient_fuzzy_result import PatientResultReader
from comparators.sets_comparator import SetsComparator

import numpy as np
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
        self.comparisonResults.sort(key=lambda comparisonResult: comparisonResult[1], reverse=True)

    def getPatientsWithSimilarityGraterThanTreshold(self, treshold=0.8):
        return filter(lambda camparisonResult: camparisonResult[1] > treshold, self.comparisonResults)

    def getMostSimilarPatients(self, numberOfPatientsToReturn=5):
        """

        :rtype: list
        """
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

class ComparisonResultStatistics(object):
    def __init__(self):
        self.simi


def comparePatients(fuzzyPatients, similarityMethodConfig):
    """

    :rtype: PatientsComparisonResult
    """
    fuzyPatientsAsFuzzySets = map(lambda fuzzyPatient: fuzzyPatient.getNumericValues(), fuzzyPatients)
    comparisonResult = setsComparator.compareSets(fuzyPatientsAsFuzzySets, similarityMethodConfig)
    return PatientsComparisonResult(fuzzyPatients, comparisonResult)


def findSimilarPatients(patientsComparisonResult, treshold=0.7):
    hits = 0
    similarPatientsCount = 0
    ratio = 0
    for patientComparison in patientsComparisonResult.patientsComparisons:
        patients = []
        sourcePatientData = patientsData.getPatientWithId(patientComparison.sourcePatient.id)
        patients.append(sourcePatientData)
        print "Fuzzy patients result most similar to: "
        print patientComparison.sourcePatient.toString()
        for similarPatients in patientComparison.getPatientsWithSimilarityGraterThanTreshold(treshold):
            similarPatientsCount = similarPatientsCount + 1
            fuzzyPatient = similarPatients[0]
            if patientComparison.sourcePatient.malignancyCharacter == fuzzyPatient.malignancyCharacter:
                hits = hits + 1
            patient = patientsData.getPatientWithId(fuzzyPatient.id)
            patients.append(patient)
            # print "{} -> {}".format(fuzzyPatient.toString(), similarPatients[1])
    print "Similar patients found: {}".format(similarPatientsCount)
    print "Patients with same character: {}".format(hits)
    if similarPatientsCount != 0:
        ratio = hits / float(similarPatientsCount)
        print "Ratio: {}".format(ratio)
    # print "Patients data: "
    # print sourcePatientData.formatHeaders()
    # for patient in patients:
    #     print patient.toString()
    print "\n\n\n"

    return {
        'hits': hits,
        'similarPatientsCount': similarPatientsCount,
        'ratio': ratio,
    }
methods = [
    {"r": 1, "method": "minkowski"},
    {"r": 2, "method": "minkowski"},
    {"method": "angular-distance"},

    {
        "aggregator": "average",
        "implication": "lukasiewicz",
        "method": "implication-similarity",
        "tnorm": "lukasiewicz"
    },
    {
        "aggregator": "average",
        "implication": "maximum",
        "method": "implication-similarity",
        "tnorm": "minimum"
    },
    {
        "aggregator": "average",
        "method": "simplified-jaccard-index",
        "tknorm": "maxiumum",
        "tnorm": "minimum"
    },
    {
        "aggregator": "average",
        "method": "simplified-jaccard-index",
        "tknorm": "lukasiewicz",
        "tnorm": "lukasiewicz"
    },
    {
        "aggregator": "average",
        "method": "simplified-jaccard-index",
        "tknorm": "probabilistic",
        "tnorm": "algebraic"
    },
]

results = []
comparisonResult = comparePatients(fuzzyPatients, methods[1])
for treshold in np.arange(0.1, 1.01, 0.1):
    similarPatientsSummary = findSimilarPatients(comparisonResult, treshold)
    similarPatientsSummary['treshold'] = treshold
    similarPatientsSummary['methodConfig'] = methods[1]
    results.append(similarPatientsSummary)

for summary in results:
    print summary

for summary in results:
    print "{} & {} & {} & {} \\\\".format("{0:.2f}".format(summary['treshold']), summary['similarPatientsCount'], summary['hits'], "{0:.2f}".format(summary['ratio']))
