import numpy


def nthRoot(x, n):
    """Should calculate prcise n-th root of number x"""
    return x ** (1 / float(n))


def clamp(array, minValue=0, maxValue=1):
    """Clamps all values in array to range specified by min and max value parameters."""
    result = []
    for x in array:
        result.append(numpy.clip(x, minValue, maxValue))
    return result


def squere(x):
    return x ** 2


def sum(x, y):
    return x + y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y