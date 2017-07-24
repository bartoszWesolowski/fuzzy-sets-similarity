window.SimilarityModule = (function () {
    //TODO:moze przerobic na klase kiedys
    calculateEvent = (similarityMethodContextProvider, fuzzySetsExtractor, extractChartCanvas) => {
        console.log('calculate event');
        $(document).on("click", similarityMethodContextProvider.buttonSelector, (event) => {
            console.log('adding event');
            const $formDiv = $(event.target).parent();
            const $mainSection = $formDiv.parent();
            const canvas = extractChartCanvas($mainSection);
            const $resultPlaceholder = $mainSection.find('.result-value');
            dataToCalculate = getDataToCalculate($formDiv,
                similarityMethodContextProvider.configExtractor,
                similarityMethodContextProvider.method,
                fuzzySetsExtractor);

            if (dataToCalculate.isValid()) {
                getSimilarityResponse(dataToCalculate, (response) => {
                    console.log('response: ' + JSON.stringify(response))
                    displayChart(canvas, response);
                    $resultPlaceholder.text(response.result);
                });
            }
         });
    }
    /*
        Extracts data from for div (set A, and set B)
        configExtractor - function that will extract config object from config node
    */
    getDataToCalculate = ($formDiv, configExtractor, method,
        fuzzySetsExtractor) => {
        const extractedSets = fuzzySetsExtractor($formDiv);
        let setA = extractedSets.setA;
        let setB = extractedSets.setB;
        let config = configExtractor($formDiv.find('.config'));
        isValid = () => {
            return setA.length > 0 && setB.length > 0;
        }
        return {
            setA,
            setB,
            method: method,
            config,
            isValid
        }
    }

    /**
     * Calls server with POST method.
     */
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
                alert('Error occured while calculating similiraty.');
            }
        });
    }

    /**
     * Display a chart representing two fuzzy sets from simiratiryResponse object on a passed canvas.
     */
    displayChart = (canvas, similarityResponse) => {
        var ctx = canvas.getContext('2d');
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

    return {
        bindCalculateEvent: calculateEvent
    }

})();