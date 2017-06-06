import random


def randomFuzzyList(length=20, min=0, max=1, digits=4):
    '''create an array of lenght with elements grater or equal to min and less or equal than max 
    - array represent random fuzzy set'''
    result = []
    for i in range(length):
        randomValue = random.uniform(min, max)
        result.append(round(randomValue, digits))
    return result
