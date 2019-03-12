def calculatePresisionAndReacall(actualGroups, predictedGroups):
    actual = toGroupToIndexesMap(actualGroups)
    predicted = toGroupToIndexesMap(predictedGroups)
    tp = getTruePositives(actual, predicted)
    fp = getFalsePositives(actual, predicted)
    fn = getFalseNegative(actual, predicted)
    recall = tp / float(fn + tp)
    precision = tp / float(fp + tp)
    fscore = (2 * precision * recall) / float(precision + recall)
    print "TP: {}".format(tp)
    print "FP: {}".format(fp)
    print "FN: {}".format(fn)
    print "FN: {}".format(fn)
    print "Recall: {}".format(recall)
    print "precision: {}".format(precision)
    print "fscore: {}".format(fscore)

def toGroupToIndexesMap(predictions):
    distinctPredictions = set(predictions)
    result = {}
    for prediction in distinctPredictions:
        result[prediction] = []

    for index, element in enumerate(predictions):
        result[element].append(index)

    return result

#sa w prawdziwym klastrze oraz sa w przypisanym klastrze
def getTruePositives(actual, predicted):
    clusters = actual.keys()
    result = 0
    for cluster in clusters:
        actualInCluster = actual[cluster]
        predictedInCluster = predicted[cluster]
        truePositivesInCluster = set(actualInCluster).intersection(predictedInCluster)
        result += len(truePositivesInCluster)

    return result

#sa w przypisanym klastrze ale nie ma ich w prawdziwym klastrze
def getFalsePositives(actual, predicted):
    clusters = actual.keys()
    result = 0
    for cluster in clusters:
        actualInCluster = actual[cluster]
        predictedInCluster = predicted[cluster]
        truePositivesInCluster = set(predictedInCluster).difference(actualInCluster)
        result += len(truePositivesInCluster)

    return result

#sa w prawdziwym klastrze ale nie ma ich w przypisanym klastrze
def getFalseNegative(actual, predicted):
    clusters = actual.keys()
    result = 0
    for cluster in clusters:
        actualInCluster = actual[cluster]
        predictedInCluster = predicted[cluster]
        truePositivesInCluster = set(actualInCluster).difference(predictedInCluster)
        result += len(truePositivesInCluster)

    return result


actual = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
predicted = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2, 1, 0, 2, 1, 2, 2, 2, 2, 1, 2, 1, 2, 1, 1, 1, 2, 2, 1, 2, 2, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 2, 1, 0, 1, 1, 1, 2, 0, 1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 1, 1, 1, 2, 1, 1, 1, 2, 2, 1, 2, 1, 2, 1, 0, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2]

# test = toGroupToIndexesMap(actual)
# tesPRediction = toGroupToIndexesMap(predicted)

calculatePresisionAndReacall(actual, predicted)