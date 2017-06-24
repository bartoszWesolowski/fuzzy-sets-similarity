var SimilarityModule = (function ($) {

    $('.calculate-button').click((event) => {
        const $formDiv = $(event.target).parent();
        const canvas = $formDiv.parent().find('.chart-canvas')[0];
        dataToCalculate = getDataToCalculate($formDiv, ($configDiv) => {
            let rValue = $configDiv.find('.config-r').val();
            return {
                r: parseInt(rValue) || 2
            }
        });
        getSimilarityResponse(dataToCalculate, (response) => {
            console.log('response: ' + JSON.stringify(response))
            displayChart(canvas, response);
        });
        
    });

    /*
        Extracts data from for div (set A, and set B)
        configExtractor - function that will extract config object from config node
    */
    getDataToCalculate = ($formDiv, configExtractor) => {
        let setAValue = $formDiv.find('.setA').val();
        let setBValue = $formDiv.find('.setB').val();
        return {
            setA: getArrayFromString(setAValue),
            setB: getArrayFromString(setBValue),
            method: 'minkowski',
            config: configExtractor($formDiv.find('.config'))
        }
    }

    getSimilarityResponse = (dataToCalculate, success) => {
        $.ajax({
            type: "POST",
            contentType: "application/json",
            dataType: "json",
            crossDomain: true,
            processData: false,
            url: 'http://localhost:5000/fuzzy/similarity',
            data: JSON.stringify(dataToCalculate),
            success: function (data) {
                success(data);
            },
            error: function (data) {
                console.log('error');
            }
        });
    }

    displayChart = ($canvas, similarityResponse) => {
        var ctx = $canvas.getContext('2d');
        var borderWidth = 5;
        const labels = _.range(Math.max(similarityResponse.setA.length, similarityResponse.setB.length))
        var myChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: labels,
                datasets: [
                    {
                        label: 'Set A',
                        data: similarityResponse.setA,
                        fill: false,
                        borderColor: "red",
                        borderWidth: borderWidth
                    }, 
                    {
                        label: 'Set B',
                        data: similarityResponse.setB,
                        fill: false,
                        borderColor: "blue",
                        borderWidth: borderWidth
                    }
                ]
            }
        });
    }

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
    }

    return {
        getArrayFromString: getArrayFromString
    }

})($);