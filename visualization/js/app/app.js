(function (_) {

    const defaultMethodName = 'minkowski';

    var app = angular.module("fuzzy-sets", ['fuzzyCharts', 'dataProviders']);

    app.directive("similarityCalculator", ['$http', 'arrayUtils', function ($http, arrayUtils) {
        return {
            restrict: "E",
            templateUrl: function (elem, attr) {
                return (attr.method || defaultMethodName) + '-template.html';
            },
            scope: {
                methodConfig: '=',
                similarityMethod: '='
            },
            controller: function ($attrs) {
                this.similarityOfSets = 0;

                this.defaultSimilarityDataConfig = {
                    setA: [],
                    setB: [],
                    config: {}
                };

                this.chartConfig = {
                    data: [
                        [1, 2],
                        [5, 3]
                    ]
                };
                var minkowski = this;

                this.updateView = function(config) {
                    const setA = config.setA || [];
                    const setB = config.setB || [];
                    this.chartConfig = {
                        data: [
                            setA,
                            setB
                        ],
                        labels: _.range(Math.max(setA.length, setB.length))
                    };
                    this.rawSetA = arrayUtils.arrayToString(config.setA) || '0 0.5 1';
                    this.rawSetB = arrayUtils.arrayToString(config.setB) || '0 0.4 0.9';
                }

                //TODO:It seems to be a dirty way to pass an object from directive attr to its controller,
                //TODO:What would be the best way to do it?
                this.init = function (config) {
                    //config might be a static json (as string) or dynamic object
                    this.method = $attrs.similarityMethod || defaultMethodName;

                    this.methodConfig = angular.fromJson(config || {});
                    this.methodConfig.method = this.method
                    this.similarityData = angular.extend(this.defaultSimilarityDataConfig, this.methodConfig)


                    this.updateView(this.methodConfig);
                    this.calculateResult();
                };

                this.calculateResult = function () {
                    this.similarityData.setA = arrayUtils.stringToArray(this.rawSetA);
                    this.similarityData.setB = arrayUtils.stringToArray(this.rawSetB);
                    console.log('Calculating similiraty for: ' + JSON.stringify(this.similarityData));
                    $http.post('http://localhost:5000/fuzzy/similarity', this.similarityData)
                        .then(
                            (response) => {
                                console.log(response);
                                this.updateView(response.data);
                                minkowski.similarityOfSets = response.data.result;
                            },
                            (errorResponse) => {
                                console.log(errorResponse);
                                alert('Error occurred! Error response: ' + JSON.stringify(errorResponse.data))
                            }
                        );
                }

            },
            controllerAs: 'similarityCalculatorCtrl'
        }
    }]);

    app.factory('arrayUtils', function () {

        const stringArraySplitter = /\s+|,|;/;
        /**
         * Converts a string with floating point numbers
         * separated by white space, coma or colon to an
         * array of floats
         */
        const stringToArray = function (rawInput) {
            //TODO: test with var b = a.split(',').map(Number);
            //TODO: also convert this to service
            const input = rawInput || '';
            return input.split(stringArraySplitter)
                .map(parseFloat)
                .filter((value) => !isNaN(value));

        }

        const arrayToString = function (possiblyArray) {
            if (angular.isArray(possiblyArray)) {
                return possiblyArray.join(", ");
            }
            return '';
        }

        return {
            stringToArray,
            arrayToString
        };
    });

    app.directive('fuzzyNavigation', function() {
        return {
            restrict: 'E',
            templateUrl: 'navigation-template.html'
        };
    });

})(_);