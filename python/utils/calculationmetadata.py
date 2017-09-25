class SimilarityCalculationMetaData:
    config = {}
    setA = [],
    setB = [],
    configIndex = 0,
    setAindex = 0,
    setBindex = 0,

    def __init__(self, config, setA, setB, configIndex, setAindex, setBindex):
        self.config = config
        self.setA = setA
        self.setB = setB
        self.configIndex = configIndex
        self.setAindex = setAindex
        self.setBindex = setBindex