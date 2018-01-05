import random


def randomFuzzyList(length=20, min=0, max=1, digits=4):
    '''create an array of lenght with elements grater or equal to min and less or equal than max 
    - array represent random fuzzy set'''
    result = []
    for i in range(length):
        randomValue = random.uniform(min, max)
        result.append(round(randomValue, digits))
    return result


def singletonFuzzyList(length=20, value=1, digits=4):
    '''create an array of lenght with elements equal to value'''
    result = []
    for i in range(length):
        result.append(round(value, digits))
    return result


def triangualrSetFunctionn(x):
    """Funkcja przynaleznosci elementu x do wzorcowego zbioru trojkatnego
    Definicja w pracy magisterskiej, strona 40. TODO: English wersion"""
    value = 0
    if x <= 0:
        value = max(0, (1 + x) / 2.0)
    else:
        value = max(0, (1 - x) / 2.0)
    return value


def triangularSet(setRange, xTransofrm=1, yTransform=1):
    """Generates transformation of triangular set defined by triangualrSetFunctionn
    """
    result = []
    for x in range(-setRange, setRange + 1):
        xArgument = (1 / float(xTransofrm)) * x
        result.append(yTransform * triangualrSetFunctionn(xArgument))

    return result


def triangular(x, a, b, c):
    if a < b < c:
        first = (x - a) / (b - a)
        second = (c - x) / (c - b)
        minimum = min(first, second)
        return max(0, minimum)
    else:
        raise AttributeError(
            "Creating triangular function requires the following arguments: a < b < c but found a = {}, b = {}, c = {}. ".format(
                a, b, c))


def trapeze(x, a, b, c, d):
    if a < b <= c < d:
        first = (x - a) / (b - a)
        second = (d - x) / (d -c)
        minimum = min(1, first, second)
        return max(0, minimum)
        return 0
    else:
        raise AttributeError()

print triangularSet(50, 1, 1)