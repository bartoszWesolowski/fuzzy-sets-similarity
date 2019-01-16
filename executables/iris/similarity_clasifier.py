from sklearn.cluster import SpectralClustering
from prediction_precision_calculator import PredictionPrecisionCalculator
import itertools
from collections import Counter
import numpy as np

import fuzyficate_iris_dataset as fuzzy_iris

from comparators.sets_comparator import SetsComparator

setsComparator = SetsComparator()

fuzzyIrisesDataSet = fuzzy_iris.getFuzzyficatedIrisDataSet(numberOfPossibleValuesForEachFeature=20,
                                                           rangeOfAroudValueFuzzySetScalar=0.1)
print "First fuzzy iris sepal lenght set: "
print fuzzyIrisesDataSet.fuzzyfiedDataset[0].sepalLen

print "Fuzzyficated irises"
print fuzzyIrisesDataSet.toFuzzySetFileFormat()


def groupIrisesUsingSimilarityMethod(methodConfig):
    fuzzyIrisesAsLists = []
    for fuzzy_iris in fuzzyIrisesDataSet.fuzzyfiedDataset:
        fuzzyIrisesAsLists.append(fuzzy_iris.fuzzySetArray())
    # print "Creating similarity matrix"
    comparisonResult = setsComparator.compareSets(fuzzyIrisesAsLists,
                                                  comparisonMethodConfig=methodConfig)

    sc = SpectralClustering(3, affinity='precomputed', n_init=100,
                            assign_labels='discretize')
    predict = sc.fit_predict(comparisonResult.resultMatrix)
    # print predict
    return predict


def getMaxFromCounter(counter):
    return max(counter.items(), key=lambda pair: pair[1])


def summarizePrediction(prediction):
    """
    Summarize the array containing predictions for isis data set
    :param prediction: array containing 150 elements with values 0, 1, 2
    Assumes that prediction with most hits for each iris group is the right one. In case one group was the most 
    popular for more then one iris group then this will not summarize the output successfully.
    """
    print "Actual    types: {}".format(fuzzyIrisesDataSet.getIrisesTypes())
    print "Predicted types: {}".format(list(prediction))

    firsTypeCounter = Counter(prediction[0:50])
    bestPredictionForFirstType = getMaxFromCounter(firsTypeCounter)
    print "first type: {}".format(firsTypeCounter)
    secondTypeCounter = Counter(prediction[50:100])
    bestPredictionForSecondType = getMaxFromCounter(secondTypeCounter)
    print "second type: {}".format(secondTypeCounter)
    thirdTypeCounter = Counter(prediction[100:150])
    bestPredictionForThirdType = getMaxFromCounter(thirdTypeCounter)
    print "third type: {}".format(thirdTypeCounter)
    predictions = [bestPredictionForFirstType, bestPredictionForSecondType, bestPredictionForThirdType]
    groups = set(map(lambda pair: pair[0], predictions))
    hits = sum(map(lambda pair: pair[1], predictions))
    if len(groups) == 3:  # All types was counted.
        print "Positive hits: {}, hit rate: {}".format(hits, hits / float(150))
    else:
        print "FAILED TO CALCULATE THE AVERAGE NUMBER OF HITS"

    precisionCalculator = PredictionPrecisionCalculator(fuzzyIrisesDataSet.getIrisesTypes(), list(prediction))
    maxAccuracy, bestPrediction = precisionCalculator.getAccuracyOfPrediction()
    print "Accuracy rate: {}".format(maxAccuracy)
    print "Actual       types: {}".format(fuzzyIrisesDataSet.getIrisesTypes())
    print "max accuracy types: {}".format(bestPrediction)
    return maxAccuracy


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

headers = "alpha & "
latexTableContent = ""

for method in methods:
    headers += "{} & ".format(method['method'])

for alpha in np.arange(0.1, 2.1, 0.1):
    fuzzyIrisesDataSet = fuzzy_iris.getFuzzyficatedIrisDataSet(numberOfPossibleValuesForEachFeature=30,
                                                               rangeOfAroudValueFuzzySetScalar=alpha)
    latexTableContent += "{}\\% &".format(alpha * 100)
    for index, method in enumerate(methods):
        print "\n######################\nGrouping irises using config: {}", format(method)
        prediction = groupIrisesUsingSimilarityMethod(method)
        accuracy = summarizePrediction(prediction=prediction)
        ending = " \\"
        if index < len(methods) - 1:
            ending = " & "
        latexTableContent += "{}{}".format("{0:.2f}".format(accuracy), ending)

    latexTableContent += "\\ \n"

print headers
print latexTableContent
