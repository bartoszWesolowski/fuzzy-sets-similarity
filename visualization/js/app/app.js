(function () {

    const defaultMethodName = 'minkowski';

    var app = angular.module("fuzzy-sets", ['chart.js']);

    app.directive('fuzzySetsChart', function() {

    });
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

                this.defaultConfig = {
                    setA: [],
                    setB: [],
                    config: {}
                };

                var minkowski = this;

                //TODO:It seems to be a dirty way to pass an object from directive attr to its controller,
                //TODO:What would be the best way to do it?
                this.init = function (config) {
                    //config might be a static json (as string) or dynamic object
                    this.methodConfig = angular.fromJson(config || {});
                    this.method = $attrs.similarityMethod || defaultMethodName;

                    this.methodConfig.method = this.method
                    this.similarityData = angular.extend(this.defaultConfig, this.methodConfig)

                    this.rawSetA = arrayUtils.arrayToString(this.methodConfig.setA) || '0 0.5 1';
                    this.rawSetB = arrayUtils.arrayToString(this.methodConfig.setB) || '0 0.4 0.9';

                    this.calculateResult();
                };

                this.calculateResult = function () {
                    this.similarityData.setA = arrayUtils.stringToArray(this.rawSetA);
                    this.similarityData.setB = arrayUtils.stringToArray(this.rawSetB);

                    $http.post('http://localhost:5000/fuzzy/similarity', this.similarityData)
                        .then(
                            (response) => {
                                console.log(response);
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

    app.controller("MinkowskiController", function () {
        console.log('minkowski');
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
})();