(function($) {
    
  $('.calculate-button').click((event) => {
      const formDiv = $(event.target).parent();
      data = getDataToCalculate(formDiv);
      getSimilarityResponse(data);
  });

  getDataToCalculate = ($formDiv) => {
    return {
        setA: [0, 0, 1],
        setB: [1, 0, 1],
        method: 'minkowski',
        config: {
            r: 2
        }
    }
  }
  
  getSimilarityResponse = (dataToCalculate) => {
    console.log(JSON.stringify(dataToCalculate));
    $.ajax({
        contentType: "application/json",
        dataType   : "jsonp",
        crossDomain: true,
        processData: false,
        url: 'http://localhost:5000/fuzzy/similarity',
        type: 'POST',
        data: JSON.stringify(dataToCalculate),
        success: function(data) {
            console.log('success');
            alert(data);
        },
        error: function(data) {
            console.log('error');
        }
    });
  }
  
})($);