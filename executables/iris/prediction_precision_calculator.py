import itertools
from collections import Counter


class PredictionPrecisionCalculator(object):
    def __init__(self, actualClasses, predictedClasses):
        """
        
        :param actualClasses: lista zawierajaca prawdziwe id klas, wartos na i-tym indexie zawiera id klasy przypisanej do i-tego obiektu
        :param predictedClasses: lista zawierajaca przypisane przez algorytm grupujacy id klas, 
        wartos na i-tym indexie zawiera id klasy przypisanej do i-tego obiektu
        poniewaz prawdziwe id klasy nie musza zawsze odpowiadac tym ktore przypisal algorytm grupujacy ciezko jest na pierwszy rzut oka stwierdzic
        czy klastrowanie jest poprawne
        Klasa ta sprawdza wszystkie mozliwe mapowania pomiedzy prawdziwmi id klas a tymi przypisanymi przez algorytm,
        i szuka tego najlepszego, dla ktorego trafnosc grupowania jest najwieksza
        """
        self.actualClasses = actualClasses
        self.actualClassLabels = list(set(actualClasses))

        self.predictedClasses = predictedClasses
        self.predictedClassLabels = list(set(predictedClasses))

        # TODO: co jesli jest mniej klas wyznaczynych w predictedClasses?

    def getClassMappings(self):
        """wyznacza wszystkie mozliwe mapowania wyznaczony klas (predictionClasse) na prawdziwe klasy"""
        actualClassesPermutations = list(itertools.permutations(list(self.actualClassLabels)))
        predictedToActualClassMappings = []
        for actualClassPermutation in actualClassesPermutations:
            mapping = {}
            for index, actualClassLabel in enumerate(actualClassPermutation):
                mapping[self.predictedClassLabels[index]] = actualClassLabel

            predictedToActualClassMappings.append(mapping)

        return predictedToActualClassMappings

    def getAllPossiblePredictions(self):
        """wyznacza wszystkie mozliwe listy z wyznaczynymi klasami, zmapowane do prawdziwych klas"""
        classMappings = self.getClassMappings()
        possiblePredictions = []
        for mapping in classMappings:
            translatedPrediction = map(lambda predictionClass: mapping[predictionClass], self.predictedClasses)
            possiblePredictions.append(translatedPrediction)

        return possiblePredictions

    def getAccuracy(self, actualClasses, prediction):
        hits = 0
        for index, predictionClass in enumerate(prediction):
            if actualClasses[index] == predictionClass:
                hits += 1
        return hits / float(len(actualClasses))

    def getAccuracyOfPrediction(self):
        """Zwraca pare, pierwszy element to maksymalna trafnosc, a drugi to prediction, zmapowany do prawdziwych klas
        przy ktorym otrzymana najwieksza trafnosc"""
        possiblePredictions = self.getAllPossiblePredictions()
        accuracies = []
        for possiblePrediction in possiblePredictions:
            accuracy = self.getAccuracy(self.actualClasses, possiblePrediction)
            accuracies.append(accuracy)

        maxAccuracy = max(accuracies)
        maxAccuracyIndex = accuracies.index(maxAccuracy)
        bestPrediction = possiblePredictions[maxAccuracyIndex]
        print "Accuracies: {}".format(accuracies)
        return maxAccuracy, bestPrediction
