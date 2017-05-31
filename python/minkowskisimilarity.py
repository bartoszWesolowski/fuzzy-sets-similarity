from fuzzyset import FuzzySet


def sim(A, B, r):
    numberOfElements = max(len(A), len(B))
    return 1 - (metric(A, B, r) / float(numberOfElements))


def metric(A, B, r):
    numberOfElements = max(len(A), len(B))
    fuzzySetA = FuzzySet(A)
    fuzzySetB = FuzzySet(B)
    sum = 0
    for i in range(numberOfElements):
        sum += abs(fuzzySetA.val(i) - fuzzySetB.val(i)) ** r

    return sum ** (1 / float(r))
