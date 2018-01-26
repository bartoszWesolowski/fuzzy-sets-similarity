(function(_) {

    var app = angular.module('dataProviders', ['array-utils-module']);

    app.controller("MinkowskiController", function () {
        const minkowskiController = this;

        this.mainExample = {
            method: 'minkowski',
            setA: [0, 0, 0.7, 0, 0, 0.4, 0, 0, 0.6, 0, 0.3, 0],
            setB: [0, 0, 0.9585, 0, 0.0754, 0.5257, 0, 0.0104, 0.7333, 0, 0.6023, 0],
            config: {
                r: 2
            }
        }

        this.examples = [
            {
                method: 'minkowski',
                setA: [0, 0.5, 0.7, 0.5, 0],
                setB: [0, 0.2, 0.5, 0.2, 0],
                config: {
                    r: 2
                }
            },
            {
                method: 'minkowski',
                setA: [0, 0.1, 0.1, 0.1, 0.1],
                setB: [1, 0.9, 0.9, 0.9, 1],
                config: {
                    r: 3
                }
            },
            {
                method: 'minkowski',
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
                    method: 'minkowski',
                    r: 2
                }
            },
            {
                method: 'minkowski',
                setA: [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 1.0, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0],
                setB: [1, 0.9, 0.8, 0.7, 0.3, 0.0, 0.3, 0.5, 0.7, 0.9, 1, 0, 0, 0, 0, 0, ],
                config: {r: 2}
            },
        ];
    });

    app.controller("AngularDistanceController", function () {

        this.mainExample = {
            method: 'angular-distance',
            setA: [0, 0, 0.7, 0, 0, 0.4, 0, 0, 0.6, 0, 0.3, 0],
            setB: [0, 0, 0.9585, 0, 0.0754, 0.5257, 0, 0.0104, 0.7333, 0, 0.6023, 0],
        }

        this.examples = [
            {
                method: 'angular-distance',
                setA: [0, 0.5, 0.7, 0.5, 0],
                setB: [0, 0.2, 0.5, 0.2, 0],
            },
            {
                method: 'angular-distance',
                setA: [0, 0.1, 0.1, 0.1, 0.1],
                setB: [1, 0.9, 0.9, 0.9, 1],
            },
            {
                method: 'angular-distance',
                setA: [0],
                setB: [1],
            },
            {
                setA: [0, 0.1, 0.1, 0.8, 0.3, 0.7, 0.1, 0.1, 0.1],
                setB: [0, 0.1, 0.1, 0.8, 0.3, 0.7, 0.1, 0.1, 0.1],
                method: 'angular-distance',
            },
            {
                method: 'angular-distance',
                setA: [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 1.0, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0],
                setB: [1, 0.9, 0.8, 0.7, 0.3, 0.0, 0.3, 0.5, 0.7, 0.9, 1, 0, 0, 0, 0, 0, ],
            },
        ];
    });

    app.controller("ImplicationSimilarityController", function () {
        this.mainExample = {
            setA: [0, 0, 0.7, 0, 0, 0.4, 0, 0, 0.6, 0, 0.3, 0],
            setB: [0, 0, 0.9585, 0, 0.0754, 0.5257, 0, 0.0104, 0.7333, 0, 0.6023, 0],
            method:'implication-similarity',
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
                method:'implication-similarity',
                config:  {
                    aggregator: 'minimum',
                    tnorm: 'minimum',
                    implication: 'maximum'
                }
            },
            {
                setA: [0, 0.5, 0.7, 0.5, 0],
                setB: [0, 0.2, 0.5, 0.2, 0],
                method:'implication-similarity',
                config:  {
                    aggregator: 'average',
                    tnorm: 'minimum',
                    implication: 'maximum'
                }
            },
            {
                setA: [0, 0.1, 0.1, 0.1, 0.1, 0.9452, 0.4276, 0.5349],
                setB: [1, 0.9, 0.9, 0.9, 1, 0.5257, 0.786],
                method:'implication-similarity',
                config: {
                    aggregator: 'average',
                    tnorm: 'lukasiewicz',
                    implication: 'maximum'
                }
            },
            {
                setA: [0, 0.1, 0.1, 0.1, 0.1, 0.9452, 0.4276, 0.5349],
                setB: [1, 0.9, 0.9, 0.9, 1, 0.5257, 0.786],
                method:'implication-similarity',
                config: {
                    aggregator: 'average',
                    tnorm: 'lukasiewicz',
                    implication: 'lukasiewicz'
                }
            }
        ];
    });

    app.controller("ComparisonDataProvider", ['$scope', 'arrayUtils', function ($scope, arrayUtils) {

        const comparisonCtrl = this;

        this.chartConfig = {
            data: [
                [],
                []
            ]
        };


        this.summaryChartConfig = {
            series: ['Sumary'],
            data: [],
            labels:[]
        }

        $scope.$on('FUZZY_SIMILARITY_CALCULATED', function(event, data) {
           console.log('event: ' + data);

            comparisonCtrl.summaryChartConfig.data.push(data.result)
            comparisonCtrl.summaryChartConfig.labels.push(data.method)
        });

        this.configurations = [];

        this.rawFuzzySets = {
            setA: "1, 0.5, 0",
            setB: "0, 0.5, 1"
        }

        this.configurationsWithoutSets = [
            {
                method: "implication-similarity",
                config:  {
                    aggregator: 'minimum',
                    tnorm: 'minimum',
                    implication: 'maximum'
                }
            },
            {
                method: "implication-similarity",
                config:  {
                    aggregator: 'average',
                    tnorm: 'minimum',
                    implication: 'maximum'
                }
            },
            {
                method: "implication-similarity",
                config: {
                    aggregator: 'average',
                    tnorm: 'lukasiewicz',
                    implication: 'maximum'
                }
            },
            {
                method: "implication-similarity",
                config: {
                    aggregator: 'average',
                    tnorm: 'lukasiewicz',
                    implication: 'lukasiewicz'
                }
            },
            {
                method: "minkowski",
                config: {
                    r: 2
                }
            },
            {
                method: "minkowski",
                config: {
                    r: 2
                }
            },
            {
                method: "minkowski",
                config: {r: 2}
            },
        ];

        this.createValidConfigurations = function() {
            const setA = arrayUtils.stringToArray(this.rawFuzzySets.setA);
            const setB = arrayUtils.stringToArray(this.rawFuzzySets.setB);

            comparisonCtrl.summaryChartConfig.data = [];
            comparisonCtrl.summaryChartConfig.labels = [];

            this.chartConfig = {
                data: [
                    setA,
                    setB
                ],
                labels: _.range(Math.max(setA.length, setB.length))
            };


            const configurations = [];
            _.each(this.configurationsWithoutSets, (value) => {
                const copied = _.extend({}, value);
                copied.setA = setA;
                copied.setB = setB;
                configurations.push(copied);
            })
            return configurations;
        };


        //$scope.$watch("rawFuzzySets", (fuzzySetsInput) => {
        //    comparisonCtrl.configurations = comparisonCtrl.createValidConfigurations(angular.extend({}, fuzzySetsInput));
        //}, true);

        this.configurations = this.createValidConfigurations();

        this.calculateResult = function() {
            this.configurations = this.createValidConfigurations();
        };
    }]);

    app.factory('fuzzyApi', ['$http', function($http) {

        const url = '';//http://bartek887.pythonanywhere.com';

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

})(_);