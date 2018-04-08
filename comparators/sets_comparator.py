from fuzzyfacades.similarity_calculator_wrapper import SimilarityCalculatorWrapper
from sets_comparosion_result import SetsComparisonResultBuilder


class SetsComparator(object):
    """Class for comparing list of sets against each other using passed comparison method config"""

    def compareSets(self, listOfSets, comparisonMethodConfig):
        """Copares all of sets in the list (each with each) using comparison method
        defined in <code>comparisonMethodConfig</code>
        :param ID - unique ID of this sets comparison 
        :return SetsComparisonResult object"""
        print "Comparing {} fuzzy sets against each other".format(len(listOfSets))
        numberOfSets = len(listOfSets)
        similarityCalculatorWrapper = SimilarityCalculatorWrapper()
        setsComparisonResultBuilder = SetsComparisonResultBuilder(listOfSets) \
            .withConfig(comparisonMethodConfig)
        for i in range(numberOfSets):
            for j in range(i, numberOfSets):
                A = listOfSets[i]
                B = listOfSets[j]
                result = similarityCalculatorWrapper.calculateSimilarityFromParsedConfig(A, B, comparisonMethodConfig)
                setsComparisonResultBuilder.withResultEntry((i, j), result)

        return setsComparisonResultBuilder.build()
