
var app = angular.module('array-utils-module', []);

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

    };

    const arrayToString = function (possiblyArray) {
        if (angular.isArray(possiblyArray)) {
            return possiblyArray.join(", ");
        }
        return '';
    };

    return {
        stringToArray,
        arrayToString
    };
});