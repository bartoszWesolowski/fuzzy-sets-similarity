(function (_) {

    const defaultMethodName = 'minkowski';

    var app = angular.module("fuzzy-sets", ['fuzzyCharts', 'dataProviders', 'array-utils-module']);

    app.directive("similarityCalculator", ['$http', 'arrayUtils', 'fuzzyApi', function ($http, arrayUtils, fuzzyApi) {
        return {
            restrict: "E",
            templateUrl: function () {
                return 'similarity-calculator-main.html';
            },
            scope: {
                name: '=',
                methodConfig: '=',
                hideSets: '=',
                hideChart: '='
            },
            controller: function ($scope, $attrs) {
                console.log('similarityCalculator controller init')
                var _self = this;

                //todo:move thic out of method config
                this.id = $scope.methodConfig.id === undefined ? new Date().getTime() : $scope.methodConfig.id;

                this.name = $scope.name || '';

                this.similarityOfSets = 0;

                this.calculationStatus = {
                    inProgress: true,
                    finished: false,
                    failed: false,
                    failureData: {},
                    start: function () {
                        this.inProgress = true;
                        this.finished = false;
                        this.failed = false;
                    },
                    finish: function () {
                        this.inProgress = false;
                        this.finished = true;
                        this.failed = false;
                    },
                    fail: function (errorResponse) {
                        this.finish();
                        this.failed = true;
                        this.failureData.message = errorResponse.data.message;
                    }
                };

                this.defaultSimilarityDataConfig = {
                    setA: [],
                    setB: [],
                };

                this.updateView = function (config) {
                    const setA = config.setA || [];
                    const setB = config.setB || [];
                    const diff = setA.length - setB.length;
                    const setToAddZeros = setA.length >= setB.length ? setB : setA;
                    for(let i = 0; i < Math.abs(diff); i++) {
                        setToAddZeros.push(0);
                    }

                    this.chartConfig = {
                        data: [
                            setA,
                            setB
                        ],
                        labels: _.range(Math.max(setA.length, setB.length))
                    };
                    this.rawSetA = arrayUtils.arrayToString(setA);
                    this.rawSetB = arrayUtils.arrayToString(setB);
                };

                this.calculateResult = function () {
                    this.similarityData.setA = arrayUtils.stringToArray(this.rawSetA);
                    this.similarityData.setB = arrayUtils.stringToArray(this.rawSetB);
                    console.log('Calculating similiraty for: ' + JSON.stringify(this.similarityData));
                    this.calculationStatus.start();
                    fuzzyApi.calculateSimilarity(this.similarityData)
                        .then(
                            (response) => {
                                console.log(response);
                                this.updateView(response.data);
                                _self.similarityOfSets = response.data.result;
                                //id added to avoid result duplication
                                var eventData = _.extend({}, response.data, {id: _self.id});

                                $scope.$emit('FUZZY_SIMILARITY_CALCULATED', eventData)
                                this.calculationStatus.finish();
                            },
                            (errorResponse) => {
                                this.calculationStatus.fail(errorResponse);
                                console.log('error response: ' + JSON.stringify(errorResponse));
                            }
                        );
                };

                this.init = function (config) {

                    this.methodConfig = angular.fromJson(config || {});
                    this.similarityData = angular.extend(this.defaultSimilarityDataConfig, this.methodConfig);


                    this.updateView(this.methodConfig);
                    this.calculateResult();
                };

                //fixme: broken
                $scope.$watch('methodConfig', function(newValue) {
                    _self.init(newValue);
                }, true);

            },
            controllerAs: 'similarityCalculatorCtrl'
        }
    }]);

    app.directive('infoBar', function () {
        return {
            restrict: 'E',
            templateUrl: 'info-bar.html'
        };
    });

    app.directive('fuzzyNavigation', function () {
        return {
            restrict: 'E',
            templateUrl: 'navigation-template.html'
        };
    });

    app.directive('rawSetsInput', function () {
        return {
            restrict: 'E',
            scope: {
                rawSetA: '=',
                rawSetB: '='
            },
            templateUrl: 'raw-sets-input.html'
        };
    });

    app.controller("FormController", ['fuzzyApi', function(fuzzyApi) {

        var formController = this;

        this.tNorms = [
            {
                label: 'Minimum',
                value: 'minimum'
            },
            {
                label: 'Lukasiewicz',
                value: 'lukasiewicz'
            },
            {
                label: 'Algebraqic',
                value: 'algebraic'
            }
        ];

        this.tkonorms = [
            {
                label: 'Maxiumum',
                value: 'maxiumum'
            },
            {
                label: 'Lukasiewicz',
                value: 'lukasiewicz'
            },
            {
                label: 'Probabilistic (pairs with algebraic)',
                value: 'probabilistic'
            }
        ];

        this.aggregators = [
            {
                label: 'Average',
                value: 'average'
            },
            {
                label: 'Minimum',
                value: 'minimum'
            },
            {
                label: 'Maximum',
                value: 'maximum'
            },

        ];

        this.implications = [
            {
                label: 'Maximum',
                value: 'maximum'
            },
            {
                label: 'Lukasiewicz',
                value: 'lukasiewicz'
            },
        ];

        this.dataSets = [];

        var downloadDataSets = () => {
            if (this.dataSets.length) {
                return;
            }
            fuzzyApi.getAvailableDataSets()
                .then(
                    (response) => {
                        console.log(response);
                        formController.dataSets = response.data.dataSets;
                    },
                    (errorResponse) => {
                        console.log('error response: ' + JSON.stringify(errorResponse));
                    }
                );

        };

        downloadDataSets();
    }]);


    app.controller("drawSetChartController", ['$http', 'arrayUtils', 'fuzzyApi', function ($http, arrayUtils, fuzzyApi) {
        return {
            restrict: "E",
            templateUrl: function () {
                return 'similarity-calculator-main.html';
            },
            scope: {
                name: '=',
                methodConfig: '=',
                hideSets: '=',
                hideChart: '='
            },
            controller: function ($scope, $attrs) {
                console.log('similarityCalculator controller init')
                var _self = this;

                //todo:move thic out of method config
                this.id = $scope.methodConfig.id === undefined ? new Date().getTime() : $scope.methodConfig.id;

                this.name = $scope.name || '';

                this.similarityOfSets = 0;

                this.calculationStatus = {
                    inProgress: true,
                    finished: false,
                    failed: false,
                    failureData: {},
                    start: function () {
                        this.inProgress = true;
                        this.finished = false;
                        this.failed = false;
                    },
                    finish: function () {
                        this.inProgress = false;
                        this.finished = true;
                        this.failed = false;
                    },
                    fail: function (errorResponse) {
                        this.finish();
                        this.failed = true;
                        this.failureData.message = errorResponse.data.message;
                    }
                };

                this.defaultSimilarityDataConfig = {
                    setA: [],
                    setB: [],
                };

                this.updateView = function (config) {
                    const setA = config.setA || [];
                    const setB = config.setB || [];
                    const diff = setA.length - setB.length;
                    const setToAddZeros = setA.length >= setB.length ? setB : setA;
                    for(let i = 0; i < Math.abs(diff); i++) {
                        setToAddZeros.push(0);
                    }

                    this.chartConfig = {
                        data: [
                            setA,
                            setB
                        ],
                        labels: _.range(Math.max(setA.length, setB.length))
                    };
                    this.rawSetA = arrayUtils.arrayToString(setA);
                    this.rawSetB = arrayUtils.arrayToString(setB);
                };

                this.calculateResult = function () {
                    this.similarityData.setA = arrayUtils.stringToArray(this.rawSetA);
                    this.similarityData.setB = arrayUtils.stringToArray(this.rawSetB);
                    console.log('Calculating similiraty for: ' + JSON.stringify(this.similarityData));
                    this.calculationStatus.start();
                    fuzzyApi.calculateSimilarity(this.similarityData)
                        .then(
                            (response) => {
                                console.log(response);
                                this.updateView(response.data);
                                _self.similarityOfSets = response.data.result;
                                //id added to avoid result duplication
                                var eventData = _.extend({}, response.data, {id: _self.id});

                                $scope.$emit('FUZZY_SIMILARITY_CALCULATED', eventData)
                                this.calculationStatus.finish();
                            },
                            (errorResponse) => {
                                this.calculationStatus.fail(errorResponse);
                                console.log('error response: ' + JSON.stringify(errorResponse));
                            }
                        );
                };

                this.init = function (config) {

                    this.methodConfig = angular.fromJson(config || {});
                    this.similarityData = angular.extend(this.defaultSimilarityDataConfig, this.methodConfig);


                    this.updateView(this.methodConfig);
                    this.calculateResult();
                };

                //fixme: broken
                $scope.$watch('methodConfig', function(newValue) {
                    _self.init(newValue);
                }, true);

            },
            controllerAs: 'similarityCalculatorCtrl'
        }
    }]);
})(_);