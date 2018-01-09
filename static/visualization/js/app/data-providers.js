(function() {

    var app = angular.module('dataProviders', []);

    app.controller("MinkowskiController", function () {
        this.mainExample = {
            setA: [0, 0, 0.7, 0, 0, 0.4, 0, 0, 0.6, 0, 0.3, 0],
            setB: [0, 0, 0.9585, 0, 0.0754, 0.5257, 0, 0.0104, 0.7333, 0, 0.6023, 0],
            config: {
                r: 2
            }
        }
        this.examples = [
            {
                setA: [0, 0.5, 0.7, 0.5, 0],
                setB: [0, 0.2, 0.5, 0.2, 0],
                config: {
                    r: 2
                }
            },
            {
                setA: [0, 0.1, 0.1, 0.1, 0.1],
                setB: [1, 0.9, 0.9, 0.9, 1],
                config: {
                    r: 3
                }
            },
            {
                setA: [0],
                setB: [1],
                config: {
                    r: 2
                }
            },
            {
                setA: [0, 0.1, 0.1, 0.8, 0.3, 0.7, 0.1, 0.1, 0.1],
                setB: [0, 0.1, 0.1, 0.8, 0.3, 0.7, 0.1, 0.1, 0.1],
                config: {
                    r: 2
                }
            },
            {
                setA: [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 1.0, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0],
                setB: [1, 0.9, , 0.8, , 0.7, , 0.3, 0.0, 0.3, 0.5, 0.7, 0.9, 1, 0, 0, 0, 0, 0, ],
                config: {r: 2}
            },
        ];
    });

    app.controller("ImplicationSimilarityController", function () {
        this.mainExample = {
            setA: [0, 0, 0.7, 0, 0, 0.4, 0, 0, 0.6, 0, 0.3, 0],
            setB: [0, 0, 0.9585, 0, 0.0754, 0.5257, 0, 0.0104, 0.7333, 0, 0.6023, 0],
            config: {
                aggregator: 'average',
                tnorm: 'minimum',
                implication: 'maximum'
            }
        }
        this.examples = [
            {
                setA: [0, 0.5, 0.7, 0.5, 0],
                setB: [0, 0.2, 0.5, 0.2, 0],
                config:  {
                    aggregator: 'minimum',
                    tnorm: 'minimum',
                    implication: 'maximum'
                }
            },
            {
                setA: [0, 0.5, 0.7, 0.5, 0],
                setB: [0, 0.2, 0.5, 0.2, 0],
                config:  {
                    aggregator: 'average',
                    tnorm: 'minimum',
                    implication: 'maximum'
                }
            },
            {
                setA: [0, 0.1, 0.1, 0.1, 0.1, 0.9452, 0.4276, 0.5349],
                setB: [1, 0.9, 0.9, 0.9, 1, 0.5257, 0.786],
                config: {
                    aggregator: 'average',
                    tnorm: 'lukasiewicz',
                    implication: 'maximum'
                }
            },
            {
                setA: [0, 0.1, 0.1, 0.1, 0.1, 0.9452, 0.4276, 0.5349],
                setB: [1, 0.9, 0.9, 0.9, 1, 0.5257, 0.786],
                config: {
                    aggregator: 'average',
                    tnorm: 'lukasiewicz',
                    implication: 'lukasiewicz'
                }
            },
            {
                setA: [0],
                setB: [1],
                config: {
                    r: 2
                }
            },
            {
                setA: [0, 0.1, 0.1, 0.8, 0.3, 0.7, 0.1, 0.1, 0.1],
                setB: [0, 0.1, 0.1, 0.8, 0.3, 0.7, 0.1, 0.1, 0.1],
                config: {
                    r: 2
                }
            },
            {
                setA: [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 1.0, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0],
                setB: [1, 0.9, , 0.8, , 0.7, , 0.3, 0.0, 0.3, 0.5, 0.7, 0.9, 1, 0, 0, 0, 0, 0, ],
                config: {r: 2}
            },
        ];
    });

    app.factory('fuzzyApi', ['$http', function($http) {

        const url = 'http://bartek887.pythonanywhere.com';

        const calculateSimilarity = function (requestBody) {
            return $http.post(`${url}/fuzzy/similarity`, requestBody);
        }

        const getAggregators = function() {
            return $http.get(`${url}/fuzzy/aggregators`);
        }

        return {
            calculateSimilarity,
            getAggregators
        }
    }]);

})();