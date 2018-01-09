window.FuzzySetExtractor = (function($) {
    
    /**
     * Converts a string with floating point numbers separated by white space, coma or colon to an array of floats
     */
    getArrayFromString = (numbersString) => {
        const result = [];
        var splittedArray = numbersString.split(/\s+|,|;/);
        console.log(JSON.stringify(splittedArray));
        for (x of splittedArray) {
            if (x) { //if not empty string
                let parsed = parseFloat(x);
                if (parsed === NaN) {
                    throw 'Can not parse ' + x + " to float value";
                }
                result.push(parsed);
            }
        }
        return result;
    };

    extractSets = function($formContainingFuzzySetInputs) {
        let setAValue = $formContainingFuzzySetInputs.find('.setA').val();
        let setBValue = $formContainingFuzzySetInputs.find('.setB').val();
        let setA = getArrayFromString(setAValue);
        let setB = getArrayFromString(setBValue);

        return {
            setA,
            setB,
        };
    };

    /**
     * Finds fuzzy sets input on comparision page
     */
    extractGlobalComparisionSets = ($formContainingFuzzySetInputs) => {
        let setAValue = $('.comparison-setA').val();
        let setBValue = $('.comparison-setB').val();
        let setA = getArrayFromString(setAValue);
        let setB = getArrayFromString(setBValue);
        return {
            setA,
            setB,
        };
    }
    return {
        extractSets,
        extractGlobalComparisionSets
    };
})($);