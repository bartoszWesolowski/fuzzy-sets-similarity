(function (_) {

    var app = angular.module('dataProviders', ['array-utils-module']);

    app.factory('fuzzyApi', ['$http', function ($http) {

        const url = '';//http://bartek887.pythonanywhere.com';

        const calculateSimilarity = function (requestBody) {
            return $http.post(`${url}/fuzzy/similarity`, requestBody);
        };

        const getAggregators = function () {
            return $http.get(`${url}/fuzzy/aggregators`);
        };

        const getAvailableDataSets = function () {
            return $http.get(`${url}/fuzzy/data-sets`);
        };

        const getDataSet = function (key) {
            return $http.get(`${url}/fuzzy/data-sets/${key}`);
        };

        return {
            calculateSimilarity,
            getAggregators,
            getAvailableDataSets,
            getDataSet
        }
    }]);

    app.controller("MinkowskiController", function () {
        const minkowskiController = this;

        this.mainExample = {
            method: 'minkowski',
            setA: [0, 0, 0.7, 0, 0, 0.4, 0, 0, 0.6, 0, 0.3, 0],
            setB: [0, 0, 0.9585, 0, 0.0754, 0.5257, 0, 0.0104, 0.7333, 0, 0.6023, 0],
            r: 2
        };

        this.examples = [
            {
                method: 'minkowski',
                setA: [0, 0.5, 0.7, 0.5, 0],
                setB: [0, 0.2, 0.5, 0.2, 0],
                r: 2

            },
            {
                method: 'minkowski',
                setA: [0, 0.1, 0.1, 0.1, 0.1],
                setB: [1, 0.9, 0.9, 0.9, 1],
                r: 3
            },
            {
                method: 'minkowski',
                setA: [0],
                setB: [1],
                r: 2
            },
            {
                setA: [0, 0.1, 0.1, 0.8, 0.3, 0.7, 0.1, 0.1, 0.1],
                setB: [0, 0.1, 0.1, 0.8, 0.3, 0.7, 0.1, 0.1, 0.1],
                method: 'minkowski',
                r: 2
            },
            {
                method: 'minkowski',
                setA: [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 1.0, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0],
                setB: [1, 0.9, 0.8, 0.7, 0.3, 0.0, 0.3, 0.5, 0.7, 0.9, 1, 0, 0, 0, 0, 0,],
                r: 2
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
                setB: [1, 0.9, 0.8, 0.7, 0.3, 0.0, 0.3, 0.5, 0.7, 0.9, 1, 0, 0, 0, 0, 0,],
            },
        ];
    });

    app.controller("ImplicationSimilarityController", function () {
        this.mainExample = {
            setA: [0, 0, 0.7, 0, 0, 0.4, 0, 0, 0.6, 0, 0.3, 0],
            setB: [0, 0, 0.9585, 0, 0.0754, 0.5257, 0, 0.0104, 0.7333, 0, 0.6023, 0],
            method: 'implication-similarity',
            aggregator: 'average',
            tnorm: 'minimum',
            implication: 'maximum'
        }

        this.examples = [
            {
                setA: [0, 0.5, 0.7, 0.5, 0],
                setB: [0, 0.2, 0.5, 0.2, 0],
                method: 'implication-similarity',
                aggregator: 'minimum',
                tnorm: 'minimum',
                implication: 'maximum'

            },
            {
                setA: [0, 0.5, 0.7, 0.5, 0],
                setB: [0, 0.2, 0.5, 0.2, 0],
                method: 'implication-similarity',
                aggregator: 'average',
                tnorm: 'minimum',
                implication: 'maximum'

            },
            {
                setA: [0, 0.1, 0.1, 0.1, 0.1, 0.9452, 0.4276, 0.5349],
                setB: [1, 0.9, 0.9, 0.9, 1, 0.5257, 0.786],
                method: 'implication-similarity',
                aggregator: 'average',
                tnorm: 'lukasiewicz',
                implication: 'maximum'

            },
            {
                setA: [0, 0.1, 0.1, 0.1, 0.1, 0.9452, 0.4276, 0.5349],
                setB: [1, 0.9, 0.9, 0.9, 1, 0.5257, 0.786],
                method: 'implication-similarity',
                aggregator: 'average',
                tnorm: 'lukasiewicz',
                implication: 'lukasiewicz'

            }
        ];
    });

    app.controller("ComparisonDataProvider", ['$scope', 'arrayUtils', 'fuzzyApi', function ($scope, arrayUtils, fuzzyApi) {

        const comparisonCtrl = this;

        this.chartConfig = {
            data: [
                [],
                []
            ]
        };

        this.selectedDataSetKey = '';

        this.similarityCalculationResults = {};

        this.summaryChartConfig = {
            series: ['Sumary'],
            data: [],
            labels: [],
            options: {
                scales: {
                    yAxes: [{
                        display: true,
                        ticks: {
                            suggestedMin: 0
                        }
                    }]
                }
            }
        };

        this.configurations = [];

        this.rawFuzzySets = {
            setA: "1, 0.5, 0",
            setB: "0, 0.5, 1"
        }

        this.configurationsWithoutSets = [
            {
                method: "implication-similarity",
                aggregator: 'minimum',
                tnorm: 'minimum',
                implication: 'maximum'
            },
            {
                method: "implication-similarity",
                aggregator: 'average',
                tnorm: 'minimum',
                implication: 'maximum'

            },
            {
                method: "implication-similarity",
                aggregator: 'average',
                tnorm: 'lukasiewicz',
                implication: 'maximum'

            },
            {
                method: "implication-similarity",
                aggregator: 'average',
                tnorm: 'lukasiewicz',
                implication: 'lukasiewicz'

            },
            {
                method: "minkowski",
                r: 2

            },
            {
                method: "minkowski",
                r: 2

            },
            {
                method: "minkowski",
                r: 2
            },
        ];

        this.createValidConfigurations = function () {
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
            _.each(this.configurationsWithoutSets, (value, index) => {
                const copied = _.extend({}, value);
                copied.setA = setA;
                copied.setB = setB;
                copied.id = index;
                configurations.push(copied);
            })
            return configurations;
        };

        this.getDataSet = function (key) {
            if (!key) {
                return;
            }
            fuzzyApi.getDataSet(key)
                .then(
                    (successResponse) => {
                        const responseBody = successResponse.data.dataSet;
                        comparisonCtrl.configurationsWithoutSets = responseBody.methods;
                        comparisonCtrl.rawFuzzySets = responseBody.rawSets;
                        comparisonCtrl.calculateResult();
                        console.log(successResponse);
                    },
                    (errorResponse) => {
                        console.log(errorResponse);
                    }
                );
        };

        this.configurations = this.createValidConfigurations();

        this.calculateResult = function () {
            this.configurations = this.createValidConfigurations();
            this.similarityCalculationResults = {};
        };

        $scope.$on('FUZZY_SIMILARITY_CALCULATED', function (event, data) {
            console.log('event: ' + data);
            comparisonCtrl.similarityCalculationResults[data.id] = data;
            const storedResults = Object.values(comparisonCtrl.similarityCalculationResults);
            const sortedResults = _.sortBy(storedResults, ['id']);
            const results = _.map(sortedResults, o => o.result);
            const labels = _.map(sortedResults, o => o.method);
            comparisonCtrl.summaryChartConfig.data = results;
            comparisonCtrl.summaryChartConfig.labels = labels;
        });

        $scope.$watch('comparisonCtrl.selectedDataSetKey', function(newValue) {
            comparisonCtrl.getDataSet(newValue);
            console.log(newValue);
        }, true);
    }]);


})(_);