from fuzzyfacades.similarity_calculator_wrapper import SimilarityCalculatorFacade
from sets_comparosion_result import SetsComparisonResultBuilder


class SetsComparator(object):
    """Class for comparing list of sets against each other using passed comparison method config"""

    def compareTwoSets(self, listOfSets, otherListOfSets, comparisonMethodConfig):
        # type: (object, object, object) -> SetsComparisonResult
        """Copares all of sets in the list (each with each) using comparison method
        defined in <code>comparisonMethodConfig</code>
        :param ID - unique ID of this sets comparison 
        :return SetsComparisonResult object"""
        print "Comparing {} fuzzy sets against each other".format(len(listOfSets))
        numberOfSets = len(listOfSets)
        similarityCalculatorWrapper = SimilarityCalculatorFacade()
        setsComparisonResultBuilder = SetsComparisonResultBuilder(listOfSets, otherListOfSets) \
            .withConfig(comparisonMethodConfig)
        for i in range(numberOfSets):
            for j in range(i, len(otherListOfSets)):
                A = listOfSets[i]
                B = otherListOfSets[j]
                result = similarityCalculatorWrapper.calculateSimilarityFromParsedConfig(A, B, comparisonMethodConfig)
                setsComparisonResultBuilder.withResultEntry((i, j), result)

        return setsComparisonResultBuilder.build()

    def compareSets(self, listOfSets, comparisonMethodConfig):
        """Copares all of sets in the list (each with each) using comparison method
        defined in <code>comparisonMethodConfig</code>
        :param ID - unique ID of this sets comparison 
        :return SetsComparisonResult object"""
        return self.compareTwoSets(listOfSets, listOfSets, comparisonMethodConfig)
