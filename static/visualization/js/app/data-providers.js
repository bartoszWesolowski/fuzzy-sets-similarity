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

    const MAIN_EXAMPLE_SETS = {
        setA: [0, 0, 0.7, 0, 0, 0.4, 0, 0, 0.6, 0, 0.3, 0],
        setB: [0, 0, 0.9585, 0, 0.0754, 0.5257, 0, 0.0104, 0.7333, 0, 0.6023, 0],
    };

    const EXAMPLES = [
        {
            setA: [0, 0.5, 0.7, 0.5, 0],
            setB: [0, 0.2, 0.5, 0.2, 0],

        },
        {
            setA: [0, 0.1, 0.1, 0.1, 0],
            setB: [1, 0.9, 0.9, 0.9, 1],
        },
        {
            setA: [0, 0, 0],
            setB: [1, 1, 1],
        },
        {
            setA: [0, 0.1, 0.1, 0.8, 0.3, 0.7, 0.1, 0.1, 0.1],
            setB: [0, 0.1, 0.1, 0.8, 0.3, 0.7, 0.1, 0.1, 0.1],
        },
        {
            setA: [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 1.0, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0],
            setB: [1, 0.9, 0.8, 0.7, 0.3, 0.0, 0.3, 0.5, 0.7, 0.9, 1, 0, 0, 0, 0, 0,],
        },
    ];

    const configureExamples = (method, configurations) =>
        EXAMPLES.map((example, index) =>_.extend(example, method, configurations[index]));

    app.controller("SimplifiedJaccardController", function () {

        const METHOD = {
            'method': 'simplified-jaccard-index'
        };

        const CONFIGS = [
            {
                aggregator: "average",
                tknorm: "maxiumum",
                tnorm: "minimum"

            },
            {
                aggregator: "average",
                tknorm: "lukasiewicz",
                tnorm: "lukasiewicz"
            },
            {
                aggregator: "average",
                tknorm: "probabilistic",
                tnorm: "algebraic"
            },
            {
                aggregator: "maximum",
                tknorm: "maxiumum",
                tnorm: "minimum"

            },
            {
                aggregator: "maximum",
                tknorm: "lukasiewicz",
                tnorm: "lukasiewicz"
            },
            {
                aggregator: "maximum",
                tknorm: "probabilistic",
                tnorm: "algebraic"
            },
            {
                aggregator: "minimum",
                tknorm: "maxiumum",
                tnorm: "minimum"

            },
            {
                aggregator: "minimum",
                tknorm: "lukasiewicz",
                tnorm: "lukasiewicz"
            },
            {
                aggregator: "minimum",
                tknorm: "probabilistic",
                tnorm: "algebraic"
            }
        ];

        this.mainExample = _.extend(MAIN_EXAMPLE_SETS, METHOD, {
            aggregator: 'average',
            tknorm: 'maxiumum',
            tnorm: 'minimum'
        });

        this.examples = configureExamples(METHOD, CONFIGS);
    });

    app.controller("MinkowskiController", function () {

        const METHOD = {
            method: 'minkowski'
        };

        const CONFIGS = [
            {
                r: 2

            },
            {
                r: 1

            },
            {
                r: 3
            },
            {
                r: 2
            },
            {
                r: 2
            },
            {
                r: 2
            },
        ];

        this.mainExample = _.extend(MAIN_EXAMPLE_SETS, METHOD, {
            r: 2
        });

        this.examples = configureExamples(METHOD, CONFIGS);
    });

    app.controller("AngularDistanceController", function () {

        const METHOD = {
            method: 'angular-distance'
        };

        this.mainExample = _.extend(MAIN_EXAMPLE_SETS, METHOD);

        //no configs needed here, no configurable parameters required for this method
        this.examples = configureExamples(METHOD, [])
    });

    app.controller("ImplicationSimilarityController", function () {

        const METHOD = {
            method: 'implication-similarity'
        };

        this.mainExample = _.extend(MAIN_EXAMPLE_SETS, METHOD, {
            aggregator: 'average',
            tnorm: 'minimum',
            implication: 'maximum'
        });


        const CONFIGS = [
            {
                aggregator: 'minimum',
                tnorm: 'minimum',
                implication: 'maximum'

            },
            {
                aggregator: 'average',
                tnorm: 'minimum',
                implication: 'maximum'

            },
            {
                aggregator: 'average',
                tnorm: 'lukasiewicz',
                implication: 'maximum'

            },
            {
                aggregator: 'average',
                tnorm: 'lukasiewicz',
                implication: 'lukasiewicz'

            }
        ];

        this.examples = configureExamples(METHOD, CONFIGS);;
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