class SimilarityMethod(object):
    def __init__(self, name, similarityCalculator, configurationParser):
        self.name = name
        self.similarityCalculator = similarityCalculator
        self.configurationParser = configurationParser
