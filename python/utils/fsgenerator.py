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
with open("randomsets.txt", "a") as myfile:
    for i in range(15):
        size = int(random.uniform(3, 5000))
        randomSet = randomFuzzyList(length=size)
        print len(randomSet)
        myfile.write(' '.join([str(x) for x in randomSet]) + "\n")
    for i in range(1):
        size = int(random.uniform(3, 5000))
        randomSet = singletonFuzzyList(length=size)
        print len(randomSet)
        myfile.write(' '.join([str(x) for x in randomSet]) + "\n")
    for i in range(1):
        size = int(random.uniform(3, 5000))
        randomSet = singletonFuzzyList(length=size, value=0.0)
        print len(randomSet)
        myfile.write(' '.join([str(x) for x in randomSet]) + "\n")
    for i in range(1):
        size = int(random.uniform(3, 5000))
        randomSet = singletonFuzzyList(length=size, value=0.5)
        print len(randomSet)
        myfile.write(' '.join([str(x) for x in randomSet]) + "\n")
