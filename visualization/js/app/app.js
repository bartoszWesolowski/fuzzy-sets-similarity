(function() {

    var app = angular.module("fuzzy-sets", []);

    app.controller("SimilarityController", function($http) {
        let similarityResult = 0;

        this.similarityEntry = {};

        this.init = function (similarityEntry) {
            this.similarityEntry = similarityEntry;
            this.getSimilarity(similarityEntry);
        }

        this.getSimilarity = (config) => {
            $http.post("http://localhost:5000/fuzzy/similarity", config)
                .then(
                    (response) => {
                        console.log(response);
                        similarityResult = response.data.result;
                    },
                    (errorResponse) => {
                        console.log(errorResponse);
                        alert("Error.!")
                    }
                );
        }

        this.resalculate = () => {
            this.getSimilarity(similarityEntry);
        }
    });

    app.directive("minkowskiSimilarity",['$http',  function($http) {
        return {
            restrict: "E",
            templateUrl: "minkowski-template.html",
            scope: {
                defaultValues: '@',
                similarityMethod: '@'
            },
            controller: function($attrs) {
                this.similarityOfSets = 0;
                console.log($attrs.similarityMethod);
                this.rawSetA = "0 0.5 1";
                this.rawSetB = "0 0.4 0.9";
                this.similarityData = {
                    setA: [],
                    setB: [],
                    config: {
                        r: 2
                    },
                    method: 'minkowski'
                };

                var minkowski = this;

                this.calculateResult = function() {
                    this.similarityData.setA = this.parseRawSetInputToArray(this.rawSetA);
                    this.similarityData.setB = this.parseRawSetInputToArray(this.rawSetB);

                    console.log("calculating result" + JSON.stringify(this.similarityData));

                    $http.post("http://localhost:5000/fuzzy/similarity", this.similarityData)
                        .then(
                            (response) => {
                                console.log(response);
                                minkowski.similarityOfSets = response.data.result;
                            },
                            (errorResponse) => {
                                console.log(errorResponse);
                                alert("Error.!")
                            }
                        );
                }

                /**
                 * Converts a string with floating point numbers
                 * separated by white space, coma or colon to an
                 * array of floats
                 */
                this.parseRawSetInputToArray = function(rawInput) {
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

            },
            controllerAs: 'minkowskiCtrl'
        }
    }]);
})();