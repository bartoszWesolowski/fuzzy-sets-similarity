from sklearn.cluster import SpectralClustering
import fuzyficate_iris_dataset as fuzzyIris
import numpy as np

from comparators.sets_comparator import SetsComparator

setsComparator = SetsComparator()

fuzzyIrisesDataSet = fuzzyIris.getFuzzyficatedIrisDataSet()

fuzzyIrisesAsLists = []
for fuzzyIris in fuzzyIrisesDataSet.fuzzyfiedDataset:
    fuzzyIrisesAsLists.append(fuzzyIris.fuzzySetArray())

comparisonResult = setsComparator.compareSets(fuzzyIrisesAsLists, comparisonMethodConfig={"r": 2, "method": "minkowski"})

print comparisonResult.resultMatrix
X = np.array([[1, 1], [2, 1], [1, 0],
              [4, 7], [3, 5], [3, 6]])

sc = SpectralClustering(3, affinity='precomputed', n_init=100,
                         assign_labels='discretize')

predict = sc.fit_predict(comparisonResult.resultMatrix)
print predict

import itertools
for key, group in itertools.groupby(predict[0:50]):
    print key, group
for key, group in itertools.groupby(predict[50:100]):
    print key, group

for key, group in itertools.groupby(predict[100:150]):
    print key, group

