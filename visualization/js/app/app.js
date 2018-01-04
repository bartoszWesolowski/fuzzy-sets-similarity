(function () {

    const defaultMethodName = 'minkowski';

    var app = angular.module("fuzzy-sets", []);

    app.directive("similarityCalculator", ['$http', function ($http) {
        return {
            restrict: "E",
            templateUrl: function (elem, attr) {
                return (attr.method || defaultMethodName) + '-template.html';
            },
            scope: {
                methodConfig: '<',
                similarityMethod: '<'
            },
            link: function(scope, element, attrs) {
                attrs.$observe('methodConfig', function(value) {
                    console.log(value);
                });
            },
            controller: function ($attrs) {
                this.similarityOfSets = 0;

                this.defaultConfig = {
                    setA: [],
                    setB: [],
                    config: {}
                };

                var minkowski = this;

                $attrs.$observe('methodConfig', function(value) {
                    console.log(value)
                });

                this.arrayToString = function (possiblyArray) {
                    if (angular.isArray(possiblyArray)) {
                        return possiblyArray.join(", ");
                    }
                    return '';
                }

                this.calculateResult = function () {
                    this.similarityData.setA = this.parseRawSetInputToArray(this.rawSetA);
                    this.similarityData.setB = this.parseRawSetInputToArray(this.rawSetB);

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

                /**
                 * Converts a string with floating point numbers
                 * separated by white space, coma or colon to an
                 * array of floats
                 */
                this.parseRawSetInputToArray = function (rawInput) {
                    //TODO: test with var b = a.split(',').map(Number);
                    //TODO: also convert this to service
                    const result = [];
                    var splittedArray = rawInput.split(/\s+|,|;/);
                    console.log(JSON.stringify(splittedArray));
                    for (x of splittedArray) {
                        if (x) { //if not empty string
                            let parsed = parseFloat(x);
                            if (isNaN(parsed)) {
                                console.log('Can not parse ' + x + " to float value. Ignoring this input.");
                            } else {
                                result.push(parsed);
                            }
                        }
                    }
                    return result;
                }


                this.method = $attrs.similarityMethod || defaultMethodName;

                this.methodConfig = angular.fromJson($attrs.methodConfig || {});
                this.methodConfig.method = this.method
                this.similarityData = angular.extend(this.defaultConfig, this.methodConfig)

                this.rawSetA = this.arrayToString(this.methodConfig.setA) || '0 0.5 1';
                this.rawSetB = this.arrayToString(this.methodConfig.setB) || '0 0.4 0.9';

                this.calculateResult();
            },
            controllerAs: 'similarityCalculatorCtrl'
        }
    }]);

    app.controller("MinkowskiController", function () {
        console.log('minkowski');
        this.examples = [
            {
                setA: "0, 0.5, 0.7, 0.5, 0",
                setB: "0, 0.2, 0.5, 0.2, 0",
                config: {
                    r: 2
                }
            },
            {
                setA: "0, 0.1, 0.1, 0.1, 0.1 0.1 0.1 0.1 0.1 ",
                setB: "1, 0.9, 0.9, 0.9, 1 1 1 1 1 1 1 1 1",
                config: {r: 2}
            },
            {
                setA: "0 ",
                setB: "1",
                config: {r: 2}
            },
            {
                setA: "0, 0.1, 0.1, 0.8, 0.3 0.7 0.1 0.1 0.1",
                setB: "0, 0.1, 0.1, 0.8, 0.3 0.7 0.1 0.1 0.1",
                config: {r: 2}
            },
            {
                setA: "0, 0.1, 0.2, 0.3, 0.4 0.5 0.6 1.0 0.6 0.5 0.4 0.3 0.2 0.1 0 ",
                setB: "1  0.9  0.8  0.7  0.3 0.0 0.3 0.5 0.7 0.9 1 0 0 0 0 0 ",
                config: {r: 2}
            },
        ];
    });
})();