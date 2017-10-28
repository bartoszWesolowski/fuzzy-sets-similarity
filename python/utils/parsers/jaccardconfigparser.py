import abstractparser
from utils import paramethers as param
from utils import constants as const
from utils import fuzzysetevaluator

class JaccardConfigParser(abstractparser.AbstractConfigurationParser):
    requiredParameters = [param.ALPHA, param.BETA, param.GAMMA, param.EVALUATOR]

    def parse(self, rawConfigMap):

        print "Parsing config for jaccard_index"
        for parameter in self.requiredParameters:
            if parameter not in rawConfigMap.keys():
                raise AttributeError(
                    "Missing {} parameter for jaccards method. Required params: {}".format(parameter,
                                                                                           self.requiredParameters))

        alpha = self.parseToIntOrRaiseAttributeError(rawConfigMap[param.ALPHA],
                                                     "Can parse alpha paramether {}".format(config[param.ALPHA]))
        beta = self.parseToIntOrRaiseAttributeError(rawConfigMap[param.BETA],
                                                    "Can parse beta paramether {}".format(config[param.BETA]))
        gamma = self.parseToIntOrRaiseAttributeError(rawConfigMap[param.GAMMA],
                                                     "Can parse alpha paramether {}".format(config[param.GAMMA]))

        evaluator = rawConfigMap[param.EVALUATOR]
        if evaluator not in fuzzysetevaluator.SUPPORTED_EVALUATORS:
            raise AttributeError(
                "Not supported evaluator found: {}. Supported evaluators: {}".format(evaluator,
                                                                                     fuzzysetevaluator.SUPPORTED_EVALUATORS))

        return {
            const.METHOD_PARAM_NAME: const.JACCARD_INDEX,
            param.ALPHA: alpha,
            param.BETA: beta,
            param.GAMMA: gamma,
            param.EVALUATOR: fuzzysetevaluator.EVALUATORS[evaluator]
        }
