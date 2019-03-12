import numpy as np


def calculateDifferenceMatrix(predictions, elements):
    """
    
    :param predictions: :type: list
    :param elements: :type: list of lists
    :return: 
    """
    clusters = set(predictions)
    elementsAsNumpyVectors = map(lambda e: np.array(e), elements)
    predictionsToElementsMap = __getPredictionToElementsMap__(predictions, elementsAsNumpyVectors)
    summary = 0
    for cluster in clusters:
        elementsInCluster = predictionsToElementsMap[cluster]
        averageVector = __getAverageVector__(elementsInCluster)
        for element in elementsInCluster:
            substracted = element - averageVector
            multiplied = np.matmul(substracted, substracted)
            summary += multiplied

    return summary


def __getPredictionToElementsMap__(predictions, elements):
    clusters = set(predictions)
    result = {}
    for cluster in clusters:
        result[cluster] = []

    for index, prediction in enumerate(predictions):
        result[prediction].append(elements[index])

    return result


def __getAverageVector__(listOfVectors):
    size = len(listOfVectors)
    summary = sum(listOfVectors)
    return summary / float(size)
