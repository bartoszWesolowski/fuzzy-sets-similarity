import unittest
from angle import angluardistance
from utils.fuzzyset import FuzzySet

class BasicTestSuite(unittest.TestCase):
    maxError = 0.000001
    exampleSet = FuzzySet([0, 0.1, 0.3, 0.5, 0.7, 0.9, 1])

    def test_similarity_of_equal_sets_should_be_one(self):
        similarity = angluardistance.sim(self.exampleSet, self.exampleSet)
        self.assertEqual(1.0, similarity)

    def test_similarity_of_set_multiplied_by_should_be_one(self):
        transformed = self.exampleSet.transform(lambda x: x * 0.1)
        similarity = angluardistance.sim(transformed.elements, self.exampleSet.elements)

        transformed = self.exampleSet.transform(lambda x: x * 0.5)
        similarity = angluardistance.sim(transformed.elements, self.exampleSet.elements)
        self.assertEqual(1.0, similarity)

        #Does not work when values multiplied by scalar are grated then 1 - base of FuzzySet implemenation that does not
        #allow a fuzzy set to have elements that has values grated than 1 and smaller than 0.
        #Works for scalars form range [0, 1)
        #transformed = self.exampleSet.transform(lambda x: x * 2)
        #similarity = angluardistance.sim(transformed.elements, self.exampleSet.elements)
        #self.assertEqual(1.0, similarity)

    def test_similarity_of_equal_sets_should_be_one(self):
        similarity = angluardistance.sim(self.exampleSet.elements, self.exampleSet.elements)
        self.assertEqual(1.0, similarity)