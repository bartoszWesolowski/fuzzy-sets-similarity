def probabilisticSum(a, b):
    return a + b - a * b


def lukasiewicz(a, b):
    return min(a + b, 1)